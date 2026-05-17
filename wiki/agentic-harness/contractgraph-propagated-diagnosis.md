# ContractGraph-Propagated Diagnosis (CGPD)

ContractGraph-Propagated Diagnosis (CGPD) is an advanced graph-aware diagnosis mechanism in SkillOps that propagates risk scores along dependency edges to proactively identify downstream vulnerabilities.

## Mechanism

While standard diagnosis assesses skills independently, CGPD uses a contraction mapping to pass risk from upstream skills to downstream dependencies. 

- **Update Rule**: `R(t+1)(s) = (1 - α)Rloc(s) + α * max(R(t)(s'))` (where `s'` are upstream parents).
- **Preemptive Maintenance**: A structurally sound skill can be flagged for validator insertion simply because it inherits high risk from upstream. By using the worst-upstream-risk rule, it ensures safety across interconnected multi-step plans.

## See Also

- [Skill Library Health Diagnosis](skill-library-health-diagnosis.md)
- [Hierarchical Skill Ecosystem Graph (HSEG)](hierarchical-skill-ecosystem-graph.md)
- [Raw Source: SkillOps Paper](../../raw/skillops-paper.md)
