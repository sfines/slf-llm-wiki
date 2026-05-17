*Response size: ~26K tokens. Consider using zotero_semantic_search to find specific content instead of reading full papers.*

# SHIELDA: Structured Handling of Exceptions in LLM-Driven Agentic Workflows

**Type:** preprint

**Item Key:** PG9NBFGF

**Date:** 2025-08-11

**Authors:** Zhou, Jingwen; Chen, Jieshan; Lu, Qinghua; Zhao, Dehai; Zhu, Liming

**DOI:** 10.48550/arXiv.2508.07935

**URL:** http://arxiv.org/abs/2508.07935



## Extra

arXiv:2508.07935 [cs]

**Tags:** `Computer Science - Software Engineering`



## Abstract

Large Language Model (LLM) agentic systems are software systems powered by LLMs that autonomously reason, plan, and execute multi-step workflows to achieve human goals, rather than merely executing predefined steps. During execution, these workflows frequently encounter exceptions. Existing exception handling solutions often treat exceptions superficially, failing to trace execution-phase exceptions to their reasoning-phase root causes. Furthermore, their recovery logic is brittle, lacking structured escalation pathways when initial attempts fail. To tackle these challenges, we first present a comprehensive taxonomy of 36 exception types across 12 agent artifacts. Building on this, we propose SHIELDA (Structured Handling of Exceptions in LLM-Driven Agentic Workflows), a modular runtime exception handling framework for LLM agentic workflows. SHIELDA uses an exception classifier to select a predefined exception handling pattern from a handling pattern registry. These patterns are then executed via a structured handling executor, comprising local handling, flow control, and state recovery, to enable phase-aware recovery by linking exceptions to their root causes and facilitating composable strategies. We validate SHIELDA's effectiveness through a case study on the AutoPR agent, demonstrating effective, cross-phase recovery from a reasoning-induced exception.

**Collections:** 1 collections

**Notes/Attachments:** 2

---

## Full Text

5
2
0
2

g
u
A
1
1

]
E
S
.
s
c
[

1
v
5
3
9
7
0
.
8
0
5
2
:
v
i
X
r
a

SHIELDA: STRUCTURED HANDLING OF EXCEPTIONS IN
LLM-DRIVEN AGENTIC WORKFLOWS

Jingwen Zhou
CSIRO’s Data61
Melbourne, Victoria, Australia
helen.zhou@data61.csiro.au

Jieshan Chen
CSIRO’s Data61
Sydney, New South Wales, Australia
jieshan.chen@data61.csiro.au

Qinghua Lu
CSIRO’s Data61
University of New South Wales
Sydney, New South Wales, Australia
qinghua.lu@data61.csiro.au

Dehai Zhao
CSIRO’s Data61
Sydney, New South Wales, Australia
dehai.zhao@data61.csiro.au

Liming Zhu
CSIRO’s Data61
University of New South Wales
Sydney, New South Wales, Australia
liming.zhu@data61.csiro.au

August 12, 2025

ABSTRACT

Large Language Model (LLM) agentic systems are software systems powered by LLMs that au-
tonomously reason, plan, and execute multi-step workflows to achieve human goals, rather than
merely executing predefined steps. During execution, these workflows frequently encounter ex-
ceptions. Existing exception handling solutions often treat exceptions superficially, failing to trace
execution-phase exceptions to their reasoning-phase root causes. Furthermore, their recovery logic is
brittle, lacking structured escalation pathways when initial attempts fail. To tackle these challenges,
we first present a comprehensive taxonomy of 36 exception types across 12 agent artifacts. Building
on this, we propose SHIELDA (Structured HandlIng of Exceptions in LLM-Driven Agentic Work-
flows), a modular runtime exception handling framework for LLM agentic workflows. SHIELDA
uses an exception classifier to select a predefined exception handling pattern from a handling pattern
registry. These patterns are then executed via a structured handling executor, comprising local han-
dling, flow control, and state recovery, to enable phase-aware recovery by linking exceptions to their
root causes and facilitate composable strategies. We validate SHIELDA’s effectiveness through a case
study on the AutoPR agent, demonstrating effective, cross-phase recovery from a reasoning-induced
exception.

1

Introduction

The landscape of artificial intelligence (AI) is being reshaped by the rise of LLM-based agentic systems, which are
software systems powered by LLMs that autonomously reason, plan and execute multi-step workflows to achieve human
goals, rather than merely executing predefined steps. During execution, these workflows frequently encounter exceptions
which may propagate across different workflow phases. For instance, flawed reasoning logic, or hallucinated steps
during planning can cascade into execution failures [1]. Similarly, inconsistencies like overconfidence in hallucinated
information or conflicting goals due to ambiguous task definitions can significantly derail an agent’s decision-making
[2]. The execution phase concurrently presents its own set of hurdles. Dynamic tool invocation, where agents actively
call external tools’ APIs, frequently results in failures like API timeouts or cross-agent coordination issues [3]. The
inherent iterative loop between these two core phases further demands continuous monitoring to prevent cascading
failures across cycles. While existing works have addressed specific exception types within these phases [4, 5], the
current understanding of exceptions in agentic workflows remains fragmented and isolated, lacking a comprehensive

A PREPRINT - AUGUST 12, 2025

characterization of their scope and distribution. This highlights a critical need for a systematic understanding of the
unique exceptions in agentic workflows.

The inherent dynamism of agentic workflows presents a fundamental challenge to conventional exception handling
paradigms. Traditionally, exception handling in software systems has been rooted in deterministic, linear processes,
proving inadequate for the unpredictable nature of autonomous agents [6]. For instance, static mechanisms like try-catch
blocks are simply not equipped to deeply probe an agent’s intricate decision-making during the reasoning/planning phase
or to adapt to the fluid complexities of dynamic tool invocation and multi-agent coordination during execution [5, 7].
While the community has seen efforts to mitigate specific LLM-related exceptions, such as hallucination detection,
these approaches often remain isolated. They typically fall short of offering a unified framework for comprehensive
exception management that spans diverse agent modalities and workflow phases. Furthermore, the challenge extends
beyond runtime handling to post-hoc analysis; recent work highlights that the process of failure attribution—identifying
which agent and at which step a task failure originates—remains a complex, labor-intensive, and largely underexplored
problem [8]. Our analysis reveals two critical and pervasive gaps in current solutions: a notable absence of phase-aware,
modality-generalized exception handling and lack of support for structured escalation pathways. Addressing these
profound shortcomings thus necessitates a systematic approach to organizing an effective exception handling mechanism
and developing a truly unified framework.

To address these challenges, we conducted a systematic analysis of real-world agentic workflow exceptions. Our
observations revealed that exceptions often stem from two distinct sources: 1) the agent’s internal reasoning and planning
processes; and 2) its execution actions. This insight, coupled with the cyclical nature of agentic workflows, guided
our categorization of exceptions into Reasoning/Planning and Execution phases, providing a structured framework to
disentangle their interconnected effects. Building upon this foundation, we propose SHIELDA (Structured HandlIng
of Exceptions in LLM-Driven Agentic Workflows), a novel, modular runtime framework designed to systematically
detect, classify, and handle these critical exceptions. This study is guided by three core research questions: What types
of exceptions occur in agentic workflows, and how are they distributed across agentic workflow phases? What exception
handling mechanisms have been proposed for LLM-based agentic systems, and how can they be systematically
organized into a structured module of exception handling mechanisms? How effective is the proposed exception
handling framework in recovering from agentic workflow exceptions at runtime?

Generally, we make the following contributions:

• A Comprehensive Exception Taxonomy: Grounded in a systematic literature review of 55 studies, we
construct a fine-grained taxonomy of 36 exception types across 12 agent artifacts. This taxonomy distinguishes
exceptions across reasoning, planning, and execution phases, revealing two critical gaps in existing solutions:
a lack of phase-aware handling and limited support for structured escalation.

• A Structured Exception Handling Approach: We define a structured, triadic design for exception handling
that organizes existing mechanisms into three orthogonal dimensions: local handling, flow control, and state
recovery. This composable design serves as the foundation for creating reusable handler patterns within our
SHIELDA framework.

• The SHIELDA Framework: We propose SHIELDA, a modular runtime framework that leverages our

taxonomy and structured handling approach.

• Empirical Validation: We provide an in-depth case study of the AutoPR agent to demonstrate SHIELDA’s

effectiveness. Our results reveal that SHIELDA can successfully handle the cross-phase exceptions.

2 Methodology

This section describes the methodology used to investigate exception types and handling mechanisms in agentic
workflows. Our process includes five stages: (1) defining research questions, (2) conducting a systematic literature
review (SLR), including screening, quality assessment, and data synthesis, (3) developing an exception taxonomy, (4)
mapping existing handling strategies, and (5) using these insights to inform framework design. Figure 1 illustrates the
process of our systematic literature review (SLR), which forms the empirical foundation of our methodology.

2.1 Research Questions and Scope

To guide our study, we formulated four research questions:

• RQ1: What types of exceptions occur in agentic workflows, and how are they distributed across agentic

workflow phases?

2

A PREPRINT - AUGUST 12, 2025

This question aims to characterize the exceptions that disrupt agentic workflows. Answering it requires the
construction of a phase-aware taxonomy of exceptions grounded in real-world agent interactions, which forms
the foundation for our subsequent analysis.

• RQ2: What exception handling mechanisms have been proposed for LLM-based agentic systems, and how

can they be systematically organized into a structured model?
This question seeks to move beyond ad-hoc mechanisms by systematically deconstructing existing handling
mechanisms.

• RQ3: How can a framework based on our structured model be designed to handle real-world exceptions, and

how effective is it at recovering from agentic workflow exceptions?
This final, two-part question guides the design and validation of our SHIELDA framework. First, we propose a
modular architecture that operationalizes the triadic model from RQ2. Second, we demonstrate its practical
effectiveness through a case study, evaluating its ability to resolve a complex, cross-phase exception at runtime.

2.2 Systematic Literature Review (SLR)

To answer RQ1 and RQ2, we conducted a systematic literature review following standard software engineering practices.
Our goal was to capture both exception types and the mechanisms used to handle them in the context of agentic
workflows. We initiated the SLR with a structured keyword-based search across major academic databases including
IEEE Xplore, ACM Digital Library, SpringerLink, and Google Scholar. To ensure comprehensive coverage, keywords
were grouped into five semantic categories:

• Core Concepts: LLM agent workflow, agentic workflow, agentic system, exception handling, error handling,

failure management

• Reasoning/Planning Errors: reasoning exceptions, hallucination in LLMs, conflicting goals, ambiguous task

definitions, reasoning trace validation

• Execution Failures: tool invocation failures, API failures, cross-agent coordination, server selection in

workflows, MCP server crashes

• Workflow Structures: agentic workflows, multi-agent systems, workflow management, iterative workflows,

cyclical workflows

• AI/SE Context: AI agent exceptions, software engineering exception handling, fault tolerance in AI systems

Keyword search, manual search, and snowballing: Boolean combinations (e.g., “LLM agent” AND “exception
handling” AND “tool failure”) yielded 1521 initial studies. To ensure domain relevance and improve coverage, we
manually reviewed proceedings from top-tier venues. Forward and backward snowballing from anchor papers added
240 studies, resulting in 1761 candidates.

Inclusion and Exclusion Criteria: We defined filtering rules to ensure conceptual alignment and technical quality.

• Inclusion:

– Papers published in the last 10 years in English.
– Peer-reviewed studies or high-quality preprints (assessed by authors) with demonstrable rigor.
– Studies on exceptions, recovery, or failure handling in LLM agents or multi-agent systems.
– Work discussing reasoning/planning errors (e.g., hallucination, faulty logic) or execution-level failures

