# Vibe Coding Oversight

Vibe coding refers to the paradigm where users describe high-level software requirements in natural language and the AI autonomously handles the implementation. While this lowers the barrier for non-experts, it introduces a significant "supervision gap". The model becomes a strong executor, but the human is relegated to a weak supervisory role, unable to properly specify intent or verify the complex outputs.

To safely enable vibe coding, oversight mechanisms like scalable interactive oversight decompose the user's vague "vibes" into structured, closed-form questions. This interaction decodes vague intents into precise specifications (like a Product Requirement Document) before the AI generates the code, preventing costly misaligned trajectories in long-horizon generation.

---
**Source:** [Steering LLMs via Scalable Interactive Oversight](../../raw/interactive-oversight-paper.md)