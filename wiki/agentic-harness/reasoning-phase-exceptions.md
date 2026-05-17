# Reasoning-Phase Exceptions

Reasoning-Phase Exceptions occur during the cognitive and planning stages of an LLM agentic workflow, prior to any external execution. These failures stem from an agent misinterpreting context, generating flawed logic, or formulating unfeasible task plans.

## Goal and Context Failures
Agents can falter immediately if the user's intent is unclear or if the working context is compromised. 
- **Ambiguous or Conflicting Goals**: The user provides underspecified or mutually exclusive objectives, leading the agent to formulate misaligned plans.
- **Context Corruption and Ambiguity**: Previous prompt contents, adversarial injections, or ambiguous UI referents contaminate the decision-making context.

## Logic and Planning Breakdowns
Even with clear goals, an agent's internal logic can fail:
- **Contradictory and Circular Reasoning**: The agent produces internally inconsistent claims or gets stuck in repetitive logical loops without forward progress.
- **Faulty Task Structuring**: The agent decomposes a task poorly, misordering dependencies or ignoring global constraints.
- **Overextended Planning**: The agent generates overly verbose, redundant, or low-yield steps that consume excessive resources.

## Memory and Knowledge Errors
Retrieval augmented systems and memory layers are prone to providing bad context to the reasoning engine:
- **Memory Poisoning and Outdated Memory**: Retaining malicious, noisy, or expired memory traces degrades decision-making.
- **Misaligned Recall**: Retrieving conceptually similar but task-inappropriate memories.
- **Hallucinated Facts**: Producing statements unsupported by the actual knowledge base structure.

## See Also
- [Agentic Exception Taxonomy](./agentic-exception-taxonomy.md)
- [Execution-Phase Exceptions](./execution-phase-exceptions.md)
- [Raw Source: SHIELDA Paper](../../raw/shielda-paper.md)