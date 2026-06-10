# Collapse Aware AI — Phase-1 Gold Build Public Proof Pack

**Project:** Collapse Aware AI  
**Owner:** Inappropriate Media Limited  
**Status:** Phase-1 Gold Build, public proof pack  
**Current public version:** v0.1  
**Date:** 10 June 2026  

> Collapse Aware AI is proprietary behavioural middleware for governed, memory-weighted behavioural selection. It is not a base model, not a chatbot wrapper, and not a claim of machine consciousness.

---

## 1. What this proof pack is

This document is a public-facing technical summary of the current Collapse Aware AI Phase-1 Gold Build.

It is designed to show, without exposing protected internals, that the system is moving from private build work into demonstrable runtime proof.

The current focus is gaming and simulation middleware: NPCs, agents, characters, and interactive systems whose behaviour can be shaped by memory, bias, governance, and runtime context without letting behaviour drift into uncontrolled chaos.

This pack is intentionally conservative. It describes what the Phase-1 system is built to demonstrate, what has been validated privately, what is still being captured publicly, and what will be shown in upcoming demos.

---

## 2. What Collapse Aware AI does

Collapse Aware AI sits between an application layer and a behavioural/response-selection layer.

In Phase-1, it demonstrates a governed selection process where repeated interaction, retained memory signals, bias controls, and governor state can influence which behavioural candidate is selected.

In plain English:

> The system can remember relevant interaction traces, weight them, and use them to influence future behavioural selection, while a governor layer can dampen, redirect, or constrain the selected behaviour.

For games, this means an NPC does not need to behave like a flat prompt-response bot. It can show controlled continuity across interaction cycles.

Example behavioural effects:

- A character can react differently after a player has helped, betrayed, ignored, or threatened them.
- Memory influence can change which behavioural option wins.
- Governance can make the system more cautious, constrained, or stable under uncertainty.
- Behaviour can vary across runs without becoming random or uncontrolled.
- Developers can test and trace why a selected behaviour changed.

---

## 3. Phase-1 Gold Build scope

Phase-1 is deliberately narrow.

It is focused on proving a licensable middleware layer for games, simulations, and controlled agent behaviour.

Phase-1 is **not** the full Phase-2 chatbot system. Phase-2 work, including deeper continuity, richer memory handling, recall refinement, and long-form conversational continuity, comes later.

Phase-1 proves the spine:

1. Application/UI sends a behavioural request.
2. API/scaffold layer handles routing, validation, trace, and state.
3. Adapter sends a clean request into the sealed Crown runtime.
4. Crown selects from candidate behaviours using governed, memory-weighted selection logic.
5. Response is mapped back to the application/UI.
6. Logs and evidence show what happened.

The public demo target path is:

```text
UI 8501 → Flask API 7860 → adapter → Crown 8001 → mapped response → UI
```

---

## 4. What has been privately validated

The following claims refer to private runtime validation and developer evidence packs. Public video and GitHub demo captures are being prepared.

### 4.1 P1–P4 scaffold wiring

The current patched scaffold has passed the P1–P4 wiring stage:

- **P1:** top-level caller fields reach the adapter instead of being collapsed into empty/default state.
- **P2:** request-time `governor_mode`, `profile`, and `bias_enabled` fields reach the adapter/harness boundary.
- **P3:** `request_id` and `thread_id` are preserved through the runtime path.
- **P4:** UI core actions route through the Flask API/scaffold layer rather than directly calling the old local stub path.

This matters because it establishes the runtime route needed for real Crown validation.

### 4.2 Clean Crown runtime package

A cleaned Crown runtime handoff package has been prepared for P5/P6/P7 validation.

The package is structured for controlled runtime testing only:

- no virtual environment folder
- no populated state database
- no private `.env`
- no cache files
- no old runtime artefacts
- 8001 runtime path for the Crown service
- sealed engine files preserved
- demo request set included
- checksums included for integrity verification

