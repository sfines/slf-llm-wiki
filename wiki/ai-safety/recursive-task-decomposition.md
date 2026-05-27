# Recursive Task Decomposition

Recursive Task Decomposition is a strategy for scalable oversight where a complex, long-horizon task is broken down into a tree-structured plan of localized subtasks. 

Instead of asking a user to evaluate an entire generated system or provide a massive upfront prompt, the AI interacts with the user at the leaf nodes of the decomposition tree. The user provides localized, low-burden feedback, which is then recursively aggregated into a cumulative preference state. This structured decomposition simplifies supervision, relieves users from managing large global scopes, and inherently scales to arbitrarily complex tasks.

---
**Source:** [Steering LLMs via Scalable Interactive Oversight](../../raw/interactive-oversight-paper.md)