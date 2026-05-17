# Distributed Reasoning Primitives

**Distributed Reasoning Primitives** are the foundational building blocks used by the [APWA framework](apwa-overview.md) to manage its parallel workflows.

## Core Primitives
1.  **Decompose:** Splitting a monolithic intent into independent specifications.
2.  **Broadcast:** Sending the same data or instructions to a pool of diverse expert agents.
3.  **Map:** Applying a reasoning loop to each element of a data shard.
4.  **Reduce:** Synthesizing the diverse or parallel outputs into a unified conclusion.
5.  **Audit:** Verifying the correctness of independent sub-task results before aggregation.

## Shifting the AI Development Paradigm
By formalizing these primitives, APWA encourages developers to think of AI agents as **distributed compute units** rather than just "chatbots." This allows for the application of traditional distributed systems theory (load balancing, fault tolerance, replication) to LLM applications.

## See Also
- [APWA Architecture](apwa-architecture.md)
- [APWA Dynamic Decomposition](apwa-dynamic-decomposition.md)
- [Agentic State Management](../agentic-ddd/agentic-state-management.md)
