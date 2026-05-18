# Agent Event Memory Perception

Agent Event Memory Perception is the cognitive module responsible for capturing, encoding, and retrieving an agent's historical interactions to ensure coherent behavior over extended simulation timelines. 

## Dual-Bank Memory Storage
To prevent decision-making from becoming isolated, single-period rational choices, the event memory module is segmented into two distinct banks:
- **Short-Term Memory**: Retains contextual information and immediate feedback for ongoing or recent activities.
- **Long-Term Memory**: Stores vector representations of high-level event summaries. These capture enduring economic patterns and major life events.

## Processing and Representation
Events are logged with specific timestamps and distilled into concise summaries. This perception mechanism allows agents to apply heuristic rules based on past successes or revise their rules of thumb after experiencing failures. When an agent needs to make a decision, an event extractor retrieves relevant memories from both banks, combining them with the agent's current persona to generate a deeply contextualized, historically aware response.

## See Also
- [LLM Instruction Tuning for Event Summarization](llm-instruction-tuning-for-event-summarization.md)
- [Agent Memory Weighting](agent-memory-weighting.md)
- [Dynamic Persona Evolution](dynamic-persona-evolution.md)
- [Raw Source: EconAI Paper](../../raw/econai-paper.md)