# Generation-Verification-Refinement Loop

The Generation-Verification-Refinement Loop is the iterative final stage of the SkillGen framework. It turns diagnostic summaries into candidate skills, rigorously evaluates their impact, and incorporates structured feedback to continually refine them.

## Candidate Skill Generation

In each round, a generation agent creates a new candidate skill using a fixed schema that includes task context, success techniques, and failure-avoidance patterns. This transforms raw diagnostics into applicable inference-time instructions.

## Verification and Refinement

The candidate skill is loaded into the agent and evaluated on a verification subset. The outcomes are compared against the baseline to measure the skill's net effect. Based on this comparison, structured feedback guides the refinement agent to edit the skill—keeping, removing, adding, or emphasizing specific components for the next round.

## See Also
- [Skill Iterative Refinement Feedback](./skill-iterative-refinement-feedback.md)
- [Verification Gate and Selection](./verification-gate-and-selection.md)
- [Skill Net-Effect Measurement](./skill-net-effect-measurement.md)
- [Raw Source: SkillGen Paper](../../raw/skillgen-paper.md)