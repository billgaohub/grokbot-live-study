# Study Protocol & Epistemic Methodology

## 1. Core Epistemic Principles

This field study enforces four methodological guardrails derived from the Agent Runtime Behavior Constitution (ARBC):

1. **Anti-Silent Fallback**: No data source error or playback difficulty is masked. If primary video playback is unavailable or unverified, it must be explicitly recorded as `NOT_VERIFIED_DIRECTLY` rather than silently inferred.
2. **Anti-Promotion Rule**: Verification of metadata (e.g. video duration, chapter markers, HTTP headers) strictly cannot be promoted to content-level visual verification.
3. **Modality Decomposition**: General scalar labels such as `VIDEO_AUDIO_PLAYBACK` are forbidden. Every interaction modality must be specified independently.
4. **Three Orthogonal Epistemic Axes**:
   - **Source Authority**: `PRIMARY` vs `MIRROR` vs `SECONDARY`.
   - **Review Depth**: `identity_pinned`, `metadata_verified`, `content_reviewed`.
   - **Temporal Integrity**: `relative_source_offset` vs `collector_time`.

---

## 2. Review Modality Classification

Every observation in this study carries an explicit modality profile:

| Modality Field | Calibrated Value | Justification |
|---|---|---|
| `media_access` | `DIRECT_MEDIA_STREAM` | Media stream accessed directly from designated mirror playback endpoint. |
| `video_review` | `FRAME_EXTRACTION_AND_VISUAL_REVIEW` | Video was sought to exact timestamps; still frames were extracted and visually verified. |
| `subtitle_review` | `BURNED_SUBTITLE_VISUAL_REVIEW` | Hardcoded bilingual subtitle text embedded within visual frames was parsed. |
| `audio_review` | `NOT_INDEPENDENTLY_REVIEWED` | No isolated digital audio track extraction, waveform analysis, or algorithmic transcription was executed. |

---

## 3. Observation Support Levels

Observations are graded into four strictly defined support levels:

1. **`PHYSICAL_EVIDENCE_VERIFIED`**:
   - Requires `content_reviewed: true`.
   - Direct matching between proposition and extracted video frame / screen action.
   - Example: OBS-008 (Amrita demonstrating cursor trajectory in Google Slides).
2. **`SECONDARY_CORROBORATED`**:
   - Derived from multi-source builder notes and corroborated against stream chapter boundaries.
   - Primary content not directly inspected frame-by-frame.
   - Example: OBS-001 (Challenge kickoff framing).
3. **`AUTHORITATIVE_DOC_ALIGNED`**:
   - Cross-checked against published official documentation (e.g. xAI official architecture overview).
4. **`UNVERIFIED`**:
   - Stated verbally during broadcast but unverifiable from external telemetry or visual frames.
   - Example: Zero-knowledge boundaries inside 1Password modal.

---

## 4. Single Source of Truth Demarcation & Epistemic Hierarchy

To prevent epistemological circularity and clarify authority boundaries:
- **Source Factual Authority**: Primary X Broadcast `1YGNrbXEeazGw` and official xAI technical documentation.
- **Media Mirror Reference**: Replay stream mirrors (e.g., Bilibili `BV19fYf6kELz` 31,513s) serving as timestamped physical playback mirrors.
- **Curated Field-Study Record Authority**: This repository (`grokbot-live-study`), providing calibrated, atomic, and reproducible event reconstructions.
- **Derived Model Authority**: Downstream specification and formal governance systems (e.g. `agent-world-state`), which ingest these records to validate abstract state transition models.

---

## 5. Phased Coverage Roadmap (Day 1, Day 2, Day 3)

### Scope Breakdown (~25 Total Hours)
1. **Day 1 (~08:45:13, BV19fYf6kELz / 31,513s)**:
   - Initial 90m slice: Complete (`OBS-001` to `OBS-016`).
   - Remainder (`T+01:30:00 → T+08:45:13`): Early game mechanics development, prompt tuning, initial web UI integration, developer coordination bottlenecks.
2. **Day 2 (~08:23:00)**:
   - Multi-agent swarm orchestration, specialized agent roles (marketing, sales, dev, customer support bots), code integration, test suite iteration.
3. **Day 3 (~07:58:00)**:
   - Live production release, real player gameplay, ~300 incoming pull requests, human-in-the-loop merge gate queuing, production bugs, and final showcase.

### Sampling & Extraction Protocol
To preserve high epistemic density without second-by-second transcription:
1. **Segment Indexing**: Map the continuous video stream into logical work sessions and milestone markers.
2. **Event Filtering**: Isolate state transitions, operational failures, human interventions, tool-call stalls, and architectural claims.
3. **Physical Probing**: Seek to exact timestamps and extract key visual frames verifying UI states.
4. **Third-Party Notes Policy**: Community summaries (e.g. `Roenel/Grok-Bot-Galaxy-Notes`) are strictly **discovery leads**, never factual authority. All assertions must be corroborated against primary footage.
5. **Cross-Day Synthesis**: Contrast early single-agent friction (Day 1) against multi-agent swarm coordination and human merge bottlenecks (Day 2/3).
