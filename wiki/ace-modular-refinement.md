# Modular Context Refinement

**Modular Context Refinement** is an implementation pattern in [Agentic Context Engineering (ACE)](agentic-context-engineering.md) where the [Agent Context](agent-harness.md) is broken into independent, editable blocks.

## Design
Instead of a single monolithic prompt, the context is structured as:
- **Persona Module:** The agent's identity and tone.
- **Tool Instruction Modules:** Specific rules for each available tool.
- **Strategy Modules:** High-level problem-solving approaches (the [Dynamic Cheatsheet](ace-dynamic-cheatsheets.md)).
- **Domain Modules:** Facts and rules about the specific codebase.

## Benefits
- **Granular Updates:** The system can update the "Git tool instructions" without risking the "Reasoning Persona."
- **Collision Avoidance:** Multiple [Reflection agents](ace-process-reflection.md) can work on different modules simultaneously.
- **[Context Collapse Prevention](ace-context-collapse.md):** Isolation prevents changes in one area from eroding technical detail in another.

## See Also
- [Agentic Context Engineering (ACE)](agentic-context-engineering.md)
- [Component Observability](ahe-component-observability.md)
- [Agent Harness](agent-harness.md)
