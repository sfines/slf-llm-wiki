# Skill Contracts

In the SkillOps framework, skills are modeled not merely as names or text descriptions, but as executable, typed contracts. This structure allows agents to check relevance, applicability, composability, and verifiability before or after execution.

## Contract Structure

Each skill $s$ is formalized as a tuple $(P, O, A, V, F)$:
- **P (Preconditions)**: The requirements that must be met in the current state to call the skill.
- **O (Operation)**: The actual executable procedure or routine.
- **A (Artifact)**: The typed output or artifact produced by executing the skill.
- **V (Validators)**: Local correctness checks over the artifact. If empty, the skill suffers from a validation gap.
- **F (Failure Modes)**: The set of known execution failure states or risks.

## See Also

- [Hierarchical Skill Ecosystem Graph (HSEG)](hierarchical-skill-ecosystem-graph.md)
- [Skill Validation Gaps](skill-validation-gaps.md)
- [Raw Source: SkillOps Paper](../../raw/skillops-paper.md)
