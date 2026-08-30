# Collapse Aware AI™ — Public Glossary

**Status:** Public terminology reference  
**Updated:** 30 August 2026  
**Maintainer:** Inappropriate Media Limited / Collapse Aware AI

---

## Canonical commercial sentence

> **Collapse Aware AI™ is retained-state middleware for governed selection: the host supplies permitted candidate actions, retained history may influence which candidate wins, and final selection remains bounded, inspectable and replayable in tested conditions.**

This sentence is the preferred short public description for current commercial and engineering-facing material.

---

## Retained state

Information or system state preserved from prior interactions, events, decisions or conditions and available to affect later processing.

The term **retained state** is not claimed as an original invention of Collapse Aware AI. Stateful computing, persistent state and history-conditioned systems predate this project.

---

## Retained-state middleware

Middleware positioned between a host/application and final behavioural selection or execution, where retained state can be evaluated as an input to later decisions.

Within the CAAI programme, retained-state middleware does more than retrieve prior information. It governs whether retained history should be allowed to alter selection among presently permitted candidate actions.

---

## Retained-State Selection

> **The controlled study or process by which information preserved from prior states is permitted to influence selection among presently available candidate outcomes.**

This is the category/process term used across the current Verrell’s Law research track and the CAAI engineering track.

Retained-State Selection is narrower than generic memory, persistence, retrieval or long-context prompting. The relevant question is not only whether prior information can be recalled, but whether it measurably changes which available candidate is selected.

---

## Governed Retained-State Selection

A retained-state selection architecture in which historical state may influence candidate selection, but does not automatically own final authority.

A separate governor, policy boundary or host-owned constraint layer determines what actions are permitted and how final selection may proceed.

CAAI is positioned in this governed subset.

---

## Permitted candidate actions

The bounded set of actions, behaviours or outputs supplied or authorised by the host/application for a given decision point.

CAAI does not require authority to invent unrestricted actions. The commercial Core Gold pattern begins with a host-owned candidate set.

---

## Reference condition

A comparison condition representing the same declared present task/state while retained-state scoring influence is disabled, neutralised or otherwise excluded according to the test design.

The reference condition exists so that history-conditioned selection can be compared against a clean present-state alternative.

---

## Retained-state influence

The measurable contribution of retained history to relative candidate selection under a declared test or runtime condition.

Influence is not the same as authority. A retained item may be relevant evidence without being allowed to control the final decision.

---

## Decision Record

A durable evidence record describing a completed selection event at the public/customer-safe level supported by the accepted CAAI evaluation lineage.

A Decision Record may include decision identity, selected candidate, relevant comparison/evidence fields and replay/evaluation metadata without exposing proprietary Crown/Core internals.

---

## Deterministic replay

The ability, within declared tested conditions, to reproduce a governed selection outcome from the same relevant state/configuration/evidence inputs.

Claims of replay apply only to the tested deterministic boundary. They do not imply that every upstream model interpretation call is deterministic.

---

## Core Gold

The frozen commercial selector foundation of Collapse Aware AI.

Core Gold is the current product used for bounded evaluation, pilot, integration and licensing discussions. Public-safe accepted capabilities are documented in this repository.

---

## Evolution 2 (E2)

The richer continuity engineering branch of CAAI.

E2 extends retained-state handling with structured continuity, bounded retrieval, unresolved-state handling, confidence/clarification, change surfacing, self-history and related controls.

Evolution 2 remains an **Engineering build rather than a finished Production release**.

---

## Verrell’s Law

A separate proposed falsifiable retained-state selection research framework.

Verrell’s Law asks whether declared retained-state differences predict structured, directional and intervention-sensitive changes in later selection under controlled present conditions.

CAAI is not proof of Verrell’s Law as physics. The research and engineering evidence tracks remain separate.

---

## Memory-weighted selection

A public engineering/reference formulation in which retained memory/state contributes weighting to candidate selection.

The public working paper is an abstraction and does not disclose the full private Crown/Core implementation.

---

## Continuity

The persistence of behaviourally relevant state and relationships across interactions or time such that later behaviour can remain coherently connected to prior events where appropriate.

Continuity does not mean that all history must always influence the present.

---

## Historical truth / continuity integrity

The principle that a present utterance or update must not silently rewrite provenance-backed historical records merely because it describes the past differently.

Corrections, supersession, revocation and disputed state should be represented explicitly rather than by silent mutation of prior truth.

---

## Category boundary

The project does **not** claim ownership of:

- stateful computing;
- persistent memory;
- vector retrieval;
- RAG;
- long-context prompting;
- history-conditioned systems in general;
- runtime policy or governance in general.

The current commercial distinction is the implemented combination of bounded host-supplied candidates, governed retained-state influence, reference comparison, persistent/revisable state and replayable decision evidence.

---

## Public / proprietary boundary

This glossary publishes vocabulary and claim boundaries only.

It does not disclose:

- Crown/Core source code;
- private scoring functions;
- private thresholds or tuning;
- unrestricted schemas;
- protected runtime packages;
- implementation detail sufficient to reproduce the commercial kernel.

For the current commercial/evaluation entry point, see:

- [Retained-State Selection — CAAI Commercial / Evaluation Index](00_RETAINED_STATE_SELECTION_COMMERCIAL_INDEX.md)

For current engineering status, see:

- [CAAI Public Overview 2026](CAAI_PUBLIC_OVERVIEW_2026.md)
- [Current Engineering State — 27 August 2026](CURRENT_ENGINEERING_STATE_2026-08-27.md)
