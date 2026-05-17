# Automating Domain-Driven Design: Experience with a Prompting Framework

**Authors:** Tobias Eisenreich, Husein Jusic, Stefan Wagner
**Date:** March 2026
**Source:** arXiv:2603.26244

## Summary
While not describing "Agentic DDD" as an architectural pattern for MAS, this paper explores the use of agents to **perform** the activities of traditional [Domain-Driven Design (DDD)](domain-driven-design.md).

## The Five-Step Framework
The authors propose a sequential prompting framework for automating DDD:
1. **Establishing Ubiquitous Language:** Generating glossaries and terminologies.
2. **Simulating Event Storming:** Identifying events and commands from requirements.
3. **Identifying Bounded Contexts:** Grouping events and defining boundaries.
4. **Designing Aggregates:** Identifying entities and value objects within contexts.
5. **Mapping to Technical Architecture:** Proposing code structures or API designs.

## Technical Validation
The prompting framework was validated against real-world requirements from **FTAPI's enterprise platform**. The study found that:
- **Steps 1-3 (Ubiquitous Language, Event Storming, Bounded Contexts):** Consistently generated valuable and usable artifacts, acting as an effective "collaborative sparring partner" for human experts.
- **Steps 4-5 (Aggregate Design, Technical Mapping):** Suffered from **error propagation**, where minor inaccuracies from earlier stages accumulated, rendering the final technical outputs impractical for direct implementation.

## Key Insights
- **AI as an Enhancer:** LLMs can enhance but not replace human architectural expertise. They are best used to reduce the effort and overhead of documentation while human experts focus on critical trade-offs.
- **Context Collapse:** The research highlights the risk of "context collapse" in long architectural sequences, where details are lost as the process moves from high-level discovery to low-level design.

## Relevance to Agentic DDD
This work shows how LLMs can be used to *bootstrap* the very structures (Bounded Contexts, Ubiquitous Language) that [Agentic DDD](agentic-ddd-overview.md) uses to build autonomous systems.

## Reference
Eisenreich, T., Jusic, H., & Wagner, S. (2026). Automating Domain-Driven Design: Experience with a Prompting Framework. arXiv preprint arXiv:2603.26244.
