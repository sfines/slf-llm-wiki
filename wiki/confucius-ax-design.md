# Agent Experience (AX) Design

**Agent Experience (AX)** is a design perspective in the [Confucius SDK](confucius-code-agent.md) focused on the internal efficiency and reasoning accuracy of the AI model.

## Core Principles
AX design treats the agent as a "user" of its own harness, aiming to:
- **Minimize Cognitive Load:** Providing tools and prompts that are easy for the model to understand and use correctly.
- **Maximize Signal-to-Noise:** Ensuring that [Working Memory](agent-working-memory.md) contains high-relevance information and minimal distraction.
- **Provide Reasoning Guardrails:** Structuring prompts to encourage logical step-throughs (e.g., CoT).

## Mechanisms in Confucius
- **[Hierarchical Working Memory](confucius-hierarchical-memory.md):** Preventing context saturation to keep the model focused.
- **Semantic Tooling:** Using clear, unambiguous descriptions in tool definitions.
- **Trajectory Distillation:** Feeding condensed, high-signal history back to the model.

## See Also
- [Confucius SDK Perspectives](confucius-sdk-perspectives.md)
- [User Experience (UX) for Autonomy](confucius-ux-design.md)
- [Developer Experience (DX) in Agents](confucius-dx-design.md)
