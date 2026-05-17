# SWE-bench 500 Evaluation

**SWE-bench 500** is a specific split of the SWE-bench benchmark used to evaluate [Autonomous Software Engineering Agents](../core-concepts/autonomous-agents.md).

## Agyn's Performance
In the [Agyn research](agyn-framework.md), the system was evaluated post-hoc on SWE-bench 500:
- **Result:** Agyn resolved **72.2%** of tasks.
- **Significance:** This score significantly outperformed single-agent baselines using comparable language models.
- **Design Insight:** Most importantly, the system was designed for **real production use** and was not specifically tuned for the benchmark, suggesting high generalizability.

## Comparison to Baselines
The evaluation demonstrated that modeling software engineering as an **organizational process** (roles, review, methodology) yields superior results compared to treating it as a simple "prompt-to-code" pipeline.

## See Also
- [Agyn Framework](agyn-framework.md)
- [Team-Based Autonomous Software Engineering](team-based-software-engineering.md)
- [SWE-Bench-Pro Analysis](../confucius/swe-bench-pro.md)
