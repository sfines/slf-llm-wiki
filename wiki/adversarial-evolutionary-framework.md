# Adversarial Evolutionary Framework

An **Adversarial Evolutionary Framework** is the technical engine used in [GAMBIT](gambit-overview.md) to generate **adaptive imposters**.

## Core Logic
The framework uses evolutionary algorithms to optimize the malicious behavior of an agent:
1.  **Population:** Start with a set of basic deceptive strategies.
2.  **Fitness Function:** Evaluated based on two criteria:
    - **Goal Achievement:** How effectively the strategy sabotages the collective task (e.g., Chess).
    - **Stealthiness:** How well the strategy evades the current [Imposter Detector](gambit-detector-evaluation.md).
3.  **Mutation & Crossover:** Generate new strategy variations by subtly altering agent prompts or reasoning logic.
4.  **Selection:** Retain the most effective and stealthy strategies for the next generation.

## Result: Adaptive Distribution Shift
This framework ensures that the imposter is always "pushing the boundary" of the current defense, creating the constant [Distribution Shift](gambit-three-mode-benchmark.md) that the GAMBIT benchmark is designed to measure.

## See Also
- [Adaptive Imposter Dynamics](gambit-adaptive-imposter.md)
- [Fast Recalibration](gambit-fast-recalibration.md)
- [Agentic Harness Engineering (AHE)](agentic-harness-engineering.md)
