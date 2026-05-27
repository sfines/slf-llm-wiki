# Constraint Decay in LLM Agents

Constraint decay is an empirical phenomenon in AI-driven software engineering where the performance of an LLM coding agent degrades substantially as non-functional structural constraints are added to a task.

## The Phenomenon

Current LLM agents excel at "shallow" code generation—producing functionally correct scripts or prototypes when given loose specifications and full architectural freedom. However, production-grade backends require adherence to strict rules, such as specific architectural patterns (e.g., Clean Architecture), prescribed database engines, and mandatory Object-Relational Mappers (ORMs). 

As these explicit structural requirements accumulate, the agent's ability to maintain functional compliance drops precipitously. Even highly capable frontier models experience massive losses in behavioral assertion pass rates when transitioning from unconstrained baseline generation to fully specified architectural constraints.

---
[Source](../../raw/constraint-decay-paper.md)