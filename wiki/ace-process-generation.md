# ACE Process: Generation

**Generation** is the first stage of the [Agentic Context Engineering (ACE)](agentic-context-engineering.md) modular process.

## Role in Context Evolution
In the generation phase, the system proposes new instructions, strategies, or evidence to be added to the [Agent Context](agent-harness.md). 

## Mechanisms
- **Bootstrapping:** Creating initial "playbooks" from task descriptions and domain documentation.
- **Candidate Proposals:** Using LLMs to suggest improvements to existing strategies based on identified performance gaps.
- **Diversity of Thought:** Generating multiple alternative approaches to a single problem to explore the strategy space.

## Addressing Brevity Bias
By separating generation from immediate application, ACE can produce detailed, domain-specific insights that might otherwise be lost if the model were simply trying to summarize its history under a strict token limit.

## See Also
- [Agentic Context Engineering (ACE)](agentic-context-engineering.md)
- [ACE Process: Reflection](ace-process-reflection.md)
- [ACE Process: Curation](ace-process-curation.md)
