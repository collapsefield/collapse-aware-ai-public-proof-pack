# Retained-State Decision Audit

**Collapse Aware AI (CAAI) — independent evaluation service**  
**Status:** Public commercial/evaluation note  
**Date:** 30 August 2026  
**Provider:** Inappropriate Media Limited, trading as Collapse Aware AI

---

## The Problem

Many AI and workflow systems now have memory, history, traces, customer state or persistent context.

That creates a second problem that storage alone does not solve:

> **What is that retained information actually allowed to change when the system chooses what to do next?**

A system can retrieve the correct history and still:

- repeat an action that already failed;
- let stale history dominate a current task;
- use a correction without superseding the earlier record;
- act on a record belonging to the wrong person or thread;
- escalate too early or too late;
- treat every remembered item as equally authoritative;
- produce a different action without being able to show why;
- rely on repeated model calls where a bounded local decision would be sufficient.

A **Retained-State Decision Audit** examines that decision boundary without requiring the organisation to adopt CAAI first.

---

## What the Customer Provides

One bounded real or anonymised system problem, for example:

- an AI/voice agent with several legitimate next actions;
- a fraud or AML workflow after risk detection;
- a collections/vulnerability treatment decision;
- an adaptive training/simulation branch;
- a game/NPC behaviour decision;
- a long-running assistant with persistent memory;
- a governed workflow where prior attempts should matter.

The customer should provide, as appropriate:

1. the current decision point;
2. the permitted action/candidate set;
3. the relevant retained history/state;
4. the existing baseline decision logic;
5. a small set of representative cases or traces;
6. any policy or non-negotiable constraints.

The evaluation can be conducted on synthetic or anonymised data where live customer data is not appropriate.

---

## What the Audit Examines

### 1. Retention map

What persists across sessions, restarts, users, workflows or cases?

### 2. Retrieval boundary

What historical information can be resurfaced, and under what conditions?

### 3. Influence boundary

Which retained items can actually change the next action or behaviour?

### 4. Authority boundary

Can memory or a generative model effectively create actions outside the declared permitted set?

### 5. Historical integrity

How are correction, supersession, revocation, contradiction and stale state handled?

### 6. Reference condition

Can the same decision be examined with retained-state influence removed, neutralised or held constant?

### 7. Replayability

Can the organisation reconstruct why a given action was selected from the relevant state/configuration?

### 8. Cost boundary

Are repeated model/provider calls being used for decisions that could be handled by a bounded local selector once the candidate set already exists?

Cost is measured, not assumed.

---

## Typical Audit Tests

A bounded audit may include tests such as:

- same present state, different histories;
- history ON vs history OFF/reference;
- stale-record injection;
- explicit correction / supersession;
- contradiction between retained records;
- revoked history;
- wrong-identity / wrong-thread history;
- failed-action recurrence;
- candidate-order permutation;
- restart/restore;
- repeated replay under frozen local conditions;
- outside-candidate action attempt.

---

## Deliverables

A Retained-State Decision Audit can produce:

- decision-boundary map;
- retained-state inventory;
- influence / authority map;
- high-risk stale-history or contradiction findings;
- baseline-vs-history test results where possible;
- replay / evidence assessment;
- model-call / token-cost measurement opportunities;
- recommended control points;
- short written findings suitable for technical/product review;
- optional proposal for a bounded CAAI evaluation if the problem maps cleanly to Core Gold.

The audit is designed to answer a practical question before a larger integration commitment:

> **Is retained history helping this system make better bounded decisions, or merely making the behaviour harder to understand?**

---

## Relationship to CAAI

The audit can stand alone.

CAAI adoption is not required.

Where the customer's problem maps to the Core Gold selection boundary, the next step can be a managed evaluation:

```text
one real/anonymised decision problem
+ permitted candidate actions
+ declared retained state
↓
reference selection
vs
CAAI governed retained-state selection
↓
replayable evidence / Decision Record
```

The objective is to prove or reject value on the customer's actual decision point before discussing a larger licence or integration.

---

## What This Service Does Not Claim

The audit is not:

- regulatory certification;
- a legal opinion;
- a cybersecurity penetration test;
- a claim that every stateful system needs CAAI;
- a guarantee of token savings;
- a guarantee that retained history should always influence behaviour;
- a general AI-safety certification.

The output is a bounded technical/evaluation assessment of **how retained state influences selection and where control/evidence may be weak**.

---

## Best-Fit Buyers

Likely best-fit environments include:

- regulated customer operations;
- collections and vulnerability workflows;
- fraud / AML / identity operations;
- contact-centre / voice AI;
- simulation / training;
- game/NPC systems;
- AI-agent platforms;
- audit-sensitive automation;
- persistent assistants;
- enterprise workflows with repeated decision points.

---

## First Contact

For a paid audit or bounded Core Gold evaluation:

**collapseawareai@gmail.com**

A first exchange can be handled by email. A customer can send a short anonymised description of:

- the decision point;
- the allowed actions;
- what history currently matters;
- what is going wrong or becoming expensive/opaque.

CAAI can then respond with a bounded evaluation structure rather than a generic middleware pitch.

---

## Related Public Material

- [CAAI Public Overview 2026](CAAI_PUBLIC_OVERVIEW_2026.md)
- [Current Engineering State — 27 August 2026](CURRENT_ENGINEERING_STATE_2026-08-27.md)
- [Independent Stateful AI & Adaptive Systems Evaluation](INDEPENDENT_STATEFUL_AI_AND_ADAPTIVE_SYSTEMS_EVALUATION.md)
- [Commercial Distinction and Evaluation Path](COMMERCIAL_DISTINCTION_AND_EVALUATION_PATH.md)
- [Retained-State Selection Benchmark v0.1](https://github.com/collapsefield/collapsefield-verrells-law/blob/main/RETAINED_STATE_SELECTION_BENCHMARK_v0.1.md)

---

**Commercial principle:** make the first purchase a bounded answer to one real decision problem. Larger integration or licensing follows only if the result earns it.
