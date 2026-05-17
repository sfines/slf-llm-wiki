# Strategic Mapping Protocols for Agents

**Strategic Mapping Protocols** define the formalized rules for interaction between [Bounded Contexts](bounded-contexts-in-mas.md) in a [Multi-Agent System](multi-agent-systems.md).

## Beyond Simple Connectivity
While technical protocols (like HTTP or gRPC) handle data transport, Strategic Mapping Protocols handle **semantic transport**:
- **ACL (Anticorruption Layer) Protocol:** Rules for how an agent translates foreign domain models into its own internal Ubiquitous Language.
- **Shared Kernel Protocol:** Agreements on which specific [Aggregates](agentic-state-management.md) or tools are shared between two agents.
- **Customer-Supplier Protocol:** How a "downstream" agent can request changes or updates from an "upstream" agent.

## Implementation via MCP
The [Model Context Protocol (MCP)](mcp.md) serves as a modern realization of these protocols, providing a standardized way to define the capabilities and constraints of these mappings.

## See Also
- [Context Mapping for Agents](context-mapping-for-agents.md)
- [Ubiquitous Language for AI](ubiquitous-language-for-ai.md)
- [Model Context Protocol (MCP)](mcp.md)
