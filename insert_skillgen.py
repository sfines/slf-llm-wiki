import os

index_path = '/Users/sfines/workspace/slf-llm-wiki/wiki/index.md'

with open(index_path, 'r') as f:
    lines = f.readlines()

new_content = []
for line in lines:
    new_content.append(line)
    if line.strip() == "- [SkillOps ALFWorld Evaluation](agentic-harness/skillops-alfworld-evaluation.md)":
        new_content.append("  - [SkillGen Framework](agentic-harness/skillgen-framework.md)\n")
        new_content.append("    - [Verified Inference-Time Skills](agentic-harness/verified-inference-time-skills.md)\n")
        new_content.append("    - [Baseline Elicitation Stage](agentic-harness/baseline-elicitation-stage.md)\n")
        new_content.append("    - [Contrastive Behavioral Induction](agentic-harness/contrastive-behavioral-induction.md)\n")
        new_content.append("    - [Local Contrastive Analysis](agentic-harness/local-contrastive-analysis.md)\n")
        new_content.append("    - [Generation-Verification-Refinement Loop](agentic-harness/generation-verification-refinement-loop.md)\n")
        new_content.append("    - [Causal Evaluation of Skill Interventions](agentic-harness/causal-evaluation-of-skill-interventions.md)\n")
        new_content.append("    - [Verification Gate and Selection](agentic-harness/verification-gate-and-selection.md)\n")
        new_content.append("    - [Skill Net-Effect Measurement](agentic-harness/skill-net-effect-measurement.md)\n")
        new_content.append("    - [Cross-Model Skill Transfer](agentic-harness/cross-model-skill-transfer.md)\n")
        new_content.append("    - [Repair vs Regression in Skills](agentic-harness/repair-vs-regression-in-skills.md)\n")
        new_content.append("    - [Skill Iterative Refinement Feedback](agentic-harness/skill-iterative-refinement-feedback.md)\n")

with open(index_path, 'w') as f:
    f.writelines(new_content)
