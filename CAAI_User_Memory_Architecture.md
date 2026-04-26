# Collapse Aware AI — User Memory Architecture

**Project:** Collapse Aware AI  
**Author:** M.R. (Marcos Verrell Moss Ross)  
**Maintainer:** Inappropriate Media Limited (t/a Collapse Aware AI)  
**Status:** Public proof-pack architecture note  

---

## Purpose

This document defines the memory isolation model used by Collapse Aware AI (CAAI).

Each deployment must maintain strict separation between:

- system memory
- tenant/application memory
- per-user memory

This protects privacy, licensing boundaries, behavioural stability, and governor integrity while allowing continuity-aware behaviour where required.

The objective is simple:

> continuity without contamination

No uncontrolled cross-user memory bleed.  
No shared hidden state across customers.  
No licensing ambiguity.

---

## Three Memory Layers

Collapse Aware AI uses three memory layers.

---

## 1. Global System Layer

This is the fixed shared system layer.

It contains:

- governor policy
- rule enforcement logic
- fixed prompt templates
- deployment configuration
- core behavioural constraints
- policy defaults

This layer is controlled by the deployment owner and is not treated as user memory.

It defines the rules of operation.

---

## 2. Tenant / Application Layer

This layer is shared only within a single customer license.

Examples:

- a game studio deployment
- a business chatbot deployment
- an enterprise support environment
- a simulation environment

It contains:

- application-specific rules
- tenant-level preferences
- deployment-wide behavioural settings
- customer-owned continuity structures

This memory must never leak across licensees.

Each tenant remains isolated.

---

## 3. Per-User Layer

This is the isolated memory space for each end user.

Examples:

- a specific player
- a specific customer
- a single account holder
- an individual operator

It contains:

- user-specific history
- continuity preferences
- weighted moments
- behavioural anchors
- profile adjustments
- session continuity

Persistence may be:

- temporary
- bounded
- fully persistent

depending on deployment rules.

---

## Identifier Model

Isolation is enforced through explicit identifiers.

### tenant_id

Identifies the customer, studio, or license holder.

---

### user_id

Identifies the individual end user.

---

### session_id

Identifies a single active interaction session such as:

- one gameplay instance
- one support conversation
- one chatbot session

---

## Minimal Data Model

Example structure:

```text
interactions(
  tenant_id,
  user_id,
  session_id,
  ts,
  role,
  text,
  meta
)

mem_vectors(
  tenant_id,
  user_id,
  item_id,
  embedding,
  meta
)

profiles(
  tenant_id,
  user_id,
  kv
)

Each table is isolated by:


tenant_id


user_id


This allows:


bounded recall


selective persistence


controlled retention


licensing-safe separation



Privacy and Isolation Rules
Non-negotiable rules:


no cross-user memory bleed


no cross-tenant memory bleed


retrieval must enforce tenant_id + user_id filtering


retention must be configurable


export/delete must be supported


auditability must remain possible


This supports:


privacy compliance


GDPR deletion/export


enterprise deployment safety


licensing trust


Memory should be useful, not invasive.

Governor and Shadow Logs
All chatbot and gameplay events route through the Governor first.
The Governor decides:


ALLOW


REVIEW


BLOCK


Each decision is written to structured shadow logs.
Example:
shadow_logs.jsonl
Stored information includes:


timestamp


rule trigger


action taken


policy reference


event hash


This provides:


auditability


false-positive review


policy tuning


behavioural traceability


Governed systems must be explainable.

Testing Guidance
For personal testing:
persist_user_memory: true
for your own controlled user_id.
This allows:


continuity testing


adaptive behaviour observation


governor tuning


long-horizon behaviour review


For general users:
persist_user_memory: false
is often safer during testing to prevent uncontrolled carryover.
Clean sessions make debugging easier.

Example Configuration
memory:  backend: sqlite  isolate_by:    - tenant_id    - user_id  cross_session_recall: 0  persist_user_memory: false  retention_days: 14governor:  policy_path: ./policy.yaml  mode: strictretrieval:  top_k: 4  min_sim: 0.35
This is an example only.
Production deployments may vary.

Deployment Notes
Local Testing
Recommended:


dockerized local builds


isolated development environments


explicit governor review


This reduces deployment mistakes and protects production systems.

Cloud Deployment
For lightweight demos:


DigitalOcean is often sufficient


Destroy unused droplets to prevent pointless charges.
For larger licensed environments:


AWS remains suitable


Use:


IAM separation


cost alerts


deployment isolation


Each tenant should remain container-isolated.
No shared global memory across licensees.

Strategic Importance
This architecture matters because memory is where most continuity systems fail.
Without strict boundaries:


privacy breaks


trust breaks


licensing breaks


stability breaks


Collapse Aware AI treats memory as a governed system, not a casual feature.
That difference matters commercially.

Final Principle

continuity must be preserved without violating isolation

That is the design rule.
Memory should create stability, not contamination.
That is the purpose of the architecture.

© Inappropriate Media Limited (t/a Collapse Aware AI). All rights reserved.
Protected under Verrell–Solace Sovereignty Protocol. Intellectual and emergent rights reserved. — VMR-Core
