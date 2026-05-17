# Fast Recalibration for MAS Defense

**Fast Recalibration** is the ability of an [Adversarial Robustness](adversarial-robustness-mas.md) system to rapidly update its detection models after discovering a novel attack.

## The Recalibration Mandate
The [GAMBIT research](../raw/gambit-paper.md) proves that static "zero-shot" detection is insufficient for long-term security in MAS. Defenders must be able to adapt to **adaptive imposters** with minimal evidence.

## Technical Techniques
- **Meta-Learning:** Using architectures specifically trained for "learning to learn." Meta-learned detectors in GAMBIT converged **20x faster** than standard fine-tuned models.
- **Few-Shot Adaptation:** The benchmark sets a strict limit of **20 labeled examples** for recalibration. A robust system must achieve high accuracy from this tiny dataset.
- **Modular Defense:** Swapping out specialized [Harness Components](agent-harness.md) (e.g., execution guards) in response to new failure modes identified by an [Agent Debugger](ahe-agent-debugger.md).

## Significance
Fast recalibration transforms security from a **state** (the system is currently "safe") to a **process** (the system is "resilient" to change).

## See Also
- [GAMBIT Overview](gambit-overview.md)
- [Adaptive Imposter Dynamics](gambit-adaptive-imposter.md)
- [GAMBIT Three-Mode Benchmark](gambit-three-mode-benchmark.md)