The Crown remains sealed IP. Public proof will show runtime behaviour and evidence, not Crown internals.

### 4.3 Bias-driven selection shift

A private Crown runtime test shows that memory/bias influence can change the selected behavioural candidate.

Public-safe example:

- bias disabled selects a neutral/default behaviour
- after a relevant memory anchor is admitted, bias enabled selects a memory-aligned behaviour
- the selected output changes under controlled conditions

This demonstrates the Phase-1 claim:

> retained interaction traces can influence future behavioural selection.

### 4.4 Governed-mode winner flip

A stronger governed-mode demo has also been prepared.

The controlled test uses the same prompt, same candidates, and same seed, with `governor_mode` as the key controlled variable.

Public-safe example:

- studio mode selects a more direct/helping response based on remembered kindness
- governed mode selects a more cautious verification response under uncertainty
- the selected behaviour changes

This demonstrates the Phase-1 claim:

> governor state can materially alter behavioural selection, not merely label it.

### 4.5 Recall and persistence

The Crown runtime supports persistent memory traces for controlled demo use.

Public demo evidence will show:

- a memory/anchor being ingested
- recall returning relevant stored traces
- subsequent selection being influenced by retained context
- restart/persistence behaviour where appropriate

---

## 5. What the public demos will show

The first public demos will avoid exposing protected internals.

They will show controlled runtime behaviour only.

Planned demo set:

### Demo A — Memory-weighted selection

Purpose: show that memory/bias can change which behavioural candidate wins.

Expected public framing:

> The same situation produces a different selected behaviour after a retained memory signal becomes relevant.

### Demo B — Governor-controlled selection

Purpose: show that governor state can change the selected output under controlled conditions.

Expected public framing:

> The same prompt and candidates can produce a different selected behaviour when the governor is active.

### Demo C — End-to-end runtime path

Purpose: show that the system works through the actual middleware route.

Expected path:

```text
UI → Flask API → adapter → Crown → mapped response → UI
```

### Demo D — Evidence and traceability

Purpose: show that the result is not hand-waved.

Evidence may include:

- request IDs
- thread IDs
- selected candidate IDs
- status codes
- response bodies with public-safe fields
- terminal logs
- screenshots
- short screen recording

---

## 6. What this proves

The Phase-1 Gold Build is designed to prove:

- memory-weighted behavioural selection
- governed runtime selection
- controlled bias influence
- repeatable candidate-selection differences
- traceable runtime behaviour
- middleware viability for games and simulations

This is not presented as magic, sentience, AGI, or a base-model replacement.

The claim is narrower and stronger:

> Collapse Aware AI is middleware for governed, memory-weighted behavioural selection over runtime interaction cycles.

---

## 7. What this does not claim

This proof pack does not claim:

- that the system is conscious
- that it is AGI
- that it replaces LLMs or game AI systems
- that Phase-2 chatbot continuity is complete
- that robotics integrations are already complete
- that Verrell’s Law is experimentally proven by this build alone
- that the public demo exposes the full protected Crown logic

Phase-1 is a working engineering proof of governed behavioural selection.

The wider roadmap remains separate.

---

## 8. Why this matters for games

Most game NPCs still struggle with meaningful continuity.

They often behave as if each interaction is isolated, or they rely on scripted state machines that are expensive to expand and fragile to maintain.

Collapse Aware AI is designed to sit as middleware between game state and behavioural output.

Potential game use cases:

- NPCs that remember player choices across encounters
- faction/character behaviour affected by prior interaction
- controlled variation between playthroughs
- governed behaviour to prevent chaotic drift
- debug-visible reasons for behavioural shifts
- studio-controlled tuning instead of black-box randomness

The commercial target is not “an NPC that says anything.”

The target is:

> NPC behaviour that changes meaningfully, remembers selectively, stays governable, and remains production-controllable.

---

## 9. Licensing direction

Collapse Aware AI is being developed as licensable middleware.

Initial licensing targets:

