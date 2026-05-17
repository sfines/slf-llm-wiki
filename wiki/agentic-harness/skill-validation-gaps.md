# Skill Validation Gaps

A validation gap occurs when an agent's skill lacks a local correctness check (validator) over the artifact it produces. This is a common and risky form of skill technical debt.

## Identifying and Resolving Gaps

In the formal Skill Contract, a gap exists when `V = ∅`. 

- **Impact**: Without validators, malformed artifacts or incorrect interfaces can silently propagate to downstream skills, causing cascading execution failures.
- **Resolution**: SkillOps detects gaps during library-time health diagnosis or task-time planning and uses the `add_validator` action to insert checks. High risk scores propagated via CGPD heavily prioritize bridging validation gaps.

## See Also

- [Skill Contracts](skill-contracts.md)
- [ContractGraph-Propagated Diagnosis (CGPD)](contractgraph-propagated-diagnosis.md)
- [Raw Source: SkillOps Paper](../../raw/skillops-paper.md)
