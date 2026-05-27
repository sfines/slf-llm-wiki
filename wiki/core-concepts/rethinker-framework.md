# ReThinker Framework

ReThinker is a confidence-aware agentic framework designed to orchestrate tool use, retrieval, and multi-agent reasoning for expert-level scientific tasks. Instead of a rigid pipeline, it dynamically allocates computational resources using a stage-wise Solver-Critic-Selector architecture guided by model confidence.

## Core Mechanisms
- **Solver Stage:** Explores the problem space using tool-enhanced iterative reasoning.
- **Critic Stage:** Applies guided reflection over the reasoning trajectory to correct high-order logical and knowledge gaps.
- **Selector Stage:** Aggregates and stabilizes candidate answers through confidence-guided (perplexity-based) multi-round adjudication, addressing verification noise and ordering bias.

## References
- [ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control](../../raw/rethinker.md)
