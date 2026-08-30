# Collapse Aware AI™ — Public Interface and Disclosure Policy

**Status:** Public disclosure boundary  
**Updated:** 30 August 2026

---

## Purpose

Collapse Aware AI publishes enough interface vocabulary, behavioural claims and evaluation structure for technical review and commercial discussion while keeping proprietary Crown/Core implementation details private.

This file explains why the public repository does not currently publish a full production OpenAPI contract for the private selector/kernel.

---

## What may be published freely

Public-safe material may include:

- category vocabulary and definitions;
- high-level host → candidate → retained-state influence → governed selection flow;
- behavioural/evaluation claims already demonstrated in accepted public-safe evidence;
- buyer-facing input/output examples that do not expose private scoring or protected schemas;
- benchmark methodology;
- evidence labels and falsification boundaries;
- customer-safe Decision Record concepts;
- bounded evaluation requirements;
- adapter-neutral integration descriptions.

---

## What is held back

The following remain private unless deliberately released under a commercial, legal or technical review process:

- Crown/Core source code;
- private scoring functions;
- exact thresholds, weights and tuning;
- private runtime schemas and unrestricted payload structures;
- internal control ordering where disclosure would materially aid cloning;
- private persistence layout;
- protected production endpoints;
- deployment secrets, credentials or infrastructure detail;
- current Evolution 2 private engineering internals beyond approved public-safe summaries.

---

## OpenAPI position

A public `openapi.yaml` is **not currently published** for the private Core/Crown runtime.

That is deliberate.

An API contract becomes part of the implementation surface. Publishing one too early can:

1. expose architecture that is not required to understand the commercial proposition;
2. freeze names or payload shapes before the buyer-facing integration boundary is final;
3. disclose details that may be better reserved for protected technical review;
4. create compatibility commitments that the current commercial wrapper does not yet need.

A future public OpenAPI document should therefore describe only a deliberately designed **buyer-safe wrapper/interface**, not the private kernel itself.

---

## Preferred public integration description

The current safe interface description is conceptual:

```text
host/application
    ↓
current decision context
+ bounded permitted candidate actions
+ relevant retained-state/evidence input
    ↓
CAAI governed retained-state selection
    ↓
selected permitted action
+ customer-safe decision/evidence record
```

The host remains authoritative for candidate permission and execution.

---

## Commercial evaluation before full API publication

A customer does not need a public production API specification to begin an evaluation.

The preferred first step is:

```text
one real or anonymised decision problem
+ permitted candidate actions
+ relevant retained history
```

The evaluation can then compare a declared reference condition against governed retained-state selection and return customer-safe evidence.

For the current commercial route see:

- [Retained-State Selection — CAAI Commercial / Evaluation Index](00_RETAINED_STATE_SELECTION_COMMERCIAL_INDEX.md)
- [Retained-State Decision Audit](RETAINED_STATE_DECISION_AUDIT.md)

---

## Change rule

Do not publish deeper implementation/interface material merely for search visibility or category ownership.

The public strategy is:

> **Publish vocabulary, problem definition, behavioural evidence and test method. Protect the engine.**

Any future production API publication should be reviewed against the then-current commercial, confidentiality, patent/prior-art and implementation boundaries before release.
