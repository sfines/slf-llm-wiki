# SCM Procurement Context

The **Procurement Context** is a specialized [Bounded Context](bounded-contexts-in-mas.md) within the [Supply Chain Case Study](agentic-ddd-case-study-supply-chain.md).

## Responsibilities
- **Supplier Management:** Tracking performance, reliability, and lead times.
- **Purchase Orders:** Automating the creation and negotiation of orders based on inventory needs.
- **Price Analysis:** Evaluating market conditions to optimize procurement costs.

## Specialized Agent: Procurement Agent
The Procurement Agent operates strictly within this context, using tools to:
- Search for alternative suppliers when a `ShipmentDelayed` event occurs.
- Negotiate contract terms within pre-defined business invariants.
- Emit `PurchaseOrderCreated` events to notify the [Inventory Context](scm-inventory-context.md).

## Semantic Contracts
The Procurement Context defines specific [Ubiquitous Language](ubiquitous-language-for-ai.md) terms such as `LeadTime`, `Quote`, and `VendorTier`.

## See Also
- [Agentic DDD Case Study: Supply Chain](agentic-ddd-case-study-supply-chain.md)
- [SCM Logistics Context](scm-logistics-context.md)
- [SCM Inventory Context](scm-inventory-context.md)
