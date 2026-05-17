import os

index_path = '/Users/sfines/workspace/slf-llm-wiki/wiki/index.md'

with open(index_path, 'r') as f:
    lines = f.readlines()

new_content = []
for line in lines:
    new_content.append(line)
    if line.strip() == "- [Agentic Context Engineering (ACE)](agentic-harness/agentic-context-engineering.md)":
        new_content.insert(-1, "  - [SHIELDA Framework](agentic-harness/shielda-framework.md)\n")
        new_content.insert(-1, "    - [Agentic Exception Taxonomy](agentic-harness/agentic-exception-taxonomy.md)\n")
        new_content.insert(-1, "    - [Reasoning-Phase Exceptions](agentic-harness/reasoning-phase-exceptions.md)\n")
        new_content.insert(-1, "    - [Execution-Phase Exceptions](agentic-harness/execution-phase-exceptions.md)\n")
        new_content.insert(-1, "    - [Structured Handling Executor](agentic-harness/structured-handling-executor.md)\n")
        new_content.insert(-1, "    - [Phase-Aware Recovery](agentic-harness/phase-aware-recovery.md)\n")
        new_content.insert(-1, "    - [Exception Classifier](agentic-harness/exception-classifier.md)\n")
        new_content.insert(-1, "    - [Handling Pattern Registry](agentic-harness/handling-pattern-registry.md)\n")
        new_content.insert(-1, "    - [Agent Local Handling](agentic-harness/agent-local-handling.md)\n")
        new_content.insert(-1, "    - [Agent Exception Flow Control](agentic-harness/agent-exception-flow-control.md)\n")
        new_content.insert(-1, "    - [Agent State Recovery](agentic-harness/agent-state-recovery.md)\n")
        new_content.insert(-1, "    - [AutoPR Exception Case Study](agentic-harness/autopr-exception-case-study.md)\n")

with open(index_path, 'w') as f:
    f.writelines(new_content)
