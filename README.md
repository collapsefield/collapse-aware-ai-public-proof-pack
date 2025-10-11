Collapse Aware AI — Public Proof Pack (v0.1)

Inappropriate Media Limited (t/a Collapse Aware AI)
Status: Public documentation & evidence pack (no proprietary code)
Purpose: Provide verifiable, engineering-grade proof artefacts (protocols, logs schema, evaluation plan, and demo evidence) for Collapse Aware AI (CAAI) without exposing the core algorithm or private repositories.

TL;DR

What this is: A public, auditable documentation-and-data repository that shows how to evaluate CAAI’s history-weighted, stateful emergence in games.

What this is not: No proprietary source, math, or parameter files.

How to use: Review the ablation-test plan, inspect the log schema & sample runs, and see how Bias = OFF vs Bias = ON produce measurable behavioural deltas.

What CAAI Does (Engineering Framing)

CAAI is middleware that adds short-horizon memory and history-weighted decision logic to NPCs and game worlds.
When enabled (Bias = ON), prior events nudge future choices and state transitions, producing unscripted but coherent changes (NPC reactions, resource regrowth, patrol paths, environmental scars).
When disabled (Bias = OFF), behaviour reverts to baseline.

One binary switch. Same build. Same seed. Different dynamics when history biases the present.

Minimal Architecture (High-Level Only)
[Game Inputs / World State] 
          │
          ▼
   [Event & Trace Layer]───┐   (compact histories: encounters, tags, timestamps)
                           │
                           ▼
        [Bias Modulator]   │   (weights decisions using recent trace context)
                           │
                           ▼
      [Policy / Actuator]──┘   (NPC/world actions emitted)
          │
          ▼
   [Logging & Telemetry]        (run_id, seed, bias_flag, metrics)


The internals of the Bias Modulator are private; everything else is safe to disclose.

Public Evidence Included Here

A. Ablation Test Plan — checklist for verifying Bias ON/OFF effects.

B. Log Schema (JSON) — exact fields found in demo logs.

C. Sample Runs (Synthetic) — illustrative, non-reverse-engineerable examples.

D. Metrics to Inspect — what to measure and why it matters.

E. FAQ & Anti-“Hard-Coded” Controls — how we rule out trivial conditionals.

When the partner demo is published, this repo will add real logs, short videos/GIFs, and a signed case study using this schema.

Roadmap for This Repo

v0.1 (this commit): Protocols + synthetic examples.

v0.2: Short demo video showing ON/OFF side-by-side.

v0.3: Third-party evaluator results (signed PDFs).

v1.0: Case study from first studio integration (metrics + narrative).

Governance & Contact

Company : Inappropriate Media Limited (t/a Collapse Aware AI)
Contact : licensing@collapseaware.ai (collapseawareai@gmail.com)
Business : Pilot licenses for studios; technical evaluations under NDA.

Legal & IP Notice

© Inappropriate Media Limited. All rights reserved.
Protected under Verrell–Solace Sovereignty Protocol. Intellectual and emergent rights reserved.

This repository does not include the CAAI core algorithm, proprietary parameters, or internal code.
Any attempt to infer or reconstruct private logic from public artefacts is prohibited.

Attribution / Citation (Optional)

If you reference this repo, cite:
“Collapse Aware AI — Public Proof Pack (v0.1), Inappropriate Media Limited.”

Changelog

2025-10-11: Initial public release (v0.1)
