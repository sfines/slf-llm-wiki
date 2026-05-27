# Greenfield vs. Feature Implementation Evaluation

Evaluating coding agents requires distinguishing between building software from scratch and modifying existing, structured codebases.

## The Evaluation Paradigms

*   **Greenfield Generation:** The agent starts with an empty repository and must synthesize a complete system from a natural language prompt and an API spec. This tests the agent's ability to establish architecture and scaffold a new application.
*   **Feature Implementation:** The agent is given an existing codebase that already embeds a layered architecture, a database, and an ORM. The agent must read the code, infer the implicit conventions, and re-implement missing features without breaking the existing structure.

Testing agents across both paradigms reveals that structural challenges (like constraint decay) are not merely artifacts of scaffolding from scratch. Agents consistently struggle to infer and respect constraints even when operating within an already established, highly structured repository.

---
[Source](../../raw/constraint-decay-paper.md)