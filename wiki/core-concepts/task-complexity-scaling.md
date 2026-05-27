# Task Complexity Scaling

Task Complexity Scaling refers to the principle that an LLM's effective context window cannot be understood independently of the task's structural complexity. As prompt length scales, the cognitive load and processing cost scale at different rates depending on the problem type.

## Complexity Classes in Long-Context Tasks
1. **Constant Scaling (Needle-in-a-Haystack):** The model must find a single piece of information. The complexity remains relatively constant regardless of how much background noise (context length) is added. Frontier models generally handle these well up to their maximum context limit.
2. **Linear Scaling:** The task requires examining and semantically transforming nearly every chunk of the input (e.g., aggregation tasks). Performance degrades rapidly as the context grows.
3. **Quadratic Scaling:** The task requires aggregating and comparing pairs of chunks across the entire dataset. [Context Rot](./context-rot.md) is extremely severe here, and traditional models fail catastrophically even at shorter lengths.

[Recursive Language Models](./recursive-language-models.md) counteract steep complexity scaling by leveraging [Recursive Task Decomposition](./recursive-task-decomposition.md), allowing the system to isolate sub-problems rather than forcing a single LLM forward-pass to evaluate the entire context structure at once.

## Related Concepts
- [Context Rot](./context-rot.md)
- [Inference-Time Scaling](./inference-time-scaling.md)


## Source
- [Recursive Language Models](../../raw/recursive-language-models-paper.md)
