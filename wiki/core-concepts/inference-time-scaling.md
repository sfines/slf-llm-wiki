# Inference-Time Scaling

Inference-Time Scaling refers to techniques that increase computational effort during the model's inference phase (i.e., at generation time) to solve complex or long-horizon problems, rather than relying solely on larger pre-trained models.

In the context of processing long documents, inference-time scaling allows a system with a small but fast "main memory" (the model's physical context window) to process far larger datasets by cleverly managing how data is fetched and manipulated. This is akin to out-of-core algorithms in traditional data processing.

[Recursive Language Models (RLMs)](./recursive-language-models.md) are a primary example of inference-time scaling applied to long-context reasoning. Rather than training a model with a 10M token context, the model uses an iterative REPL environment (see [Prompt as Environment](./prompt-as-environment.md)) and [Recursive Task Decomposition](./recursive-task-decomposition.md) to spend more inference compute evaluating sub-sections of a large document.

## Related Concepts
- [Recursive Language Models](./recursive-language-models.md)
- [Task Complexity Scaling](./task-complexity-scaling.md)


## Source
- [Recursive Language Models](../../raw/recursive-language-models-paper.md)
