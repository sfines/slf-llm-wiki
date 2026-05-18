# SkillGen Framework

SkillGen is a multi-agent framework designed for automatic, inference-time skill synthesis. It takes an existing dataset of LLM trajectories and derives a single auditable skill whose empirical net effect is verified before deployment. Rather than merely summarizing successful trajectories, SkillGen uses contrastive learning across both successes and failures.

## Multi-Agent Architecture

The framework operates using specialized agents for distinct roles. An induction agent extracts reusable success patterns and failure modes. A generation agent drafts candidate skills, while a verification agent evaluates their net effect against baseline performance.

## Core Stages

SkillGen proceeds through three main stages:
1. Baseline Elicitation
2. Contrastive Behavioral Induction
3. Generation-Verification-Refinement Loop

## See Also
- [Verified Inference-Time Skills](./verified-inference-time-skills.md)
- [Baseline Elicitation Stage](./baseline-elicitation-stage.md)
- [Contrastive Behavioral Induction](./contrastive-behavioral-induction.md)
- [Generation-Verification-Refinement Loop](./generation-verification-refinement-loop.md)
- [../core-concepts/autonomous-agents.md](../core-concepts/autonomous-agents.md)
- [Raw Source: SkillGen Paper](../../raw/skillgen-paper.md)