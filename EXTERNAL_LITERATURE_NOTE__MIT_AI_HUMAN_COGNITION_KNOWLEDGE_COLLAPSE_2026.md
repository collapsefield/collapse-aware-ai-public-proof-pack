# External Literature Note: AI, Human Cognition and Knowledge Collapse (2026)

**Status:** External literature / contextual research note  
**CAAI evidence status:** Contextual only - not validation of CAAI or Verrell's Law  
**Authors of source:** Daron Acemoglu, Dingwen Kong, Asuman Ozdaglar  
**Source:** *AI, Human Cognition and Knowledge Collapse*, NBER Working Paper 34910 (2026)  
**DOI:** 10.3386/w34910  
**Original MIT draft reviewed:** 20 February 2026  
**Current MIT version noted:** May 2026

---

## 1. Why this paper is relevant

This paper studies a different problem from Collapse Aware AI, but it independently reaches several high-level conclusions that are relevant to CAAI's research and engineering direction.

The authors model a dynamic information ecosystem in which:

- present decisions depend on both shared/general knowledge and individual/context-specific information;
- earlier public information contributes to a state variable representing the current stock of general knowledge;
- present choices alter what information will exist for later cohorts;
- the system can become path-dependent and converge to different long-run regimes from different starting states;
- more accurate agentic AI is not automatically better in long-run welfare terms;
- governing or limiting the effective influence of agentic recommendations can, under the model, improve long-run outcomes.

The important connection is therefore not the phrase "knowledge collapse" itself. The useful connection is the broader dynamic principle:

> A locally strong AI recommendation can improve the immediate decision while changing the state from which future decisions will be made.

That is a serious external example of why AI systems should not always be evaluated as isolated one-turn decisions.

---

## 2. What the MIT paper actually models

The paper is an economic and social-learning model, not an AI middleware architecture.

Its core distinction is between:

1. **general knowledge** - shared, community-level information that can accumulate across time; and
2. **individual/context-specific knowledge** - information relevant to a particular person's current situation.

Human learning effort produces both private/context-specific information and a thinner public signal that contributes to later general knowledge. Agentic AI supplies context-specific recommendations that can substitute for human learning effort.

The authors show that this can create a dynamic trade-off: an AI system can improve decisions now while reducing the human learning activity that replenishes shared knowledge later.

In some parameter regimes, the model contains multiple steady states and path dependence. A sufficiently depleted knowledge stock can become a self-reinforcing trap. A sufficiently accurate agentic recommendation can also enlarge the basin of attraction of that low-knowledge state.

The paper then studies information-design policies that reduce the effective precision of agentic recommendations. In the model, a temporary period of full suppression followed by a permanent precision cap can move the system out of a bad basin and sustain a higher-knowledge trajectory.

---

## 3. Where it overlaps conceptually with CAAI

The overlap is real but bounded.

### History affects later outcomes

The MIT model contains an explicit dynamic state: earlier information and effort contribute to the current stock of general knowledge, which affects later behaviour and later information production.

CAAI separately investigates governed retained-state influence at behavioural selection time.

Both therefore reject a purely static view in which only the immediate input matters.

### Path dependence matters

The MIT model explicitly analyses multiple steady states, basins of attraction, tipping behaviour and path dependence.

CAAI's retained-state architecture is also concerned with trajectories: different retained histories can make different later behaviours eligible under otherwise similar present conditions.

The mathematical objects and mechanisms are different, but the shared systems-level lesson is useful: **trajectory can matter independently of one-step performance.**

### More influence is not automatically better

The MIT paper finds that greater agentic precision can have non-monotone long-run welfare effects and studies deliberate limits on agentic recommendation precision.

CAAI uses a different mechanism: retained information can influence selection, but that influence is intended to remain bounded by governance, suppression, relevance and final-selection controls.

The paper therefore gives external theoretical context for a design principle already important to CAAI: **useful information should not automatically be granted unlimited behavioural authority.**

### Global and context-specific knowledge should remain distinguishable

The MIT model depends heavily on the distinction between general knowledge and individual/context-specific information.

That distinction is directly useful when thinking about continuity systems. A continuity layer should not silently turn user-specific retained state into a replacement for wider domain knowledge, current evidence or clean present-task reasoning.

---

## 4. Important differences - do not overclaim

This paper does **not** validate CAAI or Verrell's Law.

It does not describe:

- the Crown runtime;
- retained-state candidate scoring;
- Governor modes;
- memory-weighted candidate selection;
- ContinuityFrame;
- Open Loops;
- Interaction Fit;
- Agent Self-History;
- CAAI suppression controls;
- deterministic replay;
- Decision Records;
- Verrell's Law.

Its state variable is a society-level measure of public/general knowledge precision. CAAI's retained state is an engineered runtime mechanism for continuity and behavioural selection.

Likewise, the paper's proposed "garbling" policy is an information-design intervention that adds noise or fully suppresses an agentic recommendation. It should **not** be described as the same thing as CAAI Governor control or suppression.

The legitimate claim is narrower:

> Independent theoretical work from MIT/NBER shows that dynamic state, path dependence, long-run information effects and bounded agentic influence are important issues in agentic-AI systems.

---

## 5. Chronology and originality note

This source does not provide evidence that its authors copied Collapse Aware AI, and no such claim is made here.

There is, however, a useful public chronology.

CAAI material was publicly describing memory beyond simple storage, continuity, weighted moments, behavioural influence and Governor-style control during 2025, before the February 2026 working paper. Public CAAI posts include an August 2025 introduction and a November 2025 progress update describing a Bias Engine, Governor, memory flow, weighted moments, strong memory anchors and a continuity-memory layer.