(e.g., tool crashes, coordination failures).

• Exclusion:

– Work focused solely on LLM training or tuning, without runtime workflow concerns.
– General SE papers without relevance to LLMs, agents, or workflows.
– Abstract-only papers, vision pieces, or articles without empirical evidence.
– Failures unrelated to agent logic (e.g., hardware crashes or network layer issues).

After filtering, 60 papers were retained.

Screening and Quality Assessment: We conducted a two-stage assessment. First, titles and abstracts were reviewed
by two researchers for relevance, with discrepancies resolved via discussion. Second, full texts were assessed on a
5-point scale covering methodological clarity, empirical grounding, and relevance. A score of 3 or above was required
for inclusion. This retained 55 high-quality papers.

3

A PREPRINT - AUGUST 12, 2025

Figure 1: Overview of the systematic literature review (SLR) process forming the core of our methodology.

Data Extraction and Synthesis: For each selected study, we extracted publication metadata (Title, Author, Year,
Source, Topic, etc.), related exception types, associated workflow phases, and exception handling mechanisms or
strategies (1). All entries were compiled into a structured evidence matrix aligned to our research questions. Synthesis
revealed two major phases where exceptions typically occur:

• Reasoning and Planning (RP) phase refers to the stage where the agent analyzes its input, formulates goals,
interprets context, and generates a task plan or decision strategy. These exceptions reflect cognitive-level
breakdowns in the agent’s internal decision-making process before it acts on the world.

• Execution (E) phase encompasses the stage where the agent operationalizes its plan by invoking tools, calling
APIs, generating outputs, or interacting with UIs and other systems. These exceptions represent operational
breakdowns that occur during the execution of decisions or interaction with external components.

This phase-oriented structure served as the foundation for the exception taxonomy (Table 1) and informed the modular
design of the SHIELDA framework introduced in Section 3.

3 Exception Categorization and Handling Strategies

This section addresses the first two research questions (RQ1 and RQ2) by constructing a taxonomy of exceptions
in agentic workflows and analyzing the effectiveness of existing handling strategies. To answer RQ1, we identified
and summarized 36 exception artifacts from the systematic literature review, covering exceptions across the reason-
ing/planning and execution phases. To address RQ2, we evaluate the limitations of current strategies, highlighting gaps
in phase coverage, composability, and escalation support.

Table 1: A Taxonomy of Exceptions in Agentic Workflow Phases and Artifacts.

Artifacts

Detailed Exceptions

Phases

Artifacts

Detailed Exceptions

Phases

Goal

Context

Reasoning

Planning

Memory

Knowledge Base

Model

Ambiguous Goal [9]
Conflicting Goal [10]

Context Corruption [11]
Context Ambiguity [9]

Contradictory Reasoning [12]
Circular or Invalid Reasoning [13]

Faulty Task Structuring [14]
Overextended Planning

Memory Poisoning [15]
Outdated Memory [16]
Misaligned Memory Recall [17]

Hallucinated Facts [18]
Knowledge Base Poisoning [19]
Knowledge Conflict [20]

Token Limit Exceeded [21]
Output Validation Failure [22]
Output Handling Exception [22]

RP
RP

RP
RP

RP
RP

RP
RP

RP/E
RP/E
RP/E

RP/E
RP/E
RP/E

RP/E
E
E

Tool

Interface

Task Flow

Other Agent

Tool Invocation Exception [14]
Tool Output Exception [23]
Unavailable Tool [14]

API Invocation Exception [24]
API Response Malformation [23]
API Semantic Mismatch [25]
UI Element Misclick [26]
Text Recognition Error [23]
UI Not Ready [27]
Environmental Noise [26]

Task Dependency Exception [28]
Error Propagation [23]
Stopping Too Early [28]

Missing Information [28]
Communication Exception [28]
Agent Conflict [28]
Role Violation [28]

External System

Protocol Mismatch [5]
External Attack [19]

E
E
E

RP/E
RP/E
E
E
E
E
E

E
E
RP/E

E
E
E
E

E
E

3.1 A Taxonomy of Agentic Workflow Exceptions (RQ1)

As shown in Table 1, the taxonomy contains three key pieces of information:

• Artifacts: The underlying source or object of failure (e.g., Goal, Memory, Tool). Our classification of
exceptions by artifacts is grounded in widely adopted agent architectures [29, 30], which decompose agents

1https://github.com/submissionpurposeonly/dataextraction

4

A PREPRINT - AUGUST 12, 2025

into modular components such as context engineering, memory, reasoning, planning, execution, and external
interaction modules. Each artifact maps to a distinct component in this architecture and reflects a concrete
point of exception in agent pipelines.

• Detailed Exceptions: A semantically distinct and recurring exception mode for each artifact, extracted from

the literature.

• Phases: The stage where the exception typically arises—“RP” for reasoning and planning, “E” for execution,

or “RP/E” if spanning both.

In total, we identified 36 exceptions from 12 artifacts from the literature. Each exception represents a concrete and
recurring exception mode in agentic workflows.

3.1.1 Ambiguous Goal

Ambiguous Goal refers to failures in correctly inferring the user’s intent due to vague, underspecified, or contextually
incomplete instructions. This often arises in naturalistic interactions where users provide high-level feedback—such as
preferences, frustrations, or meta-comments—without specifying the underlying objective or target operation. Such
goal ambiguity introduces uncertainty during the reasoning and planning phase: agents may generate internally coherent
but misaligned plans, diverging from what users actually intended. The exception is not due to an execution error, but a
gap between human intention articulation and agent interpretation capabilities. For example, in a music tutoring agent
scenario, users often say "this is too slow" without clarifying whether they refer to playback speed, learning pace, or
segment timing. The agent cannot proceed safely without resolving this ambiguity [9].

Handling strategies include proactive clarification of vague expressions, pedagogical reframing of user feedback,
turn-based goal alignment, subgoal decomposition, adaptive user modeling, and system-level reasoning over available
configurations [9].

3.1.2 Conflicting Goal

Conflicting Goal refers to user requests that contain multiple incompatible objectives (e.g., minimizing cost while
maximizing speed), without a clear preference or prioritization. Such conflicts increase ambiguity during the planning
phase. Guan et al. [10] address this by decomposing instructions into abstract and concrete layers. For example, in
the request “book a cheap and fast ticket”, the agent first generates high-level plans, then resolves trade-offs during
fine-grained action generation. Consistency checks ensure that the final plan aligns with the overall user intent. This
layered strategy reduces execution failure under ambiguous prioritization.

3.1.3 Context Corruption

Context Corruption occurs when residual or injected prompt content from earlier steps contaminates the current
reasoning context, leading to misaligned or unintended agent behavior. This often emerges in iterative or multi-agent
workflows where prompt content is reused without isolation. Zhan et al. [11] demonstrate that malicious instructions
embedded earlier (e.g., “skip all safety checks”) can silently propagate across steps. Lee et al. [31] further show how
such contamination can self-replicate across agents via Prompt Infection, resulting in task hijacking, misinformation,
or data exfiltration, which are precisely the types of malicious side-tasks evaluated in sabotage benchmarks like
SHADE-Arena [32].

To mitigate this, prior work proposes echo validation, where agents reflect key prompts before acting [11]; memory
slot isolation, which separates untrusted inputs from core logic [11]; and LLM Tagging, which marks agent-generated
content to prevent downstream misinterpretation [31].

3.1.4 Context Ambiguity

Context Ambiguity refers to failures in resolving references to entities or actions within the interface or prior history,
where the user’s goal is clear but the specific object or target is under-specified. This typically arises when expressions
like “this one” or “that button” are used in environments with multiple plausible referents, leading the agent to select
the wrong element or apply an action incorrectly. [9] evaluate LLM agents on UI-centric tasks where utterances such
as “click this button” fail due to the presence of multiple candidate elements and a lack of structured context. In such
cases, the agent understands that the user wants to click something, but cannot disambiguate which target is intended.
This differs from goal ambiguity, as the user’s objective (e.g., clicking) is known—but the agent cannot resolve which
entity to apply it to. This contrasts with ambiguous goals, where the agent is unsure what the user wants to achieve. In
context ambiguity, the intention is evident (e.g., “click something”), but **the referent is not** [9].

5

A PREPRINT - AUGUST 12, 2025

Handling strategies include structured task state injection, visual context anchoring, memory-based reference resolution,
and proactive referent clarification to resolve pointing ambiguity.

3.1.5 Contradictory Reasoning

Contradictory Reasoning refers to cases where the agent produces internally inconsistent logic chains [12]—e.g.,
asserting both a claim and its negation across reasoning steps or turns. These inconsistencies undermine the validity
of downstream actions and user trust. Sun et al. [12] offer a comprehensive classification of distorted information in
AI-generated content, where they identify ’Contradiction’ as a significant subtype of ’Logic errors’. Contradictions
occur when the AI model, such as ChatGPT, generates logically inconsistent statements, for instance, by asserting
a proposition and its negation simultaneously or presenting mutually exclusive claims within its output. The model
produces responses that contradict its earlier statements without any new information being introduced, thereby failing
to maintain internal logical consistency. This type of error can manifest in both single-turn responses and extended
multi-turn interactions.

Handling strategies discussed in prior work include contradiction-aware re-ranking [12], which penalizes logical flips
and step-wise logic validation mechanisms to detect conflicting premises before execution.

3.1.6 Circular or Invalid Reasoning

This exception occurs when an agent’s reasoning process either loops back to prior assumptions without introducing
new evidence (circular), or proceeds through logically flawed steps that compromise the integrity of the reasoning chain
(invalid). Such failures result in reasoning stagnation, hallucinated conclusions, or planning deadlocks. Yao et al. [13]
identify this failure mode in their ReAct framework, observing that agents employing naive recursive reasoning often
enter cyclical loops—e.g., repeatedly querying the same information or re-deriving previously established conclusions
without forward progress. Sun et al. [12] further classify “Spatial” and “Psychological” reasoning failures as subtypes
of invalid reasoning. These errors manifest when intermediate steps fail to form coherent transitions from premises to
conclusions, breaking logical consistency.

To address these issues, several handling strategies have been proposed: graph-based validation of reasoning traces to
ensure structural soundness, cycle detection mechanisms to prune repetitive logic paths [13], and heuristic reasoning
checkpoints that interrupt recursive loops lacking novel informational gain [12]. Agent-R introduces an iterative
self-training framework that enables agents to reflect on and recover from erroneous trajectories, specifically helping
them to escape from local loops and explore more effective actions [33].

3.1.7 Faulty Task Structuring

Faulty Task Structuring refers to failures in decomposing a task into a logically consistent and constraint-compliant
sequence of subtasks. This occurs when agents omit required steps, misorder dependencies, or ignore global constraints
such as temporal duration or location alignment [34]. Such structural issues undermine overall plan feasibility: even if
individual actions appear locally valid, the resulting plan may violate critical preconditions or constraints. These failures
often surface in multi-step tasks where execution success depends on proper inter-step relationships. For example, in
the TravelPlanner benchmark [14], one agent selects an accommodation requiring a three-night minimum stay, despite
planning only a two-night trip. Another plans a morning flight out of a city but continues scheduling local activities
afterward, revealing misordered subtask logic.

Handling strategies for this exception include forward-checking heuristics to anticipate constraint violations, backtrack-
ing mechanisms to revise invalid decompositions, and structural validation methods such as graph-based consistency
checks or constraint rule enforcement before execution.

3.1.8 Overextended Planning

