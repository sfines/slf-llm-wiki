# Agentic Context Engineering (ACE)

Agentic Context Engineering is a framework that treats [Agent Contexts](agent-harness.md) as evolving playbooks that accumulate and refine strategies through a modular process of generation, reflection, and curation.

## Key Insights
- **Scalable Self-Improvement:** ACE enables agents to improve autonomously with low overhead by leveraging **[Natural Execution Feedback](ace-execution-feedback.md)**.
- **Structure over Brevity:** A major finding is that detailed, structured contexts are far more effective than concise, lossy summaries, addressing the **[Brevity Bias](ace-brevity-bias.md)** inherent in LLMs.
- **Self-Improving Memory:** Building on the concept of **[Dynamic Cheatsheets](ace-dynamic-cheatsheets.md)**, ACE maintains an evolving, high-signal **[Adaptive Memory](ace-adaptive-memory.md)** of successful strategies.
- **[Context Collapse Prevention](ace-context-collapse.md):** ACE uses structured, incremental updates to ensure that detailed domain knowledge is preserved over time.

## Modular Process
ACE evolves contexts through a three-stage modular process (supporting **[Modular Context Refinement](ace-modular-refinement.md)**):
1.  **[Generation](ace-process-generation.md):** Proposing new instructions and strategies.
2.  **[Reflection](ace-process-reflection.md):** Analyzing performance against execution feedback.
3.  **[Curation](ace-process-curation.md):** Selecting and organizing the most effective content.

## Performance and Benchmarks
ACE has demonstrated significant performance improvements across multiple domains:
- **Agent Benchmarks:** Achieved gains of **+10.6%** in overall performance.
- **Finance Tasks:** Improved accuracy by **+8.6%**.
- **[AppWorld Leaderboard](appworld-evaluation.md):** ACE matched the top-ranked production-level agent and surpassed it on the harder "test-challenge" split.
- **Optimization Strategy:** ACE utilizes both **[Offline and Online Optimization](ace-optimization-modes.md)** to maintain strategy relevance.

## Relationship to AHE
While **ACE** focuses primarily on the evolution of the *context* (instructions and strategies), **[Agentic Harness Engineering (AHE)](agentic-harness-engineering.md)** takes a broader view by evolving the entire *harness*, including tool implementations and middleware.

## Reference
- [Agentic Context Engineering Paper](../../raw/ace-paper.md)
