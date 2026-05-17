# Agyn Framework

The **Agyn Framework** is an open-source platform designed for configuring and deploying teams of autonomous agents to solve complex software engineering tasks.

## Core Philosophy
Agyn moves away from monolithic or simple pipeline-based agent designs, instead modeling software engineering as an **organizational process**. It replicates the structure of a human engineering team, emphasizing:
- **Role Separation:** Specialized agents for specific functions.
- **Shared Methodology:** A defined process that all agents follow.
- **Structured Communication:** Clear protocols for how agents interact.

## Agent Roles
In an Agyn team, agents are typically assigned to specialized roles:
- **[Coordinator](agyn-role-coordinator.md):** Manages the overall organizational process and task assignment.
- **[Researcher](agyn-role-researcher.md):** Conducts deep analysis of the codebase and technical requirements.
- **[Implementer](agyn-role-implementer.md):** Responsible for code changes and Pull Request (PR) creation within isolated sandboxes.
- **[Reviewer](agyn-role-reviewer.md):** Performs iterative reviews of the implementation to ensure quality and correctness.

## Key Capabilities and Results
- **Autonomous Methodology:** The system follows a [Collaborative Issue Resolution](collaborative-issue-resolution.md) flow: Analysis → Task Specification → Implementation → Iterative Review.
- **Post-hoc Performance:** When evaluated on **[SWE-bench 500](swe-bench-500.md)**, Agyn resolved **72.2%** of tasks.
- **Organizational Paradigm:** A central finding is that [Organizational Process Modeling](organizational-process-modeling.md) is as critical as model capability.
- **[Isolated Experimentation](agyn-sandbox-environments.md):** Agents operate in secure, isolated sandboxes.
- **[Structured Communication](structured-agent-communication.md):** Enables agents to collaborate following shared methodologies.

## See Also
- [Team-Based Autonomous Software Engineering](team-based-software-engineering.md)
- [Organizational Design for Agents](organizational-design-for-agents.md)
- [Multi-Agent Systems (MAS)](../core-concepts/multi-agent-systems.md)
- [Raw Source: Agyn Paper](../../raw/agyn-paper.md)

---
[🏠 Back to Home](../index.md)
