# Brevity Bias in LLMs

**Brevity Bias** is a tendency in Large Language Models to favor concise, summarized outputs over detailed, technically rich descriptions.

## Impact on Agent Contexts
In self-evolving agent systems, brevity bias can be detrimental:
- **Loss of Nuance:** When an agent summarizes its own "lessons learned," it often discards the specific environmental qualifiers needed for successful execution.
- **Documentation Erosion:** Detailed API rules or codebase facts are replaced with generic "be efficient" prompts.

## Addressing Bias in ACE
The [Agentic Context Engineering (ACE)](agentic-context-engineering.md) framework explicitly counteracts this bias by:
- **Prioritizing Detail:** The [Generation Process](ace-process-generation.md) is prompted to provide "dense, actionable strategies" rather than summaries.
- **Empirical Validation:** Using [Natural Execution Feedback](ace-execution-feedback.md) to prove that longer, more detailed contexts lead to higher success rates.

## See Also
- [Agentic Context Engineering (ACE)](agentic-context-engineering.md)
- [Context Collapse Prevention](ace-context-collapse.md)
- [ACE Process: Generation](ace-process-generation.md)
