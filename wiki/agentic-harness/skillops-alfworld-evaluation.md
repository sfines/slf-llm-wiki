# SkillOps ALFWorld Evaluation

SkillOps was empirically evaluated using the ALFWorld text-based household manipulation benchmark, simulating an environment susceptible to skill technical debt by using a curated SkillsBench library augmented with synthetic degradations.

## Key Findings

- **Standalone Performance**: Achieved 79.5% task success, outperforming the strongest LLM-planner baseline by 8.8 percentage points.
- **Plug-in Effectiveness**: Successfully served as a drop-in library-cleaning layer, improving task-time retrieval agents (like Hybrid or BM25) by 0.68 to 2.90 percentage points without modifying their core logic.
- **Token Efficiency**: The rule-based maintenance implementation used nearly zero LLM calls at library time. The use of a pruned, maintained library was neutral-to-negative in task-time token consumption.
- **Scale Resilience**: Remained stable as the skill library scaled up to 2000 skills with 90% degradation noise.

## See Also

- [SkillOps Framework](skillops-framework.md)
- [Raw Source: SkillOps Paper](../../raw/skillops-paper.md)