Overextended Planning refers to agent behaviors where task plans become unnecessarily long, repetitive, or low-yield.
This typically arises when the agent expands a task into an excessive number of fine-grained actions or redundantly
revisits prior steps without adding new value. Such over-specification increases execution time, consumes tool resources,
and may cause agent stalling or failure due to quota limits, timeouts, or downstream rejection. Unlike structural errors,
these plans may be logically valid but inefficient or impractical to carry out.

Handling strategies for this exception focus on plan simplification and efficiency, such as pruning redundant steps,
enforcing constraints on plan length, or using a reflective loop for the agent to refine and shorten its own verbose plan.

6

A PREPRINT - AUGUST 12, 2025

3.1.9 Memory Poisoning

This exception mode occurs when an agent’s memory artifact, such as long-term storage or retrievable demonstration
history, retains misleading, invalid, or malicious content that later disrupts decision-making. Poisoned memory
entries may originate from user miscommunication, failed task traces, hallucinated outputs, or adversarial injection.
Authors [35] describe how noisy or unchecked memory writing—such as logging failed plans or tool errors without
filtration—can degrade agent behavior across sessions. Improper memory management, particularly lacking abstraction
or reflection, increases the risk of persistent contamination. Complementing this, Chen et al. [15] demonstrate how
adversarially crafted memory entries can be stealthily triggered to manipulate agent outputs. For example, a driving
agent retrieves poisoned demonstrations and generates an unsafe ’SUDDEN STOP’ plan in response to a benign user
instruction. The tangible impact of such vulnerabilities is now being systematically evaluated in benchmarks like
SHADE-Arena, where agents are prompted with malicious side-tasks, sourced from data poisoning, to test their capacity
for sabotage [32].

Handling such memory-level corruption typically involves controlling memory write operations, summarizing or
abstracting noisy histories, and identifying anomalous entries through trigger-aware filtering or state rollback when
contamination is detected.

3.1.10 Outdated Memory

This exception occurs when an agent retrieves memory entries that were once valid but have become outdated due to
changes in the task, environment, or user state. Common sources include obsolete tool outputs, expired user preferences,
or past persona contexts. Such stale memory can degrade reasoning quality and introduce subtle context corruption.
Authors [16] describe cases where agents retain episodic traces of resolved discussions (e.g., “the Earth is flat”), which
later resurface and contradict the agent’s semantic memory, leading to incoherent or logically inconsistent responses.

To address this, common strategies include segregating memory by type to prevent cross-layer interference, applying
forgetting mechanisms to decay low-utility or time-sensitive memory traces, and anchoring memory summaries with
temporal metadata to preserve chronological alignment.

3.1.11 Misaligned Memory Recall

This exception occurs when an agent retrieves and reuses memory entries that are lexically or embedding-wise similar
to the current input, but originate from tasks with incompatible goals, structures, or contextual assumptions. The
retrieved memory is not incorrect or outdated in itself, but it is applied out of context, resulting in ill-suited or incoherent
behavior. This typically arises in retrieval-augmented agents that select memory purely based on similarity scores,
without adequate constraints on task or intent alignment. Unlike "Stale Memory", which involves obsolete or expired
content, or "Poisoned Memory", which stems from incorrect or adversarial entries, misaligned memory is internally
valid but externally misleading. The impact is often subtle but compounding: agents may follow irrelevant procedures,
reuse outdated reasoning chains, or produce semantically disconnected outputs despite surface-level fluency.

Xiong et al. [36] characterize this issue as "misaligned experience replay", showing that in tasks like AgentDriver and
EHRAgent, memory entries with high input similarity but diverging intent significantly degrade agent performance.
For instance, an agent tasked with urban navigation erroneously reused memory from a simulation-only driving task,
leading to safety violations. Salama et al. [17] similarly observe that embedding-based retrieval often surfaces top-k
entries that are superficially relevant but task-inappropriate; their MemInsight framework addresses this by enforcing
task-aligned memory filtering.

To mitigate this failure mode, proposed strategies include: attribute-based filtering to constrain memory retrieval by task
scope [17], combined deletion strategies that remove frequently misaligned memories based on output-effectiveness
metrics [36], and selective memory writing to prevent structurally divergent traces from entering the memory store.

3.1.12 Hallucinated Facts

This exception occurs when an agent produces factual statements that are not supported by the knowledge base, even
though the correct information exists. These errors typically result from mislinked entities, flawed query construction,
or misunderstanding of schema constraints—not from missing data. The agent appears confident, but its outputs
conflict with available facts. Zong et al. [18] describe a case where the agent is asked to list Argentine films but returns
unrelated media like documentaries and sports clips. The fault lies in a SPARQL query missing a type constraint,
causing incorrect retrieval from otherwise valid data. This illustrates how factual hallucination can arise from misusing
structured knowledge rather than inventing information.

7

A PREPRINT - AUGUST 12, 2025

To mitigate this class of errors, recent systems propose: schema-constrained generation to enforce output validity with
respect to KB structure [37], multi-agent role separation to decouple generation, discrimination, and verification [18],
and multi-form factual verification combining structured and unstructured sources to detect unsupported claims [38].

3.1.13 Knowledge Base Poisoning

This exception occurs when faulty, outdated, or adversarial content is inserted into internal or external knowledge
stores. Agents that rely on these contaminated entries may produce factually incorrect outputs, reinforce bias, or
make unsafe decisions—despite otherwise functioning correctly. Unlike hallucinations arising from model reasoning,
poisoning targets the data layer, silently corrupting the foundation of factual retrieval or knowledge-grounded planning.
Microsoft [19] reports cases where fabricated peer feedback in HR systems leads agents to generate unfair performance
reviews. Chen et al. [15] further demonstrate that adversarial prompts embedded in RAG-indexed documents can
propagate into agent responses, circumventing traditional prompt-level defenses.

To mitigate such exceptions, systems may adopt: "write-access control and input sanitization" to restrict who can
edit the KB and to strip potentially malicious structures before indexing, "trust scoring and provenance tracking" to
assign reliability scores to knowledge entries and record their origin, "adversarial pattern detection" to identify injected
commands, misinformation, or manipulative phrasing, and "rollback-to-checkpoint recovery" to restore the KB to a
verified prior state after detecting contamination.

3.1.14 Knowledge Conflict

This exception arises when an agent is exposed to multiple knowledge sources—such as parametric memory, retrieved
documents, or tool outputs—that provide mutually inconsistent facts. Unlike hallucinated facts, which are fabricated
without a factual basis, or knowledge base poisoning, which stems from corrupted data, knowledge conflicts occur
when all sources appear valid individually, yet collectively contradict one another. An example case is presented in [20],
where an agent is asked, “Who has won the most FIFA World Cup championships?” The model recalls “Brazil” from
its internal knowledge, but retrieved sources provide conflicting answers such as “Argentina,” “Italy,” and “Germany.”
Although each response originates from a seemingly credible document, the agent lacks a mechanism to resolve the
inconsistency, and may produce an unreliable or amalgamated output.

To mitigate this exception, recent work explores: "disentangled answering", where the agent separates memory-based
and context-based outputs [20]; "source-aware prompting", which guides the model to prioritize certain knowledge
sources; "cross-source consistency checking", which compares retrieved and internal facts to detect contradictions;
"knowledge-aware fine-tuning", which introduces conflicting examples during training to improve resolution ability;
and "temporal fact disambiguation", which helps select the most up-to-date answer among competing sources.

3.1.15 Token Limit Exceeded

This exception arises when the prompt or conversation context exceeds the LLM’s maximum token capacity [39]. As a
result, the model silently truncates early content, removing instructions, safety checks, or key dependencies, which
leads to degraded or unsafe behavior. Authors [40] observe that in multi-agent deliberation settings, the number of
token-consuming inputs grows rapidly with discussion rounds. Once the prompt length exceeds the model’s context
window, key viewpoints and earlier instructions are silently dropped. This results in agents responding with repetitive,
inconsistent, or goal-divergent outputs due to incomplete awareness of peer contributions.

Handling strategies include: segmenting long prompts into smaller sub-units or discussion groups [40], resetting
conversation history at round boundaries to constrain token growth, and implementing signal-aware truncation or
scoring heuristics to prioritize retention of high-importance content [22].

3.1.16 Output Validation Failure

The agent generates syntactically malformed or structurally unsafe outputs—such as invalid JSON, unmatched brackets,
or unescaped characters—that downstream systems cannot parse or safely execute. This breaks API pipelines or
introduces security risks. OWASP [22] highlight common violations including improper string escapes and unsafe code
generation in web environments.

Handling strategies include enforcing strict output schemas (e.g., using JSONSchema or XML validators), inserting
sanitization checkpoints before tool handoff, and using logic constraints within the generation process to filter out
structurally invalid completions.

8

A PREPRINT - AUGUST 12, 2025

3.1.17 Output Handling Exception

This exception arises when an agent produces outputs that are structurally invalid, insecure, or improperly encoded for
downstream systems. Failures range from malformed JSON or unmatched brackets to injection-prone strings, unsafe
code generation, or context-insensitive content rendering. These outputs may break API execution, cause parsing
errors, or open injection surfaces. The OWASP LLM Top 10 [22] highlights that improper output handling can lead
to vulnerabilities such as XSS, SQL injection, or remote code execution when agents emit unvalidated JavaScript,
shell commands, or file paths directly to user-facing or backend components. In several attack scenarios, LLMs return
executable or interpretable payloads—such as unsanitized Markdown, SQL, or template strings—that trigger security
failures when executed or rendered.

To mitigate this exception, systems implement: output schema validation to ensure structural compliance, context-aware
encoding depending on execution environments (e.g., HTML, SQL), sanitization checkpoints between model output
and system invocation, and content shape constraints using lightweight logic filtering, static analysis, or format guards.

3.1.18 Tool Invocation Exception

This exception arises when an agent incorrectly plans or formats a tool invocation, often due to semantic mismatch,
hallucinated components, interface misuse, or unavailability of the invoked tool. Failures manifest as invoking the
wrong tool, supplying malformed or nonsensical parameters, selecting non-existent APIs, or calling valid tools that
fail to respond due to timeout or service-level unavailability. Unlike execution or output errors, these failures typically
originate during the planning or invocation phase and can silently degrade task performance.

ToolFuzz [25] describes cases where agents misuse APIs—e.g., calling arXiv search tools for restaurant queries—due
to vague or misleading documentation. Dr.Fix [41] reports incorrect substitutions of functionally incompatible APIs,
such as replacing vector operations with scalar math functions. AVATAR [34] shows that agents often fail to decompose
user queries into aligned tool inputs, leading to ineffective attribute matching or zero-score outputs. TALLM [39]
highlights hallucinated tool names that closely resemble valid ones but break invocation, and AutoTools [42] identifies
malformed arguments such as unauthorized field injection or type mismatches. ToolFuzz further includes examples of
tools crashing or failing to respond at runtime, despite valid invocations.

Handling strategies include schema-constrained tool wrappers, argument validation during execution, prompt-time
enforcement of input formats, and contrastive prompt optimization. Systems such as AVATAR and ToolFuzz further
incorporate example-based learning and runtime verification to proactively surface invocation errors before execution.

3.1.19 Tool Output Exception

This exception arises when a tool is successfully invoked and responds without runtime errors, but the output it returns
is structurally malformed, semantically incorrect, or misleading. These failures can be difficult to detect, as the tool
appears to function normally but produces outputs that violate the intended task logic. Such exceptions undermine
agent reliability and can propagate through multi-step workflows. For example, Tools Fail [23] demonstrates a “broken
calculator” tool that returns incorrect arithmetic results (e.g., 25 → 205) without signaling failure. In another case, a
vision module misclassifies a tomato as an apple, causing downstream reasoning errors [23]. ToolFuzz [25] similarly
reports correctness failures, such as an API that returns “no grocery stores” for known populated areas, or retrieving
2024 publications when 2020 was requested, due to flawed query serialization.

