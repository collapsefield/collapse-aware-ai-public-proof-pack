# Local Selection Cost Measurement Protocol v0.1

**Collapse Aware AI (CAAI)**  
**Status:** Public benchmark methodology / no result claimed yet  
**Date:** 30 August 2026  
**Provider:** Inappropriate Media Limited, trading as Collapse Aware AI

---

## Purpose

CAAI can perform final selection locally once a bounded set of candidate actions/behaviours already exists.

That architecture creates a plausible cost advantage in workflows where an organisation currently makes an additional model/provider call solely to decide which prepared or permitted action should happen next.

The safe claim is:

> **Local selection may reduce repeated provider calls, token use, latency and cloud dependence in suitable integrations. The size of any saving must be measured against a fair baseline.**

This protocol defines that measurement.

It does **not** claim a guaranteed percentage reduction.

---

## The Comparison Boundary

A fair test must hold the candidate-generation boundary constant.

### Baseline condition

The system reaches a decision point with a declared set of permitted candidate actions and uses an LLM/provider call to choose among them.

### Local-selection condition

The system reaches the **same decision point with the same candidate set**, and a local bounded selector chooses among them without an additional provider decision call.

The comparison is invalid if one condition includes candidate-generation work that the other does not.

---

## Example Runtime Shape

```text
shared upstream work
current event / customer state
↓
policy / business rules
↓
permitted candidate set
↓
---------------------------------
BASELINE: provider call chooses winner
LOCAL: local selector chooses winner
---------------------------------
↓
selected permitted action
```

The purpose is not to eliminate useful model generation.

It is to identify places where a model is being paid to make a bounded final choice that can be handled locally once the decision surface is already structured.

---

## Required Test Inputs

For each test case record:

- current decision state;
- candidate set;
- policy constraints;
- retained history available to each condition;
- provider/model/version used in the baseline;
- model temperature / deterministic settings where applicable;
- prompt/template version;
- local selector version;
- local configuration/profile;
- number of repeated trials.

---

# Primary Metrics

## 1. Provider calls per completed decision

Count all provider calls required after the candidate set exists.

```text
provider_calls_baseline
provider_calls_local
```

Do not hide retries.

---

## 2. Input tokens

Record actual billed/reported input tokens for the provider decision step.

---

## 3. Output tokens

Record actual billed/reported output tokens for the provider decision step.

---

## 4. Provider cost

Use the provider's actual pricing for the tested model and date.

Report pricing assumptions explicitly.

---

## 5. Local compute cost

Estimate or measure:

- CPU/GPU usage where relevant;
- wall-clock runtime;
- hosting/runtime allocation;
- storage/I/O where material.

A local decision is not literally “free” merely because it uses no model tokens.

---

## 6. End-to-end latency

Measure from the point the candidate set is ready to the point the final decision is available.

Report:

- median;
- p95 where sample size permits;
- retries/timeouts separately.

---

## 7. Decision equivalence / quality

A cheaper decision is not automatically a better system.

Record whether each condition:

- remains inside the permitted action set;
- satisfies policy;
- chooses an accepted/defensible action;
- produces required evidence;
- remains stable across replay/repetition where expected.

---

# Secondary Metrics

Useful secondary measurements include:

- retained-history retrieval cost;
- prompt-construction cost;
- repeated transcript/context size;
- cloud network dependency;
- failure/retry rate;
- evidence-record size;
- operator review rate;
- local memory/storage growth;
- decision divergence between reference and history-conditioned conditions.

---

# Token-Saving Calculation

For a test population of `N` completed decisions:

```text
Total baseline provider tokens
= baseline input tokens + baseline output tokens

Total local-condition provider tokens
= local input tokens + local output tokens

Token reduction %
= (baseline tokens - local-condition tokens)
  / baseline tokens × 100
```

Only include calls that genuinely differ because of the selection architecture.

If both systems use the same upstream model call to generate candidates, that shared cost belongs to both sides and must not be presented as a CAAI saving.

---

# Provider-Call Reduction

A more architecture-stable metric than token percentage can be:

```text
selection-stage provider calls avoided
per 1,000 completed decisions
```

