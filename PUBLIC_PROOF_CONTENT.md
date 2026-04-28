# Collapse Aware AI — Public Proof Content (v0.2)

**Document type:** Supplementary public proof material  
**Project:** Collapse Aware AI (CAAI)  
**Author / origin:** Marcos Verrell Moss Ross (M.R.)  
**Entity:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Status:** Public-safe technical artefacts only  
**Last updated:** 2026-04-28  

---

## Security / Authorship Notice

This file forms part of the public proof and authorship record for **Collapse Aware AI**.

No proprietary Crown kernel code, private scoring logic, internal thresholds, weighting formulas, or implementation-sensitive algorithms are disclosed here.

**Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved.**

© Marcos Verrell Moss Ross / Inappropriate Media Limited. All rights reserved.

---

## A. Ablation Test Plan — Verifier Checklist

**Purpose:** empirically confirm that enabling the Bias Layer produces reproducible, non-trivial behaviour deltas compared with identical Bias OFF runs.

| Step | Description | Expected outcome |
|---:|---|---|
| 1 | Same build and same RNG seed | Baseline reproducibility confirmed |
| 2 | Run `bias_enabled = false` and save logs | Control data captured |
| 3 | Run `bias_enabled = true` and save logs | Altered state trajectories captured |
| 4 | Compare entropy, policy KL divergence, and memory-linked reaction deltas | Measurable difference visible |
| 5 | Clear `memory.json` and rerun Bias ON | Effect vanishes or reduces, proving state-dependence |
| 6 | Insert decoy cues | Negligible effect, reducing hard-coded heuristic risk |

---

## B. Public Log Schema

All public verification logs should follow a parseable schema like the example below.

```json
{
  "run_id": "uuid",
  "seed": 101,
  "bias_enabled": true,
  "tick": 540,
  "actor_id": "npc_07",
  "location_id": "forest_nw",
  "event": "encounter_wolf",
  "trace_context": {
    "recent_tags": ["wolf_sighting"],
    "time_since_last_encounter_sec": 57.9
  },
  "action": "avoid_path",
  "metrics": {
    "state_entropy_window": 2.84,
    "policy_kl_delta": 0.19,
    "reencounter_flag": true
  },
  "hash": "sha256:..."
}
```

No weights, model parameters, proprietary data, or private Crown internals are disclosed.

---

## C. Synthetic Sample Records

These records are illustrative only. They show the type of behaviour delta expected from a public-safe verification run.

### Bias OFF

```json
{
  "run_id": "r-001",
  "bias_enabled": false,
  "event": "encounter_wolf",
  "action": "continue_path",
  "metrics": {
    "state_entropy_window": 2.11,
    "policy_kl_delta": 0.03
  }
}
```

### Bias ON

```json
{
  "run_id": "r-002",
  "bias_enabled": true,
  "event": "encounter_wolf",
  "action": "avoid_path",
  "metrics": {
    "state_entropy_window": 2.84,
    "policy_kl_delta": 0.19
  }
}
```

### Memory Wipe Control

```json
{
  "run_id": "r-003",
  "bias_enabled": true,
  "event": "encounter_wolf",
  "action": "continue_path",
  "metrics": {
    "state_entropy_window": 2.10,
    "policy_kl_delta": 0.04
  }
}
```

### Interpretation

With identical seed and comparable setup:

- Bias OFF provides baseline behaviour.
- Bias ON changes the behavioural trajectory when relevant memory trace exists.
- Memory wipe reduces or removes the effect.
- Decoy cues should have little or no effect.

This supports the public claim that behaviour is influenced by stored trace state rather than simple hard-coded response branching.

---

## D. Recommended Public Metrics

| Metric | Symbol | Insight |
|---|---:|---|
| State-visitation entropy | `H` | Range and diversity of explored states |
| Policy drift | `KL` | Adaptation rate of decision policy |
| Re-encounter effect | `ΔP` | Memory influence on future reaction |
| Unique encounter rate | `U` | Variation across runs |
| Bias divergence | `ΔB` | Difference between Bias OFF and Bias ON trajectories |

---

## E. Controls Against Hard-Coded Bias

Recommended public controls:

- Single config flag: `bias_enabled`
- Deterministic seed for identical start conditions
- Memory-wipe control
- Decoy cues with near-zero expected impact
- Hash-signed logs for tamper evidence
- Repeated runs under the same scenario
- Public checksum records where appropriate

---

## F. Reviewer Quick Checklist

A reviewer should be able to verify:

- [ ] Identical seeds and configs were used.
- [ ] Bias OFF and Bias ON runs were separated clearly.
- [ ] Measurable metric deltas appear when Bias is ON.
- [ ] The effect reduces or disappears after memory wipe.
- [ ] Decoy cue impact is negligible.
- [ ] Log hashes match the published manifest.
- [ ] No proprietary kernel internals are exposed.

---

## G. Legal Notice

© Marcos Verrell Moss Ross / Inappropriate Media Limited (t/a Collapse Aware AI). All rights reserved.

Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved.

No reverse-engineering, derivative commercial use, rebranding, or extraction of the architecture is permitted without explicit written consent.

---

## Changelog

| Date | Version | Change |
|---|---:|---|
| 2025-10-11 | v0.1 | Initial release |
| 2026-04-28 | v0.2 | Reformatted for GitHub readability; converted verifier steps and metrics into tables; cleaned JSON examples; strengthened authorship/security notice |
