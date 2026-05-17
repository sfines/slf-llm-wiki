# Skill Technical Debt

Skill technical debt refers to persistent defects in an LLM agent's skill library that accumulate as skills are added, reused, patched, and linked to changing dependencies.

## Forms of Technical Debt

While a defect may not break a single skill locally, it can harm future retrieval, composition, and execution. Common patterns include:
- **Redundancy**: Duplicate or near-duplicate skills that inflate the retrieval pool and reduce precision.
- **Validation Gaps**: Missing local correctness checks (validators) allowing invalid artifacts to propagate.
- **Interface Drift / Incompatibility**: Mismatches between the output artifact of one skill and the expected input of a downstream dependency.
- **Stale Implementations**: Broken or obsolete operations, scripts, or APIs with a high failure risk.

## See Also

- [Skill Library Health Diagnosis](skill-library-health-diagnosis.md)
- [Skill Validation Gaps](skill-validation-gaps.md)
- [Raw Source: SkillOps Paper](../../raw/skillops-paper.md)
