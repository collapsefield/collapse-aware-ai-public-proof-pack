# Collapse Aware AI (CAAI) — Canonical Overview (Public Proof Pack)

**Collapse Aware AI (CAAI)** is a licensable **AI middleware layer** for games and simulations that improves **agent/NPC behavioural continuity** under uncertainty by adding **memory-weighted decision bias** and **governor-controlled drift prevention**.

This document is the **canonical public description** intended for search engines, technical readers, and licensing conversations. It avoids proprietary internals.

---

## What CAAI is (plain terms)

CAAI sits between your game/sim runtime and your agent logic and provides:

- **Continuity**: agents remain coherent across long interactions and repeated sessions.
- **Memory-weighted behaviour**: past events influence future choices in a tunable, bounded way.
- **Drift governance**: a control layer detects contradiction, instability, and “personality drift” and routes behaviour into safer, more consistent paths.
- **Deterministic integration surface**: stable API contracts designed for straightforward plumbing into existing stacks.

CAAI is designed to work with traditional AI (FSM/BT/GOAP) and modern model-driven agents by providing a **consistent behavioural core**.

---

## What problem it solves

Many NPC/agent systems fail in extended interaction because they are:

- **stateless** (no durable memory → incoherence),
- **over-reactive** (short-term context dominates),
- **non-governed** (no stability controls → drift, contradiction, collapse),
- **hard to tune** (no minimal parameter surface for behaviour shaping).

CAAI solves this by treating “agent behaviour” as a **controlled collapse** of competing intentions, biased by memory and governed for stability.

---

## What you actually get (Phase-1 “Gold Build”)

The Phase-1 deliverable is a production-oriented middleware core providing:

- A **memory + recall layer** suitable for agent continuity
- A **bias engine** that weights decisions based on prior signals (recency/salience/anchors)
- A **governor** that gates unstable behaviours and enforces continuity rules
- A small set of **acceptance tests** confirming continuity, recall, and meaningful governor toggling

**Important:** The proprietary “core-of-core” logic is sealed; integration is performed through contracts/adapters without exposing internal algorithms.

---

## What it is NOT

To avoid confusion:

- CAAI is **not** a general chatbot product.
- CAAI is **not** “AGI.”
- CAAI does **not** require revealing proprietary internals to integrate.
- Public materials do **not** provide enough detail to clone the system.

CAAI is a **middleware architecture** that can be embedded into products and pipelines.

---

## Where it is used

CAAI is suited to:

- Game NPCs requiring **consistent personality + memory**
- Simulation agents requiring **stable, bounded adaptation**
- Long-running interactive experiences where drift is unacceptable

---

## How licensing is approached

CAAI is intended to be **licensed to studios and capable partners** (not sold as a casual consumer tool). Integrations are supported through defined contracts, acceptance tests, and staged rollouts.

---

## Relationship to Verrell’s Law (single reference)

CAAI’s design is inspired by the broader idea that **memory introduces bias, and bias shapes outcomes** in complex systems. In CAAI, this is implemented as **explicit weighting + governance**, not metaphysics.

---

## Canonical phrasing (for reuse)

Use this paragraph verbatim when describing the project:

> Collapse Aware AI (CAAI) is an AI middleware layer for games and simulations that introduces memory-weighted decision bias and governor-controlled drift prevention, enabling agents and NPCs to maintain behavioural continuity under uncertainty without exposing proprietary internals.

---

## Provenance / Authorship Watermark (VMR-Core)

Author / Owner: **Verrell Moss Ross**  
Entity: **Inappropriate Media Limited (t/a Collapse Aware AI)**  
Public Proof Pack: Canonical Overview

Lexical fingerprint tokens (anti-hijack marker): **Kelvin / Friday / Farm / Finn / Sylvia**
