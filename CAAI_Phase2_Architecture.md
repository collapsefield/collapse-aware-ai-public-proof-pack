# Collapse Aware AI — Phase-2 Public Architecture

**Company:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Status:** Public-safe high-level architecture  
**Updated:** 7 August 2026

This document describes the **current public-safe Phase-2 architecture** of Collapse Aware AI (CAAI).

It intentionally omits Crown source, private scoring logic, exact coefficients, thresholds, internal database layouts and proprietary deployment mechanics.

---

## 1. Current architecture position

Phase-2 is no longer only a future concept.

The private engineering line now contains implemented, accepted and live-integrated Phase-2 modules around the frozen Core Gold / Crown selector.

The public-safe architecture is:

```text
Host / application
      ↓
Current event + permitted candidate behaviours
      ↓
Phase-2 retained-state / continuity sidecar
      ↓
Recall / correction / interpretation / agency controls
      ↓
Structured retained-state influence
      ↓
CAAI integration contract / adapter boundary
      ↓
Sealed Crown/Core final selector
      ↓
Durable private Decision Record
      ↓
Customer-safe Decision Record projection
      ↓
Phase-2 post-decision receipt
      ↓
Evaluation Forge comparison / export
```

The **selector remains the centre of gravity**. Phase-2 improves the quality, lifecycle, recall, interpretation and evidence around the retained state that can influence final selection.

---

## 2. Host-system boundary

CAAI does not need to generate the world or invent every action.

The host supplies:

- the current event / state;
- the permitted candidate behaviours or actions;
- domain truth and policy;
- the authority to execute any external action.

CAAI supplies:

- structured retained-state handling;
- revision / revocation;
- bounded recall and correction;
- continuity state;
- ambiguity / clarification posture;
- bounded agency-impact routing;
- retained-state influence into final candidate selection;
- durable selection evidence;
- managed evaluation / comparison tooling.

This boundary is important: CAAI **selects among permitted candidates**. It does not automatically replace the host system, base model, game engine or domain policy.

---

## 3. Retained-state substrate

The implemented Phase-2 direction treats retained state as governed, versioned state rather than an undifferentiated transcript dump.

Public-safe retained-state classes include:

### Weighted Moments

Important retained events with explicit lifecycle and revision history.

Supported revision directions include:

- reinforce;
- weaken;
- reframe;
- resolve;
- split;
- merge;
- revoke;
- retire/archive;
- no-update.

The engineering rule is:

> **A remembered event can remain historically real while its current meaning or influence changes.**

### Strong Anchors

Higher-persistence reference state for stable facts, project direction, role, relationship or declared policy.

Anchors are not unchallengeable beliefs and must remain revisable / governable.

### Continuity Memory

Compact active state required for useful cross-session continuity.

### Session Boot

A bounded session-start snapshot of relevant anchors, unresolved moments, current corrections and continuity state.

The objective is useful continuity without requiring raw transcript replay as the only mechanism.

---

## 4. Memory honesty and recall quality

Phase-2 separates **storage**, **retrieval**, **admission** and **use evidence**.

A stored item is not automatically relevant.

A retrieved item is not automatically permitted to influence selection.

Implemented public-safe functions include:

### Recall Router

Determines whether recall is required and which bounded state scope should be queried.

### Memory Judge

Checks returned state for relevance, contradiction, lifecycle state, scope and sufficiency before admission.

### Corrective Recall Layer

Preserves correction history and provenance rather than treating older wrong state as equally current.

### Revoked Context Guard

Known revoked / superseded state is prevented from re-entering active influence.

### Controlled Forgetting / lifecycle handling

State can be downgraded, archived or retired under explicit lifecycle rules.

### Explicit memory-use evidence

Phase-2 distinguishes between state being included in boot/retrieval and a caller explicitly reporting it as consumed, considered, ignored, rejected or unused.

It does not claim access to hidden model attention or chain-of-thought.

---

## 5. Ambiguity and confidence posture

Phase-2 can hold multiple plausible interpretations rather than turning the first plausible reading into fact.

Implemented public-safe behaviour includes:

- bounded interpretation sets;
- confidence-aware comparison;
- clarification when missing information materially affects action;
- safe common-path behaviour where ambiguity does not matter;
- high-impact deferral where uncertainty remains material;
- provisional / low-confidence memory-write decisions.

The engineering rule is:

> **Plausible is not the same as confirmed.**

No claim is made that CAAI has unrestricted semantic understanding or direct access to hidden human intent.

---

## 6. Agency-impact and productive-friction routing

The Phase-2 agency layer determines **how much intervention or completion is appropriate**, not whether a user is psychologically dependent.

Public-safe routing can distinguish between:

- direct answer;
- direct completion;
- draft only;
- preview before action;
- hint;
- scaffold;
- staged guidance;
- clarification;
- bounded options;
- defer;
- human review;
- block;
- safety-direct support.

The route must not exceed declared authority.

