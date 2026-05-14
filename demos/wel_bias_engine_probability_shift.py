"""
Weighted Emergence Layering (WEL)
Minimal Bias Engine Probability Shift Demonstration

Author:       Marcos Verrell Moss Ross (M.R.)
Organisation: Inappropriate Media Limited / Collapse Aware AI
First published publicly: 2026-05-13
Version:      WEL-DEMO-001

Purpose:
    Demonstrates how a memory-derived bias vector B(y; M_t) can alter
    candidate-selection probabilities without modifying the underlying base model.

Core claim:
    Same base logits. Same candidate set. Different memory-bias field.
    Different selected behavioural probability landscape.

Canonical public form:
    P(y_{t+1}) = Softmax(U(y; S_t, O_t) + λ B(y; M_t))

Public-boundary note:
    This demo uses a simple illustrative bias vector. It does not disclose
    production Crown internals, schemas, thresholds, private scoring rules,
    candidate-packing logic, or governor implementation details.

Requirements:
    Python 3.9+
    numpy

Copyright:
    Copyright © 2026 Marcos Verrell Moss Ross / Inappropriate Media Limited.
    This demonstration is provided for technical provenance, transparency,
    and research discussion. It does not grant permission to reproduce,
    commercialise, or incorporate the WEL framework into third-party systems
    without written permission.
"""

import numpy as np


def softmax(logits: np.ndarray) -> np.ndarray:
    """
    Numerically stable softmax.
    Converts raw logits into a probability distribution.
    """
    shifted = logits - np.max(logits)
    exp_values = np.exp(shifted)
    return exp_values / np.sum(exp_values)


def wel_probability_shift(
    base_logits: np.ndarray,
    memory_bias: np.ndarray,
    lambda_weight: float = 0.6,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Applies a WEL memory-weighted shift to candidate logits.

    This is the public-safe minimal form of:
        U(y; S_t, O_t) + λ B(y; M_t)

    Args:
        base_logits:
            Raw candidate scores from the base model or candidate generator.
        memory_bias:
            Memory-derived behavioural bias vector B(y; M_t).
            Positive values increase compatibility with retained memory.
            Negative values reduce compatibility with retained memory.
            In full WEL, this may be derived from recency, salience,
            and anchor components, but those production mechanics are not disclosed here.
        lambda_weight:
            Coupling strength controlling how strongly memory affects selection.
            Expected range: 0.0 to 1.0.

    Returns:
        baseline_probabilities:
            Probability distribution before memory weighting.
        weighted_probabilities:
            Probability distribution after memory weighting.
        adjusted_logits:
            Logits after memory-bias injection.
    """
    if base_logits.shape != memory_bias.shape:
        raise ValueError("base_logits and memory_bias must have the same shape.")
    if not 0.0 <= lambda_weight <= 1.0:
        raise ValueError("lambda_weight must be bounded between 0.0 and 1.0.")

    baseline_probabilities = softmax(base_logits)
    adjusted_logits = base_logits + (lambda_weight * memory_bias)
    weighted_probabilities = softmax(adjusted_logits)

    return baseline_probabilities, weighted_probabilities, adjusted_logits


def run_demo() -> None:
    """
    Runs a minimal WEL probability-shift demonstration.
    """
    candidates = ["Action_A", "Action_B", "Action_C", "Action_D"]

    # Base model preference:
    # Action_C starts as the strongest raw candidate under present-state utility U(y; S_t, O_t).
    base_logits = np.array([2.0, 1.5, 3.0, 0.5])

    # Public-safe memory-derived bias B(y; M_t):
    # Prior retained state favours Action_A and dampens Action_C.
    # Values are illustrative and bounded for demonstration purposes only.
    memory_bias = np.array([3.0, -0.5, -1.5, 0.0])

    lambda_weight = 0.6

    baseline, weighted, adjusted_logits = wel_probability_shift(
        base_logits=base_logits,
        memory_bias=memory_bias,
        lambda_weight=lambda_weight,
    )

    print("=== Weighted Emergence Layering Demo ===")
    print(f"Lambda coupling: {lambda_weight}")
    print()
    print("Candidate | Base Logit | Memory Bias | Adjusted Logit | Baseline Prob | WEL Weighted Prob")
    print("-" * 91)

    for candidate, raw, bias, adjusted, base_p, weighted_p in zip(
        candidates,
        base_logits,
        memory_bias,
        adjusted_logits,
        baseline,
        weighted,
    ):
        print(
            f"{candidate:<9} | "
            f"{raw:>10.2f} | "
            f"{bias:>11.2f} | "
            f"{adjusted:>14.2f} | "
            f"{base_p:>13.4f} | "
            f"{weighted_p:>17.4f}"
        )

    baseline_choice = candidates[int(np.argmax(baseline))]
    weighted_choice = candidates[int(np.argmax(weighted))]

    print()
    print(f"Baseline selected candidate:     {baseline_choice}")
    print(f"WEL weighted selected candidate: {weighted_choice}")
    print()
    print(
        "Result: Same base logits and candidate set, but memory-weighted bias "
        "changes the final behavioural probability landscape."
    )


if __name__ == "__main__":
    run_demo()
