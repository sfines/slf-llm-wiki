# Dependency Stitching

Dependency stitching is the process by which SkillOps connects individual candidate skills into a coherent execution plan during the Task-Time Loop, heavily relying on the structural edges of the HSEG.

## Dual-Constraint Stitching

SkillOps enforces stricter connectivity than traditional dependency graphs:

- A transition between $s_i$ and $s_j$ is only accepted if both a dependency edge ($s_i \xrightarrow{dep} s_j$) AND a compatibility edge ($s_i \xrightarrow{comp} s_j$) exist.
- This ensures that not only does the upstream skill produce the correct *kind* of artifact needed, but the *type* interface strictly matches the downstream requirement.
- If a dependency exists without compatibility, an intermediate type-conversion adapter must be dynamically inserted (`add_adapter`).

## See Also

- [Task-Time Skill Loop](task-time-skill-loop.md)
- [Hierarchical Skill Ecosystem Graph (HSEG)](hierarchical-skill-ecosystem-graph.md)
- [Raw Source: SkillOps Paper](../../raw/skillops-paper.md)
