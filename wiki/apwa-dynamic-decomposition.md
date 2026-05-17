# APWA Dynamic Decomposition

**Dynamic Decomposition** is the core functional module in the [APWA Architecture](apwa-architecture.md) that enables the parallel processing of complex agentic tasks.

## The Role of the Decomposer
In APWA, the "Decomposer" is a specialized agent whose sole responsibility is to transform a single, complex user intent into a set of [Non-Interfering Subproblems](apwa-non-interfering-subproblems.md). 

## Decomposition Logic
The Decomposer follows a three-step reasoning process:
1.  **Intent Analysis:** Breaking down the query to identify its components (e.g., "Analyze the legal and financial risks of X").
2.  **Independence Identification:** Determining which components are truly independent (e.g., the legal analysis does not depend on the financial analysis).
3.  **Worker Instruction Synthesis:** Generating specific, self-contained instructions for the [Parallel Workers](apwa-architecture.md#worker-layer).

## Adapting to Query Complexity
Unlike static pipelines, APWA's decomposition is dynamic. For a simple query, it might skip decomposition entirely. For a massive document retrieval task, it might generate hundreds of independent search sub-tasks.

## Benefits
- **Token Efficiency:** Each worker only receives the context needed for its specific subproblem, avoiding the "noise" of the full query.
- **Speed:** Enables the system to start processing all components of a query simultaneously.
- **Reliability:** A failure in one subproblem does not necessarily collapse the entire reasoning chain.

## See Also
- [Non-Interfering Subproblems](apwa-non-interfering-subproblems.md)
- [APWA Architecture](apwa-architecture.md)
- [Agentic Context Engineering (ACE)](agentic-context-engineering.md)