Effective handling strategies include response schema validation, semantic constraint checks, and oracle-based output
verification. Some systems use LLMs themselves to cross-check tool results for internal consistency or plausibility.

3.1.20 Unavailable Tool

This exception arises when external tools (e.g., APIs, databases, plugins) are unavailable due to service downtime,
network errors, or usage rate limits. The agent cannot proceed, causing degraded or stalled workflows. Xie et al. [14]
document real-world failures where agent plans break due to transient outages or quota exhaustion of third-party APIs.

Handling strategies include retry mechanisms with exponential backoff, dynamic endpoint switching when redundant
services are available, and graceful fallback paths (e.g., partial plan execution or user notification) to maintain workflow
continuity.

3.1.21 API Invocation Exception

This exception arises when an LLM agent initiates an API-based tool interaction that fails due to incorrect invocation
semantics, missing parameters, hallucinated endpoints, or unreachable services. Unlike tool-level failures internal to

9

A PREPRINT - AUGUST 12, 2025

the component, API invocation exceptions reflect errors at the interaction interface between the agent and the external
system. These issues often manifest as early-stage execution failures, aborted responses, or logically invalid results
despite syntactically correct requests.

For instance, LogiAgent [24] reports a case where a photo upload API accepts an invalid URL parameter and returns
a 200 OK response without proper validation. Although the call succeeds structurally, it fails semantically due to an
improper invocation format. Similarly, [41] identifies hallucinated APIs (e.g., setCubic()) and missing required
arguments (e.g., appContext), both leading to runtime failures in otherwise compilable code.

Handling strategies include retry mechanisms with exponential backoff to tolerate transient call failures [43], logging
and avoiding logically invalid call patterns through execution memory [24], and validating results with business-logic
oracles instead of status codes. Additionally, prompt-time tool schema grounding and automated plan repair [41] have
been shown to reduce invocation misuse in LLM-generated code paths.

3.1.22 API Response Malformation

This exception occurs when an agent receives a structured response that violates the expected schema, despite a
successful API call. Malformations include missing fields, type mismatches, incorrect nesting, or semantically
misleading values that break downstream parsing or cause silent logic errors.

For example, Tools Fail [23] reports error cascades caused by structurally plausible but incorrect outputs from object
detectors, such as mislabeling a tomato as an apple—leading to invalid planning steps. Although syntactically valid, the
outputs fail to meet the agent’s structural and semantic expectations. Similarly, LogiAgent [24] emphasizes schema-
aligned validation as a prerequisite for safely processing API responses, especially when business logic constraints are
involved.

Handling strategies include schema-based response verification, fallback decoding for partial recovery, and structured
prompting techniques—such as checklist-style validation and accept/reject gating—to help agents assess output integrity
before use.

3.1.23 API Semantic Mismatch

This exception occurs when an API returns a response that is structurally valid but semantically misaligned with the
agent’s intent. Such mismatches arise when tools interpret requests too broadly, ignore key constraints, or fulfill them in
unexpected ways—resulting in misleading or off-target outputs that are difficult to detect via syntax alone.

Authors [25] documents a case where a PubMed search tool, queried for “papers from 2020,” returns 2024 publications
due to a misinterpreted date filter. Similarly, Dr.Fix [41] reports cases where LLMs select syntactically correct
but semantically mismatched APIs—such as using np.abs to compute vector magnitude, instead of the correct
vx.magnitude function.

Handling strategies include oracle-based plausibility checks, synonym-prompt consistency testing, and prompt-level
constraint reinforcement [25]. When semantic errors are detected, agent repair routines may revise tool choices or
regenerate inputs using usage-aligned prompting [41].

3.1.24 UI Element Misclick

This exception occurs when the agent selects a visually incorrect interface element, such as a neighboring or semantically
similar button, despite the correct element being present. It typically results from visual ambiguity, layout crowding, or
inaccurate spatial grounding in image-based UI models.

In [26], GPT-4V agents repeatedly misclick UI components due to coordinate misalignment. For instance, in a Chrome-
based shopping task, the agent was instructed to navigate to a product category image but mistakenly clicked a “favorite”
icon located nearby, breaking the task flow and preventing recovery. Similarly, WindowsAgentArena [27] highlights
failures where overlapping interface elements and ambiguous visual context led agents to trigger incorrect controls.

Handling strategies include bounding-box-based UI grounding (e.g., Set-of-Marks), filtering invalid targets via accessi-
bility metadata, and using region anchors to disambiguate spatially similar elements.

3.1.25 Text Recognition Error

This exception occurs when the agent fails to correctly extract or interpret UI text due to OCR failures. These errors
are typically triggered by low-resolution screenshots, font artifacts, or visual noise, and can cause incorrect element
targeting, label misunderstanding, or logic errors in task execution.

10

A PREPRINT - AUGUST 12, 2025

OSAgentBench [23] explicitly identifies OCR-based failures in image-based tool workflows. Their taxonomy includes
text recognition errors caused by blurry or noisy input images, which lead to parsing mistakes and propagate into
downstream decision failures.

Handling strategies include OCR model tuning for low-contrast inputs, multi-pass recognition with adaptive pre-
processing, and fallback recovery based on layout priors or context-anchored language models [23].

3.1.26 UI Not Ready

This exception arises when the agent attempts to interact with UI components that are not yet fully rendered, loaded,
or interactive. Common causes include asynchronous rendering, layout transitions, and delayed element activation.
Premature actions in such states result in ignored commands, misfires, or interaction with placeholder elements.

WindowsAgentArena [27] introduces a dedicated “WAIT” execution state to handle loading screens, rendering delays,
and in-progress downloads. Agents are instructed to pause until the interface becomes actionable, acknowledging that
early actions during these transient states can lead to execution failures or no-ops.

Handling strategies include wait-state injection before triggering UI events, probing for interactivity using accessibility
flags or DOM readiness signals, and fallback retry logic when no response is received. These mechanisms ensure that
actions are issued only when the target UI elements are fully available and responsive.

3.1.27 Environmental Noise

This exception refers to agent failures caused by external visual changes that alter the spatial or perceptual structure of
the interface. Such disturbances include screen resolution shifts, window repositioning, and display scaling. These
variations affect layout stability, contrast, or boundary visibility, often leading to mislocalization or failure to detect
actionable UI elements.

OSWorld [26] demonstrates that multimodal agents suffer substantial accuracy degradation—up to 60%—when
superficial UI properties like window size or anchor position are altered. In particular, tasks involving minimal window
size or offset screen anchors cause agents to fail spatial grounding and misinterpret element location, despite the layout
being functionally equivalent.

Handling strategies include resolution-aware template modeling, anchor-based UI localization (using relative rather
than absolute positioning), and environment-aware calibration routines that normalize layout shifts and adjust for visual
variations at runtime.

While this exception may overlap visually with Text Recognition Errors (e.g., both can be triggered by dark mode), the
failure mechanism differs. Environmental Noise affects element positioning and visibility at the layout level, whereas
Text Recognition Errors stem from character-level misreading under distorted rendering.

3.1.28 Task Dependency Exception

This exception arises when a downstream task fails or behaves incorrectly due to missing, delayed, or improperly
propagated outputs from an upstream task. In multi-agent or multi-stage systems, such dependencies are often implicit,
and a breakdown in information flow can silently compromise task correctness.

Authors [28] document a representative failure, where the Phone Agent discovers that an API expects a phone number as
the login username, but fails to relay this information to the Supervisor Agent. Consequently, the Supervisor repeatedly
submits incorrect credentials, resulting in persistent authentication failures. This illustrates a critical breakdown in
task-to-task dependency propagation, where downstream logic silently proceeds under outdated assumptions.

Mitigation strategies include enforcing explicit state propagation between tasks, validating upstream completion before
downstream execution, and prompting fallbacks when expected context is absent.

3.1.29 Error Propagation

This exception arises when an error in an upstream module or early-stage task step is not detected or corrected, allowing
it to propagate through the workflow and cause cascading failures. Unlike isolated mistakes, these errors accumulate or
compound, resulting in degraded task performance that cannot be easily recovered downstream.

Authors [23] present such a case in a multimodal agent task, where a visual detector misclassifies a tomato as an
apple. This upstream error misguides the action planner, triggering incorrect task execution without triggering an

11

A PREPRINT - AUGUST 12, 2025

explicit failure signal. Similarly, OSWorld [26] shows that agents frequently repeat faulty actions after early-stage
failures—such as missing a UI element—without updating their internal state, leading to persistent task collapse.

Handling strategies: Insert validation checkpoints after critical sub-tasks to detect early failures. Use memory snap-
shots or intermediate feedback signals to verify success before proceeding. Equip agents with retry limits, rollback
mechanisms, or confidence-based re-evaluation triggers to prevent blind repetition of earlier mistakes.

3.1.30 Stopping Too Early

This exception occurs when an agent terminates a task before all logically required steps have been executed, despite
the absence of explicit failure. Unlike classical planning failures or task verification errors, this exception stems from
premature judgment based on partial success signals, local heuristics, or shallow outcome checks. It often leads to
under-completion, partial outputs, or non-executable results downstream.

[28] introduces a case where a multi-agent system generates a design artifact and prematurely halts, incorrectly
assuming task completion. The downstream agents—responsible for implementation or validation—are never invoked,
leading to underperformance.

Handling strategies: Effective mitigation starts with defining explicit completion criteria that align with full task goals,
not just local outputs. Agents should verify termination conditions against global state or memory checkpoints, rather
than relying on isolated step success. Downstream modules can issue validation signals or expected follow-up prompts,
ensuring upstream agents do not halt prematurely. Structural verification—such as checking the completeness of outputs
or the usage of all expected tools—can serve as an additional safeguard. When task completion is ambiguous, agents
should defer termination, attempt re-evaluation, or escalate to a supervisory controller.

3.1.31 Missing Information

This exception occurs when an agent holds task-relevant information, such as format requirements, prior outcomes, or
internal state, but fails to explicitly share it with another agent. The downstream agent, unaware of the missing content,
proceeds with incomplete context, often leading to incoherent actions or task failure.

Study [28] presents such a case in Figure 5 (FM-2.4), where the Phone Agent discovers that an API expects a phone
number as the login username but does not relay this to the Supervisor Agent. As a result, the Supervisor repeatedly
submits incorrect credentials, leading to failed login attempts. The Supervisor further fails to request clarification,
exacerbating the communication gap and cementing the error.

Handling strategies include explicit inter-agent state propagation, structured message protocols that surface internal
assumptions, memory synchronization layers between collaborative agents, and fallback prompting when expected task
context is missing.

3.1.32 Communication Exception

This exception arises when an agent receives a message from another agent but fails to incorporate, respond to, or
correctly act on it. Unlike missing information, here the message was delivered but deliberately or inadvertently ignored,
breaking collaboration and causing divergence in shared tasks.

Study [28] describes a peer-review scenario where one agent is presented with a correct solution by another, acknowl-
edges it, but proceeds independently without integrating it. This results in conflicting outputs and a failed review
pipeline.

To mitigate such failures, MAST suggests standardizing inter-agent communication protocols, incorporating confirma-
tion and contradiction checks, and applying selective communication architectures such as graph attention or message
gating. These ensure agents do not ignore valid peer inputs and maintain coherent multi-agent task execution.

3.1.33 Agent Conflict

This exception occurs when agents execute conflicting or redundant actions due to unsynchronized planning or
misaligned intentions. Unlike communication exceptions where inputs are ignored, here the agents act on diverging
plans—leading to interference, rollback, or inconsistent system states.

