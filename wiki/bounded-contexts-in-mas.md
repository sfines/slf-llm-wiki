# Bounded Contexts in Multi-Agent Systems

In [Agentic Domain-Driven Design](agentic-ddd-overview.md), **Bounded Contexts** serve as the foundational boundaries for [AI Agents](autonomous-agents.md).

## The Role of Boundaries
Traditional software engineering uses Bounded Contexts to isolate models and logic. In Multi-Agent Systems, these boundaries define:
- **Expertise:** What the agent "knows" and can reason about.
- **Autonomy:** What decisions the agent is authorized to make.
- **Data Isolation:** Which data sets the agent has access to.

## Preventing Agent Monoliths
A common failure pattern in AI development is the "God Agent"—a single agent tasked with too many disparate responsibilities. Agentic DDD solves this by:
1. Decomposing the problem into sub-domains.
2. Assigning each sub-domain to a specialized agent.
3. Enforcing the boundary through strictly defined [Semantic Contracts](ubiquitous-language-for-ai.md).

## Implementation Patterns
- **Agent-per-Context:** Each Bounded Context is served by one or more agents.
- **Context-Aware Tools:** Tools provided to an agent are scoped strictly to its Bounded Context.
- **Shared Kernels:** Minimal shared logic between agents, used only when necessary for cross-context coordination.

## See Also
- [Context Mapping for Agents](context-mapping-for-agents.md)
- [Agentic Domain-Driven Design Overview](agentic-ddd-overview.md)
