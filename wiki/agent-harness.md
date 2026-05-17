# Agent Harness

In the context of [Autonomous Agents](autonomous-agents.md), a **Harness** (or Scaffolding) is the infrastructure layer that mediates between the LLM and the external world.

## Components of a Harness
A typical harness includes:
- **System Prompts:** The core instructions and persona definitions.
- **Tool Definitions:** API schemas and descriptions for the model to use (e.g., [MCP](mcp.md)).
- **Middleware:** Logic for handling retries, error correction, and output parsing.
- **Execution Environment:** The sandboxed space (e.g., E2B, Docker) where the agent's actions are performed.
- **Observation Logic:** How the output of tools is captured and presented back to the model.

## Evolution of the Harness
Traditionally, harnesses are designed manually by engineers. Newer frameworks like [Agentic Harness Engineering (AHE)](agentic-harness-engineering.md) use "evolving agents" to automatically optimize these components based on execution feedback.

## See Also
- [Agentic Harness Engineering (AHE)](agentic-harness-engineering.md)
- [Agentic Context Engineering (ACE)](agentic-context-engineering.md)
- [Model Context Protocol (MCP)](mcp.md)