- game studios
- simulation developers
- interactive narrative teams
- virtual character systems
- research and prototyping labs
- later: robotics and agent systems where governed runtime behaviour matters

Current licensing position:

- Phase-1: gaming/NPC middleware proof
- Phase-1.5: demo, evidence, tuning, and developer-facing integration pack
- Phase-2: richer continuity-aware chatbot/agent layer after Phase-1 is stable and commercially demonstrable

Licensing discussions should be based on runtime proof, not inflated claims.

---

## 10. Current development status

Current build state:

- Phase-1 scaffold wiring: patched and evidenced privately
- clean Crown runtime package: prepared
- P5/P6 hardening: pending
  - fallback/error handling
  - request schema validation
- P7 full-chain demo evidence: pending
  - UI → API → adapter → Crown → UI
  - screenshots
  - logs
  - short demo capture

The next public milestone is the full-chain runtime demo.

---

## 11. Public evidence policy

Public releases will follow these rules:

- show behaviour, not protected internals
- show request/response evidence where safe
- avoid exposing scoring formulas or engine implementation
- avoid publishing sealed Crown code
- clearly separate private validation from public demonstration
- avoid consciousness/AGI claims
- keep public claims conservative and commercially defensible

---

## 12. Coming soon

Upcoming public proof material is planned for:

- GitHub
- Collapse Aware AI public proof pack
- Collapse Aware AI / CAAI YouTube channel
- short demo clips
- runtime screenshots
- licensing-safe technical summaries

Expected public demo themes:

1. memory changes behaviour
2. governor changes behaviour
3. runtime path is real
4. evidence is traceable
5. middleware remains controllable

---

## 13. Contact / licensing

For licensing, partnership, or technical review enquiries:

**Inappropriate Media Limited**  
Trading as: **Collapse Aware AI**  
Owner / Architect: **Marcos Ross**  

Contact details may be added here before public release.

---

## 14. Public-safe one-line summary

> Collapse Aware AI is proprietary middleware for governed, memory-weighted behavioural selection, designed first for game NPCs and simulation agents that need controlled continuity across runtime interaction cycles.

---

## 15. Public-safe short summary

Collapse Aware AI adds a governed behavioural selection layer between application state and output. In Phase-1, it demonstrates how retained interaction traces, memory weighting, bias controls, and governor state can influence which behavioural candidate is selected. The first public demos will show memory-driven selection shifts, governor-driven selection shifts, and a full UI-to-Crown runtime trace suitable for licensing review.

---

## 16. Suggested GitHub repository layout

Recommended public repository structure:

```text
collapse-aware-ai-public-proof/
├── README.md
├── PUBLIC_PROOF_PACK.md
├── demos/
│   ├── README.md
│   ├── screenshots/
│   └── video-links.md
├── evidence/
│   ├── runtime-path-summary.md
│   ├── p1-p4-wiring-summary.md
│   ├── p5-p7-status.md
│   └── public-safe-logs/
├── licensing/
│   ├── licensing-overview.md
│   └── contact.md
└── media/
    ├── logo/
    └── thumbnails/
```

Do not include private Crown source, private schemas, private scoring rules, private runtime packages, `.env` files, local databases, hidden logs, or contractor handoff files in the public repository.

---

## 17. Suggested YouTube description for first demo

> Collapse Aware AI Phase-1 Gold Build demo: governed, memory-weighted behavioural selection for game NPCs and simulation agents. This demo shows how retained interaction traces and governor state can influence selected behaviour through a controlled middleware runtime path. Protected internals are not shown. Licensing discussions welcome.

---

## 18. Version note

This is a public proof-pack document, not a source-code release.

The protected Crown runtime, internal scoring logic, private adapter details, and commercial integration materials remain proprietary to Inappropriate Media Limited.

---

## 19. Rights notice

© Inappropriate Media Limited. All rights reserved.  
Collapse Aware AI and related Crown/runtime architecture are proprietary.  
Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved.
