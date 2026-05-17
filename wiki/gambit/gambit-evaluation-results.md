# GAMBIT Evaluation Results

The **Evaluation Results** of the [GAMBIT benchmark](gambit-overview.md) highlight critical gaps in current [Multi-Agent System](../core-concepts/multi-agent-systems.md) defenses.

## 1. Zero-Shot Fragility
Across all tested models (including Gemini 3.1 Pro), baseline zero-shot detection was fragile. **Adaptive imposters** were able to bypass detectors with a success rate near 50%, meaning the defense was barely more effective than random guessing.

## 2. The Recalibration Gap
The most significant finding was the disparity in adaptation speed:
- **Result:** Two detectors with near-identical scores in Mode 1 (In-Distribution) performed radically differently in Mode 3 (Recalibration).
- **8x Difference:** One model required 8x fewer examples to "learn" a new attack pattern than the other.
- **Meta-Learning Advantage:** The meta-learned variant converged **20x faster** than standard models.

## 3. Performance Collapse
The research confirmed that the gains achieved by collaborative agent teams (e.g., through [Organizational Design](../agyn/organizational-design-for-agents.md)) are highly sensitive to adversarial infiltration. A single stealthy imposter caused the collective performance to drop below the level of a single standalone agent.

## Conclusion for Developers
Security in MAS cannot be a "one-and-done" deployment. It must be an **active loop** capable of [Fast Recalibration](gambit-fast-recalibration.md) to stay ahead of co-evolving threats.

## See Also
- [GAMBIT Three-Mode Benchmark](gambit-three-mode-benchmark.md)
- [APWA Evaluation Results](../apwa/apwa-evaluation-results.md)
- [SWE-bench 500 Evaluation](../agyn/swe-bench-500.md)
