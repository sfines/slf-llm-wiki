# Context Collapse Prevention

**Context Collapse** is a phenomenon in LLM self-improvement loops where critical details and domain expertise are "eroded away" through iterative rewriting or summarization.

## The Problem
As an agent attempts to refine its own instructions, it often tends toward more generic, high-level advice, losing the granular technical rules that were present in the initial seed prompt.

## ACE Mitigation Strategies
The [Agentic Context Engineering (ACE)](agentic-context-engineering.md) framework prevents collapse through:
1.  **Modular Refinement:** Only updating specific sections of the context rather than rewriting the entire prompt.
2.  **Structured Curation:** Using a [Reflection Process](ace-process-reflection.md) to explicitly verify that a change doesn't discard useful information.
3.  **Hierarchical Organization:** Maintaining a clear structure in the [Dynamic Cheatsheet](ace-dynamic-cheatsheets.md) so that specific technical rules are isolated from general strategies.

## Benefits
- **Persistent Expertise:** Long-term preservation of complex domain logic.
- **Stable Performance:** Preventing the "regression to the mean" that occurs in unstructured evolution loops.

## See Also
- [Agentic Context Engineering (ACE)](agentic-context-engineering.md)
- [ACE Process: Reflection](ace-process-reflection.md)
- [Brevity Bias in LLMs](ace-brevity-bias.md)
