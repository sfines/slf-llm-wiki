# Event Storming Simulation

**Event Storming Simulation** is the second stage of the [Automating DDD Framework](ddd-prompting-framework.md), where an LLM is used to perform a virtual discovery workshop.

## Process
- **Input:** Business requirements or user stories.
- **Model Action:** The LLM "brainstorms" a list of **Domain Events** (e.g., `AccountCreated`, `MessageSent`) and the **Commands** that trigger them.
- **Output:** A chronological timeline of events that defines the system's behavioral flow.

## High Utility
The research found that LLMs are exceptionally good at this discovery phase, often identifying edge-case events that human developers might overlook. It provides a valuable "starting point" for a real-world team workshop.

## See Also
- [Event Storming](event-storming.md)
- [Event Storming for Agents](event-storming-for-agents.md)
- [Automating DDD Framework](ddd-prompting-framework.md)
