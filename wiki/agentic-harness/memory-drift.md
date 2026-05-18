# Memory Drift

Memory drift is a specific mode of constraint drift where a safety constraint is omitted, distorted, or retrieved imprecisely as it passes through an agent's memory mechanisms.

## Context Summarization and Loss

In LLM-based multi-agent systems, agents frequently summarize their context or rely on vector memory for long-term state. When an explicit constraint (e.g., "do not delete files outside the `auth` directory") is continually summarized, it can easily degrade into a weaker, ambiguous directive (e.g., "clean up irrelevant files"). 

## Impact on Trajectory Safety

When memory drift occurs, the agent acts on a flawed recollection of its boundaries. Because the agent believes it is still following the rules, local self-evaluations or output checks might not detect the failure until after irreversible actions (like deleting a critical test file) have already occurred.

## See Also
- [Constraint Drift](constraint-drift.md)
- [Information-Flow Drift](information-flow-drift.md)
- [Raw Source: Constraint Drift Paper](../../raw/constraint-drift-paper.md)
