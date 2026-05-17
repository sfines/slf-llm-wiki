import os

index_path = '/Users/sfines/workspace/slf-llm-wiki/wiki/index.md'

with open(index_path, 'r') as f:
    lines = f.readlines()

new_content = []
for line in lines:
    new_content.append(line)
    if line.strip() == "- [ACE Process: Curation](agentic-harness/ace-process-curation.md)":
        new_content.append("  - [SkillOps Framework](agentic-harness/skillops-framework.md)\n")
        new_content.append("    - [Skill Technical Debt](agentic-harness/skill-technical-debt.md)\n")
        new_content.append("    - [Skill Contracts](agentic-harness/skill-contracts.md)\n")
        new_content.append("    - [Hierarchical Skill Ecosystem Graph (HSEG)](agentic-harness/hierarchical-skill-ecosystem-graph.md)\n")
        new_content.append("    - [Skill Library Health Diagnosis](agentic-harness/skill-library-health-diagnosis.md)\n")
        new_content.append("    - [Skill Maintenance Actions](agentic-harness/skill-maintenance-actions.md)\n")
        new_content.append("    - [ContractGraph-Propagated Diagnosis (CGPD)](agentic-harness/contractgraph-propagated-diagnosis.md)\n")
        new_content.append("    - [Task-Time Skill Loop](agentic-harness/task-time-skill-loop.md)\n")
        new_content.append("    - [Library-Time Skill Loop](agentic-harness/library-time-skill-loop.md)\n")
        new_content.append("    - [Skill Validation Gaps](agentic-harness/skill-validation-gaps.md)\n")
        new_content.append("    - [Dependency Stitching](agentic-harness/dependency-stitching.md)\n")
        new_content.append("    - [SkillOps ALFWorld Evaluation](agentic-harness/skillops-alfworld-evaluation.md)\n")

with open(index_path, 'w') as f:
    f.writelines(new_content)
