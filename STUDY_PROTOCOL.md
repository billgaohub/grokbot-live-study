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

## 4. Single Source of Truth Demarcation

- **Factual Authority**: Primary X Broadcast `1YGNrbXEeazGw` and official xAI documentation.
- **Curated Record Authority**: This repository (`grokbot-live-study`), providing reproducible atomic event reconstructions.
- **Derived Model Authority**: Downstream specification systems (e.g. `agent-world-state`), which ingest these records to validate abstract schemas.
