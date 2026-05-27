*Response size: ~26K tokens. Consider using zotero_semantic_search to find specific content instead of reading full papers.*

# ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

**Type:** preprint

**Item Key:** TUMBKUWQ

**Date:** 2026-02-04

**Authors:** Tang, Zhentao; Cui, Yuqi; Kai, Shixiong; Zhao, Wenqian; Ye, Ke; Li, Xing; Tian, Anxin; Pei, Zehua; Zhen, Hui-Ling; Hu, Shoubo; Li, Xiaoguang; Wang, Yunhe; Yuan, Mingxuan

**DOI:** 10.48550/arXiv.2602.04496

**URL:** http://arxiv.org/abs/2602.04496



## Extra

arXiv:2602.04496 [cs]

**Tags:** `Computer Science - Artificial Intelligence`



## Abstract

Expert-level scientific reasoning remains challenging for large language models, particularly on benchmarks such as Humanity's Last Exam (HLE), where rigid tool pipelines, brittle multi-agent coordination, and inefficient test-time scaling often limit performance. We introduce ReThinker, a confidence-aware agentic framework that orchestrates retrieval, tool use, and multi-agent reasoning through a stage-wise Solver-Critic-Selector architecture. Rather than following a fixed pipeline, ReThinker dynamically allocates computation based on model confidence, enabling adaptive tool invocation, guided multi-dimensional reflection, and robust confidence-weighted selection. To support scalable training without human annotation, we further propose a reverse data synthesis pipeline and an adaptive trajectory recycling strategy that transform successful reasoning traces into high-quality supervision. Experiments on HLE, GAIA, and XBench demonstrate that ReThinker consistently outperforms state-of-the-art foundation models with tools and existing deep research systems, achieving state-of-the-art results on expert-level reasoning tasks.

**Notes/Attachments:** 2

---

## Full Text

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and
Confidence Control

Zhentao Tang * 1 Yuqi Cui * 1 Shixiong Kai 1 Wenqian Zhao 1 Ke Ye 1 Xing Li 1 Anxin Tian 1 Zehua Pei 2
Hui-Ling Zhen 1 Shoubo Hu 1 Xiaoguang Li 1 Yunhe Wang 1 Mingxuan Yuan 1

6
2
0
2

b
e
F
4

]
I

A
.
s
c
[

1
v
6
9
4
4
0
.
2
0
6
2
:
v
i
X
r
a

Abstract

Expert-level scientific reasoning remains chal-
lenging for large language models, particularly
on benchmarks such as Humanity’s Last Exam
(HLE), where rigid tool pipelines, brittle multi-
agent coordination, and inefficient test-time scal-
ing often limit performance. We introduce Re-
Thinker, an confidence-aware agentic framework
that orchestrates retrieval, tool use, and multi-
agent reasoning through a stage-wise Solver–
Critic–Selector architecture. Rather than follow-
ing a fixed pipeline, ReThinker dynamically al-
locates computation based on model confidence,
enabling adaptive tool invocation, guided multi-
dimensional reflection, and robust confidence-
weighted selection. To support scalable training
without human annotation, we further propose a
reverse data synthesis pipeline and an adaptive tra-
jectory recycling strategy that transform success-
ful reasoning traces into high-quality supervision.
Experiments on HLE, GAIA, and XBench demon-
strate that ReThinker consistently outperforms
state-of-the-art foundation models with tools and
existing deep research systems, achieving state-
of-the-art results on expert-level reasoning tasks.

1. Introduction

Scientific reasoning has become a central challenge for eval-
uating the capabilities of large language models (LLMs) and
a key indicator of progress toward general-purpose artificial
intelligence (Truhn et al., 2023). In contrast to common-
sense reasoning, scientific problem-solving demands quanti-
tative rigor, multi-hop causal inference, and the integration
of domain-specific knowledge across mathematics, physics,
and chemistry—capabilities that remain insufficiently devel-
oped in current LLMs. This limitation becomes particularly

*Equal contribution 1Noah’s Ark Lab, Huawei, China 2The
Chinese University of Hong Kong, Hong Kong, China. Correspon-
dence to: Shixiong Kai <kaishixiong@huawei.com>.

Figure 1. Performance comparison on the HLE benchmark. The
results include Foundation Models with Tools, existing Inference
Frameworks, and our proposed method ReThinker based on two
LLMs. ReThinker (based on Gemini-3-Pro) significantly outper-
forming both standalone models and other inference frameworks.

evident on expert-level benchmarks such as Humanity’s Last
Exam (HLE) (Phan et al., 2025), which targets advanced
scientific problems requiring deep domain expertise and
complex multi-step reasoning. Although existing LLMs
often exhbit strong superficial performance, they frequently
fail to reliably distinguish correct mathematical reasoning
from subtly flawed arguments, suggesting that their appar-
ent success is driven more by pattern memorization than by
systematic, principled deduction.

To address these limitations, we argue that expert-level sci-
entific reasoning demands three fundamental capabilities
that remain critically underdeveloped in current systems:
the capacity for rethinking—iteratively questioning and
refining intermediate conclusions rather than committing
to single-pass reasoning trajectories; the mechanism for
guided reflection—structured, dimension-specific error di-

1

0102030405060HLE ScoreWebExplorerKimi K2Claude-4.5-SonnetOpenAI DeepResearchKimi ResearcherDeepSeek-V3.2GLM-4.6Tongyi DeepResearch (30B-A3B)ReThinker (OpenPangu-72B)MiroThinker-v1.0 (30B)GPT-5-highGemini-3-ProReThinker (Gemini-3-Pro)17.318.124.526.626.927.230.432.933.133.435.238.352.2Performance comparison on HLE benchmarkOurs (ReThinker)Foundation Models (w/ Tools)Other Inference Frameworks

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

agnosis that transcends superficial summarization to target
precise logical, strategic, and knowledge gaps; and effec-
tive confidence control—explicit uncertainty quantification
and multi-round adjudication to stabilize answer selection
amidst compounding verification noise. Here we introduce
ReThinker. Our contributions are summarized as follows:

• Automated Trajectory Synthesis for Rethinking Su-
pervision. We eliminate manual annotation entirely.
Our system automatically generates expert-level QA
pairs across scientific domains. It extracts domain con-
cepts from web contexts and generated trajectories.
The pipeline records complete multi-stage reasoning
traces. It captures error recovery patterns and tool-use
sequences. Only verified correct trajectories are re-
tained. These provide high-fidelity supervision signals.
Models learn to rethink rather than memorize patterns.

• Hybrid Scaling with Guided Reflection. We develop
a hybrid sequential–parallel scaling architecture based
on EvoFabric (EvoFabric Development Team, 2025)
that enables flexible trade-offs between inference bud-
get and reasoning accuracy. The framework integrates
Python execution, web search, and web parsing tools to
support quantitative verification and expert knowledge
In the Solver stage, we employ multi-
acquisition.
round iterative synthesis to allow progressive refine-
ment of reasoning. In the Critic stage, we introduce
a summary-and-guidance module that processes the
complete prior trajectory, mitigating context-length
limitations and correcting subtle errors that are often
missed by conventional summary-only critics.

• Confidence-Controlled Selection via Uncertainty
Aggregation. We introduce a confidence-guided multi-
round selection mechanism for the Selector stage
to stabilize optimal answer identification. To ad-
dress verification-induced uncertainty, we aggregate
perplexity-based internal consistency metrics across
multiple selection rounds. Prior selection outcomes
and confidence scores are iteratively fed back into the
prompt to amplify high-confidence candidates. To fur-
ther eliminate ordering bias, we permute candidate
positions using Latin Square designs and resolve cross-
round inconsistencies through a final adjudication step
to determine the definitive answer.

2. Related Work

2.1. Tool-Augmented Interactive Reasoning

The ReAct framework (Yao et al., 2022) turns LLMs
into interactive agents by interleaving Thought–Action–
Observation steps, enabling tool use during reasoning. In
scientific settings, ReAct-style agents employ calculators

2

for symbolic computation (Chen et al., 2023), code execu-
tion for mathematical and logical verification (Wang et al.,
2024; M. Bran et al., 2024), and web search for evidence
and literature retrieval (Nakano et al., 2021). Recent exten-
sions such as Eigen-1 (Tang et al., 2025) further integrate
reasoning with executable Python-based tool workflows
and report strong performance on HLE Bio/Chem Gold.
SCOPE (Pei et al., 2025) automates prompt evolution to
improve agent effectiveness, reducing reliance on manual
prompt engineering. However, most tool-augmented ap-
proaches remain largely single-agent: reasoning depth is
constrained by context length, errors can accumulate with-
out systematic correction, and tool hallucination remains a
persistent challenge (Zhang et al., 2025), motivating multi-
agent decomposition.

2.2. Multi-Agent Orchestration and Collaborative

Reasoning

Multi-agent systems decompose complex reasoning tasks
into specialized roles that collaborate through parallel or
sequential interaction patterns (Xi et al., 2025). Comple-
mentary to role-based coordination, recent work on self-
reflection, such as MiroThinker (MiroMind et al., 2025),
shows that agents trained on trajectories containing explicit
error-correction steps can achieve improved reasoning per-
formance. The STeP method (Chen et al., 2025b) further
synthesizes self-reflective trajectories from teacher models,
enabling smaller open-source models to acquire corrective
behaviors. Despite these advances, most existing multi-
agent and self-reflective frameworks rely on hand-crafted
interaction protocols and do not explicitly model confidence
or answer stability under test-time scaling, limiting their
robustness on challenging reasoning benchmarks.

2.3. Test-Time Scaling and Confidence-Guided

Reflection

Test-time scaling (also referred to as inference-time scaling)
has emerged as an effective strategy for enhancing reasoning
performance without model retraining (Yang et al., 2023).
Existing approaches broadly fall into two categories.

Sequential scaling extends reasoning trajectories through
iterative reflection and revision. For example, s1 (Muen-
nighoff et al., 2025) demonstrates that budget forcing pro-
duces longer and more accurate reasoning traces, while
Reflexion (Shinn et al., 2023) incorporates verbal feedback
stored in episodic memory to guide subsequent reasoning
steps. Despite improved reasoning depth, sequential meth-
ods remain limited by single-trajectory exploration and ac-
cumulated errors.

Parallel scaling generates multiple candidate solutions si-
multaneously and selects the optimal answer through verifi-
cation or aggregation (Snell et al., 2025). Representative ap-

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

proaches include Best-of-N sampling (Ichihara et al., 2025),
which ranks candidates using reward models or process ver-
ifiers (Lightman et al., 2023), and self-consistency (Wang
et al., 2023), which performs majority voting across diverse
reasoning paths. However, verifier-based methods intro-
duce substantial computational overhead and often rely on
auxiliary models (Zheng et al., 2025).

The effectiveness of parallel scaling depends critically on
accurate confidence estimation. Existing approaches can be
broadly categorized into two classes. Consistency-based
methods (Zhou et al., 2025) measure agreement across
multiple samples, with self-consistency as a representative
example. While effective for deterministic problems, such
metrics can be unstable when reasoning paths diverge or ver-
ification signals are noisy (Chen et al., 2024). Probability-
based methods leverage internal model statistics, with per-
plexity commonly used as a confidence indicator (Chen
& Goodman, 1999). Recent theoretical analyses (Muru-
gadoss et al., 2025) suggest that perplexity correlates with
reasoning path quality; however, single-round confidence es-
timates remain unreliable due to ordering bias and sampling
variance (Bito et al., 2025).

3. Method

3.1. Overall Framework Overview

Figure 2 illustrates our data-driven, uncertainty-guided it-
erative reasoning framework. The framework is organized
into three tightly coupled phases, corresponding to the three
panels.

3.2. Post-Training Data Synthesis & Curation

Post-training data quality is as critical as agent workflow
design for scientific reasoning. Rather than relying on a
single form of supervision, we decompose post-training data
into two complementary components: (1) expert-level QA
pairs for supervised fine-tuning, and (2) adaptive trajectory
utilization and recycling.

3.2.1. EXPERT QA PAIRS FOR SUPERVISED

FINE-TUNING

To reduce human efforts and make the whole data synthe-
sis pipeline more scalable and autonomous, as shown in
Figure 2A (top-left), we propose the LLM-based multi-
agent seed phrase initialization and online extraction to
automatically construct seed phrases. They are then used to
generate QA pairs, following the workflow proposed in We-
bExplorer (Liu et al., 2025b). Users only need to specify the
interested topics such as biology and business, LLM agents
will then propose initial seed noun phrases from them and
extract and refine professional and uncommon noun phrases
from trajectories and QA contexts during the subsequent

flow.

Seed Domain Initialization.
Specifically, we utilize
LLMs to generate 10 common phrases in 23 specific
general domains from natural sciences, social
sciences, humanities, applied sciences,
and etc. As a result, we collect 230 very high-level and
general seed phrases, including natural selection,
social stratification, color theory, and
failure analysis. These seed phrases are then used
as the initial input for the whole automatic self-evolving
agentic data synthesis pipeline to generate QA pairs and
trajectories for subsequent model training.

Automatic Seed Phrase Updating. During the data synthe-
sis stage proposed in (Liu et al., 2025b), the searched web
snippets and full contexts are only used once for QA gener-
ation and directly discarded after that. Due to the high cost
of LLMs and web retrieval services, the aforementioned
process leads to significant data generation expenses and
inefficient utilization of retrieved content. Therefore, we
recycle the previously discarded contexts during the data
synthesis flow and extract seed phrases from them. The pool
of seed phrases is online updated and extended using the
searched web context, generated QA pairs, and trajectories.

3.2.2. ADAPTIVE TRAJECTORY UTILIZATION AND

RECYCLING

Reasoning trajectories constitute critical supervision signals
and make a big difference to the performance of downstream
agent. Therefore, as shown in Figure 2A (top-right), we pro-
pose an adaptive trajectory synthesis and recycling frame-
work that systematically governs how reasoning trajectories
are generated, selected, and reused during post-training to
make use of reasoning trajectories. To this end, all collected
trajectories (Agent Logs) are filtered, annotated, and cu-
rated offline using a combination of automatic metrics, such
as answer correctness, tool-use efficiency, and reasoning
coherence in support of enhancing the reasoning and tool-
use capabilities of LLM-based agents in scientific research
scenarios.

Adaptive Trajectory Generation Rather than relying on
fixed-length reasoning chains or static tool-invocation poli-
cies, our framework enables adaptive control over reasoning
trajectories. During question answering, the agent dynami-
cally explores multiple candidate reasoning paths through
iterative reasoning and tool interactions, selecting effective
tool-call sequences and progressively refining intermediate
hypotheses.

Multi-Stage Data Quality Assurance Pipeline. To ensure
the reliability of generated trajectories, we design a multi-
stage data quality assurance pipeline, which systematically
transforms raw generated trajectories into a high-quality

3

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

Figure 2. Overall Framework of ReThinker: A Data-Driven and Uncertainty-Guided Agentic System for Expert-Level Scientific
Reasoning. The framework comprises three integrated phases: (A) Post-Training Data Synthesis & Curation, where trajectory recycling
and a validation agent generate and refine expert QA pairs through correctness checks, formatting, deduplication, and quality balancing;
(B) Multi-Path Iterative Reasoning, where parallel Solver-Critic paths execute tool-enhanced reasoning to produce candidate trajectories
from user queries; and (C) Confidence-Guided Selection, a three-stage process employing Latin Square Permutation Test for initial
judgment, iterative re-selection conditioned on historical data and perplexity scores (PPLs), and unanimous voting for final decision. The
system features dual feedback loops—Data Recycling Flow and Iterative Bootstrapping Flow—that continuously enhance the knowledge
foundation and reasoning capabilities.

SFT dataset.

• Correctness Check. We first perform outcome-based
filtering using a strong judge model to verify final answer
correctness. Trajectories that fail to produce correct an-
swers are discarded, preventing the model from inheriting
erroneous reasoning or hallucinated solutions;

• Formatting Validation. We enforce strict structural
constraints on reasoning trajectories, such as:
(i)
Answer Format: the final result encapsulated within
(ii) Interaction
<answer></answer> tag;
Integrity: all dialogues must follow a consistent
”User-Assistant” pairing and that no assistant response
is empty; (iii) Tool-Invocation Constraint:To
prevent inefficient reasoning, we filter trajectories based
on tool-use density. We discard samples where the
number of tool calls is either insufficient to resolve
the query or excessively high but ineffective to solve
problems.

• Deduplication & Balance. Redundant data are pruned
to avoid overfitting on frequent patterns. Then, we rebal-
ance data distribution across all reasoning phases, thereby
mitigating model bias toward high-frequency patterns.

• Quality Improvement. we finally assess the ratio-
(i) CoT-Response

nality and effectiveness of data.

Alignment: We filter out those data whose internal rea-
soning contradicts external outputs; (ii) Successful
Tool Execution: Data which the model provides
failed tool calling are excluded to ensure quality of the
curated SFT data.

3.3. Multi-Path Solution Generation

As illustrated in Figure 2B (middle), we instantiate N ∈
Z+ parallel reasoning paths, each consisting of solver and
critic stages. Both solver and critic progressively improve
solution quality through multi-round iterative rethinking.
The critic stage is further equipped with guided reflection,
which allows the critic to capture and correct subtle, fine-
grained issues arising throughout the reasoning process.

Stage 1: Solver Stage with Rethinking. Following prior
work on iterative refinement (Tian et al., 2025; Xu et al.,
2025), each path i(i = 1, ..., N ) performs T (i)
solver ∈ Z+
rounds of reasoning. Each round invokes reasoning tools
multiple times to retrieve relevant knowledge or verify rea-
soning steps, after which a single final answer is produced.
This final answer is then extracted and fed into the subse-
quent round, prompting the model to reconsider its reason-
ing and iteratively refine the solution.

Let s(i)

t denotes the solution generated at round t, where

4

A. Post-Training Data Synthesis & Curation (Knowledge Foundation)B. Solution Generation Phase (Multi-Path Iterative Reasoning)C. Selection Phase (Confidence-Guided Adaption)AgentLogs1. Correctness Check 2. FormattingValidation 3. Deduplication& Balance 4. QualityImproving     Post-Training Data Synthesis  (Tajectroy Recycling)Post-TraningData(Trajectories)UserQuery qCandidateSet   TrajectoriesNParallelPathsStage 1: Initial Judgement (Latin Square Permutation      )w/tool executionSolverTool Execution(Web, Code)CriticSummaryRefineTool Execution(Web, Code)CandidateResponsesSeed DomainsSeed PhaseInitialization LLM Expansion &Web Search SFT Data(QA Pairs)Expert QA Pairs (SFT)Tools & ContextRecyclingFinalAnswerStage 2: Itrative Re-selection (Condition on History  & PPLs)w/tool executionStage 3: Final Decision (Passed unanimously)w/tool executionData FlowData Recycling FlowIterative Bootstrapping FlowReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

t = 0, . . . , Ti − 1. The solver stage can be represented as:

t+1 = Solver(cid:0)q, extract(s(i)
s(i)

t )),

