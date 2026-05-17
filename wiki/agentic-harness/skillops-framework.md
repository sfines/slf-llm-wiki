# SkillOps Framework

SkillOps is a method-agnostic plug-in framework for managing large language model agent skill libraries as self-maintaining software ecosystems. It addresses the problem of skill technical debt by providing a library-management layer that runs before downstream agents use the library.

## Core Concepts

SkillOps is built on several key mechanisms:
- **Skill Contracts**: Represents each skill via a typed contract containing Preconditions, Operations, Artifacts, Validators, and Failure Modes.
- **HSEG**: Organizes skills into a Hierarchical Skill Ecosystem Graph, featuring both internal contract nodes and external relationship edges (dependency, compatibility, redundancy, alternative).
- **Dual-Loop Architecture**: Operates through two interacting loops: the Task-Time Skill Loop for executable planning and the Library-Time Skill Loop for health diagnosis and persistent skill-library updates.
- **Plug-in Interface**: Provides a `run_maintenance(raw_lib)` interface that cleans a library without requiring changes to downstream retrieval or planning agents.

## See Also

- [Skill Technical Debt](skill-technical-debt.md)
- [Hierarchical Skill Ecosystem Graph (HSEG)](hierarchical-skill-ecosystem-graph.md)
- [Raw Source: SkillOps Paper](../../raw/skillops-paper.md)
