# Recursive Language Models (RLMs)

Recursive Language Models (RLMs) represent a paradigm shift in how large language models handle context. Instead of feeding long prompts directly into the neural network (e.g., a Transformer), an RLM treats the prompt as an object in an external environment. 

By loading the prompt into a Read-Eval-Print Loop (REPL) as a programmable variable, RLMs allow the root LLM to:
1. Examine the length and structure of the prompt.
2. Programmatically decompose the prompt into manageable snippets.
3. Recursively call itself (or a sub-LLM) over these specific snippets.

This effectively bypasses the model's physical context window limitation, allowing it to handle inputs up to two orders of magnitude larger. This technique relies heavily on [Inference-Time Scaling](./inference-time-scaling.md) and [Prompt as Environment](./prompt-as-environment.md) strategies to mitigate [Context Rot](./context-rot.md) during complex tasks.

## Key Benefits
- Dramatically increases effective context length (handling 10M+ tokens).
- Outperforms context condensation/compaction by enabling dense access to arbitrary parts of the prompt.
- Retains comparable or cheaper costs per query by selectively reading context via code rather than processing the entire text unconditionally.

## Related Concepts
- [Recursive Task Decomposition](./recursive-task-decomposition.md)
- [Prompt as Environment](./prompt-as-environment.md)
- [Context Rot](./context-rot.md)
- [Inference-Time Scaling](./inference-time-scaling.md)


## Source
- [Recursive Language Models](../../raw/recursive-language-models-paper.md)
