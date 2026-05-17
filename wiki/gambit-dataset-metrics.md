# GAMBIT Dataset Metrics

The **GAMBIT Dataset** is a large-scale collection of labeled multi-agent trajectories designed to train and evaluate [Adversarial Robustness](adversarial-robustness-mas.md) systems.

## Dataset Composition
- **Total Instances:** 27,804 labeled trajectories.
- **Strategy Diversity:** 240 co-evolved imposter strategies.
- **Agent Roles:** Benign agents (playing optimally) vs. Imposter agents (sabotaging the game).
- **Substrate Problem:** Chess (providing verifiable ground truth for every move).
- **Agent Model:** Gemini 3.1 Pro.

## Labeling Schema
Each instance is labeled with:
- **Agent Identity:** Benign or Imposter.
- **Strategy ID:** The specific evolutionary variation used by the imposter.
- **Impact Score:** How much the agent's actions deviated from the optimal path and affected the collective goal.

## Research Utility
The dataset is the first of its kind to provide **co-evolved** examples, where the malicious behavior was specifically designed to bypass the defenses included in the same benchmark.

## See Also
- [GAMBIT Overview](gambit-overview.md)
- [Adaptive Imposter Dynamics](gambit-adaptive-imposter.md)
- [MultiHop-RAG Benchmark Evaluation](multihop-rag-evaluation.md)