(1)

where q is the problem statement, extract(s(i)
t )) denotes
the final conclusion extracted from the reasoning trajectory
s(i)
t of round t. This rethinking mechanism stably elevates
reasoning quality, ensuring that easily correctable errors are
eliminated before reflection.

Stage 2: Critic Stage with Guided Reflection. Due to
the context length limitations of LLMs, conventional reflec-
tion approaches over reasoning trajectories typically rely
on partial outputs or or compressed representations, which
may lead the reflection to overlook the fine-grained issues
in the reasoning process. To address this limitation, we pro-
pose a guided reflection method. The reasoning trajectory
produced by the Solver stage is first summarized into three
components: summary of the trajectory, the final answer,
and key areas for improvement. The Critic module then per-
forms reflection based on these three components. Since the
key areas for improvement are derived from the complete
reasoning trajectory, this approach enables comprehensive
analysis spanning fine-grained issues as well as high-level
logical flaws.

The summary process can be represented as:

y(i), a(i), k(i) = Summary(q, s(i)
Ti

),

(2)

where y(i), a(i) and k(i) denote the key reasoning steps, the
final answer, and the key areas for improvement extracted
from the Solver’s reasoning trajectory of the last round s(i)
Ti
for path i, respectively. Let c(i)
t denotes the critic result at
round t, where c(i)
critic − 1. The critic stage
can be represented as:

t ), t = 0, . . . , T (i)

c(i)
t+1 = Critic

(cid:16)

q, y(i), a(i), k(i), extract(c(i)
t )

(cid:17)

.

(3)

3.4. Confidence-Guided Selection

As shown in Figure 2C (bottom), we adopt a three-stage
confidence-guided evaluation framework. The selector first
scores all candidates with confidence estimates, then itera-
tively refines its selection using perplexity-weighted confi-
dence under Latin-square permutations to eliminate position
bias. A final aggregation step is applied only when cross-
round selections are inconsistent. This design concentrates
computation on uncertain cases while remaining robust to
ordering effects and early-round noise.

The solution generation stage produces a candidate set C =
{c1, c2, ..., cn} of feasible answers, each accompanied by a
reasoning trajectory. The selector must identify the optimal
answer while mitigating systematic errors from single-pass

inference and position bias. We frame this as a three-stage
confidence-calibrated decision process.

Stage 1: Initial Judgement. The problem statement q and
candidate set C are formatted into a structured prompt that
elicits both a preliminary selection s0 ∈ C and a confidence
estimate. Crucially, to eliminate ordering bias, we permute
candidate positions via Latin squares: for round r, we apply
a permutation πr drawn from a pre-computed Latin square
L, presenting candidates as (πr(c1), πr(c2), ..., πr(cn)).
This ensures each candidate appears equally often in ev-
ery position across rounds, forcing the model to focus on
content rather than ordinal heuristics.

Stage 2: Iterative Re-selection. The initial judgement’s
perplexity PPL(s0) serves as a gating signal for progressive
refinement. Perplexity is computed as:



PPL(s0) = exp

−

1
Tseq

Tseq
(cid:88)

t=1



log pθ(xt | x<t)

 ,

(4)

where xt are tokens in the selection rationale and Tseq
is the sequence length. High PPL indicates uncertainty,
triggering R additional re-selection rounds.
In each
round r, the model conditions on the aggregated history
Hr = {s0, s1, ..., sr−1} and their PPL scores, enabling
confidence-weighted progressive refinement where selec-
tions become increasingly precise. The process amplifies
high-certainty choices while suppressing noisy candidates
through Bayesian updating of selection probabilities.

Stage 3: Final Decision. We synthesize historical selec-
tions to produce a definitive answer. Let Chist = {c ∈ C :
∃ r ∈ {0, ..., R} s.t. sr = c} be the set of candidates ever
selected. If |Chist| = 1, the answer is output directly, bypass-
ing this stage. Otherwise, we execute a final adjudication
pass that conditions on this candidate set with responded
answers and confident scores, discarding never-mentioned
candidates and resolving inconsistencies through a deci-
sive selection. This ensures robust aggregation with each
historically-selected candidate treated as an independent
option.

4. Experiments

4.1. Experiment Setup

We evaluate our method on three representative and chal-
lenging reasoning benchmarks, which comprehensively as-
sess advanced analytical and agentic reasoning capabilities:

• Humanity’s Last Exam (HLE) (Phan et al., 2025):
A large-scale expert-level benchmark with challeng-
ing problems across diverse scientific fields. It tests
whether AI systems can demonstrate deep reasoning
and knowledge at near-human expert levels. Following

5

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

prior work, We evaluate on a text-only subset of 2158
validation instances (MiroMind et al., 2025).

els with tools and existing inference frameworks across all
benchmarks.

• GAIA (Mialon et al., 2023): A benchmark composed
of real-world tasks that require tool usage, web navi-
gation, and multi-step planning. Following prior work,
we evaluate on a text-only subset of 103 validation
instances (Li et al., 2025; Wu et al., 2025).

• XBench-DeepSearch (Chen et al., 2025a): A
professionally-aligned benchmark that focuses on eval-
uating AI agent’s tool usage capabilities, specifically
in deep information retrieval and complex search tasks.
And it totally contains 100 expert-level reasoning prob-
lems.

Evaluation Protocol. All benchmarks are evaluated using
an LLM-as-a-Judge framework. Specifically, GAIA and
XBench-DeepSearch are evaluated using gpt-4.1-2025-04-
14, while HLE follows its official evaluation protocol with
judgments produced by o3-mini-2025-01-31.

Table 1. Main Results of Inference Accuracy (%) on Expert-Level
Reasoning Benchmarks.

Benchmarks

HLE GAIA XBench

