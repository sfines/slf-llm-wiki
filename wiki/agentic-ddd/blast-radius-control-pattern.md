# Blast Radius Control Pattern

The **Blast Radius Control** pattern sits at the intersection of Governance (Cognitive Function) and Hierarchy (Execution Topology) in the [Two-Dimensional AI Agent Framework](./two-dimensional-agent-framework.md).

## Mechanism
When an agent acts on the real world, unexpected tool interactions or cascading failures can cause catastrophic damage. Blast Radius Control uses nested containment hierarchies to limit maximum damage. Each hierarchical level strictly constrains the child level (e.g., process sandbox -> filesystem isolation -> network restrictions -> API rate limits -> budget caps). 

The outermost layer represents the organizational risk boundary, guaranteeing that even runaway autonomous execution is bounded.

## Trade-offs
Tighter containment limits risk but severely restricts agent capabilities. Governance architects must find the minimum viable containment—the tightest sandbox that still permits the agent to accomplish its intended tasks.

## References
- Huang, J., & Zhou, J. T. (2026). A Two-Dimensional Framework for AI Agent Design Patterns.


## Source
- [A Two-Dimensional Framework for AI Agent Design Patterns](../../raw/two-dimensional-ai-agent-patterns-paper.md)
