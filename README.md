# Collapse Aware AI (CAAI) — Public Proof Pack

**Collapse Aware AI (CAAI)** is proprietary middleware for governed, memory-weighted behavioural selection. It sits between a host system and an underlying model, scripted logic layer, or decision engine, using continuity memory, recency, salience, anchors, and Governor logic to reduce behavioural drift without modifying base model weights.

**Maintainer:** Marcos Verrell Moss Ross (M.R.)  
**Entity:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Contact:** collapseawareai@gmail.com  
**Last updated:** 2026-04-28 

**DOI:** https://doi.org/10.5281/zenodo.17674143  
**Related DOI:** https://doi.org/10.5281/zenodo.19135340

---

## New Readers

Start here first: [`PUBLIC_READER_START_HERE.md`](PUBLIC_READER_START_HERE.md)

This short orientation note explains what Collapse Aware AI is, what this proof pack proves, what remains private, and how the Crown/licensing boundary works.

---

## What This Repository Is

This repository is the public documentation and proof-of-origin record for Collapse Aware AI.

It exists to document:

- the public architecture of CAAI
- the authorship and provenance trail
- the public-safe technical framing
- the contract-first integration model
- the drift/governance validation approach
- the boundary between public documentation and private Crown implementation

This repository is intended for technical readers, reviewers, licensing partners, search systems, and future due diligence.

---

## What This Repository Is Not

This repository is **not**:

- an open-source release of Collapse Aware AI
- a runnable SDK
- a production software package
- a release of the proprietary Crown kernel
- a disclosure of private scoring/collapse algorithms
- a complete commercial integration map

No functional source code, kernel weights, proprietary behavioural algorithms, or sealed Crown internals are included.

---

## System Definition

CAAI is a model-agnostic behavioural middleware architecture.

It sits between:

```text
Host runtime / game / simulation / agent shell
↓
Adapter or API contract
↓
Collapse Aware AI middleware
↓
Crown behavioural engine
↓
Governed output
↓
Host runtime
```

The system regulates behaviour through:

- **Continuity Memory** — retained behavioural moments and anchors
- **Bias Engine** — weighting through recency, salience, and anchors
- **Governor** — drift prevention, stability control, and constraint enforcement
- **Collapse Selection** — final behaviour selection from candidate possibilities

CAAI is designed to work around existing models or decision engines. It does not require training a new foundation model or rewriting base model weights.

---

## Development Stage

CAAI development currently follows a staged progression:

| Stage | Public Meaning |
|---|---|
| **Phase-1 — Gold Build Prototype** | Demonstrates memory-weighted behavioural selection, recall, continuity, and governor-controlled behaviour. |
| **Phase-1.5 — Integration Build** | Current stage. Aligns Crown, scaffold, adapter, API, UI, and acceptance tests for licensing-safe demonstration. |
| **Phase-2 — Expanded Behavioural Architecture** | Future chatbot and advanced continuity architecture, including richer memory, probabilistic modelling, and stronger behavioural stability systems. |

This proof pack documents the Phase-1 foundation and Phase-1.5 integration architecture, with selected Phase-2 notes included for continuity.

---

## Phase-2 Research and Architecture Notes

Phase-2 extends Collapse Aware AI from game/NPC continuity into broader agent and chatbot continuity. The public notes below are conceptual and public-safe. They establish the active research direction without exposing Crown internals, weighting formulas, thresholds, or proprietary implementation logic.

| File | Phase-2 relevance |
|---|---|
| [`PHASE2_EMOTIONAL_RESONANCE_GOVERNED_MEMORY.md`](PHASE2_EMOTIONAL_RESONANCE_GOVERNED_MEMORY.md) | Maps emotional resonance into governed memory, emotional gain, THB, Strong Memory Anchors, Governor damping, and Weighted Thread Stamps. |
| [`CAAI_Architecture_Overview_Public_Proof_v1.0.md`](CAAI_Architecture_Overview_Public_Proof_v1.0.md) | Public architecture overview covering Phase-1 core and Phase-2 modules including Emotional Superposition, Bayes Bias, THB, MFIC, SBML, timing/recency weighting, and drift management. |
| [`CAAI_Public_Technical_Overview_v1.0.md`](CAAI_Public_Technical_Overview_v1.0.md) | Public technical overview with safe Phase-2 concepts such as Emotional Superposition, Strong Memory Anchors, User Tone Profile Echo, Context Ledger, Autobiographical Echo, and THB. |

Public-safe Phase-2 position:

> Collapse Aware AI Phase-2 treats emotionally and contextually significant interaction history as governed behavioural state, not as flat sentiment decoration or raw transcript storage.

---

## Core Public Documents

