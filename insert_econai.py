import os

index_path = '/Users/sfines/workspace/slf-llm-wiki/wiki/index.md'

with open(index_path, 'r') as f:
    lines = f.readlines()

new_content = []
for line in lines:
    new_content.append(line)
    if line.strip() == "- [Multi-Agent Memory](agent-memory/multi-agent-memory-architectures.md)":
        new_content.append("  - [EconAI Framework](agent-memory/econai-framework.md)\n")
        new_content.append("    - [Economic Sentiment Indexing (ESI)](agent-memory/economic-sentiment-indexing.md)\n")
        new_content.append("    - [Dynamic Persona Evolution](agent-memory/dynamic-persona-evolution.md)\n")
        new_content.append("    - [Macro-Micro Economic Unified Modeling](agent-memory/macro-micro-economic-unified-modeling.md)\n")
        new_content.append("    - [Agent Event Memory Perception](agent-memory/agent-event-memory-perception.md)\n")
        new_content.append("    - [Long-Term Strategic Economic Planning](agent-memory/long-term-strategic-economic-planning.md)\n")
        new_content.append("    - [Agent Memory Weighting](agent-memory/agent-memory-weighting.md)\n")
        new_content.append("    - [Household vs Firm Agent Roles](agent-memory/household-vs-firm-agent-roles.md)\n")
        new_content.append("    - [Economic Belief Quantification](agent-memory/economic-belief-quantification.md)\n")
        new_content.append("    - [Agent Work-Consumption Dynamics](agent-memory/agent-work-consumption-dynamics.md)\n")
        new_content.append("    - [Generative Agent Societies](agent-memory/generative-agent-societies.md)\n")
        new_content.append("    - [LLM Instruction Tuning for Event Summarization](agent-memory/llm-instruction-tuning-for-event-summarization.md)\n")

with open(index_path, 'w') as f:
    f.writelines(new_content)
