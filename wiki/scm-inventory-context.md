# SCM Inventory Context

The **Inventory Context** is a specialized [Bounded Context](bounded-contexts-in-mas.md) within the [Supply Chain Case Study](agentic-ddd-case-study-supply-chain.md).

## Responsibilities
- **Stock Management:** Monitoring real-time inventory levels across multiple warehouses.
- **Order Fulfillment:** Reserving stock for incoming orders and managing picking/packing events.
- **Reorder Logic:** Identifying when stock falls below safety thresholds.

## Specialized Agent: Inventory Agent
The Inventory Agent maintains the [Aggregate Root](agentic-state-management.md) for warehouse stock. Its actions include:
- Emitting `LowStockAlert` events to trigger the [Procurement Context](scm-procurement-context.md).
- Reserving stock in response to `OrderPlaced` events.
- Optimizing warehouse layout based on fulfillment velocity.

## See Also
- [Agentic DDD Case Study: Supply Chain](agentic-ddd-case-study-supply-chain.md)
- [SCM Procurement Context](scm-procurement-context.md)
- [SCM Logistics Context](scm-logistics-context.md)
