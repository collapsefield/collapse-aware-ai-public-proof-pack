# Retained-State Selection for Regulated Next Actions

**Collapse Aware AI (CAAI) — public commercial / evaluation note**  
**Date:** 30 August 2026  
**Status:** Public-safe positioning; not legal advice or regulatory certification

---

## The Decision After Detection

Regulated operational systems are often good at identifying a condition:

- customer vulnerability;
- fraud risk;
- AML alert;
- arrears;
- complaint state;
- identity uncertainty;
- failed contact;
- prior intervention outcome;
- policy exception.

The difficult next step is often different:

> **Several responses may still be compliant or operationally legitimate. Which one should happen now, and how should prior history affect that choice?**

That is a retained-state selection problem.

---

## Example Pattern

```text
risk / vulnerability / workflow signal
        ↓
policy and business rules
        ↓
permitted candidate actions
        ↓
retained customer/case history
        ↓
governed candidate-relative influence
        ↓
selected permitted action
        ↓
replayable decision evidence
```

The customer/host remains responsible for:

- law and regulatory interpretation;
- policy;
- candidate permissions;
- execution;
- human approval where required.

CAAI does not decide what is legally permitted.

It can govern **selection among the actions the customer has already declared permitted**.

---

# Where the Pattern Appears

## Vulnerability / Consumer Duty

After vulnerability has been identified, several approved treatments may remain possible.

History can matter:

- previous support accepted or refused;
- previous channel failed;
- vulnerability state changed;
- repeated intervention became inappropriate;
- a prior arrangement remains active;
- current need conflicts with stale history.

The retained-state question is not “remember everything.”

It is:

> **Which approved treatment should prior history be allowed to favour or suppress now?**

---

## Collections / Arrears

A collections platform may already know:

- account state;
- promise-to-pay status;
- contact outcomes;
- arrangement history;
- vulnerability flags;
- dispute state;
- channel response.

Several next actions may still be valid:

- wait;
- contact;
- switch channel;
- offer arrangement;
- request information;
- escalate;
- hold;
- route to human review.

Retained-State Selection makes the history-to-action boundary explicit and testable.

---

## Fraud / AML / Identity

Detection systems can produce rich risk intelligence without uniquely determining the operational response.

Possible permitted actions might include:

- approve;
- challenge;
- request more evidence;
- route to review;
- restrict;
- hold;
- escalate.

Prior interactions can legitimately influence that downstream decision, but historical data should not silently become unlimited authority.

---

## Contact Centre / Voice AI

A voice or service agent may have several legitimate next actions:

- continue;
- clarify;
- verify;
- transfer;
- escalate;
- schedule;
- hand off;
- stop.

Relevant caller/customer history may matter, especially after repeated failed attempts or prior commitments.

CAAI focuses on the **final permitted choice**, not speech generation itself.

---

# Why This Is Different from a Risk Score

A risk score describes or predicts a condition.

It does not necessarily answer:

> **What should happen next when several actions remain legitimate?**

CAAI is not positioned as a replacement for risk detection.

It can sit downstream of detection where the action set is already bounded.

That makes it potentially complementary to existing:

- fraud engines;
- AML platforms;
- vulnerability assessment tools;
- collections systems;
- CRM/workflow engines;
- contact-centre platforms.

---

# Why This Is Different from a Policy Engine

A policy engine can answer:

> “Is this action allowed?”

Retained-State Selection asks:

> **“Among the actions that remain allowed, should relevant history change which one wins?”**

The two layers can be complementary.

---

# Evaluation in Shadow Mode

A regulated organisation does not need to let CAAI control a live customer outcome to evaluate the mechanism.

A shadow-mode test can use the same bounded case and candidate set:

```text
existing production decision continues unchanged

CAAI independently evaluates:
REFERENCE selection
vs
GOVERNED retained-state selection

results compared offline
```

This can examine:

- when history changes the winner;
- whether the change is defensible;
- whether stale/corrected history is handled correctly;
- replayability;
- Decision Records;
- provider-call/token opportunities;
- cases where retained history should remain silent.

---

# History Should Be Revisable

Regulated history is rarely static.

A useful retained-state layer needs to handle:

- correction;
- revocation;
- supersession;
- expiry;
- contradiction;
- disputed information;
- wrong-identity association;
- suppression from a current decision without necessarily deleting the underlying record.

The principle is:

> **Historical truth should not silently rewrite itself merely because the newest utterance or record says something different.**

---

# Decision Evidence

A buyer-safe decision record can answer questions such as:

- What candidate actions were permitted?
- What did the reference condition select?
- What did the governed condition select?
- Did retained state change the winner?
- Which state/configuration/version was used?
- Can the local decision be replayed?

This is useful for evaluation even when proprietary scoring internals remain private.

---

# Local Selection / Cost

Where the candidate set already exists, local final selection may avoid an additional model/provider decision call.

That can matter in high-volume regulated workflows.

The saving must be measured fairly, with shared upstream generation and policy work counted on both sides.

Protocol:

[Local Selection Cost Measurement Protocol v0.1](LOCAL_SELECTION_COST_MEASUREMENT_PROTOCOL_v0.1.md)

---

# What This Does Not Claim

CAAI is not represented here as:

- a regulator-approved decision engine;
- legal advice;
- a replacement for existing fraud/AML/vulnerability systems;
- an autonomous legal decision-maker;
- a universal next-best-action optimiser;
- proof that historical data should always influence a customer outcome.

The host defines the lawful/permitted action surface.

CAAI can be evaluated as a bounded selector inside that surface.

---

# First Paid Evaluation Shape

A practical first evaluation needs:

```text
1 anonymised regulated decision point
+ 3–8 permitted candidate actions
+ relevant historical state
+ the current/reference logic
```

The evaluation can then produce:

- reference selection;
- governed retained-state selection;
- history-on/history-off comparison;
- replay/evidence;
- stale/correction tests;
- optional cost measurement;
- a buyer-safe findings record.

This keeps the first purchase bounded and tied to a real operational problem rather than asking the organisation to license middleware before seeing value.

---

## Related Material

- [Retained-State Decision Audit](RETAINED_STATE_DECISION_AUDIT.md)
- [Local Selection Cost Measurement Protocol v0.1](LOCAL_SELECTION_COST_MEASUREMENT_PROTOCOL_v0.1.md)
- [CAAI Commercial / Evaluation Index](00_RETAINED_STATE_SELECTION_COMMERCIAL_INDEX.md)
- [Retained-State Selection Benchmark v0.1](https://github.com/collapsefield/collapsefield-verrells-law/blob/main/RETAINED_STATE_SELECTION_BENCHMARK_v0.1.md)

---

## Contact

For a bounded paid evaluation, audit, pilot or licensing discussion:

**collapseawareai@gmail.com**

---

**Commercial principle:** do not sell “memory.” Solve one expensive next-action decision where history matters and evidence matters too.
