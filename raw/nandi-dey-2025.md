# Designing Scalable Multi-Agent AI Systems: Leveraging Domain-Driven Design and Event Storming

**Authors:** Kunal Nandi, Kaustav Dey
**Date:** March 2025
**Source:** International Journal of Computer Science and Engineering (Vol. 12, No. 3)
**DOI:** 10.14445/23488387/IJCSE-V12I3P102

## Abstract Summary
This paper proposes an architectural framework that applies Domain-Driven Design (DDD) and Event Storming to Multi-Agent Systems (MAS). It addresses the complexity of defining agent boundaries and managing interactions by using Bounded Contexts as autonomy boundaries and Domain Events as communication triggers.

## Key Principles
- **Bounded Contexts as Agent Boundaries:** Defining the explicit scope of an agent's responsibility and data access, preventing "monolithic" agent designs and ensuring specialized expertise.
- **Event Storming for Discovery:** Using collaborative discovery tools to identify **Domain Events** that serve as primary communication triggers between agents, grounding interactions in business processes.
- **Ubiquitous Language:** Establishing a shared vocabulary between AI developers, domain experts, and the agents themselves to ensure semantic alignment across the system.
- **Rich Domain Models:** Encapsulating complex business logic within specific agents to make them more autonomous and robust against global system changes.

## Case Study: Supply Chain Management
The paper demonstrates the framework using an SCM case study, decomposing the system into **Procurement**, **Logistics**, **Inventory**, and **Demand Planning** contexts. Key findings include:
- **Scalability:** The system scales by adding specialized agents without increasing global complexity.
- **Robustness:** Event-driven communication allows agents to operate asynchronously and handle failures in other parts of the system gracefully (e.g., Logistics failure not impacting Procurement).
- **Latency:** Decisions are made locally within contexts, reducing the need for a central orchestrator.

## Reference
Nandi, K., & Dey, K. (2025). Designing Scalable Multi-Agent AI Systems: Leveraging Domain-Driven Design and Event Storming. SSRG International Journal of Computer Science and Engineering.
