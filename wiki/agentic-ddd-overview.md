# Agentic Domain-Driven Design (Agentic DDD)

Agentic Domain-Driven Design is an architectural framework that adapts traditional [Domain-Driven Design (DDD)](domain-driven-design.md) principles to the development of [Autonomous AI Agents](autonomous-agents.md) and [Multi-Agent Systems (MAS)](multi-agent-systems.md).

## Core Philosophy
The central goal of Agentic DDD is to provide a "worldview" for AI agents. By grounding agents in well-defined business domains, developers can manage the "dynamic complexity" (autonomy, reactivity, planning) through the "structural guardrails" provided by DDD.

## Key Tenets

### 1. [Bounded Contexts as Agent Boundaries](bounded-contexts-in-mas.md)
In Agentic DDD, a Bounded Context defines the limits of an agent's autonomy and expertise, establishing explicit [Autonomy Boundaries](agent-autonomy-boundaries.md). This prevents "monolithic" agent designs and ensures that specialized agents operate strictly within their domain's rules.

### 2. [Ubiquitous Language as Semantic Contracts](ubiquitous-language-for-ai.md)
The shared vocabulary between domain experts and developers extends to the AI models. Tool definitions, API schemas, and instructions must use the Ubiquitous Language to ensure the agent's reasoning aligns with business logic, often supported by [Rich Domain Models](rich-domain-models-for-agents.md).

### 3. [Event Storming for Agent Discovery](event-storming-for-agents.md)
[Event Storming](event-storming.md) is used to identify **[Domain Events](domain-events-as-triggers.md)**, which serve as the primary triggers for agent actions and communication between different agents in a system.

### 4. [Context Mapping for Collaboration](context-mapping-for-agents.md)
Context Mapping defines how different agents (and their respective bounded contexts) interact, providing a blueprint for reliable multi-agent orchestration.

## Benefits
- **Scalability:** Specialized agents can be added or updated without global system impact.
- **Reliability:** Clear boundaries and semantic contracts reduce hallucinations and logic errors.
- **Auditability:** Interactions are explicit and grounded in business events.

## References
- [Designing Scalable Multi-Agent AI Systems](../raw/nandi-dey-2025.md)
- [Automating Domain-Driven Design: Experience with a Prompting Framework](../raw/automating-ddd-paper.md)
