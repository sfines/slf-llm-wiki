# Rich Domain Models for Agents

A **Rich Domain Model** encapsulates business logic, rules, and invariants within the domain entities themselves, rather than delegating them to an external service or a "God Agent."

## Application in Agentic Design
In [Agentic DDD](agentic-ddd-overview.md), providing an agent with access to a rich domain model (often via [Semantic Tooling](probabilistic-consumers.md)) makes the agent more robust:
- **Constraint Enforcement:** The model itself prevents the agent from making actions that violate business rules.
- **Semantic Understanding:** The model provides a structured representation of the business domain that the agent can reason over using [Ubiquitous Language](ubiquitous-language-for-ai.md).
- **Reduced Hallucinations:** Because the business logic is "baked into" the model/tools, the agent doesn't have to "guess" the rules of the domain.

## Comparison to Anemic Models
- **Anemic Model:** Agents interact with raw data structures and must "know" the business rules to apply them correctly. (High risk of logic errors).
- **Rich Model:** Agents interact with [Entities and Aggregates](agentic-state-management.md) that expose meaningful business actions (e.g., `cancel_with_refund()`). (Low risk of logic errors).

## See Also
- [Agentic State Management](agentic-state-management.md)
- [Ubiquitous Language for AI](ubiquitous-language-for-ai.md)
