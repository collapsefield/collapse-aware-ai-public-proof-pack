# CAAI Engineering Scope and Validation

**Last updated:** 2026-07-26  
**Status:** Current public engineering scope

## Purpose

This document states what the current Collapse Aware AI (CAAI) Phase-1 Core Gold Build does, what can be tested, and what remains outside the present build.

## Current Engineering Position

Collapse Aware AI is proprietary, engine-agnostic middleware for **governed retained-state behavioural selection**.

It sits between a host system and an underlying model, scripted logic layer, simulation runtime, or decision engine.

Its role is not simply to retrieve memory or generate text. Its role is to govern how retained state is allowed to influence future behavioural selection.

## Demonstrated Phase-1 Core Gold Build Capabilities

The current completed Core Gold Build includes demonstrated support for:

- candidate behaviour selection;
- retained-state influence;
- governor-controlled behaviour;
- governed and studio operating modes;
- persistence and recall across restart;
- deterministic seed capture and replay;
- bias-on / bias-off behavioural divergence;
- request validation;
- request/runtime traceability;
- explicit degraded-mode and fallback reporting;
- stable JSON/API integration between host, adapter and Crown runtime.

The current public runtime shape is:

```text
Host system / UI / engine
        ↓
Structured input payload
        ↓
Candidate behaviours / possible outputs
        ↓
Retained-state influence
        ↓
Governor constraints
        ↓
Selected behaviour
        ↓
Diagnostic evidence / fallback status
        ↓
Persistent state update
```

Private scoring systems, thresholds, production tuning, Crown internals and proprietary implementation mechanics remain sealed.

## What Validation Means

The Core Gold Build should be evaluated through controlled engineering evidence rather than broad claims about intelligence or consciousness.

Relevant tests include:

1. **Retained-state influence** — whether prior state changes later selection under matched present conditions.
2. **Governor effect** — whether governed and studio modes produce measurable behavioural differences.
3. **Persistence** — whether retained state survives restart and remains available through recall.
4. **Deterministic replay** — whether a captured seed can reproduce the intended selection path.
5. **Validation handling** — whether malformed requests are rejected cleanly.
6. **Fallback honesty** — whether degraded operation is reported explicitly rather than hidden behind fabricated success.
7. **Integration evidence** — whether the system operates through its intended host → API/adapter → Crown chain.

## What CAAI Is Not

The current Core Gold Build is not:

- a foundation model;
- a vector database;
- standard RAG;
- long-context prompting;
- a finished AAA NPC brain;
- a complete autonomous-agent platform;
- the full Phase-2 architecture;
- a claim of AGI or machine consciousness;
- proof of Verrell’s Law as physics;
- proof of a universal or non-local memory field;
- a general hallucination cure;
- a guarantee of lower token cost for every deployment.

## Relationship to Verrell’s Law

Verrell’s Law and CAAI are connected but separate.

> Verrell’s Law = falsifiable retained-state selection research framework.  
> Collapse Aware AI = practical engineering middleware.

CAAI can be evaluated entirely through software behaviour without accepting any speculative physical interpretation of Verrell’s Law.

## Phase 2 Boundary

Weighted Emergence Layering (WEL) and broader Phase-2 capabilities are a separate development track.

Phase 2 is mapped, specified and under incremental development, but Phase-2 concepts must not be presented as features of the current Phase-1 Core Gold Build unless separately implemented and demonstrated.

## Commercial Evaluation Question

The central practical question is:

> Can governed retained state improve behavioural continuity and selection control in a host system that already has candidate actions, outputs or decisions to choose between?

That is the current licensing-relevant engineering question.
