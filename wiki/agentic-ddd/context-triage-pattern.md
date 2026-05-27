# Context Triage Pattern

The **Context Triage** pattern is a design pattern situated at the intersection of Context Engineering (Cognitive Function) and Route (Execution Topology) within the [Two-Dimensional AI Agent Framework](./two-dimensional-agent-framework.md).

## Problem & Solution
Agents often have access to far more information (conversation history, retrieved knowledge, environmental metadata) than can fit or be efficiently processed in a context window.

Context Triage applies emergency-room logic to information selection. A routing function classifies every potential information source by priority (e.g., P0: always load, P1: load if relevant, P2: load on demand, P3: never load) and dispatches them accordingly. 

## Trade-offs
Higher triage accuracy reduces context noise but increases routing latency. Over-aggressive filtering starves the agent of critical information, while under-filtering dilutes the attention quality of the LLM.

## References
- Huang, J., & Zhou, J. T. (2026). A Two-Dimensional Framework for AI Agent Design Patterns.


## Source
- [A Two-Dimensional Framework for AI Agent Design Patterns](../../raw/two-dimensional-ai-agent-patterns-paper.md)
