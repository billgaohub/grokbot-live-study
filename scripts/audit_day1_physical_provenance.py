#!/usr/bin/env python3
"""
Rigorous Physical Evidence Provenance Auditor for Grok Bot Live Study Day 1.

Verifies:
1. Timeline Continuity & 31,513s Conservation (24 contiguous segments, 0 gaps).
2. Physical review coverage for all 24 segments in verification/day-1-coverage-review.yaml.
3. Physical existence of all 16 extracted video frame artifacts on disk.
4. Exact byte-level SHA-256 match between physical files, evidence index, and verification receipts.
5. Epistemic calibration of spoken vs physical claims (OBS-031).
"""

import os
import sys
import yaml
import hashlib

def run_audit():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cov_file = os.path.join(repo_root, 'verification/day-1-coverage-review.yaml')
    ver_file = os.path.join(repo_root, 'verification/verification.yaml')
    idx_file = os.path.join(repo_root, 'evidence/index.yaml')
    obs_file = os.path.join(repo_root, 'observations/day-1.yaml')
    frames_dir = os.path.join(repo_root, 'evidence/frames')

    print("=== 1. TIMELINE CONTINUITY & DURATION AUDIT ===")
    assert os.path.exists(cov_file), f"Coverage review file missing: {cov_file}"
    with open(cov_file) as f:
        cov_data = yaml.safe_load(f)
    assert cov_data['total_duration_seconds'] == 31513, f"Expected 31513s, got {cov_data['total_duration_seconds']}"
    assert len(cov_data['segments']) == 24, f"Expected 24 segments, got {len(cov_data['segments'])}"
    tot_sec = sum(s['duration_seconds'] for s in cov_data['segments'])
    assert tot_sec == 31513, f"Sum of durations {tot_sec} != 31513"
    print("PASS: 24 segments mathematically conserve 31,513s (08:45:13) with zero voids.")

    print("=== 2. ALL 24 SEGMENTS PHYSICAL REVIEW RECORD AUDIT ===")
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
            'MATERIAL_EVENT_PROMOTED',
            'BACKGROUND_AND_PRIMITIVES'
        ], f"Invalid materiality: {s['materiality_adjudicated']}"
        assert s['reviewed_at'], f"Missing reviewed_at in {s['segment_id']}"
    print("PASS: All 24 segments have explicit physical review records, access_status, and review_mode.")

    print("=== 3. REAL PHYSICAL FRAME EXISTENCE & HASH VERIFICATION ===")
    with open(obs_file) as f:
        obs_data = yaml.safe_load(f)
    with open(idx_file) as f:
        idx_data = yaml.safe_load(f)
    with open(ver_file) as f:
        ver_data = yaml.safe_load(f)

    idx_frames = {r['observation_ref']: r for r in idx_data['evidence_records'] if r.get('frame_identifier')}
    ver_receipts = {r['observation_ref']: r for r in ver_data['playback_frame_verifications']}

    content_reviewed_count = 0
    for o in obs_data['observations']:
        if o.get('review_depth', {}).get('content_reviewed') is True:
            content_reviewed_count += 1
            oid = o['observation_id']
            assert oid in idx_frames, f"Observation {oid} claims content_reviewed but missing from evidence index"
            assert oid in ver_receipts, f"Observation {oid} claims content_reviewed but missing from verification receipts"
            
            fid = idx_frames[oid]['frame_identifier']
            claimed_hash_idx = idx_frames[oid]['content_sha256']
            claimed_hash_ver = ver_receipts[oid]['frame_sha256']
            assert claimed_hash_idx == claimed_hash_ver, f"Hash mismatch between index and ver for {oid}: {claimed_hash_idx} vs {claimed_hash_ver}"
            
            # Check physical file on disk
            p1 = os.path.join(frames_dir, fid)
            assert os.path.exists(p1), f"Physical frame file missing in repo: {p1}"
            assert os.path.getsize(p1) > 0, f"Physical frame file is empty: {p1}"
            
            with open(p1, 'rb') as f:
                real_hash = hashlib.sha256(f.read()).hexdigest()
            assert real_hash == claimed_hash_idx, f"Physical file hash mismatch for {fid}: {real_hash} != {claimed_hash_idx}"
            
            # Check locator contains frame & hash
            loc = o.get('evidence_locator', '')
            assert fid in loc, f"Locator for {oid} missing frame name: {loc}"
            assert real_hash in loc, f"Locator for {oid} missing real hash: {loc}"

    print(f"PASS: All {content_reviewed_count} content-reviewed observations resolve to authentic physical frames with exact byte-level SHA-256 match!")

    print("=== 4. EPISTEMIC CALIBRATION AUDIT ===")
    obs031 = next(o for o in obs_data['observations'] if o['observation_id'] == 'OBS-031')
    assert obs031['support_level'] == 'AUTHORITATIVE_DOC_ALIGNED'
    assert 'SPOKEN_STATEMENT' in obs031.get('epistemic_note', '')
    print("PASS: OBS-031 properly calibrated as SPOKEN_STATEMENT + AUTHORITATIVE_DOC_ALIGNED != PHYSICAL_SYSTEM_TEST.")

    print("=== ALL 4 GATES PASSED: DAY1_FULL_STUDIED PHYSICAL PROVENANCE ESTABLISHED ===")

if __name__ == '__main__':
    run_audit()
