# Collapse Aware AI™ — Engineering Evidence and Priority Position

**Date:** 30 August 2026  
**Organisation:** Inappropriate Media Limited  
**Programme:** Collapse Aware AI™ (CAAI)  
**Status:** Public-safe evidence / priority record

---

## Purpose

This note records what Collapse Aware AI™ has demonstrated in software, what that evidence means, and what is — and is not — claimed about originality.

It is deliberately narrower than a claim that history-dependent decision-making itself is new. History-dependent policies, finite-memory policies, path-dependent control and memory-conditioned action selection have substantial prior art.

The position recorded here is the specific CAAI engineering formulation and evidence package.

---

## Demonstrated CAAI Engineering Result

In controlled CAAI software tests, retained prior state has been shown to be behaviourally consequential at the final-selection layer.

Within the accepted tested conditions, CAAI has demonstrated that:

1. **retained prior state can measurably alter which host-permitted candidate is selected;**
2. **reference and retained-state-enabled conditions can be compared directly;**
3. **retained-state influence can be disabled, revised or revoked so that its contribution is testable rather than merely asserted;**
4. **local selection can be replayed in tested deterministic conditions;**
5. **selection can remain bounded to the host-supplied permitted candidate set;**
6. **Decision Records and customer-safe evidence can preserve the selection result and relevant evaluation lineage;**
7. **retained history can influence selection without automatically becoming authority.**

Compactly:

```text
same present condition
+ bounded permitted candidate set
+ different retained history
→ measurable selection difference

then

retained-state influence disabled / revised / revoked
→ comparison/reference behaviour
→ replay
→ inspectable evidence
```

The engineering principle is:

> **Retained history is eligible evidence, not automatic authority.**

---

## Evidence Class

These results constitute **engineering conformance / implementation evidence** for governed retained-state selection in CAAI.

They are not dismissed as trivial merely because the software was deliberately designed to implement retained-state influence. They establish that the architecture can be implemented, bounded, exercised, ablated, replayed and evidenced as software.

However, where the selector's own internal retained-state score is also used as the predictor in the analysis, the result is not by itself an independent empirical test of the broader Verrell's Law relation.

A stronger independent Verrell's Law test requires a retained-state compatibility measure frozen independently of the confirmatory selection outcome, or another non-circular empirical route.

---

## Relationship to Verrell's Law

The current evidence ladder is:

```text
1. Retained-State Selection mechanism in CAAI
   DEMONSTRATED IN TESTED SOFTWARE CONDITIONS

2. Governed retained-state selection architecture
   DEMONSTRATED IN TESTED SOFTWARE CONDITIONS

3. Computational analogue relevant to Verrell's Law
   SUPPORTED BY CAAI ENGINEERING RESULTS

4. Canonical quantitative Verrell's Law relation
   NOT YET INDEPENDENTLY VALIDATED OUTSIDE THE CONSTRUCTED SELECTOR

5. Wider biological / physical interpretations
   OPEN RESEARCH
```

CAAI therefore supplies direct engineering evidence for the computational retained-state selection mechanism. It does not convert that software result into proof of a universal law of cognition, biology or physics.

---

## Originality / Priority Boundary

CAAI does **not** claim invention of:

- history-dependent policies;
- finite-memory control;
- POMDP belief-state decision-making;
- hysteresis;
- reinforcement learning;
- candidate scoring;
- action verification;
- runtime policy engines;
- memory retrieval;
- path-dependent behaviour generally.

Relevant adjacent precedents include long-established history-dependent policies in POMDP research and later systems that use past interaction history when choosing or verifying actions.

A particularly close public example is **HAVE (History-Aware VErifier, CoRL 2025)**, which explicitly separates candidate action generation from a history-aware verifier that selects among proposed robot actions using past interactions.

Other adjacent 2026 work includes runtime path governance and trusted action-boundary systems that keep operational authority outside the generative model.

These precedents mean a global statement such as **"CAAI is the first system ever to use history to influence action selection"** would be unsupported.

The narrower CAAI priority position recorded here is the public formulation and demonstrated combination of:

- a host-supplied bounded permitted candidate set;
- retained state treated as candidate-relative influence rather than automatic authority;
- an explicit retained-state-disabled reference condition;
- governed final selection outside the generative component;
- retained-state lifecycle controls including revision/revocation in the accepted lineage;
- deterministic/repeatable local selection where applicable;
- replay and durable Decision Records/evidence;
- a commercial middleware boundary in which the host retains world truth, candidate permission and external execution authority.

As of this record, a prior-art review has identified adjacent components and close neighbours, but **has not established an earlier public system presenting this exact CAAI combination and evidence framing as one named retained-state middleware architecture**.

That is a bounded priority statement, not a universal novelty claim.

---

## Active WEL / AIW Relationship

**Weighted Emergence Layering (WEL)** and **Active Information Weight (AIW)** remain active CAAI/Evolution 2 concepts beneath the broader Governed Retained-State Selection framing.

They are not required as buyer-facing vocabulary, and this note does not disclose their protected implementation mechanics, scoring functions, thresholds or tuning.

---

## Why the Result Matters

The engineering distinction is not simply that software can remember.

The stronger practical question is:

> **When several actions are already permitted, can retained history be allowed to change which one wins without allowing memory itself to become authority — and can that change be compared, replayed and evidenced?**

CAAI's tested engineering record answers that question affirmatively within its declared software conditions.

Whether this formulation becomes a broader research category will depend on independent adoption, replication, comparison and use by others. This document records the CAAI position and evidence available by 30 August 2026 without claiming field-wide acceptance that does not yet exist.

---

## Public References

- CAAI Public Proof Pack: https://github.com/collapsefield/collapse-aware-ai-public-proof-pack
- Retained-State Selection Benchmark v0.1: https://github.com/collapsefield/collapsefield-verrells-law/blob/main/RETAINED_STATE_SELECTION_BENCHMARK_v0.1.md
- Verrell's Law Empirical Identification Clarification v1.0: https://github.com/collapsefield/collapsefield-verrells-law/blob/main/VERRELLS_LAW_EMPIRICAL_IDENTIFICATION_CLARIFICATION_v1.0.md
- Memory-Weighted Selection: https://github.com/collapsefield/memory-weighted-selection
- HAVE (CoRL 2025): https://proceedings.mlr.press/v305/li25e.html
- Runtime Governance for AI Agents: Policies on Paths (2026): https://arxiv.org/abs/2603.16586
- Runtime Governance for Agentic AI: Action-Boundary Control with Trusted Provenance and Fail-Closed Execution (2026): https://arxiv.org/abs/2608.16891

---

## Public / Proprietary Boundary

This record describes evidence classes, demonstrated behaviour and architectural boundaries only.

It does not publish Crown/Core source, private scoring implementation, exact thresholds/tuning, protected runtime packages, unrestricted schemas or implementation detail sufficient to reproduce the private commercial system.

© 2025–2026 Inappropriate Media Limited. Collapse Aware AI™. All proprietary implementation and commercial rights reserved.
