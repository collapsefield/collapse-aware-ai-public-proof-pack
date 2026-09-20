# Collapse-Aware AI — Computational Reformulation and Metric Specification (v1.3)

**Supersedes:** `REFEREE_RESPONSE_v1.2_VERRELLS_LAW_PATHB.pdf`
**Status:** Speculative but internally coherent computational systems theory. No empirical results are claimed in this document.
**Related deposit:** Zenodo DOI 10.5281/zenodo.17416435 (v1.1b)

---

## 0. Purpose and scope

This document restates the framework in the language of computational systems theory and specifies the metrics by which its claims can be tested. It defines what would count as evidence. It does not report evidence.

Nothing here is a claim about physics. Where earlier versions used physical terminology, that language has been withdrawn — see §3.

**Provenance of prior review.** <!-- REPLACE: name the reviewer and their standing, or delete this block entirely. Do not describe an unnamed or non-human reviewer as a referee. -->

---

## 1. Core formulation

The system is modelled as a biased diffusion in logit space.

```
dz_t = b_Ψ(z_t, M_t) dt + Σ dW_t
```

where:

| Symbol | Meaning | Units |
|---|---|---|
| `z_t` | logit vector at step `t` | logit |
| `p_t = softmax(z_t / T)` | induced distribution over candidates | — |
| `T` | temperature | — |
| `M_t` | retained state at step `t` | — |
| `b_Ψ` | bias drift | logit · step⁻¹ |
| `Σ` | diffusion matrix | logit · step⁻¹ᐟ² |
| `W_t` | standard Wiener process | — |

The drift decomposes into three terms:

```
b_Ψ = α ∇_z log π_prior(z | M_t) + β ∇_z log π_anchor(z) − γ ∇_z H(p_t)
```

- `π_prior(· | M_t)` — memory-conditioned prior, parameterised as `softmax(u(M_t) / T)` for a memory-derived logit vector `u(M_t)`, so that `∇_z log π_prior` is well defined on the same space as `z`.
- `π_anchor` — fixed reference distribution representing task or safety constraints.
- `H(p_t)` — Shannon entropy of the induced distribution; the negative gradient term sharpens `p_t`.
- `α, β, γ ≥ 0` — gain coefficients set by the adaptive gain regulator (§3).

`t` indexes sampling steps, not physical time. All rates are per step.

This reframes resolution of a candidate as probabilistic settling under adaptive bias control. It is not a physical field interaction and should not be read as one.

---

## 2. Stationary behaviour

The induced density obeys the Fokker–Planck equation

```
∂_t p = −∇ · (b_Ψ p) + ½ ∇ · (D ∇p),    D = ΣΣᵀ
```

Each term of `b_Ψ` is a gradient, so the drift is conservative:

```
b_Ψ = −∇_z U_Ψ,    U_Ψ = −[ α log π_prior(z | M_t) + β log π_anchor(z) − γ H(p_t) ]
```

With zero-flux boundaries, `d/dt ∫ p dz = 0`.

**Condition on the stationary form.** If `D = σ² I` with `σ²` constant, the stationary density is

```
p* ∝ exp(−2 U_Ψ / σ²)
```

This requires `D` constant and isotropic. Positive-definiteness alone is not sufficient; for general state-dependent or anisotropic `D` no closed-form stationary density is claimed. Earlier versions overstated this condition.

---

## 3. Terminology

Physical terminology has been withdrawn in favour of computational systems language.

| Withdrawn term | Term used here |
|---|---|
| Collapse | Probabilistic resolution |
| Bias field | State-space bias operator |
| Resonance | Feedback weighting |
| Observer effect | Contextual conditioning |
| Memory = information | Memory-conditioned prior |
| Governor | Adaptive gain regulator |

The withdrawn terms should not be treated as synonyms recoverable from context. They are not used in this framework.

---

## 4. Metrics

### 4.1 Implementation checks

These confirm the system does what the specification says. They are not evidence of useful behaviour and should not be reported as such.

| Symbol | Definition | Reads as |
|---|---|---|
| `R_b` | `corr(Δz_t, b_t)` | Response-to-bias correlation |
| `S_b` | `Var_t[R_b(t)]` | Sessional stability of that correlation |

`R_b` is near-circular by construction: if `b_t` enters the drift, then `Δz_t ≈ b_t Δt + noise`. A high value confirms correct wiring. It does not establish that retained state improves behaviour.

### 4.2 Behavioural measures

| Symbol | Definition | Reads as |
|---|---|---|
| `Δ_KL` | `mean KL(p₁ ‖ p₀)` | Magnitude of distributional shift |
| `Δ_prior` | `mean [ KL(p₀ ‖ π_prior) − KL(p₁ ‖ π_prior) ]` | Movement toward the memory prior |
| `Δ_anchor` | `mean [ KL(p₀ ‖ π_anchor) − KL(p₁ ‖ π_anchor) ]` | Stabilisation against the anchor |

`p₀` denotes the distribution under the static-bias baseline; `p₁` denotes the distribution under retained-state conditioning.

### 4.3 Selectivity

Applying retained state is only half of the specified behaviour. Withholding it where it does not apply is the other half, and is measured separately.

Each probe carries a relevance label `r ∈ {related, unrelated}`, assigned before the run and independently of system output.

```
Sel = Δ_prior | related  −  Δ_prior | unrelated
FAR = P( |Δ_KL| > τ  |  unrelated )
```

- `Sel` — selectivity index. Large positive values indicate retained state is applied where it bears on the task.
- `FAR` — false-application rate. The proportion of unrelated probes on which the system shifts its distribution beyond threshold `τ`.

**Pass condition.** `Sel` significantly greater than zero **and** `Δ_prior | unrelated` not distinguishable from zero within its confidence interval. A system scoring well on `Δ_prior` alone while failing the unrelated condition is applying stored context indiscriminately, which is a failure, not a partial success.

`τ` must be fixed and stated before the run.

### 4.4 Controls

- Fixed seeds; matched temperature across arms.
- Static-bias baseline as the comparison arm.
- Bootstrap confidence intervals; significance threshold `p < 0.01`.
- Relevance labels assigned before runs, by a party other than the system operator where practical.
- Reported alongside: mean key-vector drift `D_K` and attention entropy `H_attn`.

---

## 5. Limitations

1. No empirical results are reported here. The metrics above are proposed, not yet satisfied.
2. `R_b` is an implementation check, not a finding.
3. The stationary result in §2 holds only under constant isotropic diffusion.
4. This framework makes no claim about physics, and no result obtained under it should be presented as evidence for any physical hypothesis.
5. Any similarity between behaviour in computational and biological systems, if observed, would be a finding about information processing — not a claim that the two are equivalent.

---

© 2025–2026 Verrell Moss Ross · Inappropriate Media Ltd (t/a Collapse Aware AI)
