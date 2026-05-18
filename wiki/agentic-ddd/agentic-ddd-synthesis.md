# Agentic Domain-Driven Design: Area Synthesis

## State of Current Thought
Domain-Driven Design (DDD) provides the architectural blueprint for scaling Multi-Agent Systems. Agents are constrained within "Bounded Contexts," react to "Domain Events," and communicate via a "Ubiquitous Language." A critical advancement is the formalized "Portable Agent Authorization" model, which ensures that an agent's identity and delegated authority are cryptographically bound, enabling safe cross-boundary trust tiers.

## Areas of Controversy / Ongoing Conversation
- **Strict Autonomy vs. Orchestration:** Should agents be purely reactive to event streams (choreography), or does the non-deterministic nature of LLMs necessitate a central orchestrator to manage state and resolve conflicts?
- **Authorization Attenuation:** Implementing multi-principal workflow composition without unintentionally widening an agent's authority across domains remains a highly complex implementation challenge.

## See Also
- [Agentic Ddd Overview](./agentic-ddd-overview.md)
- [Portable Agent Authorization](./portable-agent-authorization.md)
