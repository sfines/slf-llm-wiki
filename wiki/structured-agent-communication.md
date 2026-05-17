# Structured Multi-Agent Communication

**Structured Communication** refers to the formalized protocols and channels through which agents in a [Multi-Agent System (MAS)](multi-agent-systems.md) exchange information.

## Principles in Agyn
The [Agyn Framework](agyn-framework.md) moves away from "free-form" chat between agents, instead using:
- **Typed Messages:** Defining the schema of data being passed (e.g., a "Research Report" or "Review Feedback").
- **State Hand-offs:** Clear protocols for when one agent (e.g., [Researcher](agyn-role-researcher.md)) finishes and the next (e.g., [Implementer](agyn-role-implementer.md)) begins.
- **Knowledge Sharing:** A shared [Working Memory](agent-working-memory.md) or blackboard where agents can post findings for others to consume.

## Benefits
- **Reduced Hallucinations:** Structure prevents models from "drifting" into off-topic or irrelevant chatter.
- **Scalability:** Makes it easier to add more agents to the team without increasing noise.
- **Auditability:** Humans can easily trace the flow of information through the system.

## See Also
- [Agyn Framework](agyn-framework.md)
- [Organizational Design for Agents](organizational-design-for-agents.md)
- [Context Mapping for Agents](context-mapping-for-agents.md)
