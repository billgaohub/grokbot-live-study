# Derived Analytical Rules & Hypotheses

**Analysis Scope**: Empirical derivations synthesized from the Day 1 initial 90-minute study window.  
**Epistemic Standing**: Bounded hypotheses derived from real observation (`HYPOTHESIS`); not asserted as universal laws.  

---

## 1. Environmental Default Configuration Blindness (`RULE-HYPO-001`)

### Statement
Autonomous agents operating in rich external GUI applications (such as Google Forms, cloud consoles, or SaaS dashboards) often inherit default application states (e.g., domain-restricted sharing, private workspace access, local file scopes). Without explicit prompt constraints or environment-aware preflight checks, agents tend to equate the physical *generation* of an artifact (e.g., producing a QR code image) with *task completion*. They remain blind to external accessibility barriers until out-of-band feedback is received.

### Supporting Empirical Evidence
- **`OBS-012`**: Data Dan completed form creation and rendered a QR code on screen.
- **`OBS-013`**: External audience encountered immediate "Permission Denied" errors because the form defaulted to internal workspace permissions.

### Boundary & Implication
- **Observed Scope**: 1 live unscripted demonstration.
- **System Design Implication**: Production agent architectures must decouple artifact generation from permission verification. Preflight permission assertions should be mandatory before exposing endpoints externally.

---

## 2. Steering Asymmetry in Human Intervention (`RULE-HYPO-002`)

### Statement
In multi-step failure recovery, human intervention achieves maximal leverage and lowest cognitive overhead when delivering high-level **intent-oriented semantic corrections** (e.g., *"make link public"*), rather than step-by-step GUI micromanagement (e.g., *"click settings, scroll down, toggle general access dropdown"*). This effectively exploits the agent's local perceptual-action loop while preserving human supervisory bandwidth.

### Supporting Empirical Evidence
- **`OBS-014`**: Presenter Amrita issued a concise text instruction: *"let's make sure this link is public"*.
- **`OBS-015`**: The agent autonomously traversed the Google Forms settings modal, updated the general access toggle to public, and verified external audience submissions.

### Boundary & Implication
- **Observed Scope**: Single live presenter intervention during broadcast.
- **System Design Implication**: Human-in-the-loop interfaces should prioritize semantic goal-steering over low-level coordinate remote-control.
