# Skill Library Health Diagnosis

SkillOps continuously evaluates the health of the skill library during its Library-Time Loop. It calculates scores across five specific dimensions to identify and quantify skill technical debt.

## Five-Dimensional Diagnosis

- **Utility (U)**: The fraction of recent task calls that successfully utilized a skill. Detects low-value skills.
- **Redundancy (R)**: The normalized size of the largest redundancy cluster containing the skill. Detects clones.
- **Compatibility (C)**: The fraction of dependency edges incident to the skill that are also compatibility edges. Detects interface mismatches.
- **Failure-Risk (F)**: The empirical failure rate of the skill. Detects runtime-broken skills.
- **Validation-Gap (G)**: A binary indicator of whether a skill lacks a validator.

## See Also

- [ContractGraph-Propagated Diagnosis (CGPD)](contractgraph-propagated-diagnosis.md)
- [Library-Time Skill Loop](library-time-skill-loop.md)
- [Raw Source: SkillOps Paper](../../raw/skillops-paper.md)
