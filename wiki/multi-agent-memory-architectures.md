# Multi-Agent Memory Architectures

**Multi-Agent Memory** focuses on how teams of [Autonomous Agents](autonomous-agents.md) share knowledge and learn from collective experience.

## Patterns of Sharing
- **Shared Blackboard:** A central, read-write memory space accessible to all agents in a team (e.g., [Agyn's](agyn-framework.md) shared state).
- **Peer-to-Peer Exchange:** Agents explicitly send "knowledge packets" to each other during task hand-offs.
- **Hierarchical Memory:** A coordinator agent maintains the "global" memory while individual specialists maintain "local" working memory.

## Benefits
- **Collective Intelligence:** The team can solve problems that no single agent has enough context for.
- **Consistent Worldview:** [Context Mapping](context-mapping-for-agents.md) ensures all agents use the same facts and [Ubiquitous Language](ubiquitous-language-for-ai.md).

## See Also
- [Agent Memory](agent-memory.md)
- [Multi-Agent Systems (MAS)](multi-agent-systems.md)
- [Structured Agent Communication](structured-agent-communication.md)
