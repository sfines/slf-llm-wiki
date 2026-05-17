# Recalibration Gap in Defense

The **Recalibration Gap** is a critical security insight identified by the [GAMBIT research](../raw/gambit-paper.md).

## Definition
It is the disparity between two defensive systems that appear identical in static performance but differ significantly in their ability to adapt to new information.

## The Benchmark Discovery
In the [GAMBIT Mode 3 (Recalibration)](gambit-three-mode-benchmark.md) testing:
- **Observation:** Two detectors achieved near-identical F1-scores in zero-shot detection.
- **The Gap:** When presented with a novel attack and 20 labeled examples, one detector improved its accuracy by only 5%, while the other improved by 40%.
- **8x Difference:** The high-performing model reached target accuracy with 8x fewer examples than its peer.

## Why it Matters
The recalibration gap proves that **static benchmarks are dangerous** for MAS security. A system that seems "secure" today may be completely rigid and unable to defend itself against the evolved threats of tomorrow.

## See Also
- [GAMBIT Evaluation Results](gambit-evaluation-results.md)
- [Fast Recalibration](gambit-fast-recalibration.md)
- [Meta-Agent Refinement Loop](confucius-meta-agent-loop.md)
