# Developer Experience (DX) in Agents

**Developer Experience (DX)** in the [Confucius SDK](confucius-code-agent.md) focuses on the ease with which human engineers can build, extend, and maintain the agent system.

## Core Principles
- **Extensibility:** Making it simple to add new tools, data sources (via [MCP](../core-concepts/mcp.md)), or reasoning modules.
- **Reproducibility:** Ensuring that agent behaviors can be tested and reproduced in CI/CD pipelines.
- **Modularity:** Using a "plug-and-play" architecture for harness components.

## Mechanisms in Confucius
- **Modular Extension System:** Standardized interfaces for tool integration.
- **[Meta-Agent Refinement Loop](confucius-meta-agent-loop.md):** Automating the tedious parts of agent configuration.
- **Comprehensive SDK:** Providing pre-built components for common agentic tasks (e.g., file searching, git operations).

## See Also
- [Confucius SDK Perspectives](confucius-sdk-perspectives.md)
- [Agent Experience (AX) Design](confucius-ax-design.md)
- [User Experience (UX) for Autonomy](confucius-ux-design.md)
