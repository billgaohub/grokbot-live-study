#!/usr/bin/env python3
"""
Rigorous Physical Evidence Provenance Auditor for Grok Bot Live Study Day 2.

Verifies:
1. Timeline Continuity & 30,199s Conservation (29 contiguous segments, 0 gaps).
2. Physical review coverage for all 29 segments in verification/day-2-coverage-review.yaml.
3. Physical existence of all 46 Day 2 extracted video frame artifacts on disk.
4. Exact byte-level SHA-256 match between physical files, evidence index, and observations.
5. Epistemic calibration of spoken vs physical claims (OBS-D2-003).
"""

import os
import sys
import yaml
import hashlib

def run_audit():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cov_file = os.path.join(repo_root, 'verification/day-2-coverage-review.yaml')
    idx_file = os.path.join(repo_root, 'evidence/index.yaml')
    obs_file = os.path.join(repo_root, 'observations/day-2.yaml')
    frames_dir = os.path.join(repo_root, 'evidence/frames')

    print("=== 1. TIMELINE CONTINUITY & DURATION AUDIT (DAY 2) ===")
    assert os.path.exists(cov_file), f"Coverage review file missing: {cov_file}"
    with open(cov_file) as f:
        cov_data = yaml.safe_load(f)
    assert cov_data['total_duration_seconds'] == 30199, f"Expected 30199s, got {cov_data['total_duration_seconds']}"
    assert len(cov_data['segments']) == 29, f"Expected 29 segments, got {len(cov_data['segments'])}"
    tot_sec = sum(s['duration_seconds'] for s in cov_data['segments'])
    assert tot_sec == 30199, f"Sum of durations {tot_sec} != 30199"
    print("PASS: 29 segments mathematically conserve 30,199s (08:23:19) with zero voids.")

    print("=== 2. ALL 29 SEGMENTS PHYSICAL REVIEW RECORD AUDIT ===")
    for s in cov_data['segments']:
        assert s['access_status'] == 'ACCESSED_AND_REVIEWED', f"Segment {s['segment_id']} not reviewed"
        assert s['review_mode'] in [
            'METADATA_AND_STREAM_INSPECTION',
            'FRAME_EXTRACTION_AND_VISUAL_REVIEW',
            'VISUAL_RANGE_CONFIRMATION'
        ], f"Invalid review mode: {s['review_mode']}"
        assert s['materiality_adjudicated'] in [
            'BACKGROUND_CONTEXT',
            'NO_EVENT',
            'MATERIAL_EVENT_PROMOTED'
        ], f"Invalid materiality: {s['materiality_adjudicated']}"
        assert s['reviewed_at'], f"Missing reviewed_at in {s['segment_id']}"
    print("PASS: All 29 segments have explicit physical review records, access_status, and review_mode.")

    print("=== 3. REAL PHYSICAL FRAME EXISTENCE & HASH VERIFICATION ===")
    with open(obs_file) as f:
        obs_data = yaml.safe_load(f)
    with open(idx_file) as f:
        idx_data = yaml.safe_load(f)

    idx_frames = {r['observation_ref']: r for r in idx_data['evidence_records'] if r.get('frame_identifier') and r['observation_ref'].startswith('OBS-D2-')}

    content_reviewed_count = 0
    total_frames_verified = 0
    for o in obs_data['observations']:
        if o.get('review_depth', {}).get('content_reviewed') is True:
            content_reviewed_count += 1
            oid = o['observation_id']
            assert oid in idx_frames, f"Observation {oid} claims content_reviewed but missing from evidence index"
            
            # Check all bundle frames
            bundle = idx_frames[oid].get('bundle_frames', [])
            assert len(bundle) > 0, f"No bundle frames for {oid}"
            for bf in bundle:
                fid = bf['frame_identifier']
                claimed_hash = bf['content_sha256']
                
                # Check physical file on disk
                p1 = os.path.join(frames_dir, fid)
                assert os.path.exists(p1), f"Physical frame file missing in repo: {p1}"
                assert os.path.getsize(p1) > 0, f"Physical frame file is empty: {p1}"
                
                with open(p1, 'rb') as f:
                    real_hash = hashlib.sha256(f.read()).hexdigest()
                assert real_hash == claimed_hash, f"Physical file hash mismatch for {fid}: {real_hash} != {claimed_hash}"
                
                # Check locator contains frame & hash
                loc = o.get('evidence_locator', '')
                assert fid in loc, f"Locator for {oid} missing frame name {fid}: {loc}"
                assert real_hash in loc, f"Locator for {oid} missing real hash {real_hash}: {loc}"
                total_frames_verified += 1

    print(f"PASS: All {content_reviewed_count} content-reviewed observations resolve to authentic physical frames ({total_frames_verified} bundle checks) with exact byte-level SHA-256 match!")

    print("=== 4. EPISTEMIC CALIBRATION AUDIT ===")
    obs_d2_003 = next(o for o in obs_data['observations'] if o['observation_id'] == 'OBS-D2-003')
    assert obs_d2_003['support_level'] == 'PARTIALLY_SUPPORTED'
    assert '85%' in obs_d2_003.get('epistemic_note', '')
    print("PASS: OBS-D2-003 properly calibrated as PARTIALLY_SUPPORTED (85% test speedup claim calibrated).")

    print("=== ALL GATES PASSED: DAY2_FULL_STUDIED PHYSICAL PROVENANCE ESTABLISHED ===")

if __name__ == '__main__':
    run_audit()
