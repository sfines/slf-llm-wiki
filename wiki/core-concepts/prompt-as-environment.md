# Prompt as Environment

"Prompt as Environment" is a design paradigm where a long input prompt is not directly tokenized and fed into the neural network's forward pass. Instead, it is loaded as an object or variable within an external programming environment, such as a Python Read-Eval-Print Loop (REPL).

This concept is the foundational insight behind [Recursive Language Models (RLMs)](./recursive-language-models.md). By treating the prompt as external data, the LLM acts as an agent operating over the text. It writes code to:
- Probe the document (e.g., using regex or search functions).
- Measure its length and structure.
- Extract small, relevant snippets to process directly.

## Advantages
- **Unlimited Theoretical Context:** The size of the document is bound by the environment's memory (RAM), not the model's transformer context window.
- **Selective Attention:** The model only reads the tokens it explicitly queries, significantly reducing API costs and mitigating [Context Rot](./context-rot.md).
- **Execution Feedback:** The model can iteratively refine its extraction strategy based on the execution feedback from the REPL.

## Related Concepts
- [Recursive Language Models](./recursive-language-models.md)
- [Autonomous Agents](./autonomous-agents.md)


## Source
- [Recursive Language Models](../../raw/recursive-language-models-paper.md)
