# Repair vs Regression in Skills

In agent skill synthesis, accurately measuring the success of an intervention necessitates distinguishing between "repairs" and "regressions" across a verification dataset.

## Identifying Repairs

A repair occurs when the skill intervention successfully guides the agent to solve an instance that the baseline agent previously failed. This represents the intended positive impact of the skill, directly addressing identified capability gaps.

## Tracking Regressions

A regression occurs when the skill intervention breaks an instance that the baseline agent originally solved correctly. Regressions often happen when newly added instructions overgeneralize or introduce unnecessary constraints that confuse the agent in standard scenarios. Effectively managing the tradeoff between repairs and regressions is central to verifying skill utility.

## See Also
- [Skill Net-Effect Measurement](./skill-net-effect-measurement.md)
- [Causal Evaluation of Skill Interventions](./causal-evaluation-of-skill-interventions.md)
- [Raw Source: SkillGen Paper](../../raw/skillgen-paper.md)