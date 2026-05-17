# Factual vs. Prose Transfer (Harness)

A key discovery of the [Agentic Harness Engineering (AHE)](agentic-harness-engineering.md) research is the distinction between the transferability of **Factual** vs. **Prose-based** harness components.

## Factual Components (High Transfer)
Factual components consist of structural logic, including:
- **Tool Logic:** The implementation of guardrails and middleware.
- **Memory Architectures:** The structure of hierarchical context or note-taking systems.
- **Experimental Finding:** These components evolved using GPT models provided significant Pass@1 gains (+5.1% to +10.1%) when used by alternate families like **Claude** or **Kimi**.

## Prose-Based Components (Low Transfer)
Prose components consist of natural language instructions, including:
- **Persona Definitions:** "You are a senior software engineer..."
- **Strategic Advice:** "Always check for existing tests before writing code."
- **Experimental Finding:** These tend to be "model-locked." What works as a prompt for one model family may be ignored or misinterpreted by another.

## Conclusion
AHE suggests that true "Engineering Experience" is encoded in the structural **Factual** harness rather than the **Prose** prompts.

## See Also
- [Agentic Harness Engineering (AHE)](agentic-harness-engineering.md)
- [Terminal-Bench 2](terminal-bench-2.md)
