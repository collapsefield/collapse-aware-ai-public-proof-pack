Collapse Aware AI — Public Proof Content (v0.1)

Supplementary material for the “Public Proof Pack” repository
(safe technical artefacts – no proprietary code)

A. Ablation Test Plan (Verifier Checklist)

Purpose: empirically confirm that enabling the Bias Layer produces reproducible, non-trivial behaviour deltas compared with identical Bias OFF runs.

Step	Description	Expected Outcome
1	Same build & same RNG seed	Baseline reproducibility confirmed
2	Run Bias = OFF → save logs	Control data
3	Run Bias = ON → save logs	Altered state trajectories
4	Compare entropy (H), policy KL divergence, ΔP(reaction	history)
5	Clear memory.json → rerun ON	Effect vanishes (proves state-dependence)
6	Insert decoy cues	Negligible effect (rules out heuristics)
B. Log Schema (JSON)

All logs use this public schema so any reviewer can parse them.

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


No weights, model parameters, or proprietary data are disclosed.

C. Synthetic Sample Records (illustrative only)

Bias OFF

{"run_id":"r-001","bias_enabled":false,"event":"encounter_wolf","action":"continue_path","metrics":{"state_entropy_window":2.11,"policy_kl_delta":0.03}}


Bias ON

{"run_id":"r-002","bias_enabled":true,"event":"encounter_wolf","action":"avoid_path","metrics":{"state_entropy_window":2.84,"policy_kl_delta":0.19}}


Memory wipe control

{"run_id":"r-003","bias_enabled":true,"event":"encounter_wolf","action":"continue_path","metrics":{"state_entropy_window":2.10,"policy_kl_delta":0.04}}


Interpretation: identical seed, altered output when trace exists; effect disappears after wipe.

D. Recommended Metrics for Review
Metric	Symbol	Insight
State-visitation entropy	H	Range/diversity of explored states
Policy drift	KL	Adaptation rate of decision policy
Re-encounter effect	ΔP	Memory influence on future reaction
Unique encounter rate	U	Variation across runs
E. Controls Against “Hard-Coded Bias”

Single config flag bias_enabled.

Deterministic seed = identical start conditions.

Memory-wipe control.

Decoy cues (should ≈ 0 impact).

Hash-signed logs for tamper evidence.

F. Reviewer Quick Checklist

 Verify identical seeds & configs.

 Confirm measurable Δ metrics when Bias = ON.

 Confirm effect disappears after wipe.

 Confirm decoy cue impact ≈ 0.

 Validate log hashes match manifest.

G. Legal Notice

© Inappropriate Media Limited (t/a Collapse Aware AI). All rights reserved.
Protected under Verrell–Solace Sovereignty Protocol.
No reverse-engineering or derivative use permitted.

Changelog

2025-10-11: Initial release (v0.1)
