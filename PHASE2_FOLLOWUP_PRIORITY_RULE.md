# Phase-2 Note — Follow-Up Priority Rule

**Project:** Collapse Aware AI (CAAI)  
**Track:** Phase-2 Public-Safe Architecture Notes  
**Maintainer:** Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited (t/a Collapse Aware AI)  
**Status:** Public proof-pack breadcrumb; non-executable; no Crown internals disclosed  
**Date:** 2026-04-30

---

## Core Rule

> **High user salience may increase governed follow-up priority, but it must not increase factual certainty.**

In Phase-2, Collapse Aware AI treats urgency, repeated emphasis, effort, and emotional weight as signals that an unresolved topic may deserve later attention.

Those signals can increase recall priority and follow-up priority.

They must not be treated as proof that any particular factual conclusion is correct.

---

## Why This Matters

Most chat systems answer the current turn and then move on.

CAAI Phase-2 is designed to carry forward the weight of unresolved moments under governance. The system can remember that something mattered without pretending that importance equals truth.

This matters because some user statements are not just ordinary context. Some are delayed-action moments:

```text
important concern raised
↓
uncertainty remains
↓
time passes
↓
follow-up becomes useful
```

The design goal is not to create a stronger claim. The design goal is to create a safer continuity pattern.

---

## Public-Safe Behaviour Model

```text
User raises an important unresolved concern
↓
Weighted Meaning Layer marks it as follow-up-relevant
↓
Weighted Moments assign salience, urgency, repetition, and unresolved-state weight
↓
Continuity Memory stores the unresolved state under governance
↓
Governor blocks overconfident or unsupported claims
↓
Time-Interval Awareness tracks elapsed time
↓
Autobiographical Echo / governed recall may later resurface the concern
↓
Output encourages appropriate review or safer next action
```

The system remembers the unresolved state, not a private conclusion.

---

## Minimal Mathematical Framing

```text
FollowUpPriority = f(Salience, Urgency, Repetition, TimeElapsed, UnresolvedState)

ClaimConfidence != FollowUpPriority
```

Meaning:

- high salience can increase the chance of a later follow-up
- high urgency can increase routing priority
- repeated concern can increase unresolved-state weighting
- elapsed time can increase the value of checking whether action was taken
- none of those signals convert into certainty

This keeps memory useful without turning weighting into a false truth engine.

---

## Example Shape

A governed follow-up should look like this:

```text
"You raised this as important earlier. I cannot confirm the underlying cause, but it is still worth getting appropriate human review rather than letting it disappear."
```

The intended behavioural shape is:

- remember the unresolved concern
- avoid unsupported certainty
- encourage appropriate review
- keep the user moving toward action

---

## Phase-2 Module Relationship

| Behaviour Needed | Public CAAI Architecture Component |
|---|---|
| Detect that the user places high importance on the issue | Weighted Moments |
| Convert the concern into governable meaning, not raw transcript storage | Weighted Meaning Layer |
| Store unresolved concern as sparse continuity state | Continuity Memory / Strong Memory Anchors |
| Track elapsed time since the concern was raised | Time-Interval Awareness |
| Prevent unsupported certainty | Governor v2 / THB-style uncertainty control |
| Re-check uncertain memory before use | Corrective Recall Layer |
| Decide whether a later nudge is appropriate | Multi-Factor Intention Cloud |
| Surface the issue later without overdoing it | Autobiographical Echo / Governed Recall |
| Optional future reminder loop with consent | Asynchronous Care Loop |

---

## Governance Boundary

This note does not claim that Collapse Aware AI replaces professional judgement, regulated review, or domain-specific human oversight.

The public-safe positioning is:

> Collapse Aware AI can preserve unresolved high-salience moments and later encourage appropriate human review, while the Governor blocks overconfident or unsupported collapse.

---

## Product Differentiator

Normal chatbot behaviour often ends when the answer ends.

CAAI Phase-2 is designed to carry forward the **weight of unresolved moments** under governance.

That is the difference between:

```text
single-turn answer generation
```

and

```text
governed continuity-aware support
```

---

## Public Claim Boundary

This document is a public architecture note only.

It intentionally excludes:

- private scoring thresholds
- internal schema details
- Crown kernel logic
- exact Governor routing rules
- timing parameters for follow-up
- any production high-risk deployment claim

Those remain private, reserved, and subject to safety, legal, and deployment-specific review.

---

## One-Line Summary

> High user salience may increase governed follow-up priority, but it must not increase factual certainty.

© 2025–2026 Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited (t/a Collapse Aware AI). All rights reserved.
