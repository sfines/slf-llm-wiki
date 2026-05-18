# Skill Iterative Refinement Feedback

Skill Iterative Refinement Feedback is the mechanism used to actively improve candidate skills within a generation loop, utilizing structured critiques rather than rewriting prompts entirely from scratch.

## Diagnostic Evidence Partitioning

After a candidate skill is evaluated, instances are partitioned into specific categories: successful repairs, harmful regressions, and unresolved failures. The verification agent analyzes these subsets to understand exactly how the skill influenced the outcomes.

## Targeted Update Rules

The verification agent aggregates its findings into specific, structured feedback directives. It instructs the generation agent on which components of the current skill to keep, remove, add, or emphasize. This targeted updating approach prevents prompt drift and incrementally optimizes the skill's performance over consecutive refinement rounds.

## See Also
- [Generation-Verification-Refinement Loop](./generation-verification-refinement-loop.md)
- [Repair vs Regression in Skills](./repair-vs-regression-in-skills.md)
- [Raw Source: SkillGen Paper](../../raw/skillgen-paper.md)