This matters because token counts vary with prompt design, provider and model version.

Example reporting form:

```text
Decision cases tested: 1,000
Baseline post-candidate provider calls: 1,000
Local-selection post-candidate provider calls: 0
Selection-stage provider calls avoided: 1,000
Shared upstream generation calls: unchanged and excluded from saving claim
```

That statement is stronger than claiming “zero AI cost” because it identifies exactly which calls were removed.

---

# Quality-Control Conditions

A cost result should not be published without checking at least:

1. same candidate set;
2. same declared policy constraints;
3. same current-state facts;
4. comparable retained-state information;
5. no hidden manual intervention in only one condition;
6. retries counted;
7. invalid/outside-candidate outputs counted as failures;
8. local compute included where material;
9. quality/equivalence assessed separately from cost;
10. model/provider pricing date disclosed.

---

# Three Useful Test Regimes

## Regime A — Pure bounded choice

Candidates are already authored or generated upstream.

Question:

> Can the final provider decision call be removed entirely?

This is the cleanest cost test.

---

## Regime B — Retrieval + bounded choice

The baseline injects significant prior history into a provider prompt to choose the next action.

The local condition uses structured retained state and a local selector.

Question:

> How much prompt/context processing is avoided, and does the decision remain acceptable?

---

## Regime C — Hybrid generation + local governance

The model still generates or proposes candidates, while final selection/governance is local.

Question:

> Does separating proposal from final authority reduce repeated provider calls, retries or long decision prompts while preserving quality?

---

# What Should Never Be Claimed Without Data

Do not publish statements such as:

- “CAAI cuts token cost by 100%”;
- “CAAI removes all cloud cost”;
- “CAAI is always faster than LLM selection”;
- “CAAI reduces tokens by the same percentage reported by another memory paper”;
- “local means free.”

External research may show that selective memory can reduce prompt burden in other systems, but those numbers are not CAAI results.

---

# Suggested Public Result Table

| Metric | Provider-selection baseline | Local-selection condition | Difference |
|---|---:|---:|---:|
| Completed decisions |  |  |  |
| Selection-stage provider calls |  |  |  |
| Input tokens |  |  |  |
| Output tokens |  |  |  |
| Provider cost |  |  |  |
| Local compute cost |  |  |  |
| Median selection latency |  |  |  |
| p95 selection latency |  |  |  |
| Outside-candidate failures |  |  |  |
| Accepted/defensible selections |  |  |  |
| Replay consistency |  |  |  |

---

# Relationship to Core Gold

Core Gold is relevant where the host/application already owns or can construct the permitted candidate set.

That makes the cost hypothesis specific:

> **If an existing workflow uses model/provider inference after the candidate set is already known, Core Gold may be able to move that final selection into a local governed decision layer.**

The value is not only token reduction.

Potential benefits can include:

- predictable decision latency;
- provider independence at final selection;
- reduced exposure of historical state to external model calls;
- deterministic/replayable local evidence;
- explicit reference-vs-governed comparison;
- bounded action authority.

Each should be measured separately.

---

# Relationship to External Memory Research

Recent research such as **Weighted Memory Tree** reports meaningful prompt-token reduction through selective memory activation in its own long-horizon-agent experiments.

Reference: https://arxiv.org/abs/2608.20631

That result is relevant as independent evidence that memory architecture can affect token usage, but it is **not a CAAI benchmark result**.

CAAI should publish only its own measured results under this protocol.

---

# Commercial Use

A customer-specific cost evaluation can begin with one bounded workflow:

```text
one decision point
+ existing provider-selection route
+ fixed permitted candidate set
↓
measure current calls/tokens/latency
↓
run local governed-selection comparison
↓
report actual saving or no saving
```

A null result remains useful. If the architecture does not remove a genuine provider call or does not preserve acceptable decision quality, it should not be sold as a cost-saving fit for that decision point.

---

## Contact

For a bounded cost/evaluation exercise:

**collapseawareai@gmail.com**

---

**Version:** v0.1  
**Date:** 30 August 2026  
**Status:** methodology published; no universal CAAI token-saving percentage claimed.
