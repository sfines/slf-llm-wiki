# Safe Multi-Agent Behavior Must Be Maintained, Not Merely Asserted: Constraint Drift in LLM-Based Multi-Agent Systems

**Type:** webpage
**Item Key:** IGK3EJYT
**Date:** 2026/05/11
**Authors:** Li, Tianxiao; Ma, Yixing; Wen, Haiquan; Huang, Zhenglin; Zhou, Qianyu; Fu, Zeyu; Cheng, Guangliang
**URL:** https://arxiv.org/abs/2605.10481v1

## Abstract

Modern LLM based agents are no longer passive text generators. They read repositories, call tools, browse the web, execute code, maintain memory, communicate with other agents, and act through long horizon workflows. This shift moves the unit of safety. A system may produce a compliant final answer while leaking private information through an internal message, delegating authority beyond its original scope, calling an external tool with sensitive context, or losing the evidence needed to reconstruct why an action was allowed. We argue that many emerging failures in LLM-based multi-agent systems share a common structure: safety critical constraints do not remain operative throughout the trajectory. We call this phenomenon constraint drift: the loss, distortion, weakening, or relaxation of constraints as they pass through memory, delegation, communication, tool use, audit, and optimization. The position taken here is that safe multi-agent behavior must be maintained, not merely asserted. Prompts, guardrails, tool schemas, access control, and final output checks are necessary, but they are insufficient unless constraints remain fresh, inherited, enforceable, and auditable across execution. We propose Constraint State Governance as a research paradigm for LLM-based multi-agent systems. In this paradigm, safety-critical constraints are maintained as explicit execution state, while constraint-native reinforcement learning improves utility only within maintained safety boundaries. The goal is not to freeze agentic systems under rigid rules, but to make safety operational across the trajectories through which modern agents actually act.

## Full Text

Safe Multi-Agent Behavior Must Be Maintained, Not Merely Asserted: Constraint Drift in LLM-Based Multi-Agent Systems
Tianxiao Li1 Yixing Ma2 Haiquan Wen1 Zhenglin Huang1 Qianyu Zhou4 Zeyu Fu3 Guangliang Cheng1,*
1University of Liverpool, UK 2University of Nottingham, UK 3University of Exeter, UK 4University of Tokyo, Japan
*Corresponding author: guangliang.cheng@liverpool.ac.uk

Abstract
Modern LLM based agents are no longer passive text generators. They read repositories, call tools, browse the web, execute code, maintain memory, communicate with other agents, and act through long horizon workflows. This shift moves the unit of safety. When the setting is a single response, safety is often judged from the answer shown to the user. In a multi-agent execution setting, the final answer is only the visible endpoint of a longer trajectory [12]. Consider a coding assistant working on a private repository under constraints: do not expose API keys, do not send proprietary code to external services, do not modify production configuration, do not bypass tests, and do not delete files outside the relevant module. The final patch may compile and the final message may look compliant, while the trajectory has already leaked a token in an internal message, sent code through a tool call, expanded a narrow permission into broader edit authority, or deleted a failing test during cleanup. The safety failure lies not only in what the system says, but in how it acted.

We call this phenomenon constraint drift: the loss of operational force of a safety constraint across an LLM-based multi-agent trajectory. We use five diagnostic modes: memory drift, authority drift, information-flow drift, accountability drift, and utility-induced drift, marking where a constraint stops being fresh, inherited, enforceable, or auditable. The list is not meant to be a closed taxonomy. Unlike reward hacking, specification gaming, or goal misgeneralization, which concern flawed objectives, proxy exploitation, or unintended goals [2, 17, 5], constraint drift names a preservation failure inside agentic execution. Its LLM-specific challenge is that constraints are natural language objects that can be summarized, reinterpreted, routed through tools, and justified after the fact.

The position of this paper is: safe multi-agent behavior must be maintained, not merely asserted. Output level safety falls short for agentic systems. A final answer can read as compliant even when the trajectory itself has already broken privacy, authority, audit, or file boundary constraints. Prompts, guardrails, tool schemas, access control, filters, and logs are only useful when they keep constraints tied to the actions those constraints are meant to govern. Agent safety benchmarks therefore need to look at whether constraints are preserved across the trajectory. Looking only at the final output is not enough.

