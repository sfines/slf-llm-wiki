# Agent Memory

**Agent Memory** is a core capability of foundation model-based agents, enabling them to store, retrieve, and evolve information across time and tasks. 

## Taxonomy of Memory Functions
Based on the survey "[Memory in the Age of AI Agents](../../raw/memory-age-of-agents-paper.md)", agent memory is categorized by its functional role:

### 1. [Working Memory](agent-working-memory.md)
Short-term information required for the immediate reasoning step. Typically realized through **[Token-Level Realizations](agent-token-level-memory.md)**.

### 2. [Experiential Memory](agent-experiential-memory.md)
Storage of past agent trajectories. Critical for [Continual Learning](../core-concepts/continual-learning.md) and self-improvement.

### 3. [Factual Memory](agent-factual-memory.md)
Long-term storage of declarative knowledge. Often implemented using [RAG](../advanced-retrieval/rag.md) or **[Parametric Realizations](agent-parametric-memory.md)**.

## Memory Realizations (Forms)
- **[Token-Level](agent-token-level-memory.md):** Managed within the prompt/context.
- **[Parametric](agent-parametric-memory.md):** Encoded in model weights.
- **[Latent](agent-latent-memory.md):** Managed through internal activations (research frontier).

## Memory Dynamics (Lifecycle)
- **[Formation](agent-memory-formation.md):** Encoding information into storage.
- **[Evolution](agent-memory-evolution.md):** Updating or pruning memories.
- **[Retrieval](agent-memory-retrieval.md):** Accessing stored information.

## Emerging Research
- **[Memory Automation](agent-memory-automation.md):** Self-managed memory systems.
- **[Multi-Agent Memory](multi-agent-memory-architectures.md):** Shared knowledge structures for teams.

## See Also
- [Agentic State Management](../agentic-ddd/agentic-state-management.md)
- [Continual Learning](../core-concepts/continual-learning.md)
- [Confucius Persistent Note-Taking](../confucius/confucius-persistent-notes.md)

---
[🏠 Back to Home](../index.md)
