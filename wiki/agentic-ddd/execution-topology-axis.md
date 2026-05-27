# Execution Topology Axis

In the [Two-Dimensional AI Agent Framework](./two-dimensional-agent-framework.md), the **Execution Topology** axis represents *how* data flows and how control is structurally organized within an agent system.

The six structural archetypes are:
1. **Chain:** Linear sequential pipeline where the output of step *n* feeds step *n+1*.
2. **Route:** Conditional branching where a classifier dispatches to specialized handlers.
3. **Parallel:** Concurrent fan-out with aggregation, where independent subtasks run simultaneously.
4. **Orchestrate:** A central coordinator delegates to workers and synthesizes results.
5. **Loop:** Iterative refinement with explicit exit conditions.
6. **Hierarchy:** Nested multi-level delegation, where each level can use any other topology.

Topologies determine the latency, cost, and failure characteristics of a pattern. The choice of topology must be evaluated independently of the [Cognitive Function Axis](./cognitive-function-axis.md). For instance, reasoning can be implemented as a Chain, a Route, a Parallel exploration, or a Loop.

## References
- Huang, J., & Zhou, J. T. (2026). A Two-Dimensional Framework for AI Agent Design Patterns.


## Source
- [A Two-Dimensional Framework for AI Agent Design Patterns](../../raw/two-dimensional-ai-agent-patterns-paper.md)
