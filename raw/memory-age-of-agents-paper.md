# Memory in the Age of AI Agents

**Authors:** Yuyang Hu, Shichun Liu, Yanwei Yue, et al.
**Date:** December 2025
**Source:** arXiv:2512.13564
**DOI:** 10.48550/arXiv.2512.13564

## Abstract Summary
This survey provides a comprehensive landscape of agent memory research, clarifying terminologies and proposing a unified taxonomy based on **Forms**, **Functions**, and **Dynamics**. It distinguishes agent memory from related concepts like RAG and context engineering, positioning memory as a "first-class primitive" in the design of agentic intelligence.

## Unified Taxonomy

### 1. Forms (Realizations)
- **Token-Level Memory:** Stored in the context window. It is highly accessible but limited by the model's context window capacity.
- **Parametric Memory:** Knowledge encoded in model weights via fine-tuning. It is highly scalable but computationally expensive to update and suffers from the "staleness" problem.
- **Latent Memory:** Stored in the model's internal activations or hidden states. This is an emerging area aiming for efficient, dynamic state management without large-scale retraining.

### 2. Functions (Usage)
- **[Working Memory](agent-working-memory.md):** Transient information relevant to the immediate task (e.g., current reasoning trace).
- **[Factual Memory](agent-factual-memory.md):** Long-term storage of declarative knowledge (e.g., repository structure, API documentation).
- **[Experiential Memory](agent-experiential-memory.md):** Storage of past trajectories, including successful plans and failure post-mortems, enabling [Continual Learning](continual-learning.md).

### 3. Dynamics (Lifecycle)
- **Formation:** The process of filtering and encoding raw experiences into memory.
- **Evolution:** How memories are updated, refined, or pruned to manage relevance and context.
- **Retrieval:** The mechanisms (vector, graph, or heuristic) used to access relevant information at test time.

## Key Research Frontiers
- **Memory Automation:** Self-managed memory systems.
- **Multi-Agent Memory:** Shared or collaborative memory structures.
- **Trustworthiness:** Managing hallucinations and stale information in memory.

## Reference
Hu, Y., et al. (2025). Memory in the Age of AI Agents. arXiv preprint arXiv:2512.13564.
