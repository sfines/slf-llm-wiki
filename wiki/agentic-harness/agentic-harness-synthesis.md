# Agentic Harness Engineering: Area Synthesis

## State of Current Thought
Harness engineering focuses on the middleware, observability, and lifecycle management of agents and their tools. Recent frameworks like SkillGen and SkillOps treat agent capabilities as software ecosystems requiring maintenance (e.g. managing "Skill Technical Debt"). Furthermore, the "Constraint State Governance" (CSG) paradigm argues that safety constraints must be maintained as explicit execution states to prevent "Constraint Drift" across long trajectories.

## Areas of Controversy / Ongoing Conversation
- **Proactive vs. Reactive Skill Maintenance:** Should agent skills be continuously evolved and patched at runtime (e.g., SkillWeaver), or strictly verified and gated at library-time to prevent regressions (e.g., SkillGen)?
- **Safety by Prompt vs. Safety by State:** The realization that output-checking and system prompts are insufficient has sparked debate over how deeply integrated CSG admission control algorithms must be within the LLM's execution loop.

## See Also
- [Agentic Harness Engineering](./agentic-harness-engineering.md)
- [Skillops Framework](./skillops-framework.md)
- [Constraint Drift](./constraint-drift.md)
