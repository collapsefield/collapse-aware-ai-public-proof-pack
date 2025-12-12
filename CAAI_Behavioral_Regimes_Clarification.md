# CAAI Behavioral Regimes – Clarification Note

This document clarifies how the three behavioral regimes used in the
Collapse Aware AI (CAAI) architecture should be understood.

It exists to prevent over-interpretation, mischaracterisation,
or false technical assumptions when describing the system publicly.

---

## Purpose of Behavioral Regimes

The Controlled, Hedge, and Chaos regimes are **behavioral control states**.

They are **not** separate models, equations, or hard-coded modes.
They are a conceptual framework used by the CAAI Governor to manage
stability, continuity, and risk during runtime decision-making.

---

## The Three Regimes (High-Level)

### 1. Controlled Regime
- The system is stable and coherent
- Historical continuity and anchor proximity dominate
- Behavior remains consistent, contextual, and character-aligned
- This is the default operating state

Controlled does **not** imply determinism.
It implies **bounded, memory-consistent behavior**.

---

### 2. Hedge Regime
- The system detects uncertainty or ambiguity
- The AI reduces commitment and increases cautious exploration
- Responses may probe, qualify, or defer rather than assert
- Continuity is preserved while risk is limited

Hedge is **not randomness**.
It is uncertainty-aware behavior.

---

### 3. Chaos Handling (Stabilization State)
- The system detects instability, drift, or incoherence risk
- Priority shifts from expression to stabilization
- Output freedom is reduced, not expanded
- The system re-centers on verified anchors or safe defaults

Chaos handling is **protective**, not expressive.
It exists to prevent breakdown, not to generate novelty.

---

## Important Clarifications

- Regime detection is **multi-signal**, not based on a single metric
- No public equation fully describes the internal process, as the governing mathematics are implemented privately and intentionally not disclosed in full.
- Mathematical analogies are **conceptual**, not literal implementations
- Detailed mechanics remain proprietary by design

Any description that implies:
- a single governing scalar
- a fixed equation
- or unrestricted entropy during “chaos”

…is an **over-interpretation**.

---

## Summary

CAAI behavioral regimes are:
- runtime governance concepts
- stability and risk management tools
- intentionally abstracted for safety and IP protection

They describe **how the system behaves**, not **how it is built internally**.
