# Domain Events as Agent Triggers

In [Agentic DDD](agentic-ddd-overview.md), **Domain Events** are the primary mechanism for decoupling agents and enabling asynchronous coordination.

## Definition
A Domain Event represents something that happened in the business domain (e.g., `OrderPlaced`, `ShipmentDelayed`, `PaymentProcessed`). 

## Role in Multi-Agent Systems
Unlike traditional request-response architectures where an orchestrator tells an agent what to do, an event-driven MAS uses events to trigger autonomous reasoning:
- **Autonomy:** Agents "subscribe" to events they are interested in and react independently.
- **Reactivity:** The system state evolves through a chain of events and reactions.
- **Payload Context:** Each event carries a data payload that provides the agent with the necessary [Working Memory](../agent-memory/agent-working-memory.md) for its task.

## Example: Procurement Reactive Loop
1.  **Event:** `InventoryLevelLow` is emitted by the [Inventory Agent](scm-inventory-context.md).
2.  **Trigger:** The [Procurement Agent](scm-procurement-context.md) consumes the event.
3.  **Reasoning:** The Procurement Agent analyzes supplier lead times and prices.
4.  **Action:** The agent issues a `PurchaseOrderCreated` event.

## See Also
- [Event Storming for Agents](event-storming-for-agents.md)
- [Multi-Agent System Scalability](multi-agent-system-scalability.md)
