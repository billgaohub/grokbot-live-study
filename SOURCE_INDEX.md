# Source Index & Provenance Hierarchy

## 1. Primary Source (Factual Authority)

* **Name**: Grok Bot Galaxy Day 1 Official Livestream
* **Platform**: X (formerly Twitter)
* **Broadcast ID**: `1YGNrbXEeazGw`
* **Broadcast URL**: https://x.com/i/broadcasts/1YGNrbXEeazGw
* **Official Post**: https://x.com/bot/status/2099890276315848743
* **Event Date**: 2026-09-15
* **Replay Duration**: 08:45:19
* **Location**: The Howard, 661 Howard Street, San Francisco, CA
* **Standing**: **PRIMARY_SOURCE**
* **Verification Status**: Identity pinned; player playback verified through byte-identical media mirror stream.

---

## 2. Media Mirror (Playback Inspection Source)

* **Name**: Grok Bot Galaxy Day 1 Full Replay (Bilingual Mirror)
* **Platform**: Bilibili
* **Identifier**: `BV19fYf6kELz` (AID: `117279433951023`)
* **URL**: https://www.bilibili.com/video/BV19fYf6kELz/
* **Duration**: 31,513 seconds (08:45:13)
* **Standing**: **MEDIA_MIRROR**
* **Role**: Used for high-precision timecode seeking, frame extraction, burned subtitle inspection, and duration corroboration.

### Verified Chapter Markers in Study Window
- `00:00:00` — Opening & 3-day challenge framing
- `00:02:45` — Galaxy challenge & Starbase launch contest announcement
- `00:09:20` — Host introduction and stream agenda
- `00:29:28` — Grok Bot 101 kickoff (Roman Ugarte & Amrita)
- `00:30:25` — Conceptual evolution: Chat → Copilot → Agent
- `00:40:06` — Live demo: Data Dan creation
- `00:50:05` — Multi-bot collaboration (Slide Sonya / Email Ethan / Teach a task)
- `01:10:00` — Group chat & multi-agent orchestration
- `01:20:00` — Enterprise security: VPN, credentials, 1Password
- `01:31:05` — 101 wrap-up, return to main stage

---

## 3. Authoritative Reference Documentation

* **SpaceXAI / xAI Galaxy Event**: https://x.ai/galaxy
* **Grok Bot Architecture Documentation**: https://docs.x.ai/grok-bot/overview
  - Used for authoritative adjudication of VM isolation boundaries (Firecracker microVM shared per user vs verbally asserted per-bot isolation).

---

## 4. Secondary Builder Notes (Corroboration)

* **Author**: CodeSolutionsLLC (Timed Livestream Builder Notes)
* **Format**: Public GitHub Gist
* **Standing**: **SECONDARY_CORROBORATION**
* **Usage**: Used for initial topic indexing and timeline framing; all critical events were independently re-evaluated against media frames.
