# APWA vs. Sequential Systems

A fundamental comparison provided in the [APWA research](../raw/apwa-paper.md) highlights the limitations of **Sequential Agentic Reasoning** and the advantages of the **Parallel Distributed** model.

## Sequential System Limitations
- **Latency (T = n * t):** Total time is the sum of all reasoning steps.
- **Reasoning Fatigue:** As the conversation grows longer, models tend to lose focus and hallucinate more.
- **Context Saturation:** The entire task history must fit into a single context window.
- **Propagating Errors:** A mistake in step 1 cascades throughout the entire chain.

## The APWA Parallel Advantage
- **Latency (T = max(t)):** Total time is limited only by the slowest independent sub-task.
- **Fresher Reasoning:** Each worker starts with a clean, focused context tailored to its specific subproblem.
- **Distributed Context:** Bypasses token limits by sharding the data and reasoning.
- **Error Isolation:** A failure in one subproblem does not prevent other branches from succeeding.

## When to Use Which?
- **Sequential:** Best for small, interdependent tasks where each step truly depends on the output of the previous one (e.g., a multi-turn dialogue).
- **APWA (Parallel):** Best for large-scale, decomposable tasks with high [parallelism potential](apwa-dynamic-decomposition.md) (e.g., massive data analysis or repo-wide coding tasks).

## See Also
- [APWA Architecture](apwa-architecture.md)
- [APWA Evaluation Results](apwa-evaluation-results.md)
- [Distributed Reasoning Primitives](distributed-reasoning-primitives.md)
