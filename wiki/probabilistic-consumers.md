# Probabilistic Consumers and Agent-Ready Interfaces

One of the unique challenges addressed by [Agentic DDD](agentic-ddd-overview.md) is the design of interfaces for **Probabilistic Consumers** (AI Agents).

## The Deterministic vs. Probabilistic Gap
- **Traditional Clients (Code):** Expect deterministic inputs, outputs, and error codes. They follow a pre-defined execution path.
- **Agentic Clients (AI):** Are probabilistic. They may interpret tool descriptions differently, attempt unusual combinations of actions, and fail in unpredictable ways.

## Designing Agent-Ready Interfaces
To support agents, interfaces must move beyond simple REST/GraphQL patterns and become "Agent-Ready":

### 1. Semantic Tooling
Tools must have high-quality, domain-aligned descriptions (using [Ubiquitous Language](ubiquitous-language-for-ai.md)). The agent needs to understand the "why" and "when" of using a tool, not just the "how".

### 2. Intent-Based APIs
Instead of granular CRUD operations, provide APIs that encapsulate business intent (e.g., `resolve_payment_dispute` instead of `update_transaction_status`).

### 3. Rich Feedback Loops
When an action fails, the interface should provide more than just a 400 error. It should provide "Reasoning-Enabling Feedback" that helps the agent correct its course (e.g., "The payment could not be processed because the credit limit is exceeded; consider suggesting an alternative payment method").

### 4. Guardrails and Invariants
Interfaces must explicitly enforce business invariants to prevent agents from making logical errors that bypass the LLM's own reasoning limits.

## See Also
- [Ubiquitous Language for AI](ubiquitous-language-for-ai.md)
- [Agentic Domain-Driven Design Overview](agentic-ddd-overview.md)
