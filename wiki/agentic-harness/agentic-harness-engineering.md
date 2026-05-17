# Agentic Harness Engineering (AHE)

Agentic Harness Engineering is a framework for the autonomous and observability-driven evolution of [Agent Harnesses](agent-harness.md).

## The Core Problem
In frontier coding agents, the "harness"—the infrastructure governing prompts, tools, middleware, and execution environments—is often a more significant determinant of performance than the underlying model family. However, engineering these harnesses manually is slow and error-prone due to:
- **Heterogeneous Action Spaces:** Different parts of the harness (prompts vs. tool logic) require different editing strategies.
- **Sparse Attribution:** Hard to know which specific harness change caused a success or failure in a long-horizon task.
- **Trajectory Volume:** Millions of tokens in agent logs are too dense for simple manual or automated analysis.

## The AHE Framework
AHE automates harness evolution by instrumenting the engineering loop with three observability pillars:

### 1. [Component Observability](ahe-component-observability.md)
Every editable component of the harness (e.g., [Shell-Tool Guardrails](ahe-shell-tool-guardrails.md), [Execution-Risk Middleware](ahe-execution-risk-middleware.md)) is given a file-level representation. This makes the action space explicit, allows for granular version control, and enables safe reverts.

### 2. [Experience Observability](ahe-experience-observability.md)
A distillation pipeline ([Agent Debugger](ahe-agent-debugger.md)) compresses millions of raw trajectory tokens into a "layered, drill-down evidence corpus."

### 3. [Decision Observability](ahe-decision-observability.md)
Every edit is paired with a [Self-Declared Prediction](self-declared-predictions.md) (a [Falsifiable Contract](falsifiable-contracts-in-ai.md)). These predictions are verified against the next round's task-level outcomes on benchmarks like [Terminal-Bench 2](terminal-bench-2.md).

## Key Outcomes and Insights
- **Performance Evolution:** Ten AHE iterations lifted the `pass@1` score on **Terminal-Bench 2** from 69.7% to 77.0%.
- **Cross-Family Transfer:** A major finding is the distinction between [Factual vs. Prose Transfer](factual-vs-prose-transfer.md). Factual components show strong transferability across model families.
- **Localization of Gains:** Gains are primarily concentrated in tool implementations and middleware rather than simple system prompt tweaks.
- **Efficiency:** On **SWE-bench-verified**, the evolved harness achieved top success rates while using **12% fewer tokens** than the initial seed.

## See Also
- [Agentic Domain-Driven Design](../agentic-ddd/agentic-ddd-overview.md)
- [Autonomous Agents](../core-concepts/autonomous-agents.md)
- [Agentic Context Engineering (ACE)](agentic-context-engineering.md)
- [Raw Source: Agentic Harness Engineering Paper](../../raw/agentic-harness-engineering-paper.md)

---
[🏠 Back to Home](../index.md)
