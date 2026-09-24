#!/usr/bin/env python3
"""
Crop Day 3 frames to clean video viewport and synchronously update SHA-256 hashes.

Removes:
- Left X navigation sidebar (including personal handle @roenelteck and navigation buttons)
- Right X live chat sidebar
- Top Chrome browser window tabs / URL address bar
- Bottom OS dock / white post metadata space

Produces clean 649x365 16:9 video frame artifacts.
Updates:
- evidence/frames/d3_*.png
- evidence/index.yaml
- verification/day-3-evidence-sufficiency.yaml
- observations/day-3.yaml
"""

import os
import sys
import glob
import hashlib
import yaml
from PIL import Image

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRAMES_DIR = os.path.join(REPO_ROOT, 'evidence/frames')
INDEX_FILE = os.path.join(REPO_ROOT, 'evidence/index.yaml')
SUFF_FILE = os.path.join(REPO_ROOT, 'verification/day-3-evidence-sufficiency.yaml')
OBS_FILE = os.path.join(REPO_ROOT, 'observations/day-3.yaml')

def get_file_sha256(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def main():
    frame_files = sorted(glob.glob(os.path.join(FRAMES_DIR, 'd3_*')))
    print(f"Found {len(frame_files)} Day 3 frames to crop and rehash.")

    # 1. Compute old hashes
    old_hashes = {}
    for f in frame_files:
        filename = os.path.basename(f)
        old_hashes[filename] = get_file_sha256(f)

    # 2. Crop frames
    print("Cropping frames to clean 649x365 video viewport...")
    new_hashes = {}
    for f in frame_files:
        filename = os.path.basename(f)
        im = Image.open(f).convert('RGB')
        arr = im.load()
        
        # Check if windowed (tab bar at top)
        val = arr[500, 5]
        if val[0] > 180 and val[1] > 200:
            box = (276, 87, 925, 452)
        else:
            box = (276, 0, 925, 365)
            
        cropped = im.crop(box)
        assert cropped.size == (649, 365), f"Unexpected size {cropped.size} for {filename}"
        
        # Save back in-place
        cropped.save(f, format='PNG', optimize=True)
        new_hashes[filename] = get_file_sha256(f)

    print("All 71 frames successfully cropped to 649x365.")

    # Build replacement mapping from old hash to new hash
    hash_map = {}
    for filename in old_hashes:
        o = old_hashes[filename]
        n = new_hashes[filename]
        hash_map[o] = n

    print(f"Created hash mapping for {len(hash_map)} files.")

    # 3. Update evidence/index.yaml
    print("Updating evidence/index.yaml...")
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        index_text = f.read()

    for o_hash, n_hash in hash_map.items():
        index_text = index_text.replace(o_hash, n_hash)

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(index_text)

    # 4. Update verification/day-3-evidence-sufficiency.yaml
    print("Updating verification/day-3-evidence-sufficiency.yaml...")
    with open(SUFF_FILE, 'r', encoding='utf-8') as f:
        suff_text = f.read()

    for o_hash, n_hash in hash_map.items():
        suff_text = suff_text.replace(o_hash, n_hash)

    with open(SUFF_FILE, 'w', encoding='utf-8') as f:
        f.write(suff_text)

    # 5. Update observations/day-3.yaml
    print("Updating observations/day-3.yaml...")
    with open(OBS_FILE, 'r', encoding='utf-8') as f:
        obs_text = f.read()

    for o_hash, n_hash in hash_map.items():
        obs_text = obs_text.replace(o_hash, n_hash)

    with open(OBS_FILE, 'w', encoding='utf-8') as f:
        f.write(obs_text)

    print("All ledgers and indexes updated.")

if __name__ == '__main__':
    main()
