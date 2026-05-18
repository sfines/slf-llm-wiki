# Skill Net-Effect Measurement

Skill Net-Effect Measurement provides the quantitative metric for evaluating newly synthesized agent skills. It evaluates overall performance by explicitly balancing the positive and negative impacts of the intervention.

## Calculating Net Gain

The net effect is defined as the difference between the number of baseline failures successfully repaired by the skill and the number of baseline successes inadvertently broken (regressions) by the skill.

## Balancing Repairs and Regressions

This dual-sided measurement is vital for interactive agents. A skill might offer highly effective instructions for a particular edge case, but if those instructions confuse the agent on standard tasks, the net gain will be negative. The net-effect metric inherently protects against over-indexing on specific failure modes.

## See Also
- [Causal Evaluation of Skill Interventions](./causal-evaluation-of-skill-interventions.md)
- [Verification Gate and Selection](./verification-gate-and-selection.md)
- [Repair vs Regression in Skills](./repair-vs-regression-in-skills.md)
- [Raw Source: SkillGen Paper](../../raw/skillgen-paper.md)