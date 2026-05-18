# Causal Evaluation of Skill Interventions

Causal Evaluation of Skill Interventions frames the application of an agent skill as a formal behavioral intervention. It relies on the potential outcome framework to rigorously measure the impact of adding a skill to a base agent.

## Potential Outcome Framework

For every input instance, the framework evaluates two potential outcomes: the baseline outcome (without the skill) and the skill-augmented outcome. This allows for a direct causal comparison on identical inputs.

## Measuring Treatment Effects

By evaluating outcomes under these two conditions, researchers can precisely quantify the expected net effect of the skill. This methodology ensures that performance gains are definitively attributed to the skill intervention rather than dataset variance or environmental noise.

## See Also
- [Skill Net-Effect Measurement](./skill-net-effect-measurement.md)
- [Repair vs Regression in Skills](./repair-vs-regression-in-skills.md)
- [Verified Inference-Time Skills](./verified-inference-time-skills.md)
- [Raw Source: SkillGen Paper](../../raw/skillgen-paper.md)