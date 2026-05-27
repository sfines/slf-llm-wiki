# Plan-Act Agent Architecture

The Plan-Act Agent Architecture is a common design pattern (closely related to ReAct) used to solve complex workflows. It operates in a two-stage loop:
1. **Plan:** A planner LLM reasons about the task, decomposes it, and generates a strategy or sequence of actions.
2. **Act:** An actor LLM executes the devised plan, interacting with external tools, APIs, or environments, and returning observations back to the planner.

## Challenges
While highly capable, Plan-Act architectures are computationally expensive because the planning stage often requires extensive reasoning through large language models. Optimizations like Agentic Plan Caching attempt to intercept the planning stage, reusing successful structural plans from previous analogous runs.

## References
- [Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents](../../raw/agentic-plan-caching.md)
