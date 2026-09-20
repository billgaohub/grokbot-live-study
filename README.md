# Grok Bot Live Study (Galaxy Day 1 Field Reconstruction)

[![Status](https://img.shields.io/badge/status-EMPIRICALLY_VERIFIED-brightgreen.svg)](STUDY_PROTOCOL.md)
[![Scope](https://img.shields.io/badge/scope-Day_1_First_90m-blue.svg)](timeline/day-1.md)
[![License](https://img.shields.io/badge/license-MIT%20%2F%20CC%20BY%204.0-green.svg)](LICENSE)

> **Grok Bot Live Study** is an evidence-first, curated field-study record reconstructing the initial 90-minute livestream window (`T+00:00:00` to `T+01:30:00`) of xAI's Grok Bot Galaxy live-build event (September 15, 2026). It documents atomic observations, propositional claims, human approval gate latency, operational failures, and human-steered recovery loops.

---

## 1. Single Source of Truth (SSOT) Authority Hierarchy

To prevent epistemological circularity, this repository operates under a strict three-tier authority model:

```text
Primary X Broadcast (1YGNrbXEeazGw)
= source factual authority (First-Party Ground Reality)
        ↓
grokbot-live-study (This Repository)
= curated field-study record authority (Structured Reconstruction)
        ↓
agent-world-state (Specification & Validator)
= derived model authority (Cross-Case Epistemic Abstraction)
```

- **Source Factual Authority**: Primary broadcast media and official first-party documentation hold ground truth.
- **Curated Record Authority**: This repository provides timestamped, reproducible reconstructions, atomic observations, and falsifiable claims.
- **Derived Model Authority**: Generic schema standards (e.g. `billgaohub/agent-world-state`) consume observations from here; this repository does not define universal models.

---

## 2. Study Scope & Review Modalities

### Scope Boundary
While the overall Grok Bot Galaxy event was a three-day (72-hour) continuous live-build sprint, this v0.1 release specifically establishes the frozen empirical baseline for the **Day 1 First 90-Minute Window**:
- **Temporal Window**: `T+00:00:00 → T+01:30:00` (Replay stream offset)
- **Total Atomic Observations**: 16 (`OBS-001` through `OBS-016`)
  - **7 Content-Verified Observations**: Direct visual inspection of extracted frames, UI components, cursor traces, and approval modals.
  - **9 Mirror-Metadata Aligned Observations**: Segment boundaries corroborated against mirror chapter markers and broadcast summaries.

### Calibrated Review Modalities
In alignment with strict epistemic defense principles, observer modalities are precisely decomposed:
- **`media_access`**: `DIRECT_MEDIA_STREAM` (via Bilibili replay mirror `BV19fYf6kELz`, duration 31,513s / 08:45:13)
- **`video_review`**: `FRAME_EXTRACTION_AND_VISUAL_REVIEW` (Precise timestamp seek and OCR inspection)
- **`subtitle_review`**: `BURNED_SUBTITLE_VISUAL_REVIEW` (Burned-in bilingual subtitle stream verification)
- **`audio_review`**: `NOT_INDEPENDENTLY_REVIEWED` (Audio waveforms and spoken utterances were not subject to isolated algorithmic transcription)

---

## 3. Key Empirical Findings

1. **Teach-a-Task Demonstration (`OBS-008`, `T+00:48:30`)**:
   - Presenters physically demonstrated cursor recording for building animations in Google Slides. The agent operates in a real desktop GUI environment, capturing coordinate trajectories.
2. **Approval Gate Latency & Trade-Offs (`OBS-010`, `T+00:53:15` → `T+00:56:45`)**:
   - Critical human-in-the-loop (HITL) friction documented: An approval modal blocked agent execution for **195 seconds (3m 15s)** until the human operator clicked "Allow". Demonstrates that HITL safety mechanisms dominate agent runtime latency.
3. **VM Isolation Discrepancy (`OBS-011`, `T+00:58:30`)**:
   - Presenter verbally asserted: *"One Grok Bot cannot access another Grok Bot's computer"*.
   - **Contradiction Identified**: Official documentation (`docs.x.ai/grok-bot/overview`) specifies that bot execution takes place within a single Firecracker microVM allocated per user, shared across all bots of that user.
4. **Failure → Intervention → Recovery Loop (`CORR-CHAIN-001`, `T+01:06:30` → `T+01:11:00`)**:
   - **Failure**: Agent created a Google Form with restricted access; audience reported permission errors (`OBS-013`).
   - **Intervention**: Operator issued targeted natural-language steering instruction: *"make link public"* (`INT-003`).
   - **Recovery**: Agent opened share settings modal via GUI and toggled permissions (`OBS-014`).
   - **External Verification**: Audience submitted responses live; counter on screen incremented in real time (`OBS-015`).

---

## 4. Repository Structure

```text
grokbot-live-study/
├── README.md                          # Project overview and executive summary
├── STUDY_PROTOCOL.md                  # Epistemic rules and verification standards
├── SOURCE_INDEX.md                    # Primary broadcast and mirror provenance
├── LICENSE                            # Dual MIT / CC BY 4.0 license
├── timeline/
│   └── day-1.md                       # Chronological narrative of first 90 minutes
├── observations/
│   └── observations.yaml              # 16 atomic observations with orthogonal axes
├── claims/
│   └── claims.yaml                    # Propositional claims and support grades
├── failures/
│   └── failures.yaml                  # Observed failure records
├── interventions/
│   └── interventions.yaml             # Human intervention and steering records
├── verification/
│   └── verification.yaml              # Causal recovery chains and contradiction checks
├── analyses/
│   └── derived-rules.md               # Empirical findings on approval gates and UI agents
├── evidence/
│   └── index.yaml                     # Abstract evidence locators (hashes and offsets)
└── corrections/
    └── correction-ledger.yaml         # Provenance calibrations and errata log
```

---

## 5. Licensing & Source Rights

- **Code & Schemas**: Licensed under the [MIT License](LICENSE).
- **Original Study Documentation & YAML Ledgers**: Licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
- **Third-Party Citations & Media**: References to xAI, Grok Bot, and X broadcast recordings remain property of original rights holders. No raw media files or transcripts are bundled.
