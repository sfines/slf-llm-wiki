# Confucius Code Agent (CCA)

The Confucius Code Agent is a software engineering agent designed for production-level scalability, operate on massive repositories, and sustain long-horizon sessions.

## Overview
CCA is built on top of the **Confucius SDK**, an agent development platform that prioritizes three complementary perspectives: Agent Experience (AX), User Experience (UX), and Developer Experience (DX).

## Core Architecture
- **[Unified Agent Orchestrator](unified-agent-orchestrator.md):** Manages long-context reasoning and complex tool coordination across massive codebases.
- **[Hierarchical Working Memory](confucius-hierarchical-memory.md):** Supports long-context reasoning while implementing [Context Saturation Mitigation](context-saturation-mitigation.md).
- **[Persistent Note-Taking System](confucius-persistent-notes.md):** Enables cross-session [Continual Learning](continual-learning.md) by allowing agents to save and retrieve domain-specific insights.

## Meta-Agent Loop
A key feature of CCA is its **[Meta-Agent Refinement Loop](confucius-meta-agent-loop.md)**, which automates the synthesis, evaluation, and refinement of agent configurations.

## Performance and Results
- **[SWE-Bench-Pro Analysis](swe-bench-pro.md):** CCA reached a **Resolve@1 of 54.3%**, outperforming prior research baselines.
- **Production Readiness:** The system is designed to balance **extensibility** (DX), **interpretability** (UX), and **controllability** (UX), avoiding the "black box" nature of many production systems.
- **Efficiency:** The hierarchical memory and persistent note-taking significantly reduce token overhead in long-horizon sessions.

## See Also
- [Agentic Harness Engineering (AHE)](agentic-harness-engineering.md)
- [Agent Harness](agent-harness.md)
- [Multi-Agent Systems (MAS)](multi-agent-systems.md)
- [Raw Source: Confucius Code Agent Paper](../raw/confucius-code-agent-paper.md)
