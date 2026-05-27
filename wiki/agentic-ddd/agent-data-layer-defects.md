# Agent Data-Layer Defects

In the context of constrained backend code generation, data-layer defects are the leading root cause of logic failures in LLM agents. 

## Primary Failure Modes

When an agent is forced to adhere to strict database and ORM constraints, the vast majority of its failures occur within the data layer. These defects generally fall into two categories:
1.  **Incorrect Query Composition:** The agent generates SQL queries that execute but return the wrong results due to incorrect joins, filters, or dialect-incompatible operators.
2.  **ORM Runtime Violations:** The underlying query logic is conceptually correct, but the agent misuses the ORM's API, leading to runtime crashes.

These data-layer defects demonstrate that properly interfacing with databases—whether through raw SQL or specific ORMs—is a fundamental bottleneck for autonomous coding agents building production-grade software.

---
[Source](../../raw/constraint-decay-paper.md)