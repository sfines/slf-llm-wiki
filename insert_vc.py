import os

index_path = '/Users/sfines/workspace/slf-llm-wiki/wiki/index.md'

with open(index_path, 'r') as f:
    lines = f.readlines()

new_content = []
for line in lines:
    new_content.append(line)
    if line.strip() == "- [SWE-bench 500 Evaluation](agyn/swe-bench-500.md)":
        new_content.append("  - [Multi-Agent Due Diligence Framework](agyn/multi-agent-due-diligence-framework.md)\n")
        new_content.append("    - [Event-Driven Orchestration Architecture](agyn/event-driven-orchestration-architecture.md)\n")
        new_content.append("    - [Financial Hallucination Mitigation](agyn/financial-hallucination-mitigation.md)\n")
        new_content.append("    - [Multi-Agent Structural Fallback Mechanism](agyn/multi-agent-structural-fallback-mechanism.md)\n")
        new_content.append("    - [Layout-Aware OCR Extraction](agyn/layout-aware-ocr-extraction.md)\n")
        new_content.append("    - [DAG-Structured Orchestration](agyn/dag-structured-orchestration.md)\n")
        new_content.append("    - [Autonomous Financial API Routing](agyn/autonomous-financial-api-routing.md)\n")
        new_content.append("    - [Agent-Based OSINT Retrieval](agyn/agent-based-osint-retrieval.md)\n")
        new_content.append("    - [Retrieval-Augmented Generation for Finance](agyn/retrieval-augmented-generation-for-finance.md)\n")
        new_content.append("    - [Task Decomposition in Financial Agents](agyn/task-decomposition-in-financial-agents.md)\n")
        new_content.append("    - [Multi-Agent Market Intelligence Synthesis](agyn/multi-agent-market-intelligence-synthesis.md)\n")
        new_content.append("    - [Multi-Agent Corporate Research Pipeline](agyn/multi-agent-corporate-research-pipeline.md)\n")

with open(index_path, 'w') as f:
    f.writelines(new_content)
