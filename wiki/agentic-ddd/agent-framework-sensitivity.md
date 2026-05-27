# Agent Framework Sensitivity

Framework sensitivity describes how an LLM agent's success rate in generating code is heavily influenced by the specific web framework targeted, even when the underlying functional API contract remains identical.

## Explicit vs. Convention-Heavy Frameworks

Agents exhibit significant performance disparities based on framework design paradigms:
*   **Lightweight, Explicit Frameworks:** Agents perform best in minimal, explicit frameworks (like Flask or Express). These frameworks have a direct API surface without implicit magic, making it easier for agents to explicitly define routing and logic step-by-step.
*   **Convention-Heavy Frameworks:** Agents struggle severely in frameworks that rely on implicit configurations, "magic" auto-discovery, or convention-over-configuration paradigms (such as Django or FastAPI). The hidden abstractions and implicit typings in these environments are harder for agents to successfully navigate and satisfy without violating structural constraints.

---
[Source](../../raw/constraint-decay-paper.md)