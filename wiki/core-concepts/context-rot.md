# Context Rot

Context Rot is a phenomenon observed in Large Language Models (LLMs) where the model's reasoning quality and recall accuracy degrade significantly as the input context length increases. 

Even if a model physically supports a massive context window (e.g., 1M+ tokens), its effective ability to utilize that information reliably drops off. This degradation is tied heavily to [Task Complexity Scaling](./task-complexity-scaling.md); complex tasks requiring synthesis of multiple pieces of information suffer from context rot at much shorter lengths than simple needle-in-a-haystack tasks.

## Mitigation Strategies
Traditional approaches try to mitigate context rot through context compaction or condensation (summarizing chunks as the window fills up). However, these lossy approaches fail when tasks require dense access to the original text.

Modern inference paradigms like [Recursive Language Models (RLMs)](./recursive-language-models.md) bypass context rot by isolating the full text in an external environment (see [Prompt as Environment](./prompt-as-environment.md)) and only loading relevant subsets of the text into the LLM's active context window via programmatic sub-calls.

## Related Concepts
- [Task Complexity Scaling](./task-complexity-scaling.md)
- [Recursive Language Models](./recursive-language-models.md)


## Source
- [Recursive Language Models](../../raw/recursive-language-models-paper.md)
