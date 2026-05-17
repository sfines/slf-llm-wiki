# Parametric Memory Realizations

**Parametric Memory** refers to knowledge that has been internalized into the weights of an LLM through training or fine-tuning processes.

## Characteristics
- **Massive Scale:** Can store vast amounts of world knowledge and domain facts.
- **Low Test-Time Latency:** Information retrieval doesn't require external tool calls or context tokens.
- **Update Difficulty:** Modifying the memory requires expensive retraining or fine-tuning.
- **Staleness:** Information is frozen at the time of the last training run.

## Role in Agentic Systems
While foundation models come with broad parametric memory, specialized agents often use **Parameter-Efficient Fine-Tuning (PEFT)** or **LoRA** to encode specific domain rules or [Ubiquitous Language](ubiquitous-language-for-ai.md) that should be "second nature" to the agent.

## See Also
- [Agent Memory](agent-memory.md)
- [Agent Factual Memory](agent-factual-memory.md)
- [Token-Level Memory Realizations](agent-token-level-memory.md)
- [Latent Memory Research](agent-latent-memory.md)
