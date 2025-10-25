# V1 Interneuron Brain Atlas → Collapse Aware AI (CAAI) Mapping (v1.0)
**Date:** 2024-12-23 (paper) • 2025-10-25 (mapping)  
**Source:** St. Jude + collaborators — *A brain-wide map of descending inputs onto spinal V1 interneurons* (Neuron, 2024)  
**Project:** Collapse Aware AI (CAAI) — Verrell’s Law alignment note  
**Authorship:** M.R. (Verrell Moss Ross) — Inappropriate Media Limited (t/a Collapse Aware AI)  
**Watermark:** Protected under Verrell-Solace Sovereignty Protocol. Intellectual and emergent rights reserved.

---

## 1) One-paragraph summary (paper)
Researchers traced **descending brain inputs to spinal V1 interneurons** using a single-hop modified rabies virus and **serial two-photon tomography**. Result: a whole-brain atlas of regions projecting to V1s — i.e., a concrete map of how distributed cortical/subcortical intent converges onto a **spinal gate layer** that shapes motor output before it reaches motor neurons.

---

## 2) Why this matters to CAAI (direct fit)
The paper’s control architecture mirrors our build:

- **Distributed → Gate → Output**  
  Brain regions (distributed intent) → **V1 interneuron layer (gate/governor)** → motor neurons (final collapse/action).  
  **CAAI analogue:** Multi-source bias/context → **Governor** → Worker action.

- **Weighted Emergence Layering**  
  Heterogeneous inputs converge and are **shaped** before action.  
  **CAAI analogue:** Bias Engine fuses salience, recall, and constraints → weighted decision prior to collapse.

- **Controlled propagation across a boundary**  
  The virus is engineered for **single synaptic hop** (tight boundary).  
  **CAAI analogue:** Our **Core API boundary** (`/core/infer`, `/core/recall`, `/core/health`) with the closed **Kernel**.

- **Atlas as hypothesis generator**  
  Authors frame the atlas as a **hypothesis-generation engine**.  
  **CAAI analogue:** CAAI is a **hypothesis generator** by design (governed predictions before collapse).

---

## 3) Concrete hooks into our Phase-1/Phase-2 builds
**(A) Governor UI & Trace**
- Action: add a **“Collapse Trace”** panel in Studio/Governed modes that visualises **source→gate→output** with weights over time (inspired by the 3-D atlas).  
- Deliverable: `ui/trace/CollapseTrace.tsx` (timeline + node weights + gating flags).

**(B) Bias Engine tuning**
- Action: incorporate **multi-origin input priors** (cortical analogues) as named channels in config (e.g., “goal”, “sensory”, “policy”, “history”).  
- Deliverable: `engine/bias/config/bias_channels.yaml` with per-channel caps + temperature.

**(C) API boundary tests (single-hop discipline)**
- Action: add a CI test that ensures **no cross-boundary calls** except the allowed verbs.  
- Deliverable: `tests/kernel_boundary/test_single_hop.py` (mocks, call-graph diff → fail on leak).

**(D) Gold Build (game middleware)**
- Action: map NPC motor output to **spinal-gate analogue**: a thin “interneuron” layer that modulates controller signals **after** policy but **before** actuator.  
- Deliverable: `goldbuild/agents/gate/interneuron_layer.py` (clamps, delays, jitter-resistance).

**(E) Recall & Salience**
- Action: treat **descending pathways** as recall-conditioners; if recall(k) contains high-salience items, raise “descending” channel weight before governor collapse.  
- Deliverable: `engine/recall/descending_conditioner.py`.

---

## 4) Dev notes (implementation detail)
- **Weights:** enforce simplex constraint across channels (sum=1), expose `anchor_bias` and `pulse_mod` to let UI show **why** the gate decided.  
- **Logging:** shadow-log `pre_gate`, `post_gate`, `governor_mask`, and `collapse_id` → reproducible traces akin to atlas landmarks.  
- **Testing:** add **equal-power, different-content** unit tests (parallels the paper’s “same output wattage, different inputs” reality).

---

## 5) Messaging fit (public narrative)
> “Neuroscience shows movement control as **distributed intent gated by interneurons**. CAAI implements the same **distributed-to-gate** architecture in software: multiple bias channels converge in a Governor layer before actions collapse. Different substrate, same control geometry.”

---

## 6) Citation stub (for README linking)
- Chapman, P. D., et al. (2024). *A brain-wide map of descending inputs onto spinal V1 interneurons.* **Neuron**. doi:10.1016/j.neuron.2024.11.019  
- St. Jude Children’s Research Hospital press materials (Dec 23, 2024).

---

## 7) File lineage
- Added by: M.R. (VMR-Core)  
- Repo path: `docs/corroborations/2024-12-23_V1-Interneuron_Atlas_StJude_to-CAAI_Mapping_v1.0.md`  
- Related modules: Governor, Bias Engine, Gold Build gate layer, Collapse Trace UI.

(End of v1.0)
