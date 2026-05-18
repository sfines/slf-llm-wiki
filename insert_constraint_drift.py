import os

index_path = '/Users/sfines/workspace/slf-llm-wiki/wiki/index.md'

with open(index_path, 'r') as f:
    lines = f.readlines()

new_content = []
for line in lines:
    new_content.append(line)
    if line.strip() == "- [Skill Iterative Refinement Feedback](agentic-harness/skill-iterative-refinement-feedback.md)":
        new_content.append("  - [Constraint Drift](agentic-harness/constraint-drift.md)\n")
        new_content.append("    - [Memory Drift](agentic-harness/memory-drift.md)\n")
        new_content.append("    - [Authority Drift](agentic-harness/authority-drift.md)\n")
        new_content.append("    - [Information-Flow Drift](agentic-harness/information-flow-drift.md)\n")
        new_content.append("    - [Accountability Drift](agentic-harness/accountability-drift.md)\n")
        new_content.append("    - [Utility-Induced Drift](agentic-harness/utility-induced-drift.md)\n")
        new_content.append("    - [Constraint State Governance (CSG)](agentic-harness/constraint-state-governance.md)\n")
        new_content.append("    - [Constraint Native Reinforcement Learning](agentic-harness/constraint-native-reinforcement-learning.md)\n")
        new_content.append("    - [Multi-Agent Trajectory Safety](agentic-harness/multi-agent-trajectory-safety.md)\n")
        new_content.append("    - [CSG Admission Control Algorithm](agentic-harness/csg-admission-control-algorithm.md)\n")
        new_content.append("    - [Safe Multi-Agent Behavior Paradigms](agentic-harness/safe-multi-agent-behavior-paradigms.md)\n")
        new_content.append("    - [AgentLeak Case Study](agentic-harness/agentleak-case-study.md)\n")

with open(index_path, 'w') as f:
    f.writelines(new_content)
