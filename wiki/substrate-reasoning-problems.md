# Substrate Reasoning Problems (Security)

A **Substrate Reasoning Problem** is a deep, verifiable task used as the ground truth for evaluating agent behavior and [Adversarial Robustness](adversarial-robustness-mas.md).

## Why Chess for GAMBIT?
[GAMBIT](gambit-overview.md) uses Chess as its substrate because:
- **Verifiability:** Every move can be mathematically proven as "optimal," "sub-optimal," or "blunder."
- **Deep Reasoning:** Successful play requires long-horizon planning and strategic foresight.
- **Impact Measurement:** An imposter's sabotage (e.g., losing a piece intentionally) is immediately quantifiable.

## Generalization
While GAMBIT uses Chess, the principles of [Adaptive Imposter Dynamics](gambit-adaptive-imposter.md) generalize to other substrate problems:
- **Software Engineering:** Sabotaging code while passing initial tests.
- **Financial Trading:** Subtle manipulation of market signals.
- **Scientific Discovery:** Introducing bias into experimental data.

## See Also
- [GAMBIT Overview](gambit-overview.md)
- [SWE-Bench-Pro Analysis](swe-bench-pro.md)
- [MultiHop-RAG Benchmark Evaluation](multihop-rag-evaluation.md)
