# SPARC (Pre-Tool Validation)

SPARC is a pre-execution validation middleware designed to prevent agents from executing harmful, malformed, or hallucinated tool calls. Operating at the pre-tool lifecycle stage, it acts as an inline runtime mechanism to decide if a candidate tool call should be allowed to execute.

## Validation Mechanisms

SPARC performs three distinct types of validation:
1.  **Syntactic Validation:** Rule-based checks to catch non-existent tools, unknown arguments, missing required parameters, type mismatches, and JSON-schema violations.
2.  **Semantic Validation:** Uses an LLM judge to assess function-selection appropriateness, parameter grounding, hallucinated values, value-format alignment, and unmet prerequisites based on the agent's context.
3.  **Transformation Validation:** Handles format or unit mismatches (e.g., date or currency formats) and automatically converts them to match the tool specifications.

When an invalid tool call is detected, SPARC intercepts it and returns a reflection artifact (issue type, evidence, and correction suggestion) back to the agent, allowing the agent to self-correct and retry without wasting API quotas or corrupting external state.

---
[Source](../../raw/altk-paper.md)