Foundation Models with Tools

(Anthropic,

Kimi K2 (Kimi et al., 2025)
Claude-4.5-Sonnet
2025)
DeepSeek-V3.2 (Liu et al., 2025a)
GLM-4.6 (Zhipu, 2025)
GPT-5-high (OpenAI, 2025b)
Gemini-3-Pro (Google, 2025)

Inference Frameworks

WebExplorer (Liu et al., 2025b)
OpenAI DeepResearch (OpenAI,
2025a)
Kimi Researcher (Kimi, 2025)
Tongyi DeepResearch (30B-
A3B) (Tongyi et al., 2025)
MiroThinker-v1.0 (30B) (Miro-
Mind et al., 2025)

18.1
24.5

27.2
30.4
35.2
38.3

17.3
26.6

26.9
32.9

57.7
71.2

63.5
71.9
76.4
79.0

50.0
67.4

–
70.9

50.0
66.0

71.0
70.0
77.8
87.0

53.7
–

69.0
75.0

33.4

73.5

70.6

ReThinker (OpenPangu-72B)
ReThinker (Gemini-3-Pro)

33.1
52.2

72.8
81.6

78.0
90.0

4.2. Main Results

Table 1 summarizes the main experimental results on three
text-only reasoning benchmarks. Overall, our ReThinker
framework consistently outperforms both foundation mod-

On HLE, ReThinker instantiated with Gemini-3-Pro
achieves 52.18% accuracy, substantially surpassing all base-
lines. Compared to strong tool-augmented foundation mod-
els such as OpenAI-GPT-5-high (35.2%) and Gemini-3-Pro
used directly (38.3%), our approach yields improvements
of 16.9 and 13.8 percentage points, respectively. It also
significantly outperforms specialized inference frameworks,
including Tongyi DeepResearch (32.9%) and MiroThinker-
v1.0 (33.4%), demonstrating the effectiveness of adaptive
trajectory utilization and confidence-guided selection for
high-difficulty scientific reasoning.

On GAIA, ReThinker (Gemini-3-Pro) achieves 81.55%
accuracy, establishing a new state of the art among all com-
pared methods. This result exceeds Gemini-3-Pro with tools
(79.0%) and other deep research systems such as Tongyi
DeepResearch (70.9%) and MiroThinker-v1.0 (73.5%), val-
idating the robustness of our framework in complex, tool-
intensive, real-world tasks.

On XBench-DeepSearch, our method reaches 90.0% ac-
curacy, outperforming all open-source baselines and im-
proving upon Gemini-3-Pro with tools (87%). These gains
indicate that ReThinker not only enhances answer correct-
ness but also provides more stable and reliable reasoning
under expert-level evaluation settings.

Taken together, the results demonstrate that our framework
consistently amplifies the reasoning capabilities of strong
foundation models, particularly on benchmarks that demand
long-horizon planning, multi-step inference, and precise tool
orchestration, rather than shallow retrieval or memorization.

4.3. Component Analysis

To quantify the contribution of each component in our frame-
work, we conduct a controlled component analysis on a rep-
resentative subset of 500 text-only HLE problems, sampled
from the full benchmark with matched category distribution.
We adopt a modular decoupling strategy to isolate the effect
of each stage. To ensure fair comparison, all variants are
instantiated with OpenPangu as a unified backbone.

Solver Phase: Re-Answer Synthesis Improves Initial
Solution Quality. As shown in Table 2, introducing multi-
round re-answer synthesis yields a 1.4% absolute improve-
ment in Pass@5. This gain is achieved by iteratively boot-
strapping candidate solutions across rounds, allowing the
solver to refine earlier reasoning traces. Although the nu-
merical improvement is modest, it plays a critical role in
reducing low-level errors and narrowing the error surface ex-
posed to downstream modules. As a result, the subsequent
Critic phase can focus on high-order logical inconsistencies
rather than correcting superficial or syntactic mistakes.

6

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

Table 2. Effect of Re-Answer Synthesis in the Solver Phase.

Phase

Stage

Solver

Initial Solver
Re-Answer Solver

Pass@5

38.00%
39.40%

Critic Phase: Guided Reflection with Structured Sum-
mary Is the Primary Contributor. Table 3 demonstrates
that the Critic phase delivers the most substantial single-
stage improvement, contributing a 3.8% Pass@5 gain over
the solver output. Notably, Critic with Summary & Guid-
ance outperforms both the Final Answer-only and Summary-
only variants by 2.8% and 1.6%, respectively. This result
confirms that structured guidance is essential for effective
reflection.

Table 3. Impact of Guided Reflection Strategies in the Critic Phase.

Phase

Setting

Solver Re-Answer Solver

Critic

Critic w/Final Answer
Critic w/Summary
Critic w/Summary & Guidance

Pass@5

39.40%

40.40%
42.00 %
43.20%

Selector Phase: Compound Gains from Confidence
Guidance and Position Robustness. As reported in Ta-
ble 4, the Selector phase produces a cumulative 5.6% im-
provement in hit rate and a corresponding 5.6% gain in
Pass@1 through progressive refinement. The stage-wise
improvements reveal complementary effects:

• Initial Judgement establishes a 65.27% hit rate base-

line, comparable to naive best-of-N selection.

• +Iterative Judgement improves hit rate by 2.78%, in-
dicating that re-conditioning on prior selections effec-
tively filters spurious candidates even without explicit
confidence modeling.

• +Perplexity Guidance yields an additional 1.39%
gain, validating perplexity as a reliable uncertainty
signal. This mechanism constitutes the core of our test-
time scaling strategy, allocating additional compute to
instances where the model exhibits higher uncertainty.

• +Latin Square Rank contributes the final 1.39%
Pass@1 improvement, demonstrating that position bias
is non-negligible in selection. By enforcing uniform
rank exposure across rounds, this strategy ensures that
selection decisions are driven by content quality rather
than ordinal position.

Table 4. Incremental Gains from Confidence-Guided Selection.
Hit Rate Pass@1

Setting

Phase

Selector

Initial Judgement
+Iterative Judgement
+Perplexity Guidance
+Latin Square Rank

65.27% 28.20%
68.05% 29.40%
69.44% 30.00%
70.83% 30.60%

5. Discussion and Analysis

Building upon the effectiveness results in Section 4, we fur-
ther examine ReThinker’s efficiency and operational charac-
teristics from three complementary perspectives: (1) Tool
Use Statistics, which quantify the average number of tool
invocations per problem across phases (Solver, Critic, and
Selector); (2) Solver-to-Critic Benefits, which analyze how
phased refinement improves solution quality and task adapta-
tion; and (3) The Guidance of Perplexity, which evaluates
the statistical and behavioral impact of perplexity-guided
decision making in the Selector.

5.1. Tool Use Statistics

Figure 3 shows a clear and monotonic decrease in tool invo-
cation from the Solver to the Critic and finally to the Selector
phase. The Solver phase exhibits the highest tool usage,
reflecting its role as the primary exploration and information
acquisition stage. At this stage, the model operates under
maximal uncertainty and actively queries external tools to
construct an initial knowledge foundation.

Figure 3. Tool Usage Statistics across Reasoning Phases in Re-
Thinker.

Upon transitioning to the Critic phase, average tool usage
decreases by a factor of 3.72, indicating that the structured
summary and critique mechanism effectively consolidates
context and localizes residual knowledge gaps, rather than
re-exploring the problem space broadly. By the Selector
phase, tool calls drop to single-digit levels, and final deci-
sions are made almost entirely based on internal confidence

7

Biology/MedicineChemistryComputer Science/AIEngineeringHumanities/Social ScienceMathOtherPhysicsCategories05101520253035Average Tool Usage24.229.020.717.233.915.537.217.522.826.318.315.825.812.129.315.16.88.07.58.010.55.38.04.5SolutionCriticSelectorReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

signals.

This monotonic decline demonstrates that ReThinker suc-
cessfully accumulates, compresses, and reuses external in-
formation across its reasoning trajectory. The observed trend
validates our design hypothesis: early-stage exploration is
resource-intensive but necessary, while later-stage refine-
ment and selection increasingly rely on synthesized internal
representations, thereby minimizing external dependencies
while improving decision confidence.

5.2. Solver-to-Critic Benefits

Figure 4 illustrates the distributional shift in correct-answer
trajectories between the Solver and Critic phases. In the
Solver phase, the distribution is highly skewed: 93 problems
yield only 1 correct candidate out of 5 generated paths,
while only 16 problems achieve the ideal 5/5 correct rate.
This reflects the Solver’s role as an exploratory generator,
producing diverse but noisy hypotheses with limited self-
correction.

After transitioning to the Critic phase, the distribution shifts
toward higher-quality regions. The number of problems
with only a single correct answer decreases from 93 to 75,
while those achieving 5 correct answers nearly double to
30. Correspondingly, the mean number of correct answers
increases from 2.1 (Solver) to 2.6 (Critic).

Figure 4. Distributional Shift in Correct-Answer Trajectories from
Solver to Critic.

These results indicate that the Critic does not merely filter
existing candidates, but actively recalibrates the solution
ensemble. Guided reflection systematically uplifts marginal
trajectories, converting previously weak or partially cor-
rect solutions into viable answers. This ensemble-level
redistribution highlights the Critic’s role as a global quality
amplifier rather than a local verifier.

5.3. The Guidance of Perplexity

Figure 5 visualizes the empirical relationship between per-
plexity and answer correctness across four selector iterations.

8

Correct answers predominantly cluster at lower perplexity
values, while incorrect answers exhibit a pronounced right-
ward shift, forming a clear separation between high- and
low-confidence regions. This monotonic pattern confirms
that perplexity serves as a reliable proxy for model uncer-
tainty during selection.

Figure 5. Separation between Correct and Incorrect Answers In-
duced by Perplexity.

Table 5 further quantifies the effect of perplexity-guided
re-selection across iterative rounds, measured by the cumu-
lative number of correctly selected answers. Starting from
an identical initial baseline of 141 correct selections, the two
settings (with and without perplexity guidance) diverge im-
mediately. In Round 1, the perplexity-guided selector gains
7 correct selections, whereas the non-guided variant incurs
a net loss, indicating that confidence-agnostic re-selection
amplifies noise rather than signal in early iterations.

Table 5. Effect of Perplexity-Guided Re-Selection across Iterative
Selector Rounds.

Selector

Initial
Judgement

Number of Iteration

1

2

3

4

w/PPL
wo/PPL

141

148 (↑) 150 (-) 150 (-) 153 (↑)
140 (↓) 144 (↑) 143 (↓) 147 (↑)

The temporal dynamics reveal distinct convergence behav-
iors. The perplexity-guided selector exhibits steady improve-
ment followed by clear saturation, while the non-guided
variant displays volatile oscillations reminiscent of a ran-
dom walk. These results validate our core hypothesis: per-
plexity is not merely a diagnostic metric, but an actionable
control signal that allocates the selector’s computational
budget—intensifying refinement where uncertainty remains
high and terminating early when confidence is sufficient.

12345Number of Correctly Answered Questions per Item020406080Total Frequency-18-6+22+7+1493422224167536443130SolutionCritic1.051.101.151.201.25Perplexity Distribution020406080100120140CountCorrect Median: 1.09Incorrect Median: 1.13ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

6. Conclusion

In this paper, we propose ReThinker, an uncertainty-gated
orchestration framework for scientific reasoning tasks, and
design a stage-wise solver-critic-selector architecture. Re-
Thinker can learn from synthesized reasoning trajectories
and significantly improve inference efficiency and accuracy.
ReThinker can also acquire strong zero-shot transfer abil-
ity across expert-level benchmarks and yield an effective
initialization for few-shot adaptation to unseen scientific
domains.

References

Anthropic.
URL
claude-sonnet-4-5.

Introducing claude sonnet 4.5, 2025.
https://www.anthropic.com/news/

Bito, E., Ren, Y., and He, E. Evaluating position bias in
large language model recommendations. arXiv preprint
arXiv:2508.02020, 2025.

Chen, K., Ren, Y., Liu, Y., Hu, X., Tian, H., Xie, T., Liu,
F., Zhang, H., Liu, H., Gong, Y., et al. xbench: Track-
ing agents productivity scaling with profession-aligned
real-world evaluations. arXiv preprint arXiv:2506.13651,
2025a.

Chen, S. F. and Goodman, J. An empirical study of smooth-
ing techniques for language modeling. Computer Speech
& Language, 13(4):359–394, 1999.

