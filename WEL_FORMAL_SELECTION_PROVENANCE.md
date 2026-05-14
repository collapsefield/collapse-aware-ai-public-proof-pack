# Weighted Emergence Layering (WEL)

**Subtitle:** A Memory-Weighted Selection Framework for Continuity-Aware AI Middleware
**Author:** Marcos Verrell Moss Ross (M.R.)
**Organisation:** Inappropriate Media Limited / Collapse Aware AI
**Status:** Public technical provenance note
**First published publicly:** 2026-05-13
**Version:** WEL-PROV-001

---

## 1. Purpose

Weighted Emergence Layering (WEL) is a middleware-level framework for converting stored memory, salience, recency, and anchor signals into active selection pressure over future AI behaviour.

WEL does not merely retrieve memory. It modifies the probability landscape from which behaviour is selected.

---

## 2. Core Claim

Given the same base model, same prompt, and same candidate set, different memory-weighted states can produce different selected behavioural trajectories.

In short:

**Same model. Same candidates. Different memory field. Different behaviour.**

---

## 3. What WEL Is

WEL is:

- a selection-biasing framework
- a behavioural continuity mechanism
- a memory-weighted middleware layer
- a way to make prior interactions influence future outputs without retraining the base model

---

## 4. What WEL Is Not

WEL is not:

- ordinary prompt memory
- simple retrieval augmented generation
- fine-tuning
- a claim that the base model is conscious
- proof of the full physical form of Verrell's Law

---

## 5. Formal Selection Equation

Let candidate behaviour `y` be selected from a candidate set `Y`.

Base model utility:

$$
U(y; S_t, O_t)
$$

Memory-weighted bias:

$$
B(y; M_t)
$$

Final selection distribution:

$$
\mathbf{P}(y_{t+1}) = \mathrm{Softmax}\big(U(y; S_t, O_t) + \lambda B(y; M_t)\big)
$$

Where:

- `U` = base utility or raw model preference
- `S_t` = current system/runtime state
- `O_t` = current observation/input
- `M_t` = memory state
- `B` = memory-derived behavioural bias
- `λ` = bias coupling strength
- `P(y)` = final candidate-selection probability

The coupling value `λ` controls how strongly memory-derived bias influences final selection. In practical middleware use, `λ` should be bounded to prevent memory from overwhelming task relevance, safety constraints, or governor logic.

A simple bounded form is:

$$
0 \leq \lambda \leq 1
$$

Where:

- `λ = 0` means no memory influence
- `λ = 1` means full configured memory-bias influence
- intermediate values provide tunable behavioural continuity

---

## 6. Bias Decomposition

The memory-bias term can be decomposed into recency, salience, and anchor components:

$$
B(y; M_t) = \alpha_R r(y, R_t) + \alpha_\Sigma s(y, \Sigma_t) + \alpha_A a(y, A_t)
$$

Where:

- `R_t` = recency memory
- `Σ_t` = salience memory
- `A_t` = anchor memory
- `r` = recency alignment score
- `s` = salience alignment score
- `a` = anchor alignment score
- `α_R, α_Σ, α_A` = weighting coefficients

For a bounded public form, the component weights may be treated as convex coefficients:

$$
\alpha_R + \alpha_\Sigma + \alpha_A = 1, \quad \alpha_R, \alpha_\Sigma, \alpha_A \geq 0
$$

In practical middleware use, the component alignment scores should also be normalized or clipped before coupling so that the memory-bias term remains governable and does not overwhelm base utility or safety constraints.

This avoids treating memory as a single opaque variable. WEL separates short-term recency, high-weight salience, and persistent anchor influence.

---

## 7. Recursive Memory Update

WEL is recursive. Selected behaviour updates memory, and updated memory influences future behavioural selection.

$$
M_{t+1} = \mathrm{UpdateMemory}(M_t, y_t, w_t)
$$

Where:

- `y_t` = selected behaviour
- `w_t` = weight assigned to the event
- `M_{t+1}` = updated memory state

A minimal memory update can be described as:

$$
M_{t+1} = \delta M_t + w_t \phi(y_t)
$$

Where:

- `δ` = memory retention/decay factor
- `φ(y_t)` = encoded representation of the selected behaviour
- `w_t` = event weight based on salience, recurrence, anchor relevance, or governor approval

This creates path-dependence. Behaviour at time `t` affects memory, and memory affects selection at time `t+1`.

---

## 8. Minimal Demonstration

The companion file `demos/wel_bias_engine_probability_shift.py` demonstrates the central WEL mechanism.

The simulation uses:

- the same candidate actions
- the same base logits
- a memory-derived bias vector
- a bounded coupling value λ

The expected result is that the baseline model favours one action, while the memory-weighted WEL selection favours another.

This demonstrates candidate-selection divergence caused by memory-weighted bias, not by changing the base model.

---

## 9. Expected Demonstration Result

Baseline model preference:

```text
Action_C = highest probability
```

Memory-weighted WEL preference:

```text
Action_A = highest probability
```

The important point is not the specific action labels. The important point is the mechanism:

**same base logits + different memory-bias field = different behavioural probability landscape.**

---

## 10. Relationship to Collapse Aware AI

Collapse Aware AI uses WEL as part of its middleware logic for behavioural continuity.

In Phase-1, this appears as:

- candidate generation
- memory weighting
- bias scoring
- governor checks
- final behavioural selection

WEL provides the selection-pressure layer that allows memory to influence behaviour without modifying the underlying base model.

---

## 11. Relationship to Verrell's Law

WEL is the engineering implementation branch of a broader Verrell's Law principle:

> Stored structure can bias future selection.

Within Collapse Aware AI, this is implemented as memory-weighted behavioural selection.

This document makes no claim that the broader physical interpretation of Verrell's Law is experimentally proven.

---

## 12. Differentiation from Ordinary Memory Systems

Ordinary memory systems usually retrieve context and insert it into a prompt.

WEL instead converts memory into weighted selection pressure.

This means memory does not merely inform output generation. It alters the probability surface of future behavioural selection.

This distinction matters because WEL can produce path-dependent behavioural divergence from the same base model and candidate set.

---

## 13. Provenance Statement

This document records the Weighted Emergence Layering (WEL) framework as developed by Marcos Verrell Moss Ross (M.R.) through the Collapse Aware AI project and Inappropriate Media Limited.

First published publicly: 2026-05-13.

This date establishes priority of the WEL framework terminology, notation, and architecture within the Collapse Aware AI project lineage.

The terminology, architecture, notation, and implementation framing are part of the Collapse Aware AI / Verrell's Law project lineage.

---

## 14. Copyright and Use

Copyright © 2026 Marcos Verrell Moss Ross / Inappropriate Media Limited.
All rights reserved unless otherwise stated in the repository license.

This public note is provided for technical provenance, transparency, and research discussion. It does not grant permission to reproduce, commercialise, or incorporate the WEL framework into third-party systems without written permission.
