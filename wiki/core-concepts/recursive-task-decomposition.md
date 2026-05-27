# Recursive Task Decomposition

Recursive Task Decomposition is an inference strategy where an LLM breaks a large, complex problem into smaller sub-tasks and delegates those sub-tasks to instances of itself (sub-LLMs).

When applied to long-context reasoning—as seen in [Recursive Language Models](./recursive-language-models.md)—the root LLM uses an external environment (see [Prompt as Environment](./prompt-as-environment.md)) to partition a massive document. It then dynamically generates code to invoke smaller, recursive LLM calls over those specific document partitions.

## Mechanisms in Action
1. **Filtering:** Using code execution (like regex) to filter the search space based on model priors before invoking a sub-LLM.
2. **Chunking and Sub-calling:** Dividing a massive text uniformly or semantically, and running parallel sub-LLM queries to extract answers from each chunk.
3. **Stitching:** Using the REPL environment to pass the outputs of the recursive sub-calls into variables, combining them iteratively to form the final response.

This dynamic decomposition is vital for handling tasks with high [Task Complexity Scaling](./task-complexity-scaling.md), effectively sidestepping the degradation caused by [Context Rot](./context-rot.md).

## Related Concepts
- [Recursive Language Models](./recursive-language-models.md)
- [Inference-Time Scaling](./inference-time-scaling.md)
- [Multi-Agent Systems](./multi-agent-systems.md)


## Source
- [Recursive Language Models](../../raw/recursive-language-models-paper.md)
