# Phase-1 Integration Alignment (Milestone-4 + Crown v3)
Date: 2026-03-04 (UK)  
Public Proof Pack: Integration status + architecture clarification (no proprietary implementation details)

## What this update is
This document aligns the public description of Collapse Aware AI (CAAI) Phase-1 with the *current* integration reality:

- Milestone-4 scaffold (UI + proxy + worker) is the host runtime.
- Crown v3 is the sealed “core-of-core” service providing bias scoring + collapse selection + persistence.
- Phase-1 behaviour is implemented as **candidate scoring + selection** (rerank), not “Crown generates text”.

No internal Crown math, proprietary mechanisms, or source code is disclosed here.

---

## Current Phase-1 architecture (what exists now)
CAAI is middleware around a base model / generator.

**Operational pipeline (Phase-1):**
1) Base model / worker generates **N candidates** (N configurable).  
2) Crown scores candidates using structured memory.  
3) Crown selects a final candidate (collapse selection).  
4) Governor layer applies stability / policy gating.  
5) Structured memory is updated (no raw transcript storage).

### Behavioural flow (Phase-1)
A[User Input]  
B[Base Model / Worker (candidate generation)]  
C[Crown Bias Engine (candidate scoring)]  
D[Collapse Selection (bias-weighted resolution)]  
E[Governor (stability / policy gating)]  
F[Final Output]  
G[Continuity Memory Update (structured persistence)]

A --> B --> C --> D --> E --> F --> G  
G --> C

---

## Separation of concerns (IP boundary)
**Publicly-visible facts:**
- The scaffold is a standard app runtime (UI + proxy + worker orchestration).
- Crown runs as a separate service (sealed black box boundary).
- The proxy talks to Crown over HTTP only.

**Non-public / not disclosed:**
- Crown internal scoring formulae
- weighting mechanisms / tuning
- any “special sauce” implementation details beyond high-level behaviour

---

## Runtime ports (clarity)
Ports vary by deployment, but the reference integration uses:
- UI: 8501
- Proxy/API: 7860
- Stub core (pre-integration sanity): 8000
- Crown service (post-integration): 9000

**Why two core ports appear in docs:**  
8000 is used during Day-0 sanity checks (stub). 9000 is the Crown service after integration.

---

## Minimum Phase-1 service surface (names only)
To keep the proof pack useful without enabling copy-paste theft, we list endpoint names only:

- `GET /core/health`
- `POST /core/ingest`
- `POST /core/recall`
- `POST /core/infer`
- `POST /flag`

(Exact payloads, schemas, and test scripts are part of the private integration pack.)

---

## Persistence policy (Phase-1)
Phase-1 persistence is **disk-backed structured state** (e.g. SQLite).  
Stored: anchors, moments, continuity state, flags/telemetry events (structured).  
Not stored: raw transcripts, full chat logs, or sensitive internals.

---

## Verification model (binary acceptance)
Phase-1 is acceptance-gated with six binary checks:

1) Basic inference valid  
2) Continuity influences output (after ingest)  
3) Governor measurably alters behaviour (selection or scored metrics)  
4) Flags/THB surfaced correctly  
5) Memory persists across restart  
6) Bias divergence demonstrable (bias_enabled on/off)

This is deliberate: “works or it doesn’t”, with no interpretive grading.

---

## Integration readiness status
- Milestone-4 scaffold: confirmed structurally and functionally ready as host runtime.
- Crown v3: packaged as sealed service with persistence + validation docs.
- UK-dev integration scope: adapter-level wiring only (no UI refactor, no redesign).

This pack exists to make the public description match what is *actually being integrated*.

---

## Anti-theft note (plain English)
If you’re reading this to “implement your own version”:
- You can understand the architecture from this doc.
- You cannot reproduce the Crown internals from this pack (by design).
- Licensing is required for the sealed kernel and its verified behaviour.

---

## Changelog (public-facing)
- Clarified Phase-1 is **candidate scoring + collapse selection** (rerank).
- Clarified ports and Day-0 stub vs post-integration Crown service.
- Clarified persistence is structured state, not transcripts.
- Clarified the boundary: scaffold hosts; Crown is sealed service.
