# Confucius Hierarchical Working Memory

**Hierarchical Working Memory** is a core architectural feature of the [Confucius Code Agent (CCA)](confucius-code-agent.md) designed to handle long-context reasoning in massive codebases.

## The Problem: Context Saturation
In large-scale software engineering tasks, agents often encounter "context saturation," where the sheer volume of repository data, logs, and session history overwhelms the model's ability to focus on relevant information.

## The Hierarchical Solution
Instead of a flat context buffer, Confucius SDK implements a layered memory structure:
1.  **Top-Level Goals:** The global objective of the task.
2.  **Current Sub-Task Context:** Focused information relevant to the immediate step (e.g., current file being edited).
3.  **Compressed History:** Summaries of previous actions and findings.
4.  **Episodic Detail:** Granular logs of the most recent interactions.

## Benefits
- **Improved Focus:** The agent can prioritize the most relevant information for its current reasoning step.
- **Reduced Token Usage:** By dynamically loading and unloading context layers, the system remains efficient.
- **Better Long-Horizon Planning:** The hierarchical structure makes it easier for the agent to track progress toward long-term goals.

## See Also
- [Confucius Code Agent (CCA)](confucius-code-agent.md)
- [Persistent Note-Taking System](confucius-persistent-notes.md)
- [Agentic Context Engineering (ACE)](../agentic-harness/agentic-context-engineering.md)
