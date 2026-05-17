# Hierarchical Skill Ecosystem Graph (HSEG)

The Hierarchical Skill Ecosystem Graph (HSEG) is the primary data structure used by SkillOps to organize an agent's skill library, representing both internal skill constraints and external skill relationships.

## Graph Levels

HSEG operates on two levels:
1. **Internal Skill Graph**: Represents individual skills via structured Skill Contracts linking Preconditions, Operations, Artifacts, Validators, and Failure Modes.
2. **External Graph-of-Graphs**: Connects distinct skills using four typed directed relations:
   - **Dependency (`dep`)**: An artifact from $s_i$ partially or fully satisfies the precondition of $s_j$.
   - **Compatibility (`comp`)**: The output type of $s_i$ is compatible with the input type required by $s_j$.
   - **Redundancy (`red`)**: Two skills expose equivalent interfaces (preconditions and artifacts).
   - **Alternative (`alt`)**: Two skills target the same goal but implement different operations.

## See Also

- [Skill Contracts](skill-contracts.md)
- [Dependency Stitching](dependency-stitching.md)
- [Raw Source: SkillOps Paper](../../raw/skillops-paper.md)
