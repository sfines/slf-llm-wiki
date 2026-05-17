# GAMBIT Three-Mode Benchmark

The **GAMBIT Benchmark** evaluates [Imposter Detectors](gambit-detector-evaluation.md) across three distinct modes designed to simulate the evolution of adversarial attacks in [Multi-Agent Systems](multi-agent-systems.md).

## Mode 1: Zero-Shot (In-Distribution)
- **Objective:** Measure baseline detection accuracy on attack strategies the detector has already "seen" during its training phase.
- **Significance:** Validates that the detector's core architecture is capable of identifying basic deceptions.

## Mode 2: Zero-Shot (Out-of-Distribution)
- **Objective:** Evaluate how well the detector generalizes to novel, unseen imposter strategies without any new training data.
- **Significance:** Measures robustness against **Distribution Shift**, where an attacker changes their tactics but not their fundamental nature.

## Mode 3: Fast Recalibration (Few-Shot Adaptation)
- **Objective:** Measure the speed and efficiency with which a detector can adapt to a novel attack after being given only **20 labeled examples**.
- **Significance:** This is the most critical mode in GAMBIT. It highlights the **[Recalibration Gap](gambit-evaluation-results.md)**: the fact that two detectors with identical zero-shot scores can differ vastly (up to 8x) in their ability to adapt to new threats.

## See Also
- [GAMBIT Overview](gambit-overview.md)
- [Fast Recalibration Techniques](gambit-fast-recalibration.md)
- [Imposter Detector Evaluation](gambit-detector-evaluation.md)
