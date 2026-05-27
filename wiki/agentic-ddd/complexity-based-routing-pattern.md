# Complexity-Based Routing Pattern

**Complexity-Based Routing** is an AI agent architecture pattern at the intersection of Reasoning (Cognitive Function) and Route (Execution Topology) in the [Two-Dimensional AI Agent Framework](./two-dimensional-agent-framework.md).

## Mechanism
Rather than applying expensive, deep reasoning (like 64K token Chain-of-Thought) to every query, a lightweight classifier evaluates incoming queries and routes them to an appropriate reasoning depth:
- **System 1:** Fast, direct response for simple queries.
- **System 2:** Moderate reasoning (standard Chain-of-Thought).
- **Extended Deliberation:** Deep exploration for highly complex tasks.

This mirrors Kahneman's dual-process theory and significantly optimizes token cost and latency.

## Trade-offs
The classifier's accuracy is the bottleneck. Misrouting a complex query to System 1 causes errors, while misrouting simple queries to deep deliberation wastes compute and money.

## References
- Huang, J., & Zhou, J. T. (2026). A Two-Dimensional Framework for AI Agent Design Patterns.


## Source
- [A Two-Dimensional Framework for AI Agent Design Patterns](../../raw/two-dimensional-ai-agent-patterns-paper.md)
