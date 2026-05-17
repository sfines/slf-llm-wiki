# Context Mapping for Agents

**Context Mapping** in [Agentic DDD](agentic-ddd-overview.md) defines the relationships and communication patterns between different [Bounded Contexts](bounded-contexts-in-mas.md) and their associated agents.

## Why Mapping Matters
In a [Multi-Agent System (MAS)](../core-concepts/multi-agent-systems.md), the "spaghetti interaction" problem arises when agents talk to each other without structure. Context Mapping provides the "diplomatic protocols" for these interactions.

## Common Agent Interaction Patterns
- **Upstream/Downstream:** One agent provides data or services that another consumes.
- **Customer/Supplier:** A formalized version of upstream/downstream where the downstream agent's needs influence the upstream agent's output.
- **Anticorruption Layer (ACL):** A specialized agent (or tool) that translates between the Ubiquitous Language of two different contexts.
- **Shared Kernel:** A shared set of tools or data models used by two agents to coordinate closely.
- **Published Language:** A standardized format (often using [MCP - Model Context Protocol](../core-concepts/mcp.md)) that allows agents to interoperate regardless of their internal models.

## The "Agent-Ready" Interface
Context Mapping leads to the design of "Agent-Ready" interfaces:
- **Intent-Centric:** Interfaces that allow agents to express "what" they want to achieve.
- **Constraint-Aware:** Interfaces that explicitly communicate the rules and limits of an action.
- **Probabilistic Support:** Handling the inherent uncertainty of agentic reasoning through validation and feedback loops.

## See Also
- [Bounded Contexts in MAS](bounded-contexts-in-mas.md)
- [Multi-Agent System Scalability](multi-agent-system-scalability.md)
