import os
import re

wiki_dir = '/Users/sfines/workspace/slf-llm-wiki/wiki'

syntheses = {
    'advanced-retrieval': {
        'title': 'Advanced Retrieval (RAG): Area Synthesis',
        'current': 'Modern retrieval is shifting from naive semantic vector search to structured, relational models like Pseudo-Knowledge Graphs (PKG). Maintaining in-graph text and mapping meta-paths allow agents to perform multi-hop reasoning with high vector information density, overcoming the traditional limits of context fragmentation.',
        'controversy': '- **Graph vs. Vector vs. Hybrid:** While PKGs offer superior relational awareness, the computational overhead of constructing and updating them during active agent sessions remains contested. Is the latency trade-off worth it compared to denser embeddings?\n- **Context Saturation vs. Fragmentation:** Striking the balance between providing enough retrieved context to avoid fragmentation, while avoiding context saturation that degrades LLM reasoning.',
        'links': ['rag.md', 'pseudo-knowledge-graph.md']
    },
    'agent-memory': {
        'title': 'Agent Memory: Area Synthesis',
        'current': 'Agent memory is moving beyond simple conversational append-logs into multi-tier architectures: Token, Parametric, and Latent forms fulfilling Working, Experiential, and Factual functions. Recent implementations like EconAI demonstrate that coupling memory with "Dynamic Personas" and "Economic Sentiment Indexing" allows agents to adapt to long-term environmental shifts rather than just reacting to immediate stimuli.',
        'controversy': '- **Mutable vs. Immutable Memory:** Should experiential memory be an immutable, append-only ledger for perfect auditability, or a mutable graph that decays and consolidates over time to save tokens?\n- **Memory Poisoning:** How to prevent stale, hallucinated, or adversarially injected data from corrupting the long-term memory bank, which can permanently degrade agent performance.',
        'links': ['agent-memory.md', 'econai-framework.md']
    },
    'agentic-ddd': {
        'title': 'Agentic Domain-Driven Design: Area Synthesis',
        'current': 'Domain-Driven Design (DDD) provides the architectural blueprint for scaling Multi-Agent Systems. Agents are constrained within "Bounded Contexts," react to "Domain Events," and communicate via a "Ubiquitous Language." A critical advancement is the formalized "Portable Agent Authorization" model, which ensures that an agent\'s identity and delegated authority are cryptographically bound, enabling safe cross-boundary trust tiers.',
        'controversy': '- **Strict Autonomy vs. Orchestration:** Should agents be purely reactive to event streams (choreography), or does the non-deterministic nature of LLMs necessitate a central orchestrator to manage state and resolve conflicts?\n- **Authorization Attenuation:** Implementing multi-principal workflow composition without unintentionally widening an agent\'s authority across domains remains a highly complex implementation challenge.',
        'links': ['agentic-ddd-overview.md', 'portable-agent-authorization.md']
    },
    'agentic-harness': {
        'title': 'Agentic Harness Engineering: Area Synthesis',
        'current': 'Harness engineering focuses on the middleware, observability, and lifecycle management of agents and their tools. Recent frameworks like SkillGen and SkillOps treat agent capabilities as software ecosystems requiring maintenance (e.g. managing "Skill Technical Debt"). Furthermore, the "Constraint State Governance" (CSG) paradigm argues that safety constraints must be maintained as explicit execution states to prevent "Constraint Drift" across long trajectories.',
        'controversy': '- **Proactive vs. Reactive Skill Maintenance:** Should agent skills be continuously evolved and patched at runtime (e.g., SkillWeaver), or strictly verified and gated at library-time to prevent regressions (e.g., SkillGen)?\n- **Safety by Prompt vs. Safety by State:** The realization that output-checking and system prompts are insufficient has sparked debate over how deeply integrated CSG admission control algorithms must be within the LLM\'s execution loop.',
        'links': ['agentic-harness-engineering.md', 'skillops-framework.md', 'constraint-drift.md']
    },
    'agyn': {
        'title': 'Agyn Team-Based Engineering: Area Synthesis',
        'current': 'The Agyn framework and related studies (like VC Due Diligence automation) demonstrate that replicating human organizational structures (Coordinator, Researcher, Implementer, Reviewer) significantly boosts autonomous software engineering performance. Using DAG-structured orchestration and event-driven architectures provides the necessary scaffolding to catch hallucinations and enforce structural fallbacks.',
        'controversy': '- **Fixed Roles vs. Dynamic Swarms:** Does forcing LLMs into rigid, human-like organizational charts artificially limit their collaborative potential, or is it the only reliable way to maintain coherence over long horizons?\n- **Communication Overhead:** The token cost and latency of strictly formatted, inter-agent structured communication versus fluid, unstructured collaboration.',
        'links': ['agyn-framework.md', 'multi-agent-due-diligence-framework.md']
    },
    'apwa': {
        'title': 'APWA Distributed Workloads: Area Synthesis',
        'current': 'APWA addresses the throughput limitations of sequential LLM agents by introducing dynamic task decomposition. By breaking enterprise workloads into non-interfering subproblems and applying parallel execution patterns, systems can scale reasoning horizontally across heterogeneous data sources.',
        'controversy': '- **Decomposition Accuracy:** If the initial dynamic decomposition is flawed, the parallel branches may produce incompatible outputs. \n- **Merge Conflicts in Reasoning:** At what point does the cognitive cost of synthesizing and merging parallel agent outputs exceed the benefit of distributed processing?',
        'links': ['apwa-overview.md', 'apwa-dynamic-decomposition.md']
    },
    'automating-ddd': {
        'title': 'Automating Domain-Driven Design: Area Synthesis',
        'current': 'LLMs act as "sparring partners" for software architects, simulating event storming sessions and automating the extraction of bounded contexts and aggregates. This accelerates the mapping of technical architecture from business requirements.',
        'controversy': '- **Domain Nuance:** Can AI truly grasp the subtleties of a business domain without human expert grounding?\n- **Error Propagation:** Mistakes made early in the automated aggregate design phase compound significantly when translated into technical mapping and API generation.',
        'links': ['ddd-prompting-framework.md', 'ddd-sparring-partner.md']
    },
    'confucius': {
        'title': 'Confucius Code Agent: Area Synthesis',
        'current': 'Operating autonomously on massive code repositories requires balancing Agent Experience (AX), User Experience (UX), and Developer Experience (DX). Confucius leverages a Unified Agent Orchestrator, hierarchical working memory, and a Meta-Agent Refinement Loop to continuously self-improve its approach to complex codebases.',
        'controversy': '- **Context Saturation Mitigation:** Should the framework forcefully prune context via sliding windows, or should the agent be strictly responsible for explicitly taking persistent notes and managing its own memory capacity?',
        'links': ['confucius-code-agent.md', 'confucius-meta-agent-loop.md']
    },
    'core-concepts': {
        'title': 'Core Concepts: Area Synthesis',
        'current': 'The foundational principles of Agentic Engineering merge Domain-Driven Design, Multi-Agent Systems, and Retrieval-Augmented Generation. Standards like the Model Context Protocol (MCP) are rapidly commoditizing the way agents interface with external environments and continuous learning loops.',
        'controversy': '- **Definition of Agency:** The boundary between a complex, tool-using RAG pipeline and a truly autonomous agent remains philosophically and technically blurred.\n- **Plan Caching vs. Novel Generation:** Reusing cached agentic plans improves speed and cost but risks applying outdated logic to dynamic environments.',
        'links': ['autonomous-agents.md', 'domain-driven-design.md']
    },
    'gambit': {
        'title': 'GAMBIT Adversarial Robustness: Area Synthesis',
        'current': 'As multi-agent systems scale, their vulnerability to adversarial inputs and "adaptive imposters" increases. GAMBIT establishes a benchmark and evolutionary framework for evaluating how well agents can detect and fast-recalibrate against deception or reasoning substrate attacks.',
        'controversy': '- **Defensive Prompting vs. Architectural Isolation:** Should individual agents be trained/prompted to natively detect deception, or should the system rely on strict, zero-trust architectural boundaries (like isolated sandboxes and strict capability attenuation) to limit the blast radius?',
        'links': ['gambit-overview.md', 'adversarial-robustness-mas.md']
    }
}

