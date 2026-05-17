# Agent Autonomy Boundaries

An **Autonomy Boundary** defines the explicit limit of an [AI Agent's](../core-concepts/autonomous-agents.md) power to make decisions and take actions without external approval.

## Relationship to Bounded Contexts
In [Agentic DDD](agentic-ddd-overview.md), the [Bounded Context](bounded-contexts-in-mas.md) provides the structural boundary, while the Autonomy Boundary provides the operational boundary:
- **Within the Boundary:** The agent is authorized to modify state and emit events (e.g., a Procurement Agent can place an order under $10,000).
- **Outside the Boundary:** The agent must seek "Human-in-the-loop" approval or coordinate with a higher-level [Coordinator Agent](../agyn/agyn-framework.md#agent-roles).

## Why Boundaries Matter
- **Safety:** Prevents agents from making catastrophic errors in production environments.
- **Predictability:** Developers can trust that agents will not deviate from their assigned domain logic.
- **Auditability:** Makes it clear which agent was responsible for a specific state change.

## See Also
- [Bounded Contexts in MAS](bounded-contexts-in-mas.md)
- [Agyn Framework](../agyn/agyn-framework.md)
- [Confucius SDK Perspectives (AX, UX, DX)](../confucius/confucius-sdk-perspectives.md)
