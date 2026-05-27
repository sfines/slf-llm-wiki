# Context Integration vs. Diversity

The design of LLM-based agent systems requires navigating a fundamental trade-off between the unified context of a single agent and the semantic diversity of multiple agents.

## The Trade-off

*   **Single-Agent Systems (Context Integration):** A single agent maximizes context integration by maintaining a continuous, unified memory stream. All reasoning steps share full access to the prior history, enabling effectively constant-time access to global context without loss of detail.
*   **Multi-Agent Systems (Diversity via Fragmentation):** Multiple parallel agents enable diverse exploration and specialized perspectives. However, this incurs unavoidable information fragmentation. The global context must be lossily compressed into inter-agent messages. This "coordination tax" increases synchronization overhead, cognitive load, and can lead to agents operating on divergent world states over extended interactions. 

Choosing the right architecture requires balancing the need for diverse problem-solving approaches against the penalty of fragmented context.

---
[Source](../../raw/scaling-agent-systems-paper.md)