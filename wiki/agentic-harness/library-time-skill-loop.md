# Library-Time Skill Loop

The Library-Time Loop processes execution traces asynchronously to perform global library health diagnosis and persistent skill maintenance, evolving the library into a robust software asset.

## Maintenance Process

Operating independently of task execution, the loop follows these phases:

1. **Health Diagnosis**: Computes local health scores (Utility, Redundancy, Compatibility, Failure Risk, Validation Gap) for each skill using execution logs.
2. **Risk Propagation**: Uses CGPD to flow risk through the dependency graph.
3. **Typed Actions Application**: Executes rules to clean the library by applying actions like `merge`, `repair`, `retire`, `add_validator`, and `add_adapter`.

By decoupling maintenance from execution, SkillOps avoids adding costly LLM inference overhead at task time.

## See Also

- [Skill Maintenance Actions](skill-maintenance-actions.md)
- [Task-Time Skill Loop](task-time-skill-loop.md)
- [Raw Source: SkillOps Paper](../../raw/skillops-paper.md)
