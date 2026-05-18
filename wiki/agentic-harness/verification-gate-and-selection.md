# Verification Gate and Selection

The Verification Gate and Selection mechanism acts as a critical safety and quality control checkpoint at the end of the skill synthesis process. It ensures that only skills with empirically proven utility are deployed.

## Best-of-K Selection

Because later refinement rounds do not guarantee continuous improvement, the framework tracks all generated candidates and utilizes a Best-of-K selection strategy. It identifies the candidate skill from the entire sequence that achieved the highest verified net gain.

## Verification Safeguards

The selected skill must pass a strict verification gate before being marked "active." This gate enforces thresholds on the absolute and relative net gain. Candidates failing to meet these criteria are marked "deprecated" and replaced by an empty intervention, preventing the deployment of harmful or regressive behaviors.

## See Also
- [Generation-Verification-Refinement Loop](./generation-verification-refinement-loop.md)
- [Skill Net-Effect Measurement](./skill-net-effect-measurement.md)
- [Raw Source: SkillGen Paper](../../raw/skillgen-paper.md)