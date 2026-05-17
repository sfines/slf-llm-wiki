# ACE Natural Execution Feedback

**Natural Execution Feedback** is the primary source of truth for self-improvement in the [Agentic Context Engineering (ACE)](agentic-context-engineering.md) framework.

## Definition
Unlike human-labeled datasets, natural feedback comes directly from the agent's environment:
- **Test Results:** Success or failure of unit/integration tests.
- **Compiler/Linter Errors:** Specific technical feedback on code correctness.
- **Task Outcomes:** Whether the final goal (e.g., resolving a bug report) was achieved.

## Role in the Reflection Process
In the [ACE Reflection stage](ace-process-reflection.md), the "reflection agent" analyzes this natural feedback to:
1.  Verify if a proposed strategy actually improved performance.
2.  Attribute failures to specific gaps in the current [Dynamic Cheatsheet](ace-dynamic-cheatsheets.md).
3.  Filter out "hallucinated improvements" that don't work in practice.

## Benefits
- **Zero Supervision:** Enables agents to learn and improve without expensive human labeling.
- **Environment Grounding:** Ensures that the agent's "playbook" is rooted in the actual behavior of the codebase.

## See Also
- [Agentic Context Engineering (ACE)](agentic-context-engineering.md)
- [ACE Process: Reflection](ace-process-reflection.md)
- [Agent Experiential Memory](agent-experiential-memory.md)