Routine low-impact work should not be burdened with unnecessary friction. Learning / judgement contexts may justify scaffolding, while urgent safety-relevant support should not be withheld for the sake of “teaching”.

CAAI does not infer dependency or mental state merely from repetition, bluntness, age, disability, urgency or emotional tone.

---

## 7. Final selection boundary

The host provides the candidate set.

The frozen Crown/Core pathway remains the actual final behavioural selector.

The integrated Phase-2 path maps bounded retained state and declared conditions into that real selector without moving selection logic into a second adapter-side selector.

A live controlled synthetic evaluation has demonstrated:

```text
same prompt
same candidate set
same candidate text/order
same mapped thread
same deterministic seed
```

with a reference condition selecting:

```text
candidate_A
```

and a governed retained-state condition selecting:

```text
candidate_B
```

The comparison changed both operating mode and retained-state-influence configuration, so the evidence demonstrates **live end-to-end divergence**, not isolated single-factor causality.

---

## 8. Decision Records and evidence

A committed live selection produces a durable private Decision Record.

The accepted evidence layer can project that private record into a **customer-safe Decision Record** without exposing sealed Crown internals.

The Phase-2 evidence chain can bind:

```text
retained-state package
→ mapped thread / selection request
→ private decision
→ customer-safe public decision evidence
→ Phase-2 post-decision receipt
→ Evaluation Forge comparison bundle
```

The purpose is to record operations and committed outcomes rather than generate an explanation-shaped story from a second implementation.

A Decision Record is not automatically a complete causal explanation. Strong “X caused Y” wording requires an appropriate counterfactual method.

---

## 9. Evaluation Forge and observability

The Phase-2 Evaluation Forge provides public-safe concepts for:

- versioned scenarios;
- versioned metric definitions;
- controlled comparisons;
- ablation planning;
- run evidence;
- consolidated observability;
- customer-safe JSON / HTML / PDF evidence.

The current managed-evaluation workflow can perform:

```text
preflight
→ scenario validation
→ retained-state preparation
→ reference selection
→ governed selection
→ Decision Record retrieval
→ customer-safe projection
→ Phase-2 receipts
→ comparison
→ export
```

The packaged workflow is local and bounded.

---

## 10. Failure, replay and restart behaviour

The integrated path has been exercised under controlled cases covering:

- malformed input;
- revoked / wrong-scope state;
- dependency failure;
- ambiguous delivery;
- no-blind-retry policy;
- replay under matched canonical conditions;
- duplicate request protection;
- connector / selector / evidence-layer restart;
- full-stack restart;
- downstream receipt failure after upstream commit;
- customer-safe projection failure without rewriting an already committed Core decision.

The guiding rule is:

> **A later-stage failure must never erase or rewrite an earlier committed fact.**

These tests are local engineering evidence, not formal high-availability or disaster-recovery certification.

---

## 11. Current managed-evaluation boundary

The accepted integrated package is intended for:

- synthetic demonstrations;
- CAAI-operated managed evaluations;
- bounded buyer-supplied test scenarios;
- paid pilot design;
- integration and licensing discussions.

It is not currently presented as:

- public SaaS;
- unrestricted remote API access;
- production multi-tenancy;
- finished customer-hosted deployment;
- production HA / SLA certification;
- regulatory certification.

---

## 12. Remaining Phase-2 / Phase-2+ work

The current core Phase-2 engineering line is substantial, but broader roadmap items remain future, optional or buyer-driven.

Examples include:

- outcome recording and bounded reinforcement;
- customer-specific production Governor configuration;
- broader semantic matching beyond current bounded mechanisms;
- domain-specific long-horizon optimisation;
- affective signal inputs with appropriate consent / validation;
- robotics / embodied-system inputs;
- behavioural-consistency research;
- remote security / authentication / tenant isolation;
- customer-hosted production packaging.

None of those should be treated as already delivered unless separately implemented and evidenced later.

---

## 13. Claim boundary

Phase-2 does not claim:

- consciousness or sentience;
- AGI;
- direct knowledge of human inner state;
- universal emotion or deception detection;
- quantum / electromagnetic memory as established engineering mechanism;
- regulatory compliance by default;
- calibrated real-world truth probabilities;
- universal model improvement;
- complete causal explanation of every selection.

The public engineering claim is narrower:

> **CAAI provides an integrated retained-state selection architecture in which relevant prior state can influence which permitted behaviour the real selector chooses, while reference conditions, durable records and customer-safe evidence remain inspectable.**

---

## 14. IP and disclosure boundary

Public architecture intentionally omits:

- Crown/Core source;
- exact proprietary score functions;
- private coefficients and thresholds;
- private schemas not required for review;
- runtime ZIPs;
- credentials;
- internal databases;
- detailed implementation mechanics sufficient to reproduce the product.

Commercial access, managed evaluation and integration are available by agreement with **Inappropriate Media Limited (t/a Collapse Aware AI)**.

© 2025–2026 Inappropriate Media Limited. All rights reserved.
