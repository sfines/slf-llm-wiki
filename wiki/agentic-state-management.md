# Agentic State Management

State management in [Agentic DDD](agentic-ddd-overview.md) relies on the patterns of [Entities and Aggregates](domain-driven-design.md) to ensure consistency and business integrity.

## Entities and Aggregates as Guardrails
- **Entities:** Objects with a unique identity that agents track and modify over time (e.g., a "Customer" or "Order").
- **Aggregates:** Clusters of related entities and value objects treated as a single unit for data changes. The **Aggregate Root** is the only gatekeeper for changes.

## Agents as Gatekeepers
In Agentic DDD, an agent often acts as the "manager" of an Aggregate. It is responsible for:
- **Validation:** Ensuring that any requested change complies with business rules.
- **Consistency:** Guaranteeing that the state of the aggregate remains valid after an action.
- **Persistence:** Interacting with databases or external APIs to save the state.

## Memory and State
- **Short-Term Memory (Context):** The agent's immediate reasoning context (prompt history).
- **Long-Term State (Database):** The persistent, shared state of the domain entities.
- **Test-Time Memory:** Specialized caching or memory mechanisms (like [Agentic Plan Caching](agentic-plan-caching.md)) that help agents remember successful strategies across different tasks.

## See Also
- [Agentic Domain-Driven Design Overview](agentic-ddd-overview.md)
- [Bounded Contexts in MAS](bounded-contexts-in-mas.md)
