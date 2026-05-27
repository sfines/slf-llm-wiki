# Agentic Domain-Driven Design (Agentic DDD): Area Synthesis

## Summary of the Field
Domain-Driven Design (DDD) provides the architectural blueprint for scaling Multi-Agent Systems (MAS). Agentic DDD adapts traditional DDD principles—Bounded Contexts, Ubiquitous Language, and Domain Events—to provide structural guardrails for Autonomous AI Agents. Agents are constrained within "Bounded Contexts," react to "Domain Events," and communicate via a "Ubiquitous Language." A critical advancement is the formalized "Portable Agent Authorization" model, which ensures that an agent's identity and delegated authority are cryptographically bound, enabling safe cross-boundary trust tiers. Research also explores automating DDD artifacts (Event Storming, Bounded Context identification) using LLMs as collaborative sparring partners, although long architectural chains often suffer from context collapse and error propagation.

## Definition of Key Terms
- **Bounded Contexts:** The explicit scope of an agent's responsibility, data access, and autonomy.
- **Domain Events:** Identifiable occurrences in the business domain that serve as primary communication triggers between agents.
- **Ubiquitous Language:** A shared vocabulary between domain experts, developers, and AI models ensuring semantic alignment across the system.
- **Portable Agent Authorization:** A standard allowing an agent to carry an issuer-authored authorization payload that defines its authority, permissions, and constraints, independent of the underlying transport or policy engine.
- **Typed Constraint Algebra:** A set of machine-evaluable restrictions (e.g., Numeric Limits, Temporal Windows, Enumerated Lists, String Patterns) that govern agent actions at runtime.
- **Error Propagation (Context Collapse):** The degradation of technical outputs in automated LLM pipelines where minor inaccuracies in early design stages compound over long architectural sequences.

## Top 3-5 Most Important Elements
1. **Scalability via Specialization:** Decomposing an enterprise system into specialized bounded contexts (e.g., Procurement, Logistics, Inventory) allows new agents to be integrated without increasing global complexity.
2. **Deterministic Authorization:** Defining a 3-layer authorization architecture (Credential Container, Authorization Payload, Enforcement Engine) ensures that an agent's authority is explicit, auditable, and subject to fail-closed evaluation.
3. **Event-Driven Resilience:** Communication via Domain Events allows asynchronous operations, preventing a failure in one agent (e.g., Logistics) from cascading to others.
4. **Delegation Attenuation:** As agent authority is delegated, the scope of permissions can only narrow or remain constant—never widen—enabling safe multi-principal workflow composition.

## Key Algorithms
- **Three-Layer Authorization Architecture:**
  - *Layer 1 (Credential Container):* Cryptographic envelope (JWT, Verifiable Credential) providing integrity.
  - *Layer 2 (Authorization Payload):* Contains Agent Identity, Issuer Identity, Declared Permissions, and Policy Constraints.
  - *Layer 3 (Enforcement Engine):* Evaluates constraints against the request context and merges with local policy.
- **Automated DDD Five-Step Prompting Framework:**
  1. Establishing Ubiquitous Language.
  2. Simulating Event Storming.
  3. Identifying Bounded Contexts.
  4. Designing Aggregates.
  5. Mapping to Technical Architecture.

## Main Benefits
- **Scalability and Robustness:** Agents act locally within bounded contexts, preventing monolithic AI bottlenecks.
- **Auditability and Compliance:** Cryptographically-bound constraints and portable authorization enable end-to-end traceability of autonomous decisions, crucial for regulated industries.
- **Security:** Strict attenuation rules and a fail-closed evaluation model prevent agents from exceeding their mandate.

## Main Drawbacks
- **Complexity in Implementation:** Designing typed constraint algebras and mapping context boundaries requires significant upfront architectural effort.
- **Error Propagation in Automation:** Bootstrapping DDD via LLMs degrades significantly at the aggregate and technical mapping layers.
- **Orchestration Overhead:** Managing multi-principal workflows with disparate credentials requires sophisticated receiver-side workflow policies.

## Areas of Controversy / Ongoing Conversation
- **Architectural Topology Selection:** Deciding which execution topology (Chain, Route, Hierarchy, etc.) optimally balances latency, compute cost, and blast radius for a given cognitive function.
- **Strict Autonomy vs. Orchestration:** Should agents be purely reactive to event streams (choreography), or does the non-deterministic nature of LLMs necessitate a central orchestrator to manage state and resolve conflicts?
- **Authorization Attenuation:** Implementing multi-principal workflow composition without unintentionally widening an agent's authority across domains remains a highly complex implementation challenge.
- **LLM as Architect:** The extent to which LLMs can autonomously design system architectures is debated, with current consensus favoring LLMs as "collaborative sparring partners" rather than solo architects due to context collapse.

## Domains
- **Technical Domain:** Multi-Agent Systems (MAS), Identity and Access Management (IAM), Distributed Systems Architecture.
- **Business Domain:** Supply Chain Management (SCM) (e.g., procurement, logistics, inventory), Insurance Claims Processing, High-assurance manufacturing.

## Defining Paper Citations
- A Two-Dimensional Framework for AI Agent Design Patterns (Huang & Zhou, 2026)
- [Designing Scalable Multi-Agent AI Systems: Leveraging Domain-Driven Design and Event Storming](../../raw/nandi-dey-2025.md)
- [Digital Identity for Agentic Systems: Toward a Portable Authorization Standard for Autonomous Agents](../../raw/digital-identity-agentic-systems-paper.md)
- [Automating Domain-Driven Design: Experience with a Prompting Framework](../../raw/automating-ddd-paper.md)

## See Also
- [Agentic DDD Overview](./agentic-ddd-overview.md)
- [Portable Agent Authorization](./portable-agent-authorization.md)
- [Agent Cross Boundary Trust Tiers](./agent-cross-boundary-trust-tiers.md)
- [Bounded Contexts in MAS](./bounded-contexts-in-mas.md)
- [Multi-Principal Workflow Composition](./multi-principal-workflow-composition.md)