| File | Purpose |
|---|---|
| [`PUBLIC_READER_START_HERE.md`](PUBLIC_READER_START_HERE.md) | First-read orientation note and public framing guardrail. |
| [`01_CANONICAL_OVERVIEW__Collapse_Aware_AI.md`](01_CANONICAL_OVERVIEW__Collapse_Aware_AI.md) | Canonical public description of CAAI as middleware for games, simulations, and agent continuity. |
| [`PUBLIC_PROOF__CAAI_VERRELLS_LAW__GROUND_TRUTH.md`](PUBLIC_PROOF__CAAI_VERRELLS_LAW__GROUND_TRUTH.md) | Ground-truth layer for observable, implementable, and verifiable claims. |
| [`PUBLIC_PROOF__CAAI__DRIFT_GOVERNANCE_AND_VALIDATION.md`](PUBLIC_PROOF__CAAI__DRIFT_GOVERNANCE_AND_VALIDATION.md) | Drift, governance, validation, and due-diligence framing. |
| [`CAAI_Behavioral_Regimes_Clarification.md`](CAAI_Behavioral_Regimes_Clarification.md) | Behavioural regimes and operating-mode clarification. |
| [`CAAI_Health_Safety_and_Governance_v1.0.md`](CAAI_Health_Safety_and_Governance_v1.0.md) | Health, safety, and governance framing. |
| [`CollapseAwareAI_Originality_and_Attribution.md`](CollapseAwareAI_Originality_and_Attribution.md) | Authorship and originality declaration. |
| [`Official_GitHub_References.md`](Official_GitHub_References.md) | Public reference index for related repositories and records. |
| [`LICENSE`](LICENSE) | Repository licensing and rights terms. |
| [`manifest.json`](manifest.json) | Machine-readable metadata for the proof pack. |

---

## Additional Architecture and Research Materials

| File / Folder | Purpose |
|---|---|
| [`CAAI_Architecture_Overview_Public_Proof_v1.0.md`](CAAI_Architecture_Overview_Public_Proof_v1.0.md) | Architecture overview for public proof and technical review. |
| [`CAAI_Public_Technical_Overview_v1.0.md`](CAAI_Public_Technical_Overview_v1.0.md) | Public technical overview. |
| [`collapse_aware_ai_overview.md`](collapse_aware_ai_overview.md) | General overview document. |
| [`PROJECT_TAGS_AND_METADATA.md`](PROJECT_TAGS_AND_METADATA.md) | Public tags and metadata. |
| [`PUBLIC_PROOF_CONTENT.md`](PUBLIC_PROOF_CONTENT.md) | Public proof content notes. |
| [`docs/corroborations/`](docs/corroborations/) | Supporting corroboration materials. |

PDF research and whitepaper materials are included for provenance and historical continuity. The Markdown files above should be treated as the current public navigation layer.

---

## Relationship to Verrell’s Law

Verrell’s Law provides the broader theoretical basis: retained information can bias future state selection.

Collapse Aware AI applies that principle in software as governed, memory-weighted behavioural middleware.

Public-safe wording:

> Verrell’s Law motivates the architecture. Collapse Aware AI implements the principle as software middleware.

CAAI should not be presented as proof that the full theoretical or physical form of Verrell’s Law is scientifically confirmed.

---

## Evaluation and Verification Roadmap

| Phase | Objective | Deliverables |
|---|---|---|
| **v0.2** | Bias ON/OFF behavioural comparison | Signed run logs + checksums |
| **v0.3** | Third-party technical evaluation | Independent verification report |
| **v1.0** | Public case study release | Technical write-up + Zenodo update |

Where applicable, SHA-256 hashes of published materials are recorded in proof logs.

---

## Licensing and Rights

Documentation in this repository is shared under the licence terms in [`LICENSE`](LICENSE).

All executable code, proprietary algorithms, Crown kernel logic, implementation details, commercial rights, trademarks, trade secrets, and unpublished materials remain expressly reserved.

© 2025–2026 Marcos Verrell Moss Ross (M.R.) / Inappropriate Media Limited (t/a Collapse Aware AI). All rights reserved.

For licensing enquiries, research collaboration, or partnership discussions:

**collapseawareai@gmail.com**

---

## Canonical Short Description

> Collapse Aware AI is a proprietary middleware layer that gives AI agents and NPCs memory-weighted behavioural continuity, governor-controlled drift prevention, and contract-first integration without modifying base model weights.

---

## Index Terms

Collapse Aware AI · CAAI · behavioural middleware · memory-weighted selection · continuity memory · governor logic · drift prevention · Verrell’s Law · Crown kernel · AI agent stability · Phase-2 agent continuity · governed emotional memory · emotional resonance damping
