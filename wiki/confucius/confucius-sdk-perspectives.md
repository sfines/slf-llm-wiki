# Confucius SDK Perspectives (AX, UX, DX)

The Confucius SDK, which powers the [Confucius Code Agent](confucius-code-agent.md), is structured around three core perspectives to balance performance, usability, and extensibility.

## 1. [Agent Experience (AX)](confucius-ax-design.md)
AX focuses on the agent's internal reasoning and performance. 
- **Goal:** Minimize cognitive load and maximize reasoning accuracy.
- **Mechanisms:** [Hierarchical Working Memory](confucius-hierarchical-memory.md), optimized prompts, and clear tool definitions.

## 2. [User Experience (UX)](confucius-ux-design.md)
UX focuses on the human interaction with the agent.
- **Goal:** Provide controllability, transparency, and trust.
- **Mechanisms:** Observability into agent trajectories, "human-in-the-loop" approval points, and clear communication of intent.

## 3. [Developer Experience (DX)](confucius-dx-design.md)
DX focuses on the ease of extending and maintaining the agent system.
- **Goal:** Enable rapid development and reliable tool integration.
- **Mechanisms:** Modular extension system, standardized protocols (like [MCP](../core-concepts/mcp.md)), and the [Meta-Agent refinement loop](confucius-meta-agent-loop.md).

## See Also
- [Confucius Code Agent (CCA)](confucius-code-agent.md)
- [Agent Harness](../agentic-harness/agent-harness.md)