for folder, data in syntheses.items():
    filename = f"{folder}-synthesis.md"
    filepath = os.path.join(wiki_dir, folder, filename)
    
    content = f"# {data['title']}\n\n"
    content += "## State of Current Thought\n"
    content += f"{data['current']}\n\n"
    content += "## Areas of Controversy / Ongoing Conversation\n"
    content += f"{data['controversy']}\n\n"
    content += "## See Also\n"
    for link in data['links']:
        content += f"- [{link.replace('.md', '').replace('-', ' ').title()}](./{link})\n"
        
    with open(filepath, 'w') as f:
        f.write(content)

# Update index.md
index_path = os.path.join(wiki_dir, 'index.md')
with open(index_path, 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    
    # Map index headers to folders
    mappings = {
        "- [Core Concepts]": "core-concepts",
        "- [Agentic Domain-Driven Design]": "agentic-ddd",
        "- [Agent Memory]": "agent-memory",
        "- [Advanced Retrieval (RAG)]": "advanced-retrieval",
        "- [Agentic Harness Engineering]": "agentic-harness",
        "- [Confucius Code Agent]": "confucius",
        "- [Agyn Team-Based Engineering]": "agyn",
        "- [APWA Distributed Workloads]": "apwa",
        "- [GAMBIT Adversarial Robustness]": "gambit",
        "- [Automating Domain-Driven Design]": "automating-ddd"
    }
    
    for key, folder in mappings.items():
        if line.strip().startswith(key):
            new_lines.append(f"  - [**Area Synthesis: {folder.replace('-', ' ').title()}**]({folder}/{folder}-synthesis.md)\n")

with open(index_path, 'w') as f:
    f.writelines(new_lines)