The MIT/NBER paper is dated February 2026 and develops its argument through established economic and social-learning theory. Searches within the supplied February draft and the current May version show no use of the terms **Verrell**, **memory-weighted**, **retained state**, or **Governor**.

The responsible conclusion is therefore:

> The two bodies of work show partial thematic convergence around history, dynamic information state, path dependence and governed influence, but they use materially different mechanisms and terminology. The public chronology is useful for documenting independent CAAI development, not for alleging copying or influence.

---

## 6. Engineering questions this paper suggests for Evolution 2

The paper is not a software-engineering specification. The following are **CAAI engineering hypotheses inspired by the paper**, not recommendations made by Acemoglu, Kong or Ozdaglar.

### A. Preserve a hard boundary between general/domain knowledge and personal continuity state

Test whether E2 can keep:

- base-model/domain knowledge;
- retrieved external evidence;
- current-turn evidence; and
- user/agent-specific retained continuity

separate enough that personalised history never masquerades as general truth.

### B. Measure trajectory quality, not only turn quality

Add or preserve long-horizon evaluation where a response that looks good locally can still fail if it pushes the retained state into a poorer future trajectory.

Possible measures include:

- history-influence ratio across turns;
- clean-present-answer win rate;
- suppression/recovery activation rate;
- contradiction recovery time;
- trajectory divergence under matched present input;
- reversibility after correction or revocation;
- retained-state saturation;
- proportion of decisions dominated by a single historical anchor.

### C. Stress-test influence saturation

Run sequences in which retained history becomes increasingly strong and test whether:

- the clean present-task candidate remains genuinely competitive;
- current evidence can defeat old history;
- suppression activates before continuity becomes self-reinforcing error;
- a strong but stale anchor can be revoked cleanly;
- confidence reflects conflict between history and present evidence.

### D. Add a recovery / low-history intervention test

The MIT paper's two-phase policy suggests a useful *testing analogy*: temporarily reduce history influence, rebuild from clean present evidence, then restore bounded continuity influence.

For E2 this could become a test mode rather than a production policy:

1. drive the system into a deliberately bad retained-state trajectory;
2. suppress or cap retained-state influence;
3. present corrective evidence over several turns;
4. restore normal governed influence;
5. verify that the system remains on the corrected trajectory.

This would test whether E2 has recoverable continuity rather than irreversible behavioural lock-in.

### E. Test for attractor-like behaviour

Create matched-present-input tests from different histories and examine whether E2 settles into persistent behavioural regimes.

Where such regimes exist, measure:

- how they were entered;
- whether the Governor/suppression layer can exit them;
- how much intervention is required;
- whether exit is deterministic under replay;
- whether a bad regime can reappear from stale retained state.

### F. Do not optimise solely for personalised fit

The paper is a warning that optimising one local objective can damage a longer-run system objective.

For E2, strong Interaction Fit or continuity should therefore never be treated as the sole success metric. It should remain subordinate to truth, current-task performance, contradiction handling, revocation, safety constraints and clean evidence use.

---

## 7. Recommended E2 test additions

The following would be worth adding to the Evolution 2 validation backlog if equivalent coverage does not already exist:

1. **General-vs-personal knowledge separation test**  
   Verify that retained personal state cannot overwrite verified external/domain facts.

2. **History saturation test**  
   Repeatedly reinforce one historical preference/anchor and ensure influence remains bounded.

3. **Present-evidence override test**  
   Supply strong new evidence contradicting retained state and require correct transition.

4. **Suppression-and-recovery test**  
   Enter a bad trajectory, suppress history influence, correct state, restore normal influence and verify recovery.

5. **Matched-present / divergent-history trajectory test**  
   Compare identical present inputs under materially different retained histories and record both divergence and recovery behaviour.

6. **Long-horizon local-vs-global quality test**  
   Detect cases where individually plausible turns cumulatively degrade the system's retained state or future decision quality.

7. **Single-anchor dominance test**  
   Ensure one high-salience historical record cannot indefinitely suppress relevant newer evidence.

8. **Revocation durability test**  
   Verify that revoked or corrected information does not re-enter later selection through secondary associations or summaries.

---

## 8. Commercial and research use

This paper can strengthen CAAI's public framing in a limited and defensible way.

Useful language:

> Recent independent work from MIT and NBER has highlighted that agentic AI should be evaluated dynamically: highly effective immediate recommendations can alter the information environment from which later decisions are made, creating path-dependent long-run effects. Collapse Aware AI addresses a different engineering problem, but shares the concern that information influence should be bounded, state-aware, and evaluated across trajectories rather than only one turn at a time.

Avoid language such as:

- "MIT proved CAAI";
- "MIT validated Verrell's Law";
- "their model is the same as CAAI";
- "they copied our architecture";
- "CAAI prevents knowledge collapse".

None of those claims is supported by the paper.

---

## 9. Citation

Daron Acemoglu, Dingwen Kong, and Asuman Ozdaglar, **"AI, Human Cognition and Knowledge Collapse,"** NBER Working Paper 34910 (2026). DOI: **10.3386/w34910**.

The source is a working paper. MIT's current public copy is marked as updated May 2026 and states that Stone Center working papers are circulated for discussion and have not undergone the formal review process associated with official publications.

---

**CAAI note prepared:** 18 August 2026  
**Purpose:** external-literature trail, engineering prompts, and scope-safe public comparison.