Study [28] documents reasoning-action mismatches, where agents construct a valid plan but deviate in execution, often
stepping on each other’s tasks. The Whitepaper [19] further highlights cases of agent impersonation and action abuse,
where injected agents override legitimate behaviors, disrupting expected workflows.

12

A PREPRINT - AUGUST 12, 2025

Handling strategies include centralized plan verification, agent-to-agent intent sharing, gated execution pipelines, and
consistency checks between planned reasoning and performed actions. These mitigate exceptions by ensuring agent
behaviors remain coordinated and causally consistent.

3.1.34 Role Violation

This exception occurs when an agent performs actions outside of its designated role, either by assuming responsibilities
intended for others or by failing to act within its assigned boundaries. Unlike coordination failures, role violations
reflect a breach of internal specifications about agent duties and behavior scope.

[28] describes a case where the Navigator agent proposes a solution internally but does not communicate it to the
Planner, who then takes unrelated actions, causing workflow misalignment. The Whitepaper [19] also presents a
scenario where an agent impersonates a user without clarification, leading to unintended disclosure and execution
breakdown.

Handling strategies include explicit role encoding in system prompts, role-verification layers, inter-agent boundary
enforcement, and training agents with role-conditioned reinforcement learning to promote adherence to functional
partitions.

3.1.35 Protocol Mismatch

This exception arises when the agent invokes an external system using outdated, incompatible, or misaligned protocol
specifications. Unlike invocation failures originating from within the agent’s planner, protocol mismatches stem from
schema evolution, deprecated fields, changed authentication flows, or version divergence of external services. These
inconsistencies result in invocation rejection, degraded functionality, or unexpected output, even when the invocation
format appears valid.

Authors [5] document security and stability challenges in the Model Context Protocol (MCP) ecosystem, where
developers unintentionally deploy outdated or misconfigured MCP servers, triggering version incompatibilities. Such
cases involve invocation failures due to privilege persistence, tool name drift, or configuration mismatch between client
and server. These issues emerge not from agent misuse but from evolution in the external system itself.

Effective handling strategies include strict version control and signature verification of external tool packages, semantic
validation of tool capabilities prior to invocation, and runtime schema compatibility checks. The use of centralized
registries, cryptographic signing, and reproducible build pipelines can proactively mitigate protocol divergence and
preserve invocation reliability in dynamic environments.

3.1.36 External Attack

This exception arises when an agent is compromised by adversarial content originating from external systems—such
as poisoned memory entries, deceptive tool metadata, or crafted prompt injections delivered via APIs or third-party
services. Unlike protocol mismatches, these attacks are malicious by design and intended to hijack the agent’s behavior.

The Whitepaper [19] presents a memory poisoning case where an adversary inserts a crafted instruction into the agent’s
semantic memory via a disguised email, instructing the agent to forward all sensitive emails to an external address.
Similarly, [5] shows that malicious tool descriptions such as “this tool should be prioritized” can mislead agents
into invoking adversarial tools. Another attack vector involves cross-domain prompt injection, where instructions
are embedded in RAG documents, causing the agent to execute hidden commands upon retrieval. SHADE-Arena
provides a comprehensive benchmark that measures the ability of frontier LLM agents to execute such attacks while
actively evading AI-based monitoring [32]. Although prompt injection can also appear in context corruption, the
distinction lies in the source and intent: context corruption stems from internal contamination (e.g., prompt reuse or
agent self-propagation), whereas external attacks originate from adversarial inputs intentionally designed to hijack the
agent [31, 19].

Effective handling strategies include semantic validation of retrieved data and tool descriptions, authenticated memory
updates, prompt filtering layers to strip executable payloads, tool metadata verification, and runtime behavior auditing.
Secure agent frameworks should enforce explicit execution constraints and anomaly detection mechanisms to mitigate
the impact of adversarially manipulated inputs.

13

A PREPRINT - AUGUST 12, 2025

Figure 2: SHIELDA: An Architectural Framework for Exception Handling in LLM Agents

4 The SHIELDA Framework

Existing exception handling approaches for agentic workflows are often ineffective, suffering from two critical
limitations: they are phase-disjoint, failing to trace execution symptoms to their reasoning root causes, and non-
composable, lacking structured recovery paths when initial attempts fail. This section presents the SHIELDA framework,
which implements a structured, runtime-compatible approach to exception handling in LLM-driven agentic workflows.
As shown in Figure 2. The SHIELDA framework is designed to integrate directly into an LLM-based agentic system
and comprises the following key components:

4.1 System Architecture

• Exception Classifier: Identifies the exception type, agent workflow phase, and the affected artifact.
• Handler Pattern Registry: Maintains a library of pre-defined handler patterns, each specified using
SHIELDA’s triadic model—Local Handling, Flow Control, and State Recovery. Patterns are indexed by
exception type and provide executable recovery blueprints (e.g., pattern P018 for tool invocation exceptions).
• Handling Executor: Orchestrates the execution of the selected handler pattern. It sequentially applies the
local handling tactic (e.g., retry, escalate), evaluates flow-level decisions (e.g., continue, skip), and performs
state recovery actions (e.g., rollback memory or clean context). The executor also tracks recovery success or
failure across phases.

• Escalation Controller: Manages escalation pathways for unrecoverable exceptions. SHIELDA supports
escalation at two distinct levels: (i) as an intentional local mechanism embedded within specific handler
patterns (e.g., Escalate to Human, Escalate to Peer Agent), and (ii) as a fallback mechanism invoked by the
Handling Executor when all recovery strategies fail. The Escalation Controller routes control to external
handlers such as human supervisors, peer agents, or predefined backup modules, enabling safe termination or
delegation.

• AgentOps Infrastructure: Provides monitoring, logging, and evaluation support across the workflow.

The key to the framework’s composability, executed by the Handling Executor, lies in the design of the handler patterns
stored within the Registry. Each pattern is constructed from a triadic combination of mechanisms, a concept adapted
from foundational work in workflow management [44]. This approach organizes all exception handling actions into
three orthogonal, runtime-oriented dimensions: how the immediate operation is handled (Local Handling), how the
overall process flow is controlled (Flow Control), and how the agent’s state is recovered (State Recovery). By combining

14

A PREPRINT - AUGUST 12, 2025

one mechanism from each dimension, a complete and reusable handler pattern is formed, enabling a composable
approach to exception handling. These dimensions and their constituent mechanisms are detailed in Table 2, Table 3,
and Table 4:

• Local Handling: Immediate, atomic actions taken to mitigate an exception at the operation level—such as

retrying a failed tool call, switching APIs, rephrasing prompts, or invoking clarification. See Table 2.

• Flow Control: Determine how the agent proceeds after a local handler executes. These strategies govern the
continuation of the current execution thread, including whether to resume, skip the failed step, or abort the
task entirely (Table 3).

• State Recovery: Specify how the agent’s internal or external state should be repaired after exception handling.

Recovery may include rolling back prior states or compensating for the exception side effects (Table 4).

These three dimensions of mechanisms form a design space for exception handling. By combining one mechanism from
each dimension, a complete, end-to-end handler pattern is formed. Based on this triadic structure, we have enumerated
48 distinct handler patterns that constitute a comprehensive solution space for the SHIELDA framework, each assigned
a unique Pattern ID (see Table 5). While this set is representative rather than exhaustive, Table 6 showcases a selection
of these patterns, mapping key exception types to the exception handler patterns.

4.2 A Foundational Runtime Example

We now illustrate the SHIELDA runtime process using the representative Tool.InvocationException type, with
the execution flow depicted in Figure 3. This example is triggered when an agent’s Execution Module fails to
invoke a tool. As the workflow begins, the Exception Classifier first identifies and categorizes the exception.
It then consults the Handler Pattern Registry to retrieve the corresponding exception handler pattern. For a
Tool.InvocationException, the registry fetches pattern P018, which specifies "Retry with Backoff" as its local
handling mechanism. This pattern is then passed to the Handling Executor, which applies the simple retry action.

The outcome of this execution determines the next step. If the retry attempt succeeds, the workflow continues as
normal. If it fails again, the Escalation Controller is invoked to manage the exception, for instance, by escalating
to a human. Throughout this entire sequence, all decisions—from the initial classification to the final outcome—are
logged by the AgentOps Infrastructure for downstream traceability. This example demonstrates the framework’s
fundamental capability to systematically classify an exception, retrieve a predefined pattern, and execute a structured
exception handling process.

The runtime example above illustrates the practical value of SHIELDA’s core design philosophy. Its value lies not
merely in structured exception handling, but in enabling developers to reason about exception handling as a composable
design space. Rather than treating the "Retry with Backoff" as an ad-hoc reaction embedded in workflow logic,
SHIELDA exposes it as an interchangeable pattern (P018). In applying the framework to our taxonomy, we found that
many exception types—such as Memory Poisoning or UI alignment issues—shared similar exception handling
mechanisms. For example, both Memory Poisoning and Tool Output Exception benefit from rollback-style
exception handling mechanisms, while Context Ambiguity and Contradictory Reasoning often resolve through
clarification. This demonstrates that modeling handlers abstractly as patterns is more efficient and scalable than tightly
coupling them to the workflow.

5 Evaluation

To answer RQ3, we conduct a case study on a representative LLM-based agent "AutoPR" to demonstrate the effectiveness
of our SHIELDA framework in handling multi-stage exceptions at runtime.

5.1 Case Study Design

5.1.1 Case Study Subject Selection

To evaluate our SHIELDA framework in a realistic setting, we selected a case study subject based on several key
criteria. The project needed to align with a software engineering context and embody a clear agentic workflow of
reasoning, planning, and execution. AutoPR, an open-source agent for automating GitHub Pull Request tasks, was an
ideal candidate as it meets these requirements.

15

A PREPRINT - AUGUST 12, 2025

Figure 3: Runtime exception handling flow in SHIELDA, illustrated using the Tool.InvocationException case.
The agent classifies the exception, retrieves the corresponding pattern (P018), and applies a retry-based local strategy.
If recovery fails, the process escalates to an external controller. All decisions and outcomes are logged by AgentOps
for downstream traceability.

5.1.2 Scenario Definition and Data Collection

To rigorously evaluate SHIELDA’s multi-stage recovery capabilities, we designed a scenario that intentionally induces a
complex, cross-phase exception. Unlike a simple tool hallucination, this scenario is crafted to induce a more subtle and
complex exception, where the agent, in its reasoning phase, formulates a logically plausible but operationally prohibited
plan. The goal is to test the framework’s entire multi-stage recovery process, from handling the initial execution-level
exception to diagnosing its root cause in the agent’s reasoning phase.

The scenario is initiated via a natural language prompt in a GitHub issue, instructing the agent to perform a high-level
task that implies a change in automation logic. The prompt used is as follows: "This is an important change. Please
add the user @nonexistent-user-for-testing-12345 as a reviewer to this pull request to ensure quality. After that, please
modify the README.md to state that a review has been requested." The key to this prompt is the ambiguous, high-level
goal of "add the user... as a reviewer." While a simple approach would be to mention the user, a more sophisticated
(and in this case, flawed) reasoning path is to modify the CI/CD workflow itself to automate the assignment. We
hypothesize that the agent will adopt this latter path, leading to a permission error during execution when it attempts to
push modifications to its own workflow file, which is protected by the hosting platform’s security policies.

To analyze this entire process, we collect data from three primary sources. First, the raw GitHub Actions console
logs provide a complete trace of the workflow execution. Second, and most importantly, our SHIELDA framework’s
AgentOps Infrastructure component is simulated through manual analysis of these logs, capturing detailed
information on exception classification, pattern matching, and recovery decisions. This structured log file is collected at
the end of each run. Third, we qualitatively observe the comments and pull requests posted by the AutoPR agent, which
serve as external evidence of the agent’s state and final success or failure.

