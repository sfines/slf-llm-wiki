# Imposter Detector Evaluation

**Imposter Detector Evaluation** in [GAMBIT](gambit-overview.md) involves testing various AI architectures for their ability to distinguish between benign agents and **adaptive imposters**.

## Evaluated Architectures
- **LLM-based Detectors:** Using frontier models (e.g., Gemini 3.1 Pro) to analyze communication logs and reasoning traces.
- **Meta-Learned Detectors:** Models designed for rapid [Fast Recalibration](gambit-fast-recalibration.md).
- **Ensemble Detectors:** Combining multiple models and rule-based heuristics.

## Key Findings
1.  **Zero-Shot Deception:** Even the most powerful LLMs are poor predictors of robustness when used in a zero-shot capacity. They are easily fooled by evolved strategies.
2.  **The Recalibration Gap:** The true strength of a detector is only visible in [Mode 3 (Recalibration)](gambit-three-mode-benchmark.md). Two models with identical baseline scores can show an 8x difference in their ability to "learn" the new attack pattern.
3.  **Deep Reasoning Requirement:** Effective detection requires the model to understand the **substrate task** (e.g., Chess logic) to see through "logical" but malicious agent moves.

## See Also
- [GAMBIT Three-Mode Benchmark](gambit-three-mode-benchmark.md)
- [GAMBIT Evaluation Results](gambit-evaluation-results.md)
- [Agent Role: Reviewer](agyn-role-reviewer.md)
