# Event Storming for AI Agents

**Event Storming** is a collaborative discovery technique used in [Agentic DDD](agentic-ddd-overview.md) to model the behavior and interactions of [Multi-Agent Systems (MAS)](multi-agent-systems.md).

## From Business Events to Agent Triggers
In a traditional Event Storming session, participants identify **Domain Events** (things that happened). In the context of AI agents, these events are transformed into:
- **Triggers:** Events that cause an agent to start a reasoning loop.
- **Inputs:** The data payload of the event provides the context for the agent.
- **Outputs:** An agent's action often results in a new Domain Event being emitted.

## The Storming Process for Agents
1. **Unbounded Exploration:** Identify all possible events in the business process.
2. **Timeline Alignment:** Organize events chronologically.
3. **Agent Identification:** Group events that share a common "expert" (the potential agent).
4. **Boundary Definition:** Draw [Bounded Contexts](bounded-contexts-in-mas.md) around these groups.
5. **Interaction Mapping:** Identify how events flow between different agents.

## Benefits
- **Semantic Clarity:** Ensures agents are triggered by business-meaningful events rather than technical state changes.
- **Modular Design:** Natural discovery of specialized agent roles.
- **Proactive Behavior:** Agents can "listen" for events and react autonomously, moving beyond simple request-response patterns.

## See Also
- [Agentic Domain-Driven Design Overview](agentic-ddd-overview.md)
- [Multi-Agent System Scalability](multi-agent-system-scalability.md)
