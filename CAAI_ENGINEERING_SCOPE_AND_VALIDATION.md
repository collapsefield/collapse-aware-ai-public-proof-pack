# CAAI Engineering Scope and Validation

**Last updated:** 2026-08-07  
**Status:** Current public engineering scope

## Purpose

This document states what the current Collapse Aware AI (CAAI) engineering line does, what can be tested now, and what remains outside the present managed-evaluation boundary.

## Current engineering position

Collapse Aware AI is proprietary middleware for **retained-state behavioural selection**.

It sits between a host system and an underlying model, scripted logic layer, simulation runtime or decision engine.

Its role is not simply to retrieve memory or generate text. Its role is to control how retained state is allowed to influence final selection among permitted behaviours while preserving inspectable reference and evidence paths.

The original **Phase-1 Core Gold Build remains the frozen selector foundation**. Around that foundation, a substantial Phase-2 continuity, recall, evidence and integration stack has now been implemented and exercised through the real selector.

## Demonstrated current capabilities

The current private engineering line includes demonstrated support for:

- candidate behaviour selection;
- retained-state influence;
- Studio/reference and governed operating conditions;
- persistence and recall across restart;
- deterministic seed capture and replay;
- retained-state revision and revocation;
- strong anchors, continuity memory and session boot;
- explicit memory-use / boot-consumption evidence;
- bounded ambiguity and clarification routing;
- recall routing, judging, corrective recall and revoked-context protection;
- controlled forgetting / lifecycle handling;
- agency-impact and productive-friction routing;
- evaluation metrics and consolidated observability;
- durable private Decision Records;
- formal Phase-2 integration contract;
- live Phase-2 → Core selection through the real frozen selector;
- customer-safe Decision Record projection;
- Phase-2 post-decision receipts;
- failure, replay, restart, duplicate and reconciliation hardening;
- one guided local managed-evaluation workflow;
- customer-safe JSON, HTML and PDF evidence exports.

## Current public runtime shape

```text
Host / application
        ↓
Current event + permitted candidates
        ↓
Phase-2 retained-state / continuity sidecar
        ↓
CAAI integration boundary
        ↓
Sealed Crown/Core final selector
        ↓
Durable private Decision Record
        ↓
Customer-safe Decision Record
        ↓
Managed evaluation comparison / export
```

Private scoring systems, thresholds, production tuning, Crown internals and proprietary implementation mechanics remain sealed.

## Live validation result

A controlled synthetic live evaluation held the following constant:

- prompt;
- candidate IDs;
- candidate text;
- candidate order;
- mapped thread;
- deterministic seed.

The reference condition selected `candidate_A`.

The governed retained-state condition selected `candidate_B`.

This demonstrates live end-to-end divergence through the real selector path under the declared comparison conditions.

The conditions changed both operating mode and retained-state-influence configuration, so the result is not described as isolated single-factor causality.

## What validation means now

Relevant technical evaluation can test:

1. **Retained-state influence** — whether prior state changes later selection under controlled matched present conditions.
2. **Reference-versus-governed comparison** — whether declared operating conditions produce inspectable differences.
3. **Persistence** — whether retained state and committed records survive restart.
4. **Deterministic replay** — whether canonical controlled conditions reproduce the expected selection behaviour where determinism is promised.
5. **Revision / revocation** — whether corrected or revoked state is handled without silently rewriting history.
6. **Recall quality** — whether wrong-scope, stale, contradicted or revoked state can be blocked before influence.
7. **Decision evidence** — whether committed selections produce durable records and customer-safe projections.
8. **Failure honesty** — whether dependency failure, ambiguous delivery and downstream errors preserve already-committed facts rather than fabricating success/failure.
9. **Duplicate protection** — whether repeated operator actions avoid silent duplicate decisions.
10. **Managed-evaluation operation** — whether the end-to-end workflow can run from preflight through customer-safe export.

## What CAAI is not

The current system is not presented as:

- a foundation model;
- a vector database;
- standard RAG;
- long-context prompting;
- a complete autonomous-agent platform;
- public SaaS;
- production multi-tenancy;
- finished customer-hosted deployment;
- high-availability certification;
- remote-security certification;
- a claim of AGI or machine consciousness;
- proof of Verrell’s Law as established physics;
- proof of a universal or non-local memory field;
- a universal hallucination cure;
- a universal emotion or deception detector;
- a guarantee of lower token cost for every deployment;
- complete causal proof for every internal contribution.

## Phase-2 boundary

Phase-2 is no longer accurately described as merely mapped/specifed.

Implemented and evidenced Phase-2 work now includes retained-state lifecycle, continuity, recall quality, ambiguity handling, agency-impact routing, evaluation/observability, live integration and customer-safe evidence linkage.

Broader Phase-2 / Phase-2+ concepts still requiring separate future evidence include:

- outcome recording and bounded reinforcement;
- buyer-specific production Governor configuration;
- broader semantic matching;
- domain-specific long-horizon optimisation;
- affective signal inputs;
- robotics / embodied inputs;
- behavioural-consistency research;
- customer-hosted production packaging;
- remote security, authentication and tenant isolation.

## Relationship to Verrell’s Law

Verrell’s Law and CAAI remain separate evidence tracks.

> Verrell’s Law = proposed falsifiable retained-state selection research framework.  
> Collapse Aware AI = practical proprietary engineering middleware.

CAAI can be evaluated entirely through software behaviour without accepting speculative physical interpretation.

## Commercial evaluation question

The licensing-relevant engineering question is now:

> **Can retained history produce useful, controlled and inspectable changes in final selection for a buyer system that already has legitimate candidate actions, outputs or interventions?**

The current managed-evaluation package exists to answer that question with a bounded buyer-specific scenario.

See also:

- [Current Engineering State](CURRENT_ENGINEERING_STATE_2026-08-07.md)
- [Managed Evaluation Evidence](MANAGED_EVALUATION_EVIDENCE_2026-08-07.md)
