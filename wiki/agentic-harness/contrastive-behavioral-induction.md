# Contrastive Behavioral Induction

Contrastive Behavioral Induction is the second stage of the SkillGen process, responsible for compressing baseline agent trajectories into an explicit summary diagnostic. It analyzes and clusters both successes and failures to identify underlying behavioral patterns.

## Failure and Success Analysis

The induction agent creates root-cause summaries for failed rollouts and embeds them into clusters representing recurring failure modes. Similarly, successful rollouts are summarized to describe reusable procedures, environmental conditions, and robustness checks.

## Generating Diagnostic Summaries

The resulting diagnostic summary includes an overall task description, cluster-level failure summaries, cluster-level success summaries, and targeted local contrastive observations. This low-dimensional representation is then used to generate task-specific candidate skills.

## See Also
- [Local Contrastive Analysis](./local-contrastive-analysis.md)
- [Baseline Elicitation Stage](./baseline-elicitation-stage.md)
- [Generation-Verification-Refinement Loop](./generation-verification-refinement-loop.md)
- [../agent-memory/agent-experiential-memory.md](../agent-memory/agent-experiential-memory.md)
- [Raw Source: SkillGen Paper](../../raw/skillgen-paper.md)