# Grok Bot Live Study: Empirical Field Reconstruction (xAI Galaxy 3-Day Sprint)

[![Status](https://img.shields.io/badge/status-EMPIRICALLY_VERIFIED-brightgreen.svg)](STUDY_PROTOCOL.md)
[![Scope](https://img.shields.io/badge/current%20scope-Day_1_First_90m-blue.svg)](timeline/day-1.md)
[![Lifecycle](https://img.shields.io/badge/lifecycle-ACTIVE__FIELD__STUDY-blue.svg)](#lifecycle-state--evolution-roadmap)
[![License](https://img.shields.io/badge/license-MIT%20%2F%20CC%20BY%204.0-green.svg)](LICENSE)

> **Grok Bot Live Study** is an evidence-first, curated field-study repository reconstructing xAI's **Grok Bot Galaxy** live-build sprint (September 15–17, 2026). It documents atomic observations, propositional claims, human approval gate latency, operational failures, multi-agent coordination, and human-steered recovery loops.

---

## 1. Single Source of Truth (SSOT) Authority Hierarchy

To prevent epistemological circularity, this repository operates under a strict three-tier authority model:

```text
Primary X Broadcast (1YGNrbXEeazGw) & Mirrors
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

## 2. Event Scope, Lifecycle State & Evolution Roadmap

### 3-Day Full Event Landscape (~25 Hours)
The official xAI Grok Bot Galaxy event ran across three consecutive days (September 15–17, 2026), comprising roughly **25 hours of continuous field stream**:
- **Day 1**: ~08:45:13 (31,513s, Replay mirror `BV19fYf6kELz`): Kickoff, agent setup, Google Slides cursor demonstrations, approval gate latencies, and initial Google Form failure/recovery.
- **Day 2**: ~08:23:00: Deep multi-agent build sprint, bot swarm orchestration, specialized roles (marketing, sales, support bots), and codebase integration.
- **Day 3**: ~07:58:00: Live production launch, real player gameplay, ~300 incoming PRs, merge bottlenecks, launch bugs, and final showcase.

### Lifecycle State
This study is an **`ACTIVE_FIELD_STUDY`** progressing through phased historical reconstruction:

| Dimension | Current Epistemic Status | Scope Target |
|---|---|---|
| **Repository Existence** | `VERIFIED` | Public citable research repository |
| **Public Entry v0.1** | `VERIFIED` | Initial calibrated release |
| **Day 1 First 90m** | `VERIFIED` (16 atomic observations) | Initial kickoff & permission failure |
| **Day 1 Full Coverage** | `INCOMPLETE` | ~08:45:13 full broadcast |
| **Day 2 Coverage** | `NOT YET STUDIED` | ~08:23:00 multi-agent sprint |
| **Day 3 Coverage** | `NOT YET STUDIED` | ~07:58:00 launch, 300 PRs & showcase |
| **3-Day Cross-Day Synthesis** | `NOT STARTED` | Multi-agent coordination patterns |
| **Operational Decision** | **`PROCEED`** | Phased empirical coverage expansion |

### Target Repository Architecture
As full 3-day coverage expands, the repository structure evolves into a day-partitioned hierarchy:

```text
grokbot-live-study/
├── timeline/
│   ├── day-1.md                        # Day 1 timeline (T+00:00:00 to T+08:45:13)
│   ├── day-2.md                        # Day 2 timeline (T+00:00:00 to T+08:23:00)
│   └── day-3.md                        # Day 3 timeline (T+00:00:00 to T+07:58:00)
├── observations/
│   ├── day-1.yaml                      # Atomic observations for Day 1
│   ├── day-2.yaml                      # Atomic observations for Day 2
│   └── day-3.yaml                      # Atomic observations for Day 3
├── analyses/
│   ├── day-1.md                        # Day 1 focused analysis
│   ├── day-2.md                        # Day 2 focused analysis
│   ├── day-3.md                        # Day 3 focused analysis
│   └── cross-day-synthesis.md          # 3-Day unified multi-agent synthesis
├── corrections/
│   └── correction-ledger.yaml          # Formal claim corrections & calibrations
└── STUDY_PROTOCOL.md                   # Epistemic axes & sampling methodology
```

### Phased Empirical Methodology (Anti-Mechanical Transcribing)
We explicitly reject mechanical second-by-second transcription of 25 hours of video. Instead, we enforce our proven risk-weighted extraction pipeline:

$$\text{Full Source Access} \longrightarrow \text{Segment Demarcation} \longrightarrow \text{Critical Event Extraction} \longrightarrow \text{Atomic Observation} \longrightarrow \text{Physical Frame Review} \longrightarrow \text{Claim/Contradiction Audit} \longrightarrow \text{Cross-Day Synthesis}$$

- **Third-Party Notes Policy**: Independent public community summaries (e.g. `Roenel/Grok-Bot-Galaxy-Notes`) serve strictly as **discovery leads and index markers**, never as factual authority. Every observation promoted to this study requires physical verification against primary media streams.
- **Priority Research Phenomena**: Focus compute on high-leverage architectural phenomena:
  - Production deployment gates and user feedback friction
  - Multi-bot orchestration bottlenecks (marketing/sales/dev roles)
  - Human merge gates and PR review queues (~300 PRs on Day 3)
  - Failure recovery loops, rollback events, and runtime bugs

### Calibrated Review Modalities (v0.1 Baseline)
- **`media_access`**: `DIRECT_MEDIA_STREAM` (via Bilibili mirror `BV19fYf6kELz`, duration 31,513s / 08:45:13)
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
│   └── day-1.yaml                     # 16 atomic observations with orthogonal axes
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