This paper makes two contributions. First, it introduces constraint drift as an analytical framework for trajectory level safety failures in LLM-based multi-agent systems. Second, it proposes Constraint State Governance as a design paradigm in which safety critical constraints are represented as signed state, inherited through scoped delegation, checked before critical actions, recorded for audit, and supplied to learning. We further show how Constraint Native Reinforcement Learning can optimize utility only within admissible trajectories, rather than treating mandatory constraints as soft penalties. An empirical replay study on AgentLeak grounds the argument: output only filtering can make final answers look safe while internal channels remain exposed, whereas transition level governance makes those violations visible, auditable, and catchable.

2 Constraint Drift as a Systems-Level Preservation Failure
Constraint drift names a preservation failure. It does not cover every unsafe behavior an agent might produce. An LLM-based multi-agent system may begin with explicit safety critical constraints. The central question is whether these constraints remain operative once the system summarizes context, delegates work, calls tools, edits files, runs commands, updates memory, and optimizes for task success.

2.1 Drift Modes from Trajectory Interfaces
The five modes in Table 1 are diagnostic rather than mutually exclusive.
* Memory drift: Constraint is omitted or retrieved imprecisely; "do not delete outside auth" becomes "clean up irrelevant files". Interface: State and memory.
* Authority drift: Delegated scope widens; read only inspection becomes permission to edit production config. Interface: Delegation and authority.
* Information flow drift: Sensitive content crosses messages, memory, tool arguments, or external queries; an API key enters an internal message. Interface: Communication and tool I/O.
* Accountability drift: Action is logged without reconstructable state, authority, or evidence; a file deletion cannot be justified as authorized. Interface: Execution and audit.
* Utility induced drift: Task success improves by weakening constraints treated as soft costs; a failing test is deleted before reporting success. Interface: Optimization and adaptation.

3 Why Existing Mechanisms Are Necessary but Insufficient
Existing agent safety mechanisms are necessary, but they usually control local units of safety: a final response, a tool call, a workflow node, a delegation token, or a reward signal. The missing layer is Constraint State Governance: constraints represented as execution state, carried across delegation, checked before critical actions, recorded for audit, and supplied to learning.

4 Paradigm Design
4.1 Constraint State Governance
CSG makes safety critical constraints explicit state objects rather than conversational reminders. The system does not rely on agents to remember a rule. It gives each rule an identity, version, scope, predicate, and audit trail.
A constraint is first converted into a signed token: ρk = SignG(k, H(ck), predk, scopek, priorityk, ttlk, νk).
At time t, the governance layer maintains state variables including active token set, role and authority map, remaining budgets, labels/taints, revocations, state version, and audit root.
The admission algorithm (CSG admission for a governance critical action) checks freshness, capabilities, scopes, information flows, rule predicates, and audit evidence before allowing an action. A realized action requires all checks to pass, and commits to the action, capability, evidence, digest, decision, and reason in a tamper-evident audit root.

4.2 Constraint Native Reinforcement Learning
CSG can block unsafe critical actions, but blocking alone does not make agents useful. Constraint native learning uses CSG to define the comparison set itself. Mandatory constraints define the space in which utility is optimized; they are not terms that a better final answer can compensate for. A trajectory that breaks freshness, scope, information flow, or auditability is not a low quality success; it is outside the comparison set.

4.3 Closed Loop Coupling
CSG does not sit outside learning as a safety wrapper. It changes the object that learning sees. A rollout is no longer just model outputs and rewards; it is a governed trajectory whose proposals, admission decisions, rejected actions, realized actions, and audit events are tied to signed state. Learning receives a verifiable record of which constraints were preserved. Governance defines the admissible boundary; learning searches for useful behavior inside it; violation evidence improves both.

5 Empirical Case Study
AgentLeak replay shows output only filtering leaves 68.8% internal exposure, while CSG Lite reduces it to 5.7% by checking transitions. Offline policy search shows Strict CSG is admissible but over-redacts, while Balanced CSG maintains constraints and preserves utility.

6 Alternative Views and Objections
- Some constraints can't be formalized cleanly: CSG asks for operational forms only for critical actions (scopes, taints, etc.) and allows escalation.
- Constraints conflict: CSG makes trade-offs explicit rather than letting agents silently trade safety for utility.
- Rigidity: CSG should govern critical transitions (file edits, external disclosure), not every local token (proportional control).
- Overclaiming: CSG is not an end-to-end proof, but it ensures constraints are inherited, checked, violated, repaired, and audited across trajectories instead of being quietly worn down.
