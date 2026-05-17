# SWE-Bench-Pro Analysis

**SWE-Bench-Pro** is a benchmark for evaluating [Software Engineering Agents](autonomous-agents.md) on real-world, large-scale issues.

## Role in CCA Evaluation
The [Confucius Code Agent (CCA)](confucius-code-agent.md) used SWE-Bench-Pro to demonstrate its production readiness and scalability.

## Key Performance Metrics
- **Resolve@1:** CCA achieved a **54.3%** resolution rate.
- **Comparison:** This score outperformed prior research-grade agents and matched or exceeded several commercial-grade systems under controlled conditions (identical models and tools).

## Insights from Analysis
The CCA research found that high Resolve@1 scores were driven by:
- **Hierarchical Context:** Effective management of massive codebase data.
- **Refined Tool-Use:** The Meta-Agent's ability to optimize how the model interacts with complex toolchains.
- **Resilience:** The ability to recover from execution errors through the [AX/UX/DX design perspectives](confucius-sdk-perspectives.md).

## See Also
- [Confucius Code Agent (CCA)](confucius-code-agent.md)
- [Terminal-Bench 2](terminal-bench-2.md)
- [SWE-bench 500 Evaluation](swe-bench-500.md)
