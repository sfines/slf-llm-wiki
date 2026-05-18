import os

index_path = '/Users/sfines/workspace/slf-llm-wiki/wiki/index.md'

with open(index_path, 'r') as f:
    lines = f.readlines()

new_content = []
for line in lines:
    new_content.append(line)
    if line.strip() == "- [Agentic Domain-Driven Design](agentic-ddd/agentic-ddd-overview.md)":
        new_content.append("  - [Portable Agent Authorization](agentic-ddd/portable-agent-authorization.md)\n")
        new_content.append("    - [Agent Identity vs Authorization](agentic-ddd/agent-identity-vs-authorization.md)\n")
        new_content.append("    - [Three-Layer Authorization Architecture](agentic-ddd/three-layer-authorization-architecture.md)\n")
        new_content.append("    - [Typed Constraint Algebra](agentic-ddd/typed-constraint-algebra.md)\n")
        new_content.append("    - [Agent Delegation Attenuation](agentic-ddd/agent-delegation-attenuation.md)\n")
        new_content.append("    - [Multi-Principal Workflow Composition](agentic-ddd/multi-principal-workflow-composition.md)\n")
        new_content.append("    - [Governed Semantic Resolution](agentic-ddd/governed-semantic-resolution.md)\n")
        new_content.append("    - [Stateful Enforcement Profiles](agentic-ddd/stateful-enforcement-profiles.md)\n")
        new_content.append("    - [Pre-Flight Authorization Discovery](agentic-ddd/pre-flight-authorization-discovery.md)\n")
        new_content.append("    - [Agent Cross-Boundary Trust Tiers](agentic-ddd/agent-cross-boundary-trust-tiers.md)\n")
        new_content.append("    - [Use Case: Insurance Claims Agent Authorization](agentic-ddd/insurance-claims-agent-authorization.md)\n")
        new_content.append("    - [Use Case: Supply Chain Agent Authorization](agentic-ddd/supply-chain-agent-authorization.md)\n")

with open(index_path, 'w') as f:
    f.writelines(new_content)
