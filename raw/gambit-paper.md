# GAMBIT: A Three-Mode Benchmark for Adversarial Robustness in Multi-Agent LLM Collectives

**Authors:** Alexandre Le Mercier, Chris Develder, Thomas Demeester
**Date:** May 13, 2026
**Source:** arXiv:2605.09027
**DOI:** 10.48550/arXiv.2605.09027

## Abstract Summary
This paper introduces **GAMBIT**, a benchmark designed to evaluate the adversarial robustness of Multi-Agent Systems (MAS) against **adaptive imposters**. Unlike prior benchmarks that focus on static attacks, GAMBIT models the co-evolution of attacks and defenses. It features three evaluation modes—In-Distribution, Out-of-Distribution, and Fast Recalibration—and uses chess as a substrate for evaluating agent reasoning and imposter impact.

## Key Innovations
- **Three-Mode Evaluation:** Moving beyond zero-shot scores to measure adaptation speed (recalibration).
- **Adaptive Imposter Framework:** An evolutionary system that allows imposter agents to bypass detectors.
- **Fast Recalibration:** Techniques (e.g., meta-learning) that enable detectors to adapt to novel attacks from just 20 labeled examples.
- **Large-Scale Dataset:** 27,804 labeled instances spanning 240 co-evolved strategies.

## Key Results
- **Stealthy Imposters:** The evolved imposter achieved a **50.5% F1-score** against a Gemini 3.1 Pro detector, making it nearly undetectable.
- **Recalibration Gap:** Two detectors with similar zero-shot scores differed by **8x** in adaptation ability.
- **Meta-Learning Efficiency:** Meta-learned detectors converged **20x faster** than standard models during recalibration.

## Reference
Mercier, A. L., et al. (2026). GAMBIT: A Three-Mode Benchmark for Adversarial Robustness in Multi-Agent LLM Collectives. arXiv preprint arXiv:2605.09027.
