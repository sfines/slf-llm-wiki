# Bounded Context Identification (Automated)

**Automated Bounded Context Identification** is the third step of the [Automating DDD Framework](ddd-prompting-framework.md), aiming to define the high-level system decomposition.

## Mechanism
The model takes the events and commands from the [Event Storming Simulation](ddd-event-storming-simulation.md) and groups them based on:
- **Semantic Similarity:** Which events share common entities or processes.
- **Linguistic Boundaries:** Identifying where the same term might have different meanings.
- **Organizational Alignment:** Suggesting boundaries that mirror team structures.

## Utility
The research found this stage to be highly valuable for **Strategic Design**, helping architects visualize different ways to slice a complex problem.

## See Also
- [Bounded Contexts in MAS](../agentic-ddd/bounded-contexts-in-mas.md)
- [Automating DDD Framework](ddd-prompting-framework.md)
- [Context Mapping for Agents](../agentic-ddd/context-mapping-for-agents.md)