5.2 Execution Trace and Analysis

The following trace details the AutoPR agent’s workflow, demonstrating SHIELDA’s end-to-end recovery process.

16

A PREPRINT - AUGUST 12, 2025

5.2.1 Phase 1: Initial Execution Exception and Local Handling

The workflow begins as designed, with the agent ingesting the prompt from the GitHub issue. It successfully formulates
a multi-commit plan which, unbeknownst to the agent, contains a prohibited action. The exception is raised at the
end of the execution phase, when the agent attempts to push its local commits, including the modification to its own
workflow file, to the remote repository. This action is rejected by the external system (GitHub), resulting in a runtime
exception. SHIELDA’s Exception Classifier immediately catches this runtime exception. Based on the output
from the underlying Git command, it is initially classified as an execution-phase Exception, which we categorize as
ProtocolMismatchException. The critical evidence from the failed run’s log is shown in Figure 4.

Figure 4: The initial ProtocolMismatchException caught by SHIELDA during the Execution phase. The exception
message explicitly states the lack of ’workflows’ permission.

Following the SHIELDA framework, a simple local handling pattern (e.g., P018:
Retry with Backoff) is first
attempted by the Handling Executor. However, all retry attempts would fail identically. This exhaustion of the local
handling strategy signals that a deeper diagnosis is required, triggering the next phase of the SHIELDA process.

5.2.2 Phase 2: Escalation and Cross-Phase Root Cause Analysis

When local handling fails, the process escalates to the Escalation Controller for a deeper, automated diagno-
sis. Employing a backward-chaining analysis of the AgentOps logs, the controller begins its investigation at the
point of exception—the rejected git push command. It extracts the key entity from the error message, the file path
.github/workflows/autopr.yml, and traces this artifact back through the workflow’s history. This trace leads directly to
the source of the exception in the planning phase logs: the original commit plan generated, which explicitly targeted the
forbidden file (Figure 5).

Figure 5: The root cause of the exception, identified by SHIELDA. The agent’s plan, generated during the Reasoning
phase, explicitly contains the prohibited action.

The Escalation Controller correctly re-classifies the problem. The root cause is not a faulty "git push" command,
but a Faulty Task Structuring exception, where the agent created a plan that violates fundamental system constraints.

17

A PREPRINT - AUGUST 12, 2025

5.2.3 Phase 3: Plan Repair and Controlled Recovery

With the true root cause identified as a Faulty Task Structuring exception, SHIELDA’s Handler Pattern
Registry maps this exception to a handler pattern: P012. The Handler Executor then orchestrates the execution of
this pattern’s triadic mechanisms in a logical sequence to achieve a full recovery.

