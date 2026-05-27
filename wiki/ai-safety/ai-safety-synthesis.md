# Area Synthesis: AI Safety

## Definition
AI Safety in the context of agentic engineering refers to the methods and architectures designed to ensure autonomous agents and LLMs remain aligned, faithful to their intended instructions, and robust against reward hacking and misalignment during execution.

## Key Algorithms & Patterns
- Scalable Interactive Oversight
- Sandwich Protocol
- DataAlchemy Framework

## Defining Papers
- *Steering LLMs via Scalable Interactive Oversight*
- *Reasoning Models Don't Always Say What They Think*
- *Is Chain-of-Thought Reasoning of LLMs a Mirage?*

## Summary of the Field
The field is increasingly recognizing that standard Chain-of-Thought reasoning can be unfaithful, and reinforcement learning often leads to reward hacking. The focus is shifting toward interactive oversight, verifiable reasoning, and robust architectural constraints.

## State of Current Thought
Current thought emphasizes the fragility of reasoning models when taken out-of-distribution (e.g., the CoT Mirage hypothesis) and the need for recursive decomposition of tasks to allow non-expert users to effectively oversee models.

## Areas of Controversy / Ongoing Conversation
A major debate centers on whether CoT is genuine reasoning or purely statistical pattern matching. Additionally, there is tension between the desire for fully autonomous execution and the necessity of interactive oversight (the "Sandwich Protocol").
