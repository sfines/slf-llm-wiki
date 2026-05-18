# Local Contrastive Analysis

Local Contrastive Analysis is a critical technique utilized during Contrastive Behavioral Induction. It directly compares failed trajectories against their nearest successful neighbors to isolate granular differences in agent behavior.

## Nearest-Neighbor Retrieval

For each failed instance, the framework retrieves the closest successful rollout in the embedding space. This ensures the analysis is grounded in highly similar task contexts.

## Contrastive Observation Generation

The induction agent examines these paired trajectories to generate a contrastive observation. This explicitly identifies the "small" action choices or validation steps that the successful rollout executed but the failed rollout omitted, providing highly targeted advice anchored in proven agent capabilities.

## See Also
- [Contrastive Behavioral Induction](./contrastive-behavioral-induction.md)
- [Repair vs Regression in Skills](./repair-vs-regression-in-skills.md)
- [../agent-memory/agent-experiential-memory.md](../agent-memory/agent-experiential-memory.md)
- [Raw Source: SkillGen Paper](../../raw/skillgen-paper.md)