# Baseline Elicitation Stage

The Baseline Elicitation Stage is the foundational first step in the SkillGen framework. It is designed to collect successful and failed trajectories by running a base agent on a designated induction dataset.

## Dual-Stratum Collection

This stage intentionally captures both successes and failures. Failures highlight the capability gaps where the base agent requires assistance, while successes identify the procedures the agent is already capable of executing correctly. Analyzing both is crucial to ensure generated skills don't provide misleading advice or redundant instructions.

## Verification Caching

In addition to collecting induction data, this stage caches no-skill baseline outcomes on a separate verification subset. This cached data is later used to measure the net effect of generated skills against the original baseline agent.

## See Also
- [SkillGen Framework](./skillgen-framework.md)
- [Contrastive Behavioral Induction](./contrastive-behavioral-induction.md)
- [Repair vs Regression in Skills](./repair-vs-regression-in-skills.md)
- [Raw Source: SkillGen Paper](../../raw/skillgen-paper.md)