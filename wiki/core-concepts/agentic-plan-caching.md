# Agentic Plan Caching (APC)

Agentic Plan Caching (APC) is a novel test-time memory mechanism that targets the reduction of serving costs for LLM-based agents following a Plan-Act paradigm. By extracting, storing, adapting, and reusing structured plan templates from completed agent execution logs, APC avoids the overhead of redundant planning.

## Key Features
- **Task-Level Caching:** Unlike chatbot-oriented semantic caching that looks at query-level inputs, APC focuses on task-level caching.
- **Template Adaptation:** Employs lightweight models (e.g., small LLMs) to adapt generalized templates into context-specific action plans, rather than relying on expensive planner models for every step.
- **Data-Dependent Outcomes:** Specifically designed to handle agent scenarios where outputs depend not just on the user's prompt but on external data and environmental context, which often breaks traditional semantic caching.

## References
- [Agentic Plan Caching: Test-Time Memory for Fast and Cost-Efficient LLM Agents](../../raw/agentic-plan-caching.md)
