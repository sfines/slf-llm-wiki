# Constraint State Governance

Constraint State Governance (CSG) is a design paradigm for LLM-based multi-agent systems where safety-critical constraints are treated as explicit, executable, and verifiable execution state rather than mere conversational prompts.

## State Tokens and Hashes

In CSG, constraints are not natural language instructions that an agent must "remember." Instead, rules are converted into signed tokens containing an identity, version, scope, executable predicate, and audit trail. The system maintains an active digest of all constraints, roles, budgets, and taints. 

## Pre-Action Admission

Under CSG, any critical action proposed by an agent must pass through an admission control layer. The action is evaluated against the signed constraint state to verify freshness, capability scope, information flow, and audit evidence. If the action violates the active state, it is blocked, preventing constraint drift from materializing in the environment.

## Proportional Control

CSG aims for proportional control, governing critical transitions (e.g., file edits, external API calls) heavily while allowing light-weight local reasoning to remain unencumbered. It explicitly bounds agent behavior within safe trajectories.

## See Also
- [Constraint Drift](constraint-drift.md)
- [CSG Admission Control Algorithm](csg-admission-control-algorithm.md)
- [Constraint Native Reinforcement Learning](constraint-native-reinforcement-learning.md)
- [Raw Source: Constraint Drift Paper](../../raw/constraint-drift-paper.md)
