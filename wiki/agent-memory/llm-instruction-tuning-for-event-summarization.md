# LLM Instruction Tuning for Event Summarization

LLM Instruction Tuning for Event Summarization is a technique used to improve an agent's ability to encode memories by moving beyond the standard zero-shot capabilities of foundational models. 

## The Need for Tuning
In complex economic simulations, agents generate vast amounts of experiential data. Relying on an untuned LLM to summarize these events often results in inconsistent or poorly formatted memories, degrading the agent's long-term planning capabilities.

## Structured Summarization
To resolve this, the memory summarization module is fine-tuned using specific instructions and structured formats. A high-quality event summary typically requires:
1. A clear introduction to the task background.
2. The specific economic activities or interactions that occurred.
3. Explicit summarization instructions dictating how the data should be compressed.

By instruction-tuning the LLM on this strict format, the system generates highly reliable, concise, and objective memory representations that can be efficiently stored in vector banks and retrieved during future decision-making cycles.

## See Also
- [Agent Event Memory Perception](agent-event-memory-perception.md)
- [Dynamic Persona Evolution](dynamic-persona-evolution.md)
- [Raw Source: EconAI Paper](../../raw/econai-paper.md)