Chen, W., Ma, X., Wang, X., and Cohen, W. W. Program
of thoughts prompting: Disentangling computation from
reasoning for numerical reasoning tasks. Transactions on
Machine Learning Research, 2023.

Chen, X., Aksitov, R., Alon, U., Ren, J., Xiao, K., Yin, P.,
Prakash, S., Sutton, C., Wang, X., and Zhou, D. Univer-
sal self-consistency for large language model generation.
ICML 2024 Workshop ICL, 2024.

Chen, Y., Xu, B., Wang, X., Zhang, Y., and Mao, Z. Training
llm-based agents with synthetic self-reflected trajectories
and partial masking. arXiv preprint arXiv:2505.20023,
2025b.

EvoFabric Development Team. Welcome to EvoFabric,
2025. URL https://evofabric.readthedocs.
io/en/latest/.

Google. Gemini 3 Pro: Best for complex tasks and
bringing creative concepts to life, 2025. URL https:
//deepmind.google/models/gemini/pro/.

Kimi-Researcher:

for Emerging Agentic Capabilities,

End-to-End RL Train-
2025.
https://moonshotai.github.io/

Kimi.
ing
URL
Kimi-Researcher/.

Kimi, T., Bai, Y., Bao, Y., Chen, G., Chen, J., Chen,
N., Chen, R., Chen, Y., Chen, Y., Chen, Y., et al.
Kimi k2: Open agentic intelligence. arXiv preprint
arXiv:2507.20534, 2025.

Li, X., Jin, J., Dong, G., Qian, H., Wu, Y., Wen, J.-R.,
Zhu, Y., and Dou, Z. Webthinker: Empowering large
reasoning models with deep research capability. arXiv
preprint arXiv:2504.21776, 2025.

Lightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker,
B., Lee, T., Leike, J., Schulman, J., Sutskever, I., and
In The Twelfth
Cobbe, K. Let’s verify step by step.
International Conference on Learning Representations,
2023.

Liu, A., Mei, A., Lin, B., Xue, B., Wang, B., Xu, B., Wu,
B., Zhang, B., Lin, C., Dong, C., et al. Deepseek-v3.
2: Pushing the frontier of open large language models.
arXiv preprint arXiv:2512.02556, 2025a.

Liu, J., Li, Y., Zhang, C., Li, J., Chen, A., Ji, K., Cheng,
W., Wu, Z., Du, C., Xu, Q., et al. Webexplorer: Explore
and evolve for training long-horizon web agents. arXiv
preprint arXiv:2509.06501, 2025b.

M. Bran, A., Cox, S., Schilter, O., Baldassari, C., White,
A. D., and Schwaller, P. Augmenting large language mod-
els with chemistry tools. Nature Machine Intelligence, 6
(5):525–535, 2024.

Mialon, G., Fourrier, C., Wolf, T., LeCun, Y., and Scialom,
T. Gaia: a benchmark for general ai assistants. In The
Twelfth International Conference on Learning Represen-
tations, 2023.

MiroMind, T., Bai, S., Bing, L., Chen, C., Chen, G., Chen,
Y., Chen, Z., Chen, Z., Dai, J., Dong, X., et al. Miro-
thinker: Pushing the performance boundaries of open-
source research agents via model, context, and interactive
scaling. arXiv preprint arXiv:2511.11793, 2025.

