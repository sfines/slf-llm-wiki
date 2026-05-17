# Non-Interfering Subproblems

A **Non-Interfering Subproblem** is a unit of work in the [APWA framework](apwa-overview.md) that can be executed independently of all other units within the same workflow.

## Definition of Independence
In the context of [Agent-Parallel Workloads](apwa-parallel-execution-patterns.md), two subproblems are non-interfering if:
- **No Shared State:** Neither subproblem requires the intermediate output of the other to proceed.
- **Atomic Operations:** Each can be completed by a single reasoning loop or a fixed set of tool calls.
- **Self-Contained Context:** The data required to solve the subproblem is fully identifiable during the [Decomposition phase](apwa-dynamic-decomposition.md).

## Identifying Independence
The APWA Decomposer uses several strategies to identify these units:
- **Temporal Splitting:** Dividing a long-term analysis by time periods (e.g., "Analyze Q1," "Analyze Q2").
- **Categorical Splitting:** Dividing a task by domains (e.g., "Legal," "Technical," "Financial").
- **Data Sharding:** Splitting a large dataset into smaller chunks for parallel review.

## The APWA Guarantee
The primary innovation of APWA is its focus on **Independence Guarantees**. By strictly enforcing non-interference, the architecture avoids the coordination overhead that limits the scalability of traditional [Multi-Agent Systems](../core-concepts/multi-agent-systems.md).

## See Also
- [APWA Dynamic Decomposition](apwa-dynamic-decomposition.md)
- [Agentic State Management](../agentic-ddd/agentic-state-management.md)
- [Context Saturation Mitigation](../confucius/context-saturation-mitigation.md)
