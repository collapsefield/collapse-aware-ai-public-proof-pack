# Retained-State Selection for Agentic AI Runtime Governance

**Collapse Aware AI (CAAI) — public engineering / commercial note**  
**Date:** 30 August 2026  
**Status:** Public-safe architecture positioning; not a security certification

---

## The Runtime Gap

Agentic AI increasingly separates two questions:

1. **What is the agent allowed to do?**
2. **Among the actions that remain allowed, which one should actually happen now?**

Runtime policy, permissions and security controls are essential for the first question.

**Retained-State Selection** addresses a narrower second question:

> **When several actions are already permitted, should relevant prior history influence which one wins — and can that influence remain bounded, inspectable and replayable?**

---

## Why Prompt Memory Is Not Enough

A model can receive a long history and still:

- repeat an action that failed earlier;
- overreact to stale context;
- ignore a correction;
- choose an allowed but badly timed action;
- fail to distinguish an unresolved issue from a revoked one;
- change behaviour without leaving a deterministic local decision record.

Putting more history into the prompt does not create a trusted final-selection boundary.

---

## A Layered Runtime Model

A useful agentic architecture can be expressed as:

```text
model / planner proposes possibilities
        ↓
identity / permissions / policy
        ↓
permitted candidate action set
        ↓
retained-state relevance / lifecycle / influence
        ↓
clean reference competes with history-conditioned alternatives
        ↓
governed final selection
        ↓
execution by host
        ↓
decision / evidence lineage
```

The host remains authoritative for execution.

Retained memory does not get permission to invent a new action merely because it contains one.

---

## Relationship to Runtime-Governance Research

Recent independent work makes the external-authority boundary increasingly explicit.

Examples include:

- **Policies on Paths** — path-aware deterministic runtime policy evaluation;  
  https://arxiv.org/abs/2603.16586
- **Aegis** — model proposals mediated by a trusted runtime before tool execution;  
  https://arxiv.org/abs/2608.16891
- **Five Primitives for Governing Autonomous AI Agents at Runtime** — runtime mediation, bounded action vocabularies and attestable evidence;  
  https://arxiv.org/abs/2608.26696

These works are adjacent rather than identical to CAAI.

They strengthen a general architectural principle:

> **The generative model should not be the sole authority over consequential execution.**

CAAI’s narrower contribution is to add **governed history-conditioned selection among already-permitted candidates**.

Full convergence comparison:

https://github.com/collapsefield/memory-weighted-selection/blob/main/research_notes/INDEPENDENT_CONVERGENCE_MAP_2026-08-30.md

---

## Agentic Decision Points That Fit

Potential bounded decision points include:

- retry vs stop;
- clarify vs execute;
- tool A vs tool B;
- continue autonomously vs request approval;
- same-channel follow-up vs channel switch;
- escalation vs ordinary handling;
- reopen an unresolved task vs treat it as closed;
- repeat a previously successful action vs avoid a previously failed one;
- use remembered context vs deliberately ignore it for the present task.

CAAI is most relevant when **all candidates are legitimate** but history should not be allowed to influence them invisibly or without control.

---

## Historical Integrity Matters

Long-running agents face a specific memory failure:

> a present statement can falsely describe the past, and a compliant model may rewrite its own historical interpretation to agree.

A governed retained-state system should distinguish:

- a new instruction for future behaviour;
- a claim about what happened earlier;
- an explicit correction/supersession;
- ambiguous or disputed history.

Current CAAI engineering work treats historical truth/provenance and supersession as separate from simple conversational agreement.

That matters because memory that can silently rewrite itself is not a reliable control input.

---

## Why a Clean Reference Path Matters

History should not win merely because history exists.

For a bounded decision, a useful comparison is:

```text
REFERENCE
same policy-adjusted present decision surface
with retained-state score contribution disabled

vs

GOVERNED
same permitted decision surface
with eligible retained-state influence enabled
```

The question becomes measurable:

> **Did history actually earn the right to change the winner?**

---

## Decision Evidence

Where a retained-state effect changes the selected action, useful evidence can include:

- decision identity;
- candidate set;
- reference selection;
- governed selection;
- retained-state influence enabled/disabled state;
- relevant provenance;
- configuration/version;
- replay result;
- customer-safe Decision Record.

The private scoring implementation does not need to be disclosed for the buyer to see whether history changed the decision.

---

## Cost / Provider Independence

If an agent already has a bounded permitted candidate set, an additional model call may not always be required to choose the final action.

CAAI can perform final selection locally in suitable architectures.

Potential savings must be measured against the actual baseline rather than asserted.

Protocol:

[Local Selection Cost Measurement Protocol v0.1](LOCAL_SELECTION_COST_MEASUREMENT_PROTOCOL_v0.1.md)

---

## What CAAI Is Not in This Context

CAAI is not represented as:

- a replacement for authentication;
- an access-control system;
- a cybersecurity firewall;
- a universal policy engine;
- a guarantee of agent safety;
- a tool that gives an agent permission to execute outside host policy;
- a general autonomous-agent framework.

It is a **selection/governance component inside a larger runtime architecture**.

---

## Evaluation Route

A useful first evaluation requires only:

```text
one real/anonymised agent decision
+ current policy constraints
+ permitted actions
+ relevant history
```

Then compare:

- reference vs history-conditioned selection;
- allowed-set integrity;
- stale/corrected history handling;
- restart/replay behaviour;
- evidence;
- provider calls/tokens where relevant.

No full production integration is required to establish whether the decision boundary is useful.

---

## Contact

For a bounded paid evaluation or retained-state decision audit:

**collapseawareai@gmail.com**

---

**Position:** policy determines what may happen; governed retained-state selection can help determine which permitted action should win when history legitimately matters.
