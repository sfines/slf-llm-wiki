# Token-Level Memory Realizations

**Token-Level Memory** is the most common form of memory in foundation model-based [Autonomous Agents](../core-concepts/autonomous-agents.md), relying on the model's self-attention mechanism over a sequence of tokens.

## Characteristics
- **Real-Time Accessibility:** Information is immediately available within the reasoning loop.
- **Capacity Constraints:** Strictly limited by the model's context window (e.g., 128k or 1M tokens).
- **High Cost:** Processing large token sequences increases latency and API costs.

## Implementation Patterns
- **Chat History:** Storing the raw sequence of interactions.
- **[Hierarchical Working Memory](../confucius/confucius-hierarchical-memory.md):** Organizing tokens into logical layers to maximize relevance.
- **Active Summarization:** Periodically compressing the token sequence to fit within limits.
- **Scratchpads:** Reserving a portion of the context for intermediate reasoning.

## See Also
- [Agent Memory](agent-memory.md)
- [Agent Working Memory](agent-working-memory.md)
- [Parametric Memory Realizations](agent-parametric-memory.md)