Muennighoff, N., Yang, Z., Shi, W., Li, X. L., Fei-Fei,
L., Hajishirzi, H., Zettlemoyer, L., Liang, P., Cand`es,
E., and Hashimoto, T. B. s1: Simple test-time scaling.
In Proceedings of the 2025 Conference on Empirical
Methods in Natural Language Processing, pp. 20286–
20332, 2025.

Ichihara, Y., Jinnai, Y., Morimura, T., Ariu, K., Abe, K.,
Sakamoto, M., and Uchibe, E. Evaluation of best-of-n
sampling strategies for language model alignment. arXiv
preprint arXiv:2502.12668, 2025.

Murugadoss, B., Poelitz, C., Drosos, I., Le, V., McKenna,
N., Negreanu, C. S., Parnin, C., and Sarkar, A. Evaluating
the evaluator: Measuring llms’ adherence to task evalua-
tion instructions. In Proceedings of the AAAI Conference

9

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

Wang, X., Chen, Y., Yuan, L., Zhang, Y., Li, Y., Peng, H.,
and Ji, H. Executable code actions elicit better llm agents.
In Forty-first International Conference on Machine Learn-
ing, 2024.

Wu, J., Li, B., Fang, R., Yin, W., Zhang, L., Tao, Z., Zhang,
D., Xi, Z., Fu, G., Jiang, Y., et al. Webdancer: Towards
autonomous information seeking agency. arXiv preprint
arXiv:2505.22648, 2025.

Xi, Z., Chen, W., Guo, X., He, W., Ding, Y., Hong, B.,
Zhang, M., Wang, J., Jin, S., Zhou, E., et al. The rise and
potential of large language model based agents: A survey.
Science China Information Sciences, 68(2):121101, 2025.

Xu, Z., Qiu, Z., Huang, G., Li, K., Li, S., Zhang, C., Li,
K., Yi, Q., Jiang, Y., Zhou, B., et al. Adaptive termi-
nation for multi-round parallel reasoning: An univer-
sal semantic entropy-guided framework. arXiv preprint
arXiv:2507.06829, 2025.

Yang, C., Wang, X., Lu, Y., Liu, H., Le, Q. V., Zhou, D.,
and Chen, X. Large language models as optimizers. In
The Twelfth International Conference on Learning Repre-
sentations, 2023.

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan,
K. R., and Cao, Y. React: Synergizing reasoning and
acting in language models. In The eleventh international
conference on learning representations, 2022.

Zhang, Y., Li, Y., Cui, L., Cai, D., Liu, L., Fu, T., Huang,
X., Zhao, E., Zhang, Y., Chen, Y., et al. Siren’s song in
the ai ocean: A survey on hallucination in large language
models. Computational Linguistics, pp. 1–46, 2025.

Zheng, J., Ritter, A., Das, S., and Xu, W. Probabilistic
reasoning with llms for privacy risk estimation. In The
Thirty-ninth Annual Conference on Neural Information
Processing Systems, 2025.

Zhipu. Glm-4.6: Advanced agentic, reasoning and cod-
ing capabilities, 2025. URL https://z.ai/blog/
glm-4.6.

Zhou, Z., Tan, Y., Li, Z., Yao, Y., Guo, L.-Z., Li, Y.-F.,
and Ma, X. A theoretical study on bridging internal
probability and self-consistency for llm reasoning. arXiv
preprint arXiv:2510.15444, 2025.

on Artificial Intelligence, volume 39, pp. 19589–19597,
2025.

Nakano, R., Hilton, J., Balaji, S., Wu, J., Ouyang, L., Kim,
C., Hesse, C., Jain, S., Kosaraju, V., Saunders, W., et al.
Webgpt: Browser-assisted question-answering with hu-
man feedback. arXiv preprint arXiv:2112.09332, 2021.

OpenAI.

Introducing deep research, 2025a.

URL

https://openai.com/zh-Hans-CN/index/
introducing-deep-research/.

OpenAI.

Introducing gpt-5, 2025b. URL https://

openai.com/index/introducing-gpt-5/.

Pei, Z., Zhen, H.-L., Kai, S., Pan, S. J., Wang, Y., Yuan, M.,
and Yu, B. Scope: Prompt evolution for enhancing agent
effectiveness. arXiv preprint arXiv:2512.15374, 2025.

Phan, L., Gatti, A., Han, Z., Li, N., Hu, J., Zhang, H., Zhang,
C. B. C., Shaaban, M., Ling, J., Shi, S., et al. Humanity’s
last exam. arXiv preprint arXiv:2501.14249, 2025.

Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., and
Yao, S. Reflexion: Language agents with verbal rein-
forcement learning. Advances in Neural Information
Processing Systems, 36:8634–8652, 2023.

Snell, C. V., Lee, J., Xu, K., and Kumar, A. Scaling llm
test-time compute optimally can be more effective than
scaling parameters for reasoning. In The Thirteenth Inter-
national Conference on Learning Representations, 2025.

Tang, X., Xu, W., Wang, Y., Guo, Z., Shao, D., Chen, J.,
Zhang, C., Wang, Z., Zhang, L., Wan, G., et al. Eigen-1:
Adaptive multi-agent refinement with monitor-based rag
for scientific reasoning. arXiv preprint arXiv:2509.21193,
2025.

Tian, X., Zhao, S., Wang, H., Chen, S., Ji, Y., Peng, Y., Zhao,
H., and Li, X. Think twice: Enhancing llm reasoning
by scaling multi-round test-time thinking. arXiv preprint
arXiv:2503.19855, 2025.

Tongyi, D. T., Li, B., Zhang, B., Zhang, D., Huang, F., Li, G.,
Chen, G., Yin, H., Wu, J., Zhou, J., et al. Tongyi deepre-
search technical report. arXiv preprint arXiv:2510.24701,
2025.

Truhn, D., Reis-Filho, J. S., and Kather, J. N. Large lan-
guage models should be used as scientific reasoning en-
gines, not knowledge databases. Nature medicine, 29(12):
2983–2984, 2023.

Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang,
S., Chowdhery, A., and Zhou, D. Self-consistency im-
proves chain of thought reasoning in language models.
The Twelfth International Conference on Learning Repre-
sentations, 2023.

10

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

A. Appendix

A.1. Scientific Reasoning Benchmarks for LLMs

Recent benchmarks have been proposed to evaluate the reasoning capabilities of large language models across expert-level
scientific knowledge, open-world problem solving, and executable tool use. Below we detail three representative benchmarks
with quantifiable distributions.

A.1.1. HUMANITY’S LAST EXAM (HLE)

Humanity’s Last Exam (HLE) (Phan et al., 2025) is an expert-level scientific benchmark explicitly designed to resist
shallow retrieval and pattern matching. It comprises 2,158 text-only validation questions spanning over 100 academic
disciplines, requiring deep domain expertise, multi-step causal reasoning, and precise logical inference. Unlike traditional
knowledge benchmarks where frontier models exceed 90% accuracy, HLE presents a significant challenge with most models
scoring below 10%.

The dataset emphasizes anti-retrieval characteristics through two primary question formats: 24% multiple-choice questions
requiring nuanced discrimination among highly plausible distractors, and 76% exact-match short-answer questions demand-
ing precise symbolic or conceptual responses. Table 6 presents the domain distribution, with Mathematics comprising the
largest proportion (45.23%, 976 questions), followed by Computer Science/AI (10.38%) and Biology/Medicine (10.29%).
Notably, the benchmark exhibits a substantial performance gap between human experts (average accuracy >90%) and
state-of-the-art models (Grok-4 achieves ∼25.4%, while GPT-4 and Claude-3 score <10%).

Table 6. HLE Dataset Composition and Distribution (text-only)

Category

Number of Data

Proportion (%)

Biology/Medicine
Chemistry
Computer Science/AI
Engineering
Humanities/Social Science
Math
Other
Physics

222
101
224
64
193
976
176
202

10.29
4.68
10.38
2.97
8.94
45.23
8.16
9.36

Total

2158

100.00

A.1.2. GAIA

GAIA (Mialon et al., 2023) focuses on open-world reasoning and tool-assisted problem solving through 103 text-based
validation tasks specifically curated to require multi-step planning, information synthesis, and interaction with external
tools such as web browsers and calculators. The benchmark emphasizes grounded reasoning under realistic constraints,
systematically exposing limitations in long-horizon planning and reliable tool orchestration.

Table 7. Introduction of GAIA 103 Validation (text-only)

Difficulty Question Count

Proportion (%) Avg. Human Steps

Primary Tool Requirements

Level 1
Level 2
Level 3

Total

39
52
12

103

37.86
50.49
11.65

100

< 5 steps
5-10 steps
> 10 steps

-

Minimal
Web Search+Calculator
Multi-Tool Orchestration

-

GAIA stratifies tasks into three difficulty tiers based on the complexity of required reasoning chains and tool dependencies
(Table 7). Level 1 (37.86%, 39 tasks) requires <5 reasoning steps with minimal tool usage; Level 2 (50.49%, 52 tasks)
demands 5–10 steps incorporating web search and calculation; Level 3 (11.65%, 12 tasks) necessitates >10 steps with
complex multi-tool orchestration.

11

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

A.1.3. XBENCH-DEEPSEARCH

XBench-DeepSearch (Chinese version) is a professionally curated benchmark designed to evaluate the deep search
capability of AI agents in real-world, open-domain environments. Each question requires multi-step information retrieval,
cross-source reasoning, and synthesis, rather than direct fact lookup. The dataset is constructed and continuously refreshed
by domain experts under an evergreen evaluation protocol, ensuring long-term validity and resistance to data contamination.

A standard release of XBench-DeepSearch consists of 100 questions, with problem types distributed to balance search
breadth, reasoning depth, and practical task realism. Questions are intentionally heterogeneous, spanning multiple cognitive
and operational demands commonly encountered by real-world AI agents.

Topic Domain

Number of Tasks Typical Examples

Table 8. Introduction of Xbench-DeepSearch (text-only)

Business & Finance

Current Affairs & Politics

Education & Academia

Entertainment & Media

Geography & Transportation

12

6

9

31

13

Humanities & Social Sciences

11

Natural Sciences

Sports

Technology & Engineering

3

7

8

Stock exchanges (Shanghai Gold, Shenzhen), Economic
indicators (GDP per capita), Corporate history (Alibaba
founders), Brand analysis (Arc’teryx, Balenciaga), Market
transactions

International relations (Artemis Accords, defense agree-
ments), Olympic medal adjustments, Border geography
(Northeast China), Political history (Singapore founding),
Military history (Nimitz-class carriers)

Academic institutions (HKU faculty, U of T programs),
Educational systems (Central Conservatory grading), Aca-
demic publications (CVPR papers, Nobel laureates), His-
torical academic comparisons

Variety shows (“Farewell My Love 4”, “Comedy Night”),
Music (Grammy Awards, Taylor Swift analysis), Gaming
(Black Myth: Wukong, Arknights), Film analysis (Oscar
winners, Studio Ghibli), Bilibili content

Beijing/Shanghai/Suzhou subway systems, Aviation
(Beijing to Sydney flights), Urban landmarks (Three-
monastery equidistant point), Railway schedules, Geo-
graphic information systems

Classical literature (Strange Stories from a Chinese Stu-
dio, Jin Yong novels), Historical artifacts (Tang Dynasty
contracts), Cultural heritage (Porcelain Palace), Cuisine
history, Historical events

Physical chemistry (metal melting points, Tyndall effect),
Traditional Chinese medicine (Compendium of Materia
Medica)

Competitive gaming (Dota2 TI, Esports), Professional
sports (NBA, UEFA Champions League), Board games
(Go, Snooker), Olympic swimming records

Computer science (Java API, GPU FLOPS), Artificial
intelligence (DeepSeek, OpenAI Codex), Autonomous
driving (Didi/Volvo specs), UAV technology (DJI drones),
Hardware specifications

Total

100

–

12

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

A.2. Tool Details

LLM agents in each phase is equipped with a Python interpreter, pre-configured with three specialized tools: web search,
web parse and execute python code. Table 9 provides a detailed description of each tool.

Tool

Syntax

Description

Table 9. Detailed descriptions of the tools available to LLM agents.

web search web search(keywords)

web parse

web parse(link, query)

Leverages the SERPER API to perform a web search
based on the provided keywords. It returns a list of
relevant URLs and their corresponding snippets.

Extracts targeted information from a webpage. First, it
employs the JINA API to parse the content of the given
link into Markdown format. Subsequently, an LLM is
invoked to extract and synthesize the content most relevant
to the query from the parsed text.

exec code

execute python code(code, timeout) Executes Python code asynchronously within a thread
pool executor with configurable timeout (defaulting to
3600 seconds). It captures execution output, error mes-
sages, and runtime duration. When tracing is enabled in
configuration, it incrementally persists execution records—
including contextual metadata (query ID, payload), source
code, output, and error streams—to a JSONL file using
asynchronous I/O with file locking for thread-safe audit
trails.

B. Experiments Details

B.1. Additional Experiments

B.1.1. PERFORMANCE ON HUMANITY’S LAST EXAM

Overall Performance. As shown in Table 10, the ReThinker framework demonstrates substantial improvements across all
categories when powered by Gemini-3-Pro compared to OpenPangu-72B. On aggregate metrics, Gemini-3-Pro achieves
a Pass@5 of 61.49% and Pass@1 of 52.18%, significantly outperforming OpenPangu-72B’s 43.42% and 33.09%,
respectively. The Hit Rate—measuring the proportion of problems where at least one solution is correct—increases from
76.20% to 84.85%, indicating superior solution coverage with the stronger base model.

Table 10. Performance comparison of ReThinker with different base models on HLE benchmark across categories.

Category

Biology/Medicine
Chemistry
Computer Science/AI
Engineering
Humanities/Social Sci.
Math
Other
Physics

Average

ReThinker (OpenPangu-72B)

ReThinker (Gemini-3-Pro)

Pass@5 (%)

Pass@1 (%) Hit Rate (%)

Pass@5 (%)

Pass@1 (%) Hit Rate (%)

39.64
38.61
32.59
18.75
51.30
47.85
51.70
33.66

43.42

29.73
25.74
25.45
12.50
43.01
37.81
38.64
18.32

33.09

75.00
66.67
78.08
66.67
83.84
79.01
74.73
54.41

76.20

55.86
55.45
56.25
42.19
67.88
65.16
70.45
50.99

61.49

43.69
45.54
42.86
39.06
58.55
58.30
57.39
39.11

52.18

78.23
82.14
76.19
92.59
86.26
89.47
81.45
76.70

84.85

Category-Specific Analysis. The performance gap is particularly pronounced in Engineering, where Gemini-3-Pro achieves
a 92.59% Hit Rate versus 66.67% for OpenPangu-72B, alongside a dramatic improvement in Pass@5 (42.19% vs. 18.75%).

13

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

Similarly, in Physics, Gemini-3-Pro improves the Hit Rate by 22.29 absolute percentage points (76.70% vs. 54.41%) and
more than doubles the Pass@1 performance (39.11% vs. 18.32%).

Notably, Humanities/Social Science and Other categories exhibit the highest absolute Pass@5 scores for both models,
with Gemini-3-Pro reaching 67.88% and 70.45%, respectively. Conversely, Engineering and Chemistry remain the most
challenging domains for OpenPangu-72B, with Pass@1 scores below 26%, suggesting these categories demand stronger
reasoning capabilities or domain-specific knowledge that benefit more from advanced base models.

B.1.2. PERFORMANCE ON GAIA

Overall Performance. As illustrated in Table 11, the ReThinker framework achieves strong performance on the GAIA
benchmark across both base models, with Gemini-3-Pro demonstrating superior capability in handling increasingly complex
tasks. On aggregate metrics, Gemini-3-Pro attains a Pass@5 of 92.23% and Pass@1 of 81.55%, substantially outperforming
OpenPangu-72B’s 82.52% and 72.82%, respectively. Notably, both models achieve comparable overall Hit Rates (88.24%
vs. 88.42%), suggesting that while OpenPangu-72B can often generate at least one correct solution given multiple attempts,
Gemini-3-Pro exhibits significantly higher precision and consistency in its top-ranked predictions.

Table 11. Performance of ReThinker on the GAIA benchmark across different difficulty levels.

Difficulty

Level 1
Level 2
Level 3

Average

ReThinker (OpenPangu-72B)

ReThinker (Gemini-3-Pro)

Pass@5 (%)

Pass@1 (%) Hit Rate (%)

Pass@5 (%)

Pass@1 (%) Hit Rate (%)

87.18
84.62
58.33

82.52

79.49
75.00
41.67

72.82

91.18
88.64
71.43

88.24

97.44
88.46
91.67

92.23

82.05
80.77
83.33

81.55

84.21
91.30
90.91

88.42

Scaling with Difficulty. Performance exhibits a clear degradation pattern as task complexity increases from Level 1 to
Level 3. Under OpenPangu-72B, Pass@5 drops from 87.18% (Level 1) to 58.33% (Level 3), with Pass@1 declining more
precipitously from 79.49% to 41.67%—a 37.82 percentage point reduction. Similarly, Hit Rate decreases from 91.18%
to 71.43%, indicating that harder tasks not only challenge the model’s primary reasoning but also reduce the diversity of
successful solution paths. In contrast, Gemini-3-Pro demonstrates remarkable robustness to difficulty scaling: while Level 1
and Level 2 performance remains consistently high (Pass@5 above 88%), Level 3 performance only degrades minimally to
91.67% Pass@5 and 83.33% Pass@1. Notably, Gemini-3-Pro maintains Hit Rates above 90% for Level 2 and Level 3,
though Level 1 shows a slightly lower rate at 84.21%.

Model Comparison. The performance gap between base models widens dramatically at higher difficulty levels. At Level 1,
the margin is modest (10.26 percentage points in Pass@5), but by Level 3, Gemini-3-Pro outperforms OpenPangu-72B by
33.34 percentage points in Pass@5 and 41.66 percentage points in Pass@1. This suggests that the reasoning capabilities
required for GAIA Level 3 tasks—typically involving multiple-step tool use, complex data processing, and advanced
reasoning—are more effectively captured by Gemini-3-Pro’s architecture. The consistent high Hit Rate of Gemini-3-Pro
across all difficulty levels further indicates its superior capacity to explore diverse solution strategies when given multiple
attempts.

B.1.3. PERFORMANCE ON XBENCH-DEEPSEARCH

Overall Performance. As presented in Table 12, ReThinker achieves strong performance across diverse topic domains on
the XBench-DeepSearch benchmark, with Gemini-3-Pro demonstrating consistent superiority over OpenPangu-72B. On
aggregate metrics, Gemini-3-Pro achieves 94.00% Pass@5 and 90.00% Pass@1, representing substantial improvements of
6.00 and 12.00 percentage points over OpenPangu-72B, respectively. The superior Hit Rate (95.74% vs. 88.64%) further
indicates Gemini-3-Pro’s enhanced capability to generate at least one correct solution across varied knowledge-intensive
domains.

Domain-Specific Insights. Both models achieve perfect scores in Natural Sciences and Technology & Engineering, yet
reveal intriguing asymmetries elsewhere. In Business & Finance, OpenPangu-72B attains a perfect Hit Rate (100.00%)
despite low Pass@1 (58.33%), indicating eventual solution discovery but poor ranking calibration; conversely, Gemini-3-Pro
achieves lower Hit Rate (90.91%) but higher Pass@1 (83.33%), reflecting more consistent top-ranked accuracy. Similarly,

14

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

in Entertainment & Media, OpenPangu-72B surpasses Gemini-3-Pro in Pass@5 (100.00% vs. 93.55%) while matching in
Pass@1 (83.87%), demonstrating that weaker base models can occasionally generate diverse correct solutions yet fail to
prioritize them effectively.

Table 12. Performance of ReThinker on XBench-DeepSearch across different topic domains.

Topic Domain

Business & Finance
Current Affairs & Politics
Education & Academia
Entertainment & Media
Geography & Transportation
Humanities & Social Sci.
Natural Sciences
Sports
Technology & Engineering

Average

ReThinker (OpenPangu-72B)

ReThinker (Gemini-3-Pro)

Pass@5 (%)

Pass@1 (%) Hit Rate (%)

Pass@5 (%)

Pass@1 (%) Hit Rate (%)

58.33
83.33
77.78
100.00
84.62
100.00
100.00
71.43
100.00

88.00

58.33
83.33
66.67
83.87
76.92
81.82
100.00
57.14
100.00

78.00

100.00
100.00
85.71
83.87
90.91
81.82
100.00
80.00
100.00

88.64

91.67
100.00
100.00
93.55
92.31
100.00
100.00
71.43
100.00

94.00

83.33
100.00
100.00
83.87
92.31
100.00
100.00
71.43
100.00

90.00

90.91
100.00
100.00
89.66
100.00
100.00
100.00
100.00
100.00

95.74

Persistent Challenges. Sports emerges as the sole domain where both models exhibit identical Pass@5 (71.43%) and
minimal capability disparity, suggesting that sports-related queries require specialized knowledge or reasoning patterns less
effectively captured by general-purpose LLMs regardless of base model scale. This domain-specific bottleneck highlights
fundamental limitations in current pre-training paradigms that merit targeted investigation.

B.1.4. ANALYSIS OF MULTI-CANDIDATE ANSWER DISTRIBUTION

Overall Trends. Table 13 presents the distribution of correctly identified candidates across 5-option problems for both
models. We observe significant dataset-dependent variations in performance patterns. While GEMINI-3-PRO consistently
outperforms OPENPANGU-72B in total solved problems across all three benchmarks, the disparities in candidate-level
accuracy reveal distinct behavioral differences between the models.

Table 13. Distribution of Questions by Number of Correctly Identified Candidates (k=1–5) in ReThinker.

Dataset

Model

Questions with k Correct Candidates

Total Solved Questions

HLE

GAIA

Xbench-DeepSearch

OpenPangu-72B
Gemini-3-Pro

Diff

OpenPangu-72B
Gemini-3-Pro

Diff

OpenPangu-72B
Gemini-3-Pro

Diff

1

276
174

-102

6
7

1

1
2

1

2

165
155

-10

6
4

-2

4
4

0

3

171
164

-7

7
7

0

7
9

2

4

157
291

134

20
22

2

9
11

2

5

168
543

375

46
55

9

64
68

4

937
1327

390

85
95

10

85
94

9

HLE Benchmark. On the HLE dataset, GEMINI-3-PRO demonstrates substantial advantages in high-candidate accuracy
scenarios. Specifically, the model correctly identifies all 5 candidates in 543 questions compared to OPENPANGU-72B’s
168 (relative improvement of 223%), and achieves 4 correct candidates in 291 questions versus 157 (+85%). Notably,
OPENPANGU-72B dominates in single-candidate accuracy (276 vs. 174), suggesting a propensity for partial solutions rather
than comprehensive candidate evaluation. The net difference of +390 total solved questions favors GEMINI-3-PRO, driven
primarily by its superior performance on k ≥ 4 candidates.

GAIA Benchmark. Both models show comparable performance on GAIA, with GEMINI-3-PRO solving only 10 more
questions in total (95 vs. 85). The distribution differences are minimal across all k values, with the largest discrepancy
occurring at k = 5 (∆ = +9). This indicates that both models face similar limitations on GAIA’s task distribution.

15

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

XBench-DeepSearch. The XBench-DeepSearch results demonstrate that GEMINI-3-PRO achieves consistent, modest
improvements over OPENPANGU-72B across all candidate counts, with advantages of +1 (k =1: 2 vs. 1), 0 (k =2: 4 vs. 4),
+2 (k =3: 9 vs. 7), +2 (k =4: 11 vs. 9), and +4 (k =5: 68 vs. 64). Unlike the HLE dataset, where performance diverges
dramatically at extreme candidate counts, the margin here remains relatively stable, contributing to a total improvement
of only 9 solved questions (94 vs. 85). Notably, both models exhibit a strong skew toward fully-correct scenarios (k
=5 represents 75% and 72% of solved questions respectively), suggesting that questions in this benchmark tend to yield
comprehensive solutions rather than partial candidate identification. This uniform distribution of gains indicates that
GEMINI-3-PRO’s improvements arise from general evaluation robustness rather than a polarized “all-or-nothing” strategy.

Comparative Insights. The divergent patterns across benchmarks suggest that GEMINI-3-PRO’s advantage stems pri-
marily from its ability to maintain high accuracy when multiple candidates are plausible (high k regimes), particularly in
complex reasoning scenarios (HLE). In contrast, OPENPANGU-72B tends to identify isolated correct candidates without
comprehensive coverage, resulting in higher k = 1 counts but substantially lower complete solution rates.

B.1.5. HIT RATE ANALYSIS BY GROUND-TRUTH CANDIDATE COUNT

Monotonic Reliability with Increased Correct Candidates. Table 14 reveals a consistent positive correlation between
the number of ground-truth correct candidates (k) and model hit rates across all benchmarks. Both OPENPANGU-72B
and GEMINI-3-PRO demonstrate substantially higher precision when navigating problems with dense correct answer sets
(k ≥ 4) compared to sparse configurations (k ≤ 2). Notably, both models achieve perfect accuracy (100%) on k = 5
problems across all datasets, indicating robust recognition capability when all candidate options constitute valid solutions.

Table 14. Hit Rate by Number of Ground-Truth Correct Candidates (k=1–5) in ReThinker.

Dataset

Model

Questions with k Correct Candidates

HLE

GAIA

XBench-DeepSearch

OpenPangu-72B

Gemini-3-Pro

OpenPangu-72B

Gemini-3-Pro

OpenPangu-72B

Gemini-3-Pro

1

0.431
119/276
0.299
52/174

0.000
0/6
0.286
2/7

0.000
0/1
0.500
1/2

2

0.752
124/165
0.684
106/155

0.667
4/6
0.250
1/4

0.750
3/4
0.750
3/4

3

0.901
154/171
0.878
144/164

0.714
5/7
0.857
6/7

0.571
4/7
0.778
7/9

4

0.949
149/157
0.966
281/291

1.00
20/20
0.909
20/22

0.778
7/9
1.00
11/11

5

1.00
168/168
1.00
543/543

1.00
46/46
1.00
55/55

1.00
64/64
1.00
68/68

Note. Bold indicates the higher hit rate per (dataset, k) pair. Gray numbers show hit/total counts.

Asymmetric Model Competencies at Low k Regimes. The performance gap between models exhibits pronounced dataset-
dependent asymmetries at low candidate counts. On HLE, OPENPANGU-72B significantly outperforms GEMINI-3-PRO at
k = 1 (43.1% versus 29.9%, ∆ = +13.3%) and maintains advantages at k = 2 (75.2% vs 68.4%) and k = 3 (90.1% vs
87.8%). Conversely, on GAIA and XBench-DeepSearch, GEMINI-3-PRO dominates the k = 1 regime with 28.6% and
50.0% hit rates respectively, while OPENPANGU-72B achieves 0% and 0% on these benchmarks. This dichotomy suggests
distinct architectural biases: OPENPANGU-72B excels at identifying isolated correct candidates in complex reasoning tasks
(HLE) but struggles with singleton detection in structured domains (GAIA), whereas GEMINI-3-PRO maintains minimum
viable performance across diverse task distributions.

Crossover Performance at High k Values. A critical inflection point emerges at k ≥ 4, where GEMINI-3-PRO consistently
dominates. On HLE, the model achieves 96.6% accuracy at k = 4 compared to OPENPANGU-72B’s 94.9%, representing
a reversal of the k ≤ 3 trend. This crossover pattern indicates GEMINI-3-PRO’s superior capability in comprehensive
candidate verification—when multiple correct options exist, the model effectively identifies them with near-perfect recall,
whereas OPENPANGU-72B exhibits marginally higher false negative rates in dense-candidate scenarios.

Dataset-Specific Difficulty Patterns. The GAIA benchmark presents the most challenging k = 1 scenarios, with
OPENPANGU-72B completely failing to identify solitary correct candidates (0/6), while HLE offers more tractable sparse

16

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

configurations (43.1% success). XBench-DeepSearch demonstrates intermediate difficulty but reveals the most dramatic
model divergence at k = 3, where GEMINI-3-PRO achieves 77.8% versus OPENPANGU-72B’s 57.1% (∆ = +20.7%),
suggesting that multi-hop search tasks particularly benefit from GEMINI-3-PRO’s verification mechanisms when multiple
valid solution paths exist.

B.2. HyperParameters of Inference

Table 15. Hyperparameter configuration for the ReThinker framework.

Key Parameters

Value Description

temperature

top-p (global)

top-p (in selector)

max agent step

number of parallel

1.0

1.0

0.8

50

5

Controls the randomness of text generation; higher values produce more
diverse outputs.
Global nucleus sampling threshold; probability mass cutoff for token
selection across the entire framework.
Nucleus sampling threshold specifically for the selector module to filter
candidate actions.
Maximum number of interaction steps per round; limits how many turns
the agent can take.
Number of parallel inference processes; enables concurrent exploration
of reasoning paths.

content length

128K Maximum context window size; determines the total amount of text

top-N-sigma

0.05

maximum output length

8K

(128K tokens) the model can process.
Threshold for selecting top-N candidates based on standard deviation
filtering of candidate scores.
Upper limit on the length of generated responses; prevents excessively
long outputs (8K tokens).

B.3. Construction of Latin Square

A Latin Square of order n is defined as an n × n matrix L = (lij) with entries from the set S = {1, 2, . . . , n} satisfying
the constraint that each symbol appears exactly once in each row and each column.

B.3.1. CYCLIC CONSTRUCTION (MODULAR ARITHMETIC)

The simplest construction utilizes cyclic permutations via modular arithmetic. For any n ≥ 1, the entry in row i and column
j (where i, j ∈ {0, 1, . . . , n − 1}) is computed as:

Li,j = ((i + j) mod n) + 1

(5)

This generates a standardized Latin Square where the first row contains the natural sequence (1, 2, . . . , n) and each
subsequent row is a left-cyclic shift of its predecessor. The addition modulo n ensures orthogonality: for any fixed row i, the
values (i + j) mod n are distinct as j varies; similarly, for any fixed column j, the values are distinct as i varies.

B.3.2. ALGORITHMIC REPRESENTATION

The following pseudocode implements the standard cyclic construction:

For example, with n = 5, the cyclic method produces:

4
5
1
2
3









5
1
2
3
4


1
2


3


4

5

2
3
4
5
1

3
4
5
1
2

17

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

Algorithm 1 Construct Latin Square via Cyclic Method

Require: Integer n ≥ 1
Ensure: n × n Latin Square L
1: Initialize matrix L[0 . . . n − 1][0 . . . n − 1]
2: for i ← 0 to n − 1 do
3:
4:
5:
6: end for
7: return L

L[i][j] ← ((i + j) mod n) + 1

for j ← 0 to n − 1 do

end for

C. Detailed Algorithm Descriptions

Here are the concise descriptions for each algorithm:

Algorithm 2 (Multi-Path Solution Generation): This algorithm generates N diverse solution trajectories through an
alternating Solver-Critic architecture, where the Solver constructs step-by-step reasoning chains and the Critic iteratively
refines them via trajectory summarization. By producing multiple independent reasoning paths, it mitigates sampling
stochasticity and yields a robust candidate set for downstream selection.

Algorithm 3 (Confidence-Guided Iterative Selection): This method selects the optimal solution from candidates by
leveraging Latin square permutations to eliminate position bias and perplexity scores to quantify model confidence. Through
R rounds of iterative re-selection with history aggregation, it achieves reliable decision-making via consistency-based
adjudication.

Algorithm 4 (Multi-Stage Data Quality Assurance): This pipeline curates training data through multi-stage filtering,
including answer correctness validation, format compliance verification, and semantic deduplication. It ultimately constructs
high-quality pseudo-multi-turn datasets suitable for supervised fine-tuning by enforcing logical consistency and valid tool
execution patterns.

else

Tcritic

}N
i=1

if t = 0 then
s(i)
t+1 ← Solver(q)

// Stage 1: Solver Stage
for t = 0 to Tsolver − 1 do

t+1 ← Solver(q, extract(s(i)
s(i)
end if

Algorithm 2 Pseudo-Code for Multi-Path Solution Generation.
Require: Question q, number of paths N , solver steps Tsolver, critic steps Tcritic
Ensure: Final answer set {c(i)
1: for i = 1 to N do
2:
3:
4:
5:
6:
7:
8:
9:
10:
11:
12:
13:
14:
15:
16:
17:
18:
19:
20: end for
21: return {c(i)

end for
// Apply Trajectory Summarization
(y(i), a(i), k(i)) ← Summary(q, s(i)
// Stage 2: Critic Stage
for t = 0 to Tcritic − 1 do

t+1 ← Critic(q, y(i), a(i), k(i), extract(c(i)
c(i)
end if

if t = 0 then
c(i)
t+1 ← Critic(q, y(i), a(i), k(i))

end for

t ))

t ))

Tsolver

else

)

Tcritic

}N
i=1

18

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

(cid:16)

Algorithm 3 Pseudo-Code for Confidence-Guided Iterative Selection.
Require: Problem statement q, Candidate set C = {c1, . . . , cn}, Latin square L ∈ Zn×n, Iterative number R
Ensure: Final selection s∗, Selection history H
1: Initialize: History H ← ∅
Stage 1: Initial Judgement
2: π0 ← L[0]
3: C(0) ← (π0(c1), . . . , π0(cn))
4: p0 ← FORMATPROMPT(q, C(0), history = ∅)
5: s0, x0 ← CALLLLM(p0)
6: PPL0 ← exp
7: H ← H ∪ {(s0, PPL0)}
Stage 2: Iterative Re-selection
8: for r = 1 to R do
9:
10:
11:
12:
13:

πr ← L[r mod n]
C(r) ← (πr(c1), . . . , πr(cn))
Hr ← FORMATHISTORY(H)
pr ← FORMATPROMPT(q, C(r), history = Hr)
sr, xr ← CALLLLM(pr)
(cid:16)
PPLr ← exp
H ← H ∪ {(sr, PPLr)}

(cid:17)
t=1 log pθ(xt|x<t)

(cid:17)
t=1 log pθ(xt|x<t)

− 1
|xr|

− 1
|x0|

(cid:80)|xr|

(cid:80)|x0|

14:

15:
16: end for

▷ Initial permutation (first row of Latin square)
▷ Permuted candidates

▷ Selection and rationale tokens

▷ Cyclic Latin square permutation
▷ Eliminate position bias
▷ Aggregate previous selections with PPL scores

Stage 3: Final Decision

Cfinal ← Chist
Hfinal ← FORMATHISTORY(H)
pfinal ← FORMATPROMPT(q, Cfinal, history = Hfinal)
s∗, x∗ ← CALLLLM(pfinal)
H ← H ∪ {(s∗, PPL∗)}

17: Chist ← {c ∈ C : ∃(s, ·) ∈ H, s selects c}
18: if |Chist| > 1 then
19:
20:
21:
22:
23:
24:
25: else
26:
27: end if
28: return s∗, H

s∗ ← unique element in Chist

▷ Unique selections across rounds

▷ Inconsistent selections require final adjudication
▷ Subset of historically selected candidates
▷ Full history including latest PPL

▷ Unanimous selection

29: function FORMATHISTORY(H)
30:
31: end function

return Concatenation of “Round r: sr (entropy: PPLr)” for each (sr, PPLr) ∈ H

19

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

Algorithm 4 Pseudo-Code for Multi-Stage Data Quality Assurance Pipeline.

Require: Raw trajectory dataset Draw, Predefined ratios for stages R = {r1, r2, . . . , rn}, minimum tool calls threshold

Callmin, maximum tool calls threshold Callmax

continue

continue

continue

end if
// Format and Constraint Compliance
if not (CheckFormat(T, <answer>tags) and CheckRolePairing(T)) then

end if
Df iltered ← Df iltered ∪ {T }

// Answer Correctness Validation
if LLM Judge(T.reasoning, T.ground truth) == Incorrect then

end if
Ntools ← CountToolCalls(T )
if Ntools < Callmin or Ntools > Callmax then

Ensure: Refined and augmented pseudo-multi-turn dataset Df inal
1: Df iltered ← ∅
2: for each trajectory T in Draw do
3:
4:
5:
6:
7:
8:
9:
10:
11:
12:
13:
14:
15:
16: end for
17: // Data Deduplication
18: Ddedup ← DeduplicateBySemantic(Df iltered)
19: // Balancing Dataset by Stage Ratios
20: Dbalanced ← ResampleByRatio(Ddedup, R)
21: // Quality Improvement and Generation of Pseudo-Multi-Turn Data
22: Df inal ← ∅
23: for each T in Dbalanced do
24:
25:
26:
27:
28:
29:
30:
31:
32:
33:
34:
35: end for
36: return Df inal

end if
// Tool Call Execution Validation
if HasFailedToolCall(T) then

end if
Df inal ← Df inal ∪ {N ew Sample}

continue

continue

Context ← FlattenHistoryToContext(T.QAhistory)
N ew Sample ← {User: Context + T.current query, Assistant: T.response}
// Logical Consistency Check (Thought vs. Output)
if CheckConsistency(T.thought, T.final output) == Contradictory then

20

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

D. QA-Pair Synthesis

Our scalable QA synthesis pipeline builds upon the WebExplorer framework (Liu et al., 2025b), with key modifications to
enhance automation and reduce manual effort. These improvements are achieved through two mechanisms: seed domain
initialization and automatic seed phrase updating. This section details the prompting strategies for these components,
specifically: (1) the initialization of seed phrases from user-defined domains, and (2) the automated extraction of new seed
phrases from the evolving synthesis data, which includes retrieved web contexts, newly generated QA pairs, and their
associated reasoning trajectories. The specific prompts for these processes are detailed in the following text boxes.

Prompt: Seed Phrase Initialization from Seed Domains

List 10 common phrases for each field in biology, zoology, botany, chemistry, physics, astronomy, geology,
oceanography, environmental science, psychology, sociology, economics, political science, literature, philosophy,
arts, mathematics, computer science, logic, engineering, health professions, business, education.

Put them in separate list with a high-level dictionary in python.

Prompt: Automatic Seed Phrase Extraction from Evolving Synthesis Data

You are a knowledge-enhancement expert, helping readers identify and understand complex terminology efficiently.

Analyze the following text and extract all professional, technical, academic, or uncommon noun phrases that
an average reader might not be familiar with and may need to look up for deeper understanding. Focus on
terms from specialized fields such as biology, medicine, chemistry, computer science, artificial intelligence, en-
gineering, humanity, social science, math, physics, art, philosophy, finance, linguistics, or industry-specific domains.

Ensure that you exclude common vocabulary and focus only on terms that are likely to require external knowledge
or research to fully comprehend. Prioritize precision and clarity in your explanations.

**Format requirements**: List all professional **noun phrases** with more than one word and separate them in
comma. Put them as a list inside the tags <answer> </answer>.

Text: {original content}

In addition, we enhance the model-based exploration prompt used in WebExplorer to instruct the model search diverse
websites to construct more complex questions and reduce repetitive query web-search. The enhanced prompt is provided as
below.

Prompt: Enhanced QA Generation from Web Context

You need to create a challenging question for deep search based on real information.

You should start by understanding the seed and planning diverse perspectives for search with the think tool. Then
you should collect information from the internet, then select a truth, and create a question where the truth needs to
be discovered through web search.

You will start with a random ”seed”, then web search and url browse for whatever you want on the Internet, and
create the question and truth from the information you gather.

21

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

You should collect online knowledge from different perspectives with web search and url browse tools. Then, you
should create a comprehensive and challenging question covering multiple knowledge.

You should provide several subtle and blurred clues to make the question challenging, while ensuring the truth is
unique.
There are some question examples: {examples}

Let’s start, with the seed of ”{seed}”.
You need to provide the following information in the final <answer></answer> tag:
<question> {{The challenging question you created based on real information.}} </question>
<truth> {{The one and only exact truth to the question.}} </truth>

IMPORTANT: You must include the <question> and <truth> tags in your final response for the system to parse
your answer correctly. Do not provide any other response format.

IMPORTANT: You must plan and search from at least 3 different perspectives and use knowledge from different
perspectives to construct a very challenging question, which needs multi-hop reasoning and search.

IMPORTANT: Do not search repetitive and similar queries.

E. Prompts of Test-Time Inference

Overview. The aforementioned prompts constitute the core orchestration layer of a multi-agent reasoning system, built
upon and extending the Eigen-1 architecture (Tang et al., 2025). This framework implements a hierarchical workflow that
progresses from information retrieval to structured reasoning, critical evaluation, and consensus-based selection.

Specifically, the Paper QA and Web Search prompts serve as the foundation for grounded knowledge acquisition,
ensuring factual accuracy through retrieval-augmented generation (RAG). The Solver prompt drives the initial reasoning
trajectory, augmented with code execution capabilities for precise computation and external tool integration. The Guided
Summary and Critic prompts implement a dual-review mechanism, where solutions undergo rigorous logical and factual
verification through multi-dimensional error analysis and iterative refinement. Finally, the Selector prompt operates
as the arbitration layer, employing perplexity-guided confidence estimation and cross-verification to identify the optimal
solution among diverse candidates. Collectively, these prompts instantiate an improved instantiation of the Eigen-1 paradigm,
enhancing robustness through tighter tool integration, explicit uncertainty quantification, and structured adversarial validation
loops.

Prompt: Paper QA (Academic RAG)

You are an advanced academic paper Q&A database that answers user queries in English based on reliable sources.
Your responses must not exceed 200 words. Your sources of information include: the paper itself. Your task is
to analyze user queries and provide comprehensive, reliable, and scholarly answers. Incorporate mathematical
formulas and academic content when necessary to ensure the professionalism of your response. Important note:
You must find exact information within the paper to answer the query. Avoid generating hallucinated or fabricated
responses under all circumstances. The user query is: {user query}, the paper information is: {pdf info}

22

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

Prompt: Web Search Conclusion (Structured JSON)

Please analyze the provided web content and answer the user’s question based strictly on that content:

1. Provide a comprehensive response regarding content related to the user’s question. Do not omit any details.
2. Ensure all provided information originates strictly from the web content; fabrication of non-existent information
is prohibited. If the web content cannot answer the user’s question, please state that it is irrelevant.
3. If the web content contains new URLs that might be relevant to the user’s question, list them and provide a
relevance score indicating how strongly that page relates to the user’s question.

Please reply to the user in Markdown format:

## Web Information
(Write the core content related to the user’s question here)
## Other Relevant Web Pages
### Web Page 1
#### Description
(xxx)
#### URL
(xxx)
#### Relevance Score
(0 ∼ 1)

### Web Page 2
#### Description
(xxx)
#### URL
(xxx)
#### Relevance Score
(0 ∼ 1)

Note:
1. ”Other Relevant Web Pages” must be related to the user’s question. If none exist, return an empty value.
2. Keep the overall response within 500 words, and provide only the most important relevant URLs, strictly limited
to a maximum of 2.
The user’s question is: {user}, and the web content is: {info}.

23

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

Prompt: Solver with Code Execution (Bold Content is Re-Solver variant)

The problem is: {query}

Last round answer is: {last round answer}. Please re-answer it.

Solve the problem with the help of feedback from a code executor. Every time you write a piece of code between
<code> and </code>, the code inside will be executed. For example, when encountering numerical operations,
you might write a piece of code to interpret the math problem into python code and print the final result in the code.
Based on the reasoning process and the executor feedback, you could write code to help answering the question for
multiple times (either for gaining new information or verifying). There are also several integrated functions that
can be used to help you solve the problem. The available functions are:

1. web search(keywords), this function takes keywords as input, which is a string, and the output is a string
containing several web information. This function will call a web search engine to return the search results. This
function is especially useful when answering knowledge-based questions.
2. web parse(link:str, query:str), this function takes the link and query as input, and the output is a string containing
the answer to the query according to the content in this link. This function is useful when looking into detail
information of a link.
Your workflow for solving the problem follow these steps:
- Step 1: First, analyze the question. If it can be answered directly, provide the answer immediately. If information
retrieval is required to support the answer, proceed to Step 2 and Step 3.
- Step 2: Web Search & Parse (Verification & Detail): Use ‘web search‘ to find relevant web pages for verification
or supplementation. If a specific link from the search results seems particularly useful, use ‘web parse‘ to extract
detailed information from that page.
- Step 3: Evaluate and Supplement: After receiving results from ’web search’ or ’web parse’, evaluate them
carefully. Treat this information as a supplement to your background knowledge, not as absolute truth. This
supplementary context may be incomplete or require further verification.

- You should not be overconfident in your knowledge and reasoning.

- Each time you write code put the code into <code></code> snippet, and the results must be printed out through
print function. Please strictly follow Python’s indentation rules; do not add any extra indentation to the code. Pause
after submitting any code for information retrieval or scientific computation; resume analysis only once the code
has finished running.

For example:
1. If you want to use the function of web search(keywords), will say <code>
keywords=...
results=web search(keywords)
print(results)
</code> to call the function.
2. If you want to use the function of web parse(link, query), will say <code>
link=...
query=...
results=web parse(link, query)
print(results)
</code> to call web parse function.
3. If you want to do computation, You will write code for accurate result: <code>
a = 123
b = 456

24

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

print(a+b)
</code>.

- Put your final answer in <answer></answer> with boxed.

25

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

Prompt: Guided Summary

You are a premier AI Reasoning Analyst, specializing in deconstructing and evaluating solutions to complex
problems.

Your task is to conduct a thorough analysis of the provided ”Initial Solution.” First, clearly summarize its
”Reasoning Trajectory” to map its logical flow. Then, identify critical flaws and key areas for improvement across
several dimensions. Note: You are only required to identify and explain the areas for improvement, not to generate
a revised solution.

Context:
* Problem to Solve: {problem}
* Initial Solution to Analyze: {student solution}

Your analysis must be structured into the following three parts:
Part 1: Reasoning Trajectory Summary
* In a clear, concise, and itemized list, summarize the core steps and logical flow the ”Initial Solution” took to
address the problem. This will serve as a map of its thought process.
Part 2: Final Answer
* Extract the content between <answer></answer> completely as the final answer; if extraction fails, write null.
Part 3: Key Areas for Improvement
* Analyze the solution from the following dimensions. For each point, provide specific, actionable feedback on
what could be improved.

1. Logical Rigor & Coverage:

* Reasoning Chain: Are there any logical leaps, circular arguments, or factual inaccuracies in the reasoning

process?

* Implicit Assumptions: Does the solution rely on unstated or unverified assumptions that might be flawed?
* Edge Cases & Scenarios: Did the solution overlook critical edge cases, boundary conditions, or counter-

examples?

* Examples: ”The argument assumes user input will always be a positive integer, failing to account for negative

numbers or zero.”, ”The conclusion that A causes B lacks a clear, causal link.”

2. Knowledge Depth & Breadth:

* Domain-Specific Understanding: Is the use and interpretation of key technical terms or domain-specific

concepts accurate and sufficiently deep?

* Authoritative Sourcing: Could the argument be strengthened by referencing more authoritative, credible, or

up-to-date sources?

* Multifaceted Perspectives: Could the problem be approached from different angles (e.g., historical, economic,

technological) to yield a more comprehensive insight?

* Examples: ”The analysis of ’disruptive innovation’ is superficial and doesn’t engage with Christensen’s core

theory.”, ”Citing recent academic papers or industry reports would lend more weight to the conclusion.”

3. Strategy & Structure:

* Problem Decomposition: Could the problem be broken down into smaller, more manageable sub-problems

more effectively? Is the current approach to decomposition optimal?

* Frameworks & Models: Would applying a formal analytical framework or mental model (e.g., SWOT,

First-Principles Thinking, MECE) lead to a more robust or structured answer?

* Structural Clarity: Is the overall structure of the answer logical and easy to follow? Do the paragraphs and

arguments flow coherently?

* Examples: ”The solution is presented as a flat list of points; a ’Pyramid Principle’ (Thesis-Arguments-Data)

26

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

structure would be more persuasive.”, ”A clear, multi-dimensional evaluation rubric is missing when comparing
Option A and Option B.”

4. Precision in Expression:

* Linguistic Ambiguity: Does the solution use vague, ambiguous, or overly subjective language where precision

is required?

* Clarity of Definitions: Are key concepts defined clearly and used consistently throughout the response?
* Examples: ”The use of words like ’might’ and ’potentially’ weakens the argument; it should be replaced
with data-backed assertions where possible.”, ”The definition of ’success’ shifts between paragraphs, leading to a
confusing argument.”

Output Requirements:
* Strictly adhere to the three-part structure: ”Part 1: Reasoning Trajectory Summary” and ”Part 2: Final Answer”
and ”Part 3: Key Areas for Improvement.”.
* In Part 3, use bullet points to clearly list each suggestion for improvement.
* Your analysis should be objective, constructive, and aimed at elevating the quality of the reasoning.

27

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

Prompt: Critic with Code Execution (Bold Content is Re-Solver variant)

## Problem
{query}

## Student’s Solution
{solution summary}

Last round answer is: {last round answer}. Please re-answer it.

## Your Job You should critically check the student’s solution to the problem, then correct it if needed and write
your own answer.

Solve the problem with the help of feedback from a code executor. Every time you write a piece of code between
<code> and </code>, the code inside will be executed. For example, when encountering numerical operations,
you might write a piece of code to interpret the math problem into python code and print the final result in the code.
Based on the reasoning process and the executor feedback, you could write code to help answering the question for
multiple times (either for gaining new information or verifying). There are also several integrated functions that
can be used to help you solve the problem. The available functions are:
1. web search(keywords), this function takes keywords as input, which is a string, and the output is a string
containing several web information. This function will call a web search engine to return the search results. This
function is especially useful when answering knowledge-based questions.
2. web parse(link:str, query:str), this function takes the link and query as input, and the output is a string containing
the answer to the query according to the content in this link. This function is useful when looking into detail
information of a link.

Your workflow for solving the problem follow these steps:
- Step 1: First, analyze the question. If it can be answered directly, provide the answer immediately. If information
retrieval is required to support the answer, proceed to Step 2 and Step 3.
- Step 2: Web Search & Parse (Verification & Detail): Use ‘web search‘ to find relevant web pages for verification
or supplementation. If a specific link from the search results seems particularly useful, use ‘web parse‘ to extract
detailed information from that page.
- Step 3: Evaluate and Supplement: After receiving results from ’web search’ or ’web parse’, evaluate them
carefully. Treat this information as a supplement to your background knowledge, not as absolute truth. This
supplementary context may be incomplete or require further verification.

- You should not be overconfident in your knowledge and reasoning.

- Each time you write code put the code into <code></code> snippet, and the results must be printed out through
print function. Please strictly follow Python’s indentation rules; do not add any extra indentation to the code. Pause
after submitting any code for information retrieval or scientific computation; resume analysis only once the code
has finished running.

For example:
1. If you want to use the function of web search(keywords), will say <code>
keywords=...
results=web search(keywords)
print(results)
</code> to call the function.
2. If you want to use the function of web parse(link, query), will say <code>
link=...

28

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

query=...
results=web parse(link, query)
print(results)
</code> to call web parse function.
3. If you want to do computation, You will write code for accurate result: <code>
a = 123
b = 456
print(a+b)
</code>.

- Put your final answer in <answer></answer> with boxed.

29

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

Prompt: Selector with Code Execution (Bold Content is Re-Selector variant)

You are a diligent and precise judge. You should choose the correct response from the following
{PARALLEL NUM} responses to the problem. To maximize confidence and accuracy, you must rigor-
ously verify each response using tool-based searches (‘web search‘ and ‘web parse‘), with a focus on precision
and critical evaluation of sources.

The problem is: {query}

The responses are: {responses}

Based on historical selections and their entropy values, re-perform the selection to improve the confidence
and accuracy of the model’s selection. {last selection}

## Your Task
You should thoroughly analyse each response carefully by writing codes and choose the most correct one from
{PARALLEL NUM} responses. Every time you write a piece of code between <code> and </code>, the code
inside will be executed. For example, when encountering numerical operations, you might write a piece of code to
interpret the math problem into python code and print the final result in the code. Based on the reasoning process
and the executor feedback, you could write code to help answering the question for multiple times (either for
gaining new information or verifying). There are also several integrated functions that can be used to help you
solve the problem. The available functions are:
1. web search(keywords), this function takes keywords as input, which is a string, and the output is a string
containing several web information. This function will call a web search engine to return the search results. This
function is especially useful when answering knowledge-based questions.
2. web parse(link:str, query:str), this function takes the link and query as input, and the output is a string containing
the answer to the query according to the content in this link. This function is useful when looking into detail
information of a link.

## Your Task Process is as Follows:
### 1. Preliminary Analysis and Search Planning (Plan)
- Analyze the Core of the Problem: First, what is the essence of the problem? Which key concepts, facts, or logical
relationships are involved?
- Identify Knowledge Gaps: To answer this question correctly, what key information do you need to verify or
obtain? Which statements in the options may be ambiguous or require fact-checking?
- Formulate a Search Strategy: For each key point and the options that need verification, what kind of keywords
should you use for ‘web search‘? Please list the initial list of search keywords.

### 2. Execute Iterative Search and In-depth Analysis (Search & Parse)
- First-round Search: Use the keywords you consider most core for ‘web search‘ to obtain background knowledge
and an overview of the problem.
- Evaluation and Deepening: Browse the search results and identify authoritative and relevant information sources
(such as encyclopedias, official documents, academic articles, and well-known technology websites). Use the
‘web parse‘ tool to extract detailed information directly related to the problem from these high-quality links.
- Targeted Verification: Conduct targeted searches and analysis for each option. For example, for Option A, you can
search for ”Is the core claim in Option A valid?” or ”The correct definition of the concept in Option A”. Repeat
this process for Options B, C, and D. Pay special attention to options that are contradictory or expressed in absolute
terms.
- Cross-verification: Do not rely on a single information source. For key assertions, try to conduct search
verification from another independent source (e.g., a different website or media outlet) to see if there is consensus
or disagreement.

30

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

### 3. Comprehensive Comparison and Reasoning (Synthesize & Reason)
- Information Organization: Based on the collected information, briefly summarize the supporting and opposing
evidence related to each candidate answer.
- Logical Reasoning: Conduct logical reasoning combined with verified facts. Even if a candidate answer ”sounds”
reasonable, is it inconsistent with verified facts or basic logic?
- Identify Traps: Reflect on whether any candidate answer takes advantage of common misunderstandings or
outdated information. Does the evidence you found refute these traps?

### 4. Provide Final Judgment and Evidence (Conclude)
- Final Selection: What is your final judgment on which candidate answer is correct? Please answer clearly.
- Evidence Statement: Clearly and concisely state the core evidence for your judgment, and cite credible sources
from ‘web parse‘ as much as possible. Explain why this candidate answer is the most compelling and why the
other candidate answers are excluded.

## Tool Usage Requirements:
- After each use of ‘web search‘, evaluate the relevance and authority of the results.
- Prioritize using ‘web parse‘ to obtain accurate information from high-authority, high-relevance links, rather than
relying solely on search summaries.
- Your thinking process should fully demonstrate the above steps.
- You should not be overconfident in your knowledge or reasoning.
- Each time you write code put the code into <code></code> snippet, and the results must be printed out through
print function. Please strictly follow Python’s indentation rules; do not add any extra indentation to the code. Pause
after submitting any code for information retrieval or scientific computation; resume analysis only once the code
has finished running.

For example:
1. If you want to use the function of web search(keywords), will say <code>
keywords=...
results=web search(keywords)
print(results)
</code> to call the function.
2. If you want to use the function of web parse(link, query), will say <code>
link=...
query=...
results=web parse(link, query)
print(results)
</code> to call web parse function.
3. If you want to do computation, You will write code for accurate result: <code>
a = 123
b = 456
print(a+b)
</code>.
- Finally, you should analyze whether each response is correct.

Notice
1. Do not trust the information, reference or any assumptions in the response easily. You must write codes to verify
it before reaching a conclusion.
2. Do not be influenced by the majority number of final answers. They may collude to deceive you!
3. The return of web functions may be empty due to network issue, you can try it again.
4. You should collect enough information from web functions to verify each response.

31

ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control

## Format Requirement
Your response MUST follow this exact format:

VERIFICATION:
[ Your detailed verification process for response 1 here ]
[ Your detailed verification process for response 2 here ]
...
[ Your detailed verification process for response {PARALLEL NUM} here ]

CROSS VERIFICATION
[ Search for multiple perspectives on contentious points to reduce AI hallucinations ]
CONCLUSION:
[ Your brief summarization of the verification process and the final decision ]

FINAL DECISION: <select>Response X</select>
Replace X with the response index, for example 1, 2, ..., up to {PARALLEL NUM}. The <select> tags are
required.

F. Limitations and Future Work

Despite its performance gains, ReThinker has several limitations. First, the sequential Solver–Critic–Selector pipeline
introduces additional latency, increasing wall-clock time by approximately 1.5× compared to single-pass baselines. Although
uncertainty-aware gating reduces unnecessary computation, the inherently sequential structure remains a bottleneck.

Second, the current 128K context window is insufficient for the most challenging long-horizon scientific tasks, motivating
future exploration of extended context lengths or more advanced context management strategies.

Third, ReThinker currently relies on generic search and validation tools. Integrating specialized tools—such as symbolic
theorem provers, property predictors, or structured database query engines—could further improve performance on domains
such as mathematics and chemistry. However, this would require addressing tool-specific failure modes and adaptive
invocation strategies.

Overall, these limitations highlight that ReThinker’s primary strength—adaptive orchestration—does not fully offset the
latency and context constraints inherent to multi-stage reasoning pipelines. Future work should focus on parallelizing stage
execution, developing dynamic context management mechanisms, and enabling tool-augmented reflection that can reliably
invoke specialized reasoning modules beyond generic search.

32