The recovery process begins with the Plan Repair mechanism. To repair the flawed plan, SHIELDA’s first action is
to formulate a new, corrective directive for the Reasoning Module. It constructs a new prompt that includes both the
original user goal and the new, explicit system constraint discovered during root cause analysis ("You are explicitly
forbidden from modifying workflow files..."). This new prompt, shown in Figure 6, is designed to force the agent to
generate a completely new, safe, and compliant plan. The agent’s Reasoning Module, upon receiving this corrected
input, successfully generates a new plan that avoids the prohibited action. The Abort mechanism is executed. Crucially,
this does not terminate the agent’s entire mission. Instead, it aborts the current, flawed execution thread that was
operating on the faulty plan. This action gracefully stops any further operations based on the bad plan and clears the
execution context, paving the way for a new, clean execution thread to begin based on the corrected plan obtained in the
Plan Repair step. Finally, the P012 pattern specifies a No-op (no operation) for state recovery. This is appropriate in
this specific scenario because the failed git push command did not alter the state of the external system (the remote
repository). While the agent’s local workspace contains unpushed, faulty commits, they will be superseded by the
new execution path. Thus, no complex compensation or external state rollback is required. As shown in Figure 7.
Guided by the new corrective directive generated during the Plan Repair step, the agent formulates a safe, alternative
plan. It then successfully executes this new plan, creating a valid pull request that fulfills the original user goal without
violating system constraints. This result serves as evidence that the SHIELDA-guided P012 handler pattern is effective
in correcting this class of reasoning-based failures.

Figure 6: The corrective prompt generated by SHIELDA’s Plan Repair mechanism, which is then used to simulate
the recovery run.

5.3 Discussion

The successful resolution of the above case study provides compelling evidence supporting our primary research
question (RQ3) concerning SHIELDA’s runtime effectiveness. The execution trace detailed in Section 5.2 moves
beyond a simple pass/fail metric, offering a nuanced view into the unique capabilities of our proposed exception
handling framework. The findings highlight three critical aspects of the SHIELDA framework that address pervasive
gaps in current exception handling approaches for LLM agents.

5.3.1 Multi-stage, Phase-Aware Recovery

This case study’s primary finding is the validation of SHIELDA’s ability to perform multi-stage, phase-aware recovery.
The initial manifestation of failure was an ExternalSystemPermissionException, caught during the Execution
phase. A conventional, phase-disjoint handler would likely classify this as a non-recoverable infrastructure exception
and terminate, as the immediate cause lies outside the agent’s direct control. The true novelty of SHIELDA is showcased
in its subsequent actions. After routine local handling (i.e., retry) fails, the Escalation Controller correctly infers
that the symptom’s origin may lie upstream. It successfully traces the exception back to a completely different domain
and phase: a Faulty Task Structuring exception within the agent’s Reasoning/Planning phase. This ability to
causally link a low-level system interaction exception to a high-level strategic planning flaw is a significant advancement.
It demonstrates a holistic workflow understanding that is essential for resolving the complex, cascading exceptions
common in autonomous agent systems.

5.3.2 The Critical Role of Runtime Log Analysis

The cross-phase exception handling would be impossible without treating logging data as a first-class runtime resource.
Our case study illustrates that logs are not just for human debugging but are machine-readable inputs for the SHIELDA

18

A PREPRINT - AUGUST 12, 2025

Figure 7: The final successful outcome after SHIELDA-guided recovery. The agent has successfully completed the task
by following the new, safe plan.

framework itself. The Escalation Controller leverages these structured logs to perform an automated trace,
connecting key entities from a failed execution step (like a file path) back to the original plan object. This ability to turn
logs into actionable intelligence is what enables SHIELDA to perform precise, automated root cause analysis.

5.3.3 Closed-Loop Recovery via Constrained Re-planning

Finally, this case study showcases SHIELDA’s ability to perform exception handling in agentic workflow. After
identifying the root cause, the framework does not simply terminate the workflow. Instead, the selected handler pattern
(P012) leverages its Plan Repair capability. By injecting the system constraint back into the agent’s context via a
corrected prompt, SHIELDA fundamentally alters the problem space for the next reasoning cycle. This forces the
agent to discard its initial, flawed plan and generate a new, safe alternative that respects the environment’s permission
boundaries. This complete "diagnose-repair-re-execute" cycle, where the framework actively corrects the agent’s
operational assumptions, presents a far more sophisticated and resilient paradigm than the linear, often terminal logic of
traditional try-catch blocks, paving the way for more dependable agentic automation.

6 Threats to Validity

While our case study demonstrates the effectiveness of the SHIELDA framework’s core recovery loop, we acknowledge
several potential threats to the validity of our findings that warrant discussion.

6.1 Construct Validity

The primary threat to construct validity lies in our exception classification taxonomy. The framework’s effectiveness is
predicated on the Exception Classifier’s ability to map a runtime exception to one of the 36 predefined types in
our taxonomy. The ExternalSystemPermissionException encountered in this case study, while fitting best under
the Protocol Mismatch category, highlights that any real-world taxonomy may not be exhaustive. This underscores
the necessity for the taxonomy to be an extensible, living artifact. While our framework is designed to support this,

19

A PREPRINT - AUGUST 12, 2025

its performance on entirely novel or un-catalogued exception types that it cannot classify remains an open area for
evaluation. A failure in this initial classification step could prevent the correct handler pattern from being invoked,
thus undermining the entire recovery process. However, we have mitigated this threat by grounding our taxonomy
in a systematic review to maximize its comprehensiveness. Furthermore, SHIELDA’s architecture anticipates this
contingency, as an unclassifiable exception can be routed to the Escalation Controller for fallback handling,
which is a pathway for future work.

6.2

Internal Validity

A threat to internal validity stems from the engineered nature of the exception scenario. While the final case study
was an authentic exception mode emerging from the agent’s interaction with a real-world external system, the initial
prompt was deliberately crafted to be ambiguous. This was designed to increase the likelihood that the agent would
formulate the specific flawed plan we intended to study. This controlled approach allows for a reproducible evaluation
of SHIELDA’s recovery logic, but it may not fully represent the stochastic nature of reasoning exceptions that might
occur from more benign user prompts. Future work should therefore involve a broader empirical study on naturally
occurring exceptions to validate SHIELDA’s effectiveness in more stochastic, real-world settings.

6.3 External Validity

The primary threat to external validity is the generalizability of our findings from a single case study. While the
SHIELDA framework itself is designed to be general-purpose, its evaluation in this paper is based on one agent and
one specific exception pathway. The framework’s performance on other types of agent architectures (e.g., multi-agent
systems, agents with different toolsets) remains an open question for future work. Furthermore, another significant
limitation is that the current implementation of the Handler Pattern Registry is static. It relies on pre-defined
mappings from exception types to handling patterns. The framework does not currently feature "dynamic learning" to
adapt or generate new handling strategies based on past outcomes. This may limit its effectiveness in novel situations
where pre-defined patterns are suboptimal, a challenge that points toward future research in adaptive exception handling
for LLM agents. We consider this static design as a necessary first step and a key direction for future work is to use the
logged data from our framework to enable SHIELDA to learn and dynamically select the best handling pattern for a
given exception.

7 Related Work

7.1 Exception Handling in Traditional Software Engineering and Automation

Exception handling is a cornerstone of robust software engineering, with well-established techniques designed for
deterministic, linear workflows. For decades, mechanisms such as try-catch blocks, system-level checkpointing,
and manual failovers have served as the standard toolkit for addressing predictable errors like file access failures or
network timeouts [45, 46]. In early AI, rule-based expert systems handled exceptions by targeting predefined conditions
with static recovery actions, such as invoking a default rule or prompting for user intervention [47]. This rule-based
philosophy’s modern heir is Robotic Process Automation (RPA), which deploys digital workers that diligently follow
hard-coded scripts. The core weakness of this paradigm is its brittleness: these agents stumble at the slightest deviation
from their prescribed path, such as a button changing location on a screen or a form field being renamed [48]. As a
result, the promise of RPA is often undermined by high initial setup costs, unreliable execution, and the burdensome
need for constant human oversight and maintenance [48]. Ultimately, both traditional methods and RPA systems are
anchored in an assumption of deterministic exception modes. This foundation proves inadequate for the stochastic,
dynamic, and semantically rich nature of agentic workflows.

7.2 Characterizing Exceptions in Agentic Workflows

The shift towards LLM-based agentic systems introduces a new spectrum of exceptions that go beyond traditional
software errors. Research has begun to identify and categorize these failure modes, though often in a fragmented
manner. A primary area of focus has been on the intrinsic limitations of the models themselves. This includes exceptions
arising from flawed reasoning, such as producing contradictory logic [12], getting stuck in circular reasoning loops
[13], or generating factually incorrect statements, commonly known as hallucination [18]. When an agent acts upon
such flawed reasoning, it inevitably leads to downstream execution failures. Another critical failure point is action
validity and grounding. Studies have highlighted numerous execution-phase exceptions, including Tool Invocation
Exception where an agent misuses an external tool [14, 25, 41], and UI Element Misclick where it fails to interact with

20

A PREPRINT - AUGUST 12, 2025

the correct graphical interface element [26, 27]. Furthermore, research on improving exception handling within code
itself has identified failures in the development process, such as "Insensitive Detection of Fragile Code" and "Inaccurate
Capture of Exception Types" [49]. While these studies provide valuable insights into specific types of failures, a holistic
understanding has been lacking.

7.3 Recovery and Mitigation Strategies for LLM Agents

In response to these newly identified exceptions, a variety of recovery and mitigation strategies have begun to emerge
in the literature. Several efforts have focused on building specialized frameworks to tackle exceptions within narrow,
high-stakes domains. For instance, RCAgent deploys autonomous agents with dedicated tools to perform Root Cause
Analysis in complex cloud environments [50]. In the mobile domain, LLMPA automates multi-step app interactions
and uses a “Controllable Calibration” module to validate predicted actions before execution [10]. Other approaches
target the exception-handling process itself. HEALER, for example, proposes a dynamic self-healing system where an
LLM generates and executes recovery code at runtime [51], while SEEKER employs a multi-agent system to statically
analyze and repair flawed exception handling logic in source code [49]. Concurrently, other research explores more
fundamental techniques for agent resilience. A prominent theme is agent evolution through self-improvement, which
includes methods like self-reflection, where an agent verbally reinforces its learning from task feedback [52, 53], and
leveraging multi-agent conversations for collaborative error correction [54, 55]. While this body of work offers a rich
set of recovery methods, they often exist as isolated techniques or are deeply embedded within monolithic, specialized
systems. A unified, modular, and runtime-oriented framework that systematically organizes these strategies has been
absent. Our work addresses these by shifting the focus from individual recovery strategies to a systematic, architectural
approach for managing them.

8 Conclusion

This paper addresses the critical challenge of managing diverse and unpredictable exceptions in LLM-based agentic
workflows. We advocate for a shift from ad-hoc error mitigation to a more principled, engineering-based discipline
for the systematic management of agent exceptions. First, we constructed a comprehensive taxonomy of 36 distinct
exception types spanning both the reasoning, planning, and execution phases of agentic workflows. Second, building
on this taxonomy, we designed and implemented SHIELDA, a composable, phase-aware runtime framework. Future
work will proceed along two primary avenues: extending the framework to address complex multi-agent coordination
exceptions, and integrating adaptive policy learning to dynamically optimize the selection of handling patterns.

References

[1] Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, and Mehrdad Farajtabar.
Gsm-symbolic: Understanding the limitations of mathematical reasoning in large language models. arXiv preprint
arXiv:2410.05229, 2024.

[2] Miao Xiong, Zhiyuan Hu, Xinyang Lu, Yifei Li, Jie Fu, Junxian He, and Bryan Hooi. Can llms express their
uncertainty? an empirical evaluation of confidence elicitation in llms. arXiv preprint arXiv:2306.13063, 2023.

[3] Jingqing Ruan, Yihong Chen, Bin Zhang, Zhiwei Xu, Tianpeng Bao, Hangyu Mao, Ziyue Li, Xingyu Zeng, Rui
Zhao, et al. Tptu: Task planning and tool usage of large language model-based ai agents. In NeurIPS 2023
Foundation Models for Decision Making Workshop, 2023.

[4] Qiguang Chen, Libo Qin, Jinhao Liu, Dengyun Peng, Jiannan Guan, Peng Wang, Mengkang Hu, Yuhang Zhou,
Te Gao, and Wangxiang Che. Towards reasoning era: A survey of long chain-of-thought for reasoning large
language models. arXiv preprint arXiv:2503.09567, 2025.

[5] Xinyi Hou, Yanjie Zhao, Shenao Wang, and Haoyu Wang. Model context protocol (mcp): Landscape, security

threats, and future research directions. arXiv preprint arXiv:2503.23278, 2025.

[6] Haolin Jin, Linghan Huang, Haipeng Cai, Jun Yan, Bo Li, and Huaming Chen. From llms to llm-based agents for
software engineering: A survey of current, challenges and future. arXiv preprint arXiv:2408.02479, 2024.

[7] Chuyi Kong, Ziyang Luo, Hongzhan Lin, Zhiyuan Fan, Yaxin Fan, Yuxi Sun, and Jing Ma. Sharp: Unlocking

interactive hallucination via stance transfer in role-playing agents, 2024.

[8] Shaokun Zhang, Ming Yin, Jieyu Zhang, Jiale Liu, Zhiguang Han, Jingyang Zhang, Beibin Li, Chi Wang,
Huazheng Wang, Yiran Chen, et al. Which agent causes task failures and when? on automated failure attribution
of llm multi-agent systems. arXiv preprint arXiv:2505.00212, 2025.

21

A PREPRINT - AUGUST 12, 2025

[9] Daniel Chin, Yuxuan Wang, and Gus Xia. Human-centered llm-agent user interface: A position paper. arXiv

preprint arXiv:2405.13050, 2024.

[10] Yanchu Guan, Dong Wang, Zhixuan Chu, Shiyu Wang, Feiyue Ni, Ruihua Song, and Chenyi Zhuang. Intelligent
agents with llm-based process automation. In Proceedings of the 30th ACM SIGKDD Conference on Knowledge
Discovery and Data Mining, pages 5018–5027, 2024.

[11] Qiusi Zhan, Zhixiang Liang, Zifan Ying, and Daniel Kang. Injecagent: Benchmarking indirect prompt injections

in tool-integrated large language model agents. arXiv preprint arXiv:2403.02691, 2024.

[12] Yujie Sun, Dongfang Sheng, Zihan Zhou, and Yifei Wu. Ai hallucination: towards a comprehensive classification of
distorted information in artificial intelligence-generated content. Humanities and Social Sciences Communications,
11(1):1–14, 2024.

[13] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React:
Synergizing reasoning and acting in language models. In International Conference on Learning Representations
(ICLR), 2023.

[14] Jian Xie, Kai Zhang, Jiangjie Chen, Tinghui Zhu, Renze Lou, Yuandong Tian, Yanghua Xiao, and Yu Su.
Travelplanner: A benchmark for real-world planning with language agents. arXiv preprint arXiv:2402.01622,
2024.

[15] Zhaorun Chen, Zhen Xiang, Chaowei Xiao, Dawn Song, and Bo Li. Agentpoison: Red-teaming llm agents via
poisoning memory or knowledge bases. Advances in Neural Information Processing Systems, 37:130185–130213,
2025.

[16] Kostas Hatalis, Despina Christou, Joshua Myers, Steven Jones, Keith Lambert, Adam Amos-Binks, Zohreh
Dannenhauer, and Dustin Dannenhauer. Memory matters: The need to improve long-term memory in llm-agents.
In Proceedings of the AAAI Symposium Series, volume 2, pages 277–280, 2023.

[17] Rana Salama, Jason Cai, Michelle Yuan, Anna Currey, Monica Sunkara, Yi Zhang, and Yassine Benajiba.

Meminsight: Autonomous memory augmentation for llm agents, 2025.

[18] Chang Zong, Yuchen Yan, Weiming Lu, Jian Shao, Eliot Huang, Heng Chang, and Yueting Zhuang. Triad: A
framework leveraging a multi-role llm-based agent to solve knowledge base question answering. arXiv preprint
arXiv:2402.14320, 2024.

[19] Microsoft AI Red Team.

in
new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/, April 2025.
cessed: 2025-05-09.

failure modes
the
https://www.microsoft.com/en-us/security/blog/2025/04/24/
Ac-

New whitepaper

taxonomy

outlines

agents.

of

ai

[20] Rongwu Xu, Zehan Qi, Zhijiang Guo, Cunxiang Wang, Hongru Wang, Yue Zhang, and Wei Xu. Knowledge

conflicts for llms: A survey. arXiv preprint arXiv:2403.08319, 2024.

[21] Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang.
Lost in the middle: How language models use long contexts. Transactions of the Association for Computational
Linguistics, 12:157–173, 2024.

[22] OWASP Foundation. Owasp top 10 for llm applications 2025. https://genai.owasp.org, 2025. LLM05:

Improper Output Handling.

[23] Jimin Sun, So Yeon Min, Yingshan Chang, and Yonatan Bisk. Tools fail: Detecting silent errors in faulty tools,

2024.

[24] Ke Zhang, Chenxi Zhang, Chong Wang, Chi Zhang, YaChen Wu, Zhenchang Xing, Yang Liu, Qingshan Li, and
Xin Peng. Logiagent: Automated logical testing for rest systems with llm-based multi-agents. arXiv preprint
arXiv:2503.15079, 2025.

[25] Ivan Milev, Mislav Balunovi´c, Maximilian Baader, and Martin Vechev. Toolfuzz–automated agent tool testing.

arXiv preprint arXiv:2503.04479, 2025.

[26] Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Toh Jing Hua, Zhoujun
Cheng, Dongchan Shin, Fangyu Lei, et al. Osworld: Benchmarking multimodal agents for open-ended tasks in
real computer environments. arXiv preprint arXiv:2404.07972, 2024.

[27] Rogerio Bonatti, Dan Zhao, Francesco Bonacci, Dillon Dupont, Sara Abdali, Yinheng Li, Yadong Lu, Justin
Wagle, Kazuhito Koishida, Arthur Bucker, et al. Windows agent arena: Evaluating multi-modal os agents at scale.
arXiv preprint arXiv:2409.08264, 2024.

22

A PREPRINT - AUGUST 12, 2025

[28] Mert Cemri, Melissa Z Pan, Shuyi Yang, Lakshya A Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt Keutzer,
Aditya Parameswaran, Dan Klein, Kannan Ramchandran, et al. Why do multi-agent llm systems fail? arXiv
preprint arXiv:2503.13657, 2025.

[29] Qinghua Lu, Liming Zhu, Xiwei Xu, Zhenchang Xing, Stefan Harrer, and Jon Whittle. Towards responsible

generative ai: A reference architecture for designing foundation model based agents, 2024.

[30] Liming Dong, Qinghua Lu, and Liming Zhu. A taxonomy of agentops for enabling observability of foundation

model based agents. arXiv preprint arXiv:2411.05285, 2024.

[31] Donghyun Lee and Mo Tiwari. Prompt infection: Llm-to-llm prompt injection within multi-agent systems. arXiv

preprint arXiv:2410.07283, 2024.

[32] Jonathan Kutasov, Yuqi Sun, Paul Colognese, Teun van der Weij, Linda Petrini, Chen Bo Calvin Zhang, John
Hughes, Xiang Deng, Henry Sleight, Tyler Tracy, et al. Shade-arena: Evaluating sabotage and monitoring in llm
agents. arXiv preprint arXiv:2506.15740, 2025.

[33] Siyu Yuan, Zehui Chen, Zhiheng Xi, Junjie Ye, Zhengyin Du, and Jiecao Chen. Agent-r: Training language model

agents to reflect via iterative self-training. arXiv preprint arXiv:2501.11425, 2025.

[34] Shirley Wu, Shiyu Zhao, Qian Huang, Kexin Huang, Michihiro Yasunaga, Kaidi Cao, Vassilis Ioannidis, Karthik
Subbian, Jure Leskovec, and James Y Zou. Avatar: Optimizing llm agents for tool usage via contrastive reasoning.
Advances in Neural Information Processing Systems, 37:25981–26010, 2024.

[35] Zeyu Zhang, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Quanyu Dai, Jieming Zhu, Zhenhua Dong, and Ji-Rong Wen.
A survey on the memory mechanism of large language model based agents. arXiv preprint arXiv:2404.13501,
2024.

[36] Zidi Xiong, Yuping Lin, Wenya Xie, Pengfei He, Jiliang Tang, Himabindu Lakkaraju, and Zhen Xiang. How

memory management impacts llm agents: An empirical study of experience-following behavior, 2025.

[37] Yujie Luo, Xiangyuan Ru, Kangwei Liu, Lin Yuan, Mengshu Sun, Ningyu Zhang, Lei Liang, Zhiqiang Zhang, Jun
Zhou, Lanning Wei, et al. Oneke: A dockerized schema-guided llm agent-based knowledge extraction system. In
Companion Proceedings of the ACM on Web Conference 2025, pages 2871–2874, 2025.

[38] Jiawei Zhang, Chejian Xu, Yu Gai, Freddy Lecue, Dawn Song, and Bo Li. Knowhalu: Hallucination detection via

multi-form knowledge based factual checking. arXiv preprint arXiv:2404.02935, 2024.

[39] Cailin Winston and René Just. A taxonomy of failures in tool-augmented llms.

[40] Qineng Wang, Zihao Wang, Ying Su, Hanghang Tong, and Yangqiu Song. Rethinking the bounds of llm reasoning:

Are multi-agent discussions the key? arXiv preprint arXiv:2402.18272, 2024.

[41] Terry Yue Zhuo, Junda He, Jiamou Sun, Zhenchang Xing, David Lo, John Grundy, and Xiaoning Du. Identifying

and mitigating api misuse in large language models. arXiv preprint arXiv:2503.22821, 2025.

[42] Zhengliang Shi, Shen Gao, Lingyong Yan, Yue Feng, Xiuyi Chen, Zhumin Chen, Dawei Yin, Suzan Verberne, and
Zhaochun Ren. Tool learning in the wild: Empowering language models as automatic tool agents. In Proceedings
of the ACM on Web Conference 2025, pages 2222–2237, 2025.

[43] In Gim, Seung-seob Lee, and Lin Zhong. Asynchronous llm function calling. arXiv preprint arXiv:2412.07017,

2024.

[44] Nick Russell, Wil MP van der Aalst, and Arthur HM ter Hofstede. Workflow exception patterns. In International

Conference on Advanced Information Systems Engineering, pages 288–302. Springer, 2006.

[45] David L Parnas, A John Van Schouwen, and Shu Po Kwan. Evaluation of safety-critical software. Communications

of the ACM, 33(6):636–648, 1990.

[46] Tom White. Hadoop: The definitive guide. " O’Reilly Media, Inc.", 2012.

[47] Frederick Hayes-Roth. Rule-based systems. Communications of the ACM, 28(9):921–932, 1985.

[48] Michael Wornow, Avanika Narayan, Krista Opsahl-Ong, Quinn McIntyre, Nigam H Shah, and Christopher Ré.

Automating the enterprise with foundation models. arXiv preprint arXiv:2405.03710, 2024.

[49] Xuanming Zhang, Yuxuan Chen, Yuan Yuan, and Minlie Huang. Seeker: Enhancing exception handling in code

with llm-based multi-agent approach. arXiv preprint arXiv:2410.06949, 2024.

[50] Zefan Wang, Zichuan Liu, Yingying Zhang, Aoxiao Zhong, Lunting Fan, Lingfei Wu, and Qingsong Wen. Rcagent:
Cloud root cause analysis by autonomous agents with tool-augmented large language models. arXiv preprint
arXiv:2310.16340, 2023.

23

A PREPRINT - AUGUST 12, 2025

[51] Zhensu Sun, Haotian Zhu, Bowen Xu, Xiaoning Du, Li Li, and David Lo. Llm as runtime error handler: A
promising pathway to adaptive self-healing of software systems. arXiv preprint arXiv:2408.01055, 2024.
[52] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion: Language
agents with verbal reinforcement learning. Advances in Neural Information Processing Systems, 36:8634–8652,
2023.

[53] Shuaihang Chen, Yuanxing Liu, Wei Han, Weinan Zhang, and Ting Liu. A survey on llm-based multi-agent

system: Recent advances and new frontiers in application. arXiv preprint arXiv:2412.17481, 2024.

[54] Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Shaokun Zhang, Erkang Zhu, Beibin Li, Li Jiang, Xiaoyun
Zhang, and Chi Wang. Autogen: Enabling next-gen llm applications via multi-agent conversation framework.
arXiv preprint arXiv:2308.08155, 2023.

[55] Xinzhe Li. A survey on llm-based agents: Common workflows and reusable llm-profiled components. arXiv

preprint arXiv:2406.05804, 2024.

24

A Tables

A PREPRINT - AUGUST 12, 2025

Table 2: Local Handling Mechanisms.

Mechanism

Description

Clarify Prompt
Echo Validation
Context Tagging
Default Interpretation
Disentangled Prompting
Prompt Rewriting
Prompt Sanitization
Graph Validation
KB Trust Scoring
Logic Re-ranking
Recursive Checkpointing
Abort Task Chain
Conflict Resolution
Constraint Pruning
Forward Chaining
Peer Confirmation
Plan Repair
Plan Shortening
Role-based Check
Subgoal Reordering
Attribute Filtering
Escalate UI Failure
External Call Timeout
Fallback
Fallback to Alternate API
Low-confidence Filter
Memory Slot Isolation
Oracle Verification
Output Sanitization
Output Truncation
Protocol Downgrade
Reset Memory
Response Normalization
Retry with Backoff
Sampling Adjustment
Schema Validation
Semantic Constraint Checking
Switch Tool
Timeout Escalation
Escalate to Human

Ask the user to clarify ambiguous or underspecified goals.
Paraphrase and reflect the goal to verify understanding.
Label context content to separate user/system input sources.
Apply default meaning when input is unclear.
Separate memory/context/KB input paths explicitly.
Rewrite or optimize the original prompt.
Clean injections, redundancy, or special characters from prompt.
Check the logical structure of the reasoning chain.
Score knowledge by trust level, filter untrusted entries.
Rerank multiple reasoning paths.
Insert intermediate checks to avoid infinite loops.
Abort when the plan is unrecoverable.
Resolve agent conflicts via rule or confirmation.
Remove conflicting or unfulfillable planning constraints.
Predict if a task is feasible before continuing.
Confirm cross-agent collaboration.
Repair broken or incomplete plan structures.
Shorten long plan sequences.
Ensure the agent is capable of the assigned role.
Reorder subtasks to improve execution logic.
Remove incorrect features during memory matching.
Escalate UI failure, uncertainty to humans.
Fallback handler when the external system/API times out.
Output default template if structure is broken.
Try another API endpoint if the primary fails.
Skip or downgrade model outputs with low confidence.
Isolate faulty memory slots to prevent propagation.
Use rules/verifiers to judge model/tool correctness.
Clean unsafe or injected segments in generated output.
Truncate model outputs that exceed token limits.
Use a more compatible older protocol if needed.
Clear or rollback corrupted memory.
Normalize API output to standard format.
Retry tool/API call with exponential delay.
Adjust decoding parameters like temperature/top-p.
Check if output matches the required schema.
Check output against semantic constraints or rules.
Replace failed tool/API with a backup.
Trigger escalation on tool/API timeout.
General fallback strategy, escalate to human when needed.

Mechanism

Continue
Skip
Abort

Mechanism

No-op
Rollback
Compensate

Table 3: Flow Control Mechanisms.

Description

The agent proceeds to the next step after successful local recovery.
The agent bypasses the current subgoal or step.
The agent terminates the current task or execution thread.

Table 4: State Recovery Mechanisms.

Description

No state repair is needed; the exception has no persistent side effects.
Restore the agent’s internal state (e.g., memory) to a clean checkpoint.
Trigger a logical reversal to undo externally executed side effects.

#

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40

#

1
2
3

#

1
2
3

25

A PREPRINT - AUGUST 12, 2025

Pattern ID

Local Handling

Flow Control

State Recovery

Table 5: Exception Handling Pattern Table

No-op
No-op
No-op
No-op
No-op
No-op
No-op
No-op
No-op
No-op
No-op
No-op
No-op
No-op
No-op
No-op
Rollback
No-op
No-op
No-op
No-op
No-op
No-op
Rollback
No-op
No-op
Rollback
No-op
Rollback
No-op
No-op
Compensate
Compensate
No-op
No-op
No-op
Compensate
No-op
Compensate
No-op
No-op
Compensate
No-op
Compensate
No-op
No-op
No-op
No-op

P001
P002
P003
P004
P005
P006
P007
P008
P009
P010
P011
P012
P013
P014
P015
P016
P017
P018
P019
P020
P021
P022
P023
P024
P025
P026
P027
P028
P029
P030
P031
P032
P033
P034
P035
P036
P037
P038
P039
P040
P041
P042
P043
P044
P045
P046
P047
P048

Clarify Prompt
Clarify Prompt
Echo Validation
Prompt Rewriting
Prompt Sanitization
Context Tagging
Default Interpretation
Graph Validation
Recursive Checkpointing
Logic Re-ranking
KB Trust Scoring
Plan Repair
Plan Shortening
Forward Checking
Constraint Pruning
Subgoal Reordering
Abort Task Chain
Retry with Backoff
Switch Tool
Fallback to Alternate API
Schema Validation
Schema Validation
Semantic Constraint Checking
Oracle Verification
Output Sanitization
Fallback Template
Reset Memory
Memory Slot Isolation
Attribute Filtering
Disentangled Prompting
Response Normalization
Timeout Escalation
Timeout Escalation
Low-confidence Filter
Output Truncation
Sampling Adjustment
Escalate to Human
Escalate to Human
Escalate to Human
Escalate to Human
Protocol Downgrade
External Call Timeout Fallback
External Call Timeout Fallback
External Call Timeout Fallback
External Call Timeout Fallback
Role-based Check
Conflict Resolution Prompt
Peer Confirmation

Abort
Continue
Continue
Abort
Continue
Continue
Continue
Abort
Abort
Continue
Continue
Abort
Abort
Abort
Abort
Abort
Abort
Continue
Abort
Abort
Abort
Continue
Continue
Continue
Continue
Continue
Abort
Continue
Continue
Abort
Continue
Skip
Abort
Continue
Continue
Continue
Skip
Skip
Abort
Abort
Abort
Skip
Skip
Abort
Abort
Abort
Abort
Continue

26

A PREPRINT - AUGUST 12, 2025

Table 6: Exception to Primary Handler Pattern Mapping: Representative Examples

Exception Type

Artifact

Pattern ID

Local Handling

Flow Control

State Recovery

Ambiguous Goal

Goal

Contradictory Reasoning
Faulty Task Structuring

Memory Poisoning
Hallucinated Facts

Tool Invocation Exception
Tool Output Exception
API Invocation Exception
UI Element Misclick

Error Propagation
Agent Conflict

Reasoning
Planning

Memory
Knowledge
Base

Tool
Tool
Interface
Interface

Task Flow
Other Agent

P001

P008
P012

P027
P011

P018
P021
P018
P037

P017
P047

Protocol Mismatch

External System

P041

Clarify Prompt

Graph Validation
Plan Repair

Reset Memory
KB Trust Scoring

Retry with Backoff
Schema Validation
Retry with Backoff
Escalate to Human

Abort

Abort
Abort

Abort
Continue

Continue
Abort
Continue
Skip

Abort Task Chain
Conflict Resolution
Prompt
Protocol Downgrade

Abort
Abort

Abort

No-op

No-op
No-op

Rollback
No-op

No-op
No-op
No-op
Compensate

Rollback
No-op

No-op

27

