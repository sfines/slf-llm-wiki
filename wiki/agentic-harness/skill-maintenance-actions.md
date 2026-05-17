# Skill Maintenance Actions

Based on the health diagnosis of the skill library, SkillOps applies typed maintenance actions to repair and optimize the ecosystem, reducing skill technical debt without manual intervention.

## Typed Actions

- **merge**: Collapses a redundant pair of skills connected by a redundancy edge, retaining the one with higher utility.
- **repair**: Rewrites the operation of a high-risk skill using execution failure logs as feedback.
- **retire**: Removes obsolete, consistently failing, or extremely low-utility skills to prune the retrieval candidate pool.
- **add_validator**: Inserts a validation check when a skill has a validation gap, often inheriting it from a matching sibling.
- **add_adapter**: Inserts a type-conversion shim when one skill depends on another but their interfaces lack a compatibility edge.
- **instantiate**: Binds a task-specific argument value to a parameterized skill during task time.

## See Also

- [Library-Time Skill Loop](library-time-skill-loop.md)
- [Skill Library Health Diagnosis](skill-library-health-diagnosis.md)
- [Raw Source: SkillOps Paper](../../raw/skillops-paper.md)
