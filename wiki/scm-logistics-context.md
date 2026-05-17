# SCM Logistics Context

The **Logistics Context** is a specialized [Bounded Context](bounded-contexts-in-mas.md) within the [Supply Chain Case Study](agentic-ddd-case-study-supply-chain.md).

## Responsibilities
- **Shipment Tracking:** Monitoring the real-time status of goods in transit.
- **Route Optimization:** Dynamic adjustment of transportation paths based on external events (weather, traffic).
- **Carrier Management:** Selecting and communicating with logistics providers.

## Specialized Agent: Logistics Agent
The Logistics Agent listens for external telemetry events and reacts by:
- Emitting `ShipmentDelayed` events when a delay is detected.
- Re-routing shipments to minimize impact on [Inventory Context](scm-inventory-context.md).
- Providing real-time ETA updates to the [Demand Planning Context](scm-demand-planning-context.md).

## See Also
- [Agentic DDD Case Study: Supply Chain](agentic-ddd-case-study-supply-chain.md)
- [SCM Procurement Context](scm-procurement-context.md)
- [SCM Inventory Context](scm-inventory-context.md)
