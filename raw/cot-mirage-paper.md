*Response size: ~31K tokens. Consider using zotero_semantic_search to find specific content instead of reading full papers.*

# Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens

**Type:** preprint

**Item Key:** A8IEQCA4

**Date:** 2025-08-13

**Authors:** Zhao, Chengshuai; Tan, Zhen; Ma, Pingchuan; Li, Dawei; Jiang, Bohan; Wang, Yancheng; Yang, Yingzhen; Liu, Huan

**DOI:** 10.48550/arXiv.2508.01191

**URL:** http://arxiv.org/abs/2508.01191



## Extra

arXiv:2508.01191 [cs]

**Tags:** `Computer Science - Artificial Intelligence` `Computer Science - Computation and Language` `Computer Science - Machine Learning`



## Abstract

Chain-of-Thought (CoT) prompting has been shown to improve Large Language Model (LLM) performance on various tasks. With this approach, LLMs appear to produce human-like reasoning steps before providing answers (a.k.a., CoT reasoning), which often leads to the perception that they engage in deliberate inferential processes. However, some initial findings suggest that CoT reasoning may be more superficial than it appears, motivating us to explore further. In this paper, we study CoT reasoning via a data distribution lens and investigate if CoT reasoning reflects a structured inductive bias learned from in-distribution data, allowing the model to conditionally generate reasoning paths that approximate those seen during training. Thus, its effectiveness is fundamentally bounded by the degree of distribution discrepancy between the training data and the test queries. With this lens, we dissect CoT reasoning via three dimensions: task, length, and format. To investigate each dimension, we design DataAlchemy, an isolated and controlled environment to train LLMs from scratch and systematically probe them under various distribution conditions. Our results reveal that CoT reasoning is a brittle mirage that vanishes when it is pushed beyond training distributions. This work offers a deeper understanding of why and when CoT reasoning fails, emphasizing the ongoing challenge of achieving genuine and generalizable reasoning.

**Notes/Attachments:** 2

---

## Full Text

Data Mining and Machine Learning Lab
| Is Chain-of-Thought |     |     |      |     |              | Reasoning |     |      | of  | LLMs |     | a   |     |
| ------------------- | --- | --- | ---- | --- | ------------ | --------- | --- | ---- | --- | ---- | --- | --- | --- |
| Mirage?             |     | A   | Data |     | Distribution |           |     | Lens |     |      |     |     |     |
ChengshuaiZhao1,ZhenTan1,PingchuanMa1,DaweiLi1,BohanJiang1,YanchengWang1,YingzhenYang1
andHuanLiu1
1ArizonaStateUniversity,USA
Chain-of-Thought(CoT)promptinghasbeenshowntoimproveLargeLanguageModel(LLM)performance
on various tasks. With this approach, LLMs appear to produce human-like reasoning steps before
providing answers (a.k.a., CoT reasoning), which often leads to the perception that they engage in
5202 guA 31  ]IA.sc[  3v19110.8052:viXra deliberateinferentialprocesses. However,someinitialfindingssuggestthatCoTreasoningmaybemore
superficialthanitappears,motivatingustoexplorefurther. Inthispaper,westudyCoTreasoningviaa
datadistributionlensandinvestigateifCoTreasoningreflectsastructuredinductivebiaslearnedfrom
in-distributiondata, allowingthe modeltoconditionallygenerate reasoning pathsthatapproximate
thoseseenduringtraining. Thus,itseffectivenessisfundamentallyboundedbythedegreeofdistribution
discrepancybetweenthetrainingdataandthetestqueries. Withthislens,wedissectCoTreasoningvia
threedimensions: task,length,andformat. Toinvestigateeachdimension,wedesign DataAlchemy,
anisolatedandcontrolledenvironmenttotrainLLMsfromscratchandsystematicallyprobethemunder
variousdistributionconditions. OurresultsrevealthatCoTreasoningisabrittlemiragethatvanishes
whenitispushedbeyondtrainingdistributions. Thisworkoffersadeeperunderstandingofwhy and
whenCoTreasoningfails,emphasizingtheongoingchallengeofachievinggenuineandgeneralizable
reasoning. OurcodeisavailableatGitHub:https://github.com/ChengshuaiZhao0/DataAlchemy.
1. Introduction
| Recent | years | have witnessed |     | Large |     | Language |     |     |     |     |     |     |     |
| ------ | ----- | -------------- | --- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Test Cases
| Models’ | (LLMs) | dominant |     | role | in various | do- |     |     |     |     |     | Distribution |     |
| ------- | ------ | -------- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | ------------ | --- |
Discrepancy
| mains (Li     | et al., | 2025b; | Ting    | et        | al., 2025; | Zhao    |     |     |     |     |     |     |     |
| ------------- | ------- | ------ | ------- | --------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| et al., 2025, |         | 2023)  | through | versatile |            | prompt- |     |     |     |     |     |     |     |
Format
| ing techniques |     | (Kojima | et  | al., 2022; |     | Wei et al., |     |     |     |     |     |     |     |
| -------------- | --- | ------- | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Training
| 2022; Yao | et  | al., 2023). |     | Among | these, | Chain- |     |     |     |     |     |     |     |
| --------- | --- | ----------- | --- | ----- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
   Data
| of-Thought | (CoT) | prompting |     | (Wei | et  | al., 2022) |     |     |     |     |     |     |     |
| ---------- | ----- | --------- | --- | ---- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Training
| has emerged      |           | as a prominent |               | method       |            | for elic- |        | Task |          | Length      |     |           |         |
| ---------------- | --------- | -------------- | ------------- | ------------ | ---------- | --------- | ------ | ---- | -------- | ----------- | --- | --------- | ------- |
| iting structured |           | reasoning      |               | from         | LLMs       | (a.k.a.,  |        |      |          |             |     | Testing   |         |
| CoT reasoning).  |           | By             | appending     |              | a simple   | cue       |        |      |          |             |     |           |         |
| such as          | “Let’s    | think          | step by       | step,”       | LLMs       | decom-    |        |      |          |             |     |           |         |
| pose complex     |           | problems       | into          | intermediate |            | steps,    |        |      |          |             |     |           |         |
| producing        | outputs   |                | that resemble |              | human-like |           |        |      |          |             |     |           |         |
| reasoning.       | It        | has been       | shown         |              | to be      | effective |        |      |          |             |     |           |         |
|                  |           |                |               |              |            |           | Figure | 1 |  | The data | perspective |     | lens. CoT | reason- |
| in tasks         | requiring | logical        |               | inference(Xu |            | et al.,   |        |      |          |             |     |           |         |
2024), mathematical problem solving (Imani ing’s effectiveness is fundamentally bounded by
thedegreeofdistributiondiscrepancybetweenthe
etal.,2023),andcommonsensereasoning(Wei
|              |     |                                |     |     |     |     | training | data       | and | the test      | queries. | Guided    | by this |
| ------------ | --- | ------------------------------ | --- | --- | --- | --- | -------- | ---------- | --- | ------------- | -------- | --------- | ------- |
| etal.,2022). |     | TheempiricalsuccessesofCoTrea- |     |     |     |     |          |            |     |               |          |           |         |
|              |     |                                |     |     |     |     | lens,    | we dissect |     | CoT reasoning |          | via three | dimen-  |
soningleadtotheperceptionthatLLMsengage
|               |         |             |           |     |                |         | sions: | task, | length, | and | format. |     |     |
| ------------- | ------- | ----------- | --------- | --- | -------------- | ------- | ------ | ----- | ------- | --- | ------- | --- | --- |
| in deliberate |         | inferential | processes |     | (Ling          | et al., |        |       |         |     |         |     |     |
| 2023; Yu      | et al., | 2023;       | Zhang     | et  | al., 2024a,c). |         |        |       |         |     |         |     |     |
Correspondingauthor(s): {czhao93,ztan36,pingchua,daweili5,bjiang14,yancheng.wang,yingzhen.yang,huanliu}@asu.edu

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
However,acloserexaminationrevealsinconsistenciesthatchallengethisoptimisticview. Consider
this straightforward question: “The day the US was established is in a leap year or a normal year?”
When prompted with the CoT prefix, the modern LLM Gemini responded: “The United States was
established in 1776. 1776 is divisible by 4, but it’s not a century year, so it’s a leap year. Therefore, the
day the US was established was in a normal year.” This response exemplifies a concerning pattern: the
modelcorrectlyrecitestheleapyearruleandarticulatesintermediatereasoningsteps,yetproducesa
logically inconsistent conclusion (i.e., asserting 1776 is both a leap year and a normal year). Such
inconsistencies suggest that there is a distinction between human-like inference and CoT reasoning.
AnexpandingbodyofanalysesrevealsthatLLMstendtorelyonsurface-levelsemanticsandclues
ratherthanlogicalprocedures(Chenetal.,2025b;Kambhampati,2024;Lanhametal.,2023;Stechly
et al., 2024). LLMs construct superficial chains of logic based on learned token associations, often
failingontasksthatdeviatefromcommonsenseheuristicsorfamiliartemplates(Tangetal.,2023). In
the reasoning process, performance degrades sharply when irrelevant clauses are introduced, which
indicatesthatmodelscannotgrasptheunderlyinglogic(Mirzadehetal.,2024). Thisfragilitybecomes
even more apparent when models are tested on more complex tasks, where they frequently produce
incoherent solutions and fail to follow consistent reasoning paths (Shojaee et al., 2025). Collectively,
these pioneering works deepen the skepticism surrounding the true nature of CoT reasoning.
In light of this line of research, we question the CoT reasoning by proposing an alternative lens
through data distribution and further investigating why and when it fails. We hypothesize that
CoT reasoning reflects a structured inductive bias learned from in-distribution data, allowing the
model to conditionally generate reasoning paths that approximate those seen during training. As
such, its effectiveness is inherently limited by the nature and extent of the distribution discrepancy
between training data and the test queries. Guided by this data distribution lens, we dissect CoT
reasoningviathreedimensions: (i)task—TowhatextentCoTreasoningcanhandletasksthatinvolve
transformations or previously unseen task structures. (2) length—how CoT reasoning generalizes to
chains with length different from that of training data; and (3) format—how sensitive CoT reasoning
is to surface-level query form variations. To evaluate each aspect, we introduce DataAlchemy,
a controlled and isolated experiment that allows us to train LLMs from scratch and systematically
probe them under various distribution shifts.
Our findings reveal that CoT reasoning works effectively when applied to in-distribution or near
in-distribution data but becomes fragile and prone to failure even under moderate distribution shifts.
Insomecases,LLMsgeneratefluentyetlogicallyinconsistentreasoningsteps. Theresultssuggestthat
what appears to be structured reasoning can be a mirage, emerging from memorized or interpolated
patternsinthetrainingdataratherthanlogicalinference. Theseinsightscarryimportantimplications
for both practitioners and researchers. For practitioners, our results highlight the risk of relying on
CoT as a plug-and-play solution for reasoning tasks and caution against equating CoT-style output
with human thinking. For researchers, the results underscore the ongoing challenge of achieving
reasoningthatisbothfaithfulandgeneralizable,motivatingtheneedtodevelopmodelsthatcanmove
beyond surface-level pattern recognition to exhibit deeper inferential competence. Our contributions
are summarized as follows:
★ Novel perspective. We propose a data distribution lens for CoT reasoning, illuminating that its
effectivenessstemsfromstructuredinductivebiaseslearnedfromin-distributiontrainingdata. This
framework provides a principled lens for understanding why and when CoT reasoning succeeds or
fails.
★ Controlled environment. Weintroduce DataAlchemy,anisolatedexperimentalframework
that enables training LLMs from scratch and systematically probing CoT reasoning. This controlled
setting allows us to isolate and analyze the effects of distribution shifts on CoT reasoning without
2

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
interference from complex patterns learned during large-scale pre-training.
★ Empiricalvalidation. Weconductsystematicempiricalvalidationacrossthreecriticaldimensions—
task, length, and format. Our experiments demonstrate that CoT reasoning exhibits sharp perfor-
mance degradation under distribution shifts, revealing that seemingly coherent reasoning masks
shallow pattern replication.
★ Real-world implication. This work reframes the understanding of contemporary LLMs’ reasoning
capabilities and emphasizes the risk of over-reliance on COT reasoning as a universal problem-
solvingparadigm. Itunderscoresthenecessityforproperevaluationmethodsandthedevelopment
of LLMs that possess authentic and generalizable reasoning capabilities.
2. Related Work
2.1. LLM Prompting and CoT
Chain-of-Thought (CoT) prompting revolutionized how we elicit reasoning from Large Language
Modelsbydecomposingcomplexproblemsintointermediatesteps(Weietal.,2022). Byaugmenting
few-shot exemplars with reasoning chains, CoT showed substantial performance gains on various
tasks(Imanietal.,2023;Weietal.,2022;Xuetal.,2024). Buildingonthis,severalvariantsemerged.
Zero-shot CoT triggers reasoning without exemplars using instructional prompts (Kojima et al.,
2022), and self-consistency enhances performance via majority voting over sampled chains (Wang
et al., 2023). To reduce manual effort, Auto-CoT generates CoT exemplars using the models them-
selves (Zhang et al., 2023). Beyond linear chains, Tree-of-Thought (ToT) frames CoT as a tree search
over partial reasoning paths (Yao et al., 2023), enabling lookahead and backtracking. SymbCoT
combines symbolic reasoning with CoT by converting problems into formal representations (Xu
et al., 2024). Recent work increasingly integrates CoT into the LLM inference process, generating
long-form CoTs (Guo et al., 2025; Jaech et al., 2024; Team et al., 2025; Team, 2024). This enables
flexible strategies like mistake correction, step decomposition, reflection, and alternative reasoning
paths(Chenetal.,2025a;Yeoetal.,2025). Thesuccessofpromptingtechniquesandlong-formCoTs
has led many to view them as evidence of emergent, human-like reasoning in LLMs. In this work, we
challengethatviewpointbyadoptingadata-centricperspectiveanddemonstratingthatCoTbehavior
arises largely from pattern matching over training distributions.
2.2. Discussion on Illusion of LLM Reasoning
WhileChain-of-Thoughtpromptinghasledtoimpressivegainsoncomplexreasoningtasks,agrowing
body of work has started questioning the nature of these gains (Kambhampati et al., 2025; Stechly
et al., 2024, 2025). One major line of research highlights the fragility of CoT reasoning. Minor and
semantically irrelevant perturbations such as distractor phrases or altered symbolic forms can cause
significant performance drops in state-of-the-art models (Mirzadeh et al., 2024; Tang et al., 2023).
Models often incorporate such irrelevant details into their reasoning, revealing a lack of sensitivity
to salient information. Other studies show that models prioritize the surface form of reasoning over
logical soundness; in some cases, longer but flawed reasoning paths yield better final answers than
shorter, correct ones (Bentham et al., 2024). Similarly, performance does not scale with problem
complexity as expected—models may overthink easy problems and give up on harder ones (Shojaee
et al., 2025). Another critical concern is the faithfulness of the reasoning process. Intervention-based
studies reveal that final answers often remain unchanged even when intermediate steps are falsified
oromitted(Lanhametal.,2023),aphenomenondubbedtheillusionoftransparency(Benthametal.,
2024; Chen et al., 2025b). Together, these findings suggest that LLMs are not principled reasoners
but rather sophisticated simulators of reasoning-like text. However, a systematic understanding of
3

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
Task Generalization
|     |       | Basic Atoms |       |       |     | Element Gen. |       |     |     | Transformation Gen.  |     | Input  |
| --- | ----- | ----------- | ----- | ----- | --- | ------------ | ----- | --- | --- | -------------------- | --- | ------ |
| A   | B C D | E F G       | H I J | K L M |     |              |       |     |     | ID 𝑓1 ◦ 𝑓1 → 𝑓1 ◦ 𝑓1 |     |        |
|     |       |             |       |       | ID  | A B C        | D A B | C D |     |                      |     | Output |
N O P Q R S T U V W X Y Z C M P { 𝑓 1  ◦   𝑓 1,  𝑓 1  ◦   𝑓 2 ,  𝑓2 ◦ 𝑓1} → 𝑓2 ◦ 𝑓2
|     |     |                |     |     | CMP | A B C | D D C | B A | 𝑓 S | 𝑓 1  ◦ 𝑓 1  →     | 𝑓 1   ◦  𝑓 2 |          |
| --- | --- | -------------- | --- | --- | --- | ----- | ----- | --- | --- | ----------------- | ------------ | -------- |
|     |     | El emen t (l = |  5) |     |     |       |       |     | P   | O O D             |              | Training |
|     |     |                |     |     | OOD | A B C | D A B | C E | OOD | 𝑓1 ◦ 𝑓1 → 𝑓2 ◦ 𝑓2 |              |          |
Testing
|                        | A   | P P | L E              |     |     |                       |     |     |     |     |                       |     |
| ---------------------- | --- | --- | ---------------- | --- | --- | --------------------- | --- | --- | --- | --- | --------------------- | --- |
|                        |     |     |                  |     |     | Length Generalization |     |     |     |     | Format Generalization |     |
| 𝑓1: ROT Transformation |     |     | 𝑓2: Cyclic Shift |     |     |                       |     |     |     |     |                       |     |
Text Length Gen.
|     | +13   |     |     | +1    |     |     |     | Reasoning Step Gen. |                      | Insert |                 |     |
| --- | ----- | --- | --- | ----- | --- | --- | --- | ------------------- | -------------------- | ------ | --------------- | --- |
|     |       |     |     |       | A B | C D |     |                     |                      | A      | B C D A B ? C D |     |
| A   | P P L | E   | A P | P L E |     |     |     | 𝑓S: 𝑓 1  ◦          | 𝑓 1  →   𝑓 1         |        |                 |     |
|     |       |     |     |       | A B | C   |     |                     | Delete               | A      | B C D A C D     | 𝑓 S |
|     |       |     |     |       |     |     |     | 𝑓1 ◦ 𝑓 1  →         |   𝑓 1   ◦   𝑓 1 ◦ 𝑓1 |        |                 |     |
|     |       |     |     |       |     |     |     |                     | Modify               | A      | B C D A B C ?   |     |
| N   | C C Y | R   | E A | P P L | A B | C D | A   |                     |                      |        |                 |     |
|
Figure 2 Framework of DataAlchemy. It creates an isolated and controlled environment to train
LLMs from scratch and probe the task, length, and format generalization.
| why  | and | when CoT       | reasoning |     | fails is | still a | mystery. |     |     |     |     |     |
| ---- | --- | -------------- | --------- | --- | -------- | ------- | -------- | --- | --- | --- | --- | --- |
| 2.3. | OOD | Generalization |           | of  | LLMs     |         |          |     |     |     |     |     |
Out-of-distribution (OOD) generalization, where test inputs differ from training data, remains a
key challenge in machine learning, particularly for large language models (LLMs)(Budnikov et al.,
2025; Yang et al., 2024, 2023; Zhang et al., 2024b). Recent studies show that LLMs prompted
to learn novel functions often revert to similar functions encountered during pretraining (Garg
et al., 2022; Wang et al., 2024). Likewise, LLM generalization frequently depends on mapping new
problems onto familiar compositional structures (Song et al., 2025). CoT prompting improves OOD
generalization (Wei et al., 2022), with early work demonstrating length generalization for multi-step
problems beyond training distributions (Shen et al., 2025; Yao et al., 2025). However, this ability is
not inherent to CoT and heavily depends on model architecture and training setups. For instance,
stronggeneralizationinarithmetictaskswasachievedonlywhenalgorithmicstructureswereencoded
into positional encodings (Cho et al., 2024). Similarly, finer-grained CoT demonstrations during
trainingboostOODperformance,highlightingtheimportanceofdatagranularity(Wangetal.,2025a).
TheoreticalandempiricalevidenceshowsthatCoTgeneralizeswellonlywhentestinputssharelatent
structures with training data; otherwise, performance declines sharply (Li et al., 2025a; Wang et al.,
2025b). Despite its promise, CoT still struggles with genuinely novel tasks or formats. In the light
of these brilliant findings, we propose rethinking CoT reasoning through a data distribution lens:
decomposing CoT into task, length, and format generalization, and systematically investigating each
| in a | controlled | setting. |              |     |      |     |     |     |     |     |     |     |
| ---- | ---------- | -------- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
| 3.   | The        | Data     | Distribution |     | Lens |     |     |     |     |     |     |     |
We propose a fundamental reframing to understand what CoT actually represents. We hypothesize
thattheunderlyingmechanismisbetterunderstoodthroughthelensofdatadistribution: ratherthan
executingexplicitreasoningprocedures,CoToperatesasapattern-matchingprocessthatinterpolates
and extrapolates from the statistical regularities present in its training distribution. Specifically, we
posit that CoT’s success stems not from a model’s inherent reasoning capacity, but from its ability
to generalize conditionally to out-of-distribution (OOD) test cases that are structurally similar to
| in-distribution |     | exemplars. |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
To formalize this view, we model CoT prompting as a conditional generation process constrained
by the distributional properties of the training data. Let D denote the training distribution over
train
input-outputpairs (𝑥,𝑦),where𝑥 representsareasoningproblemand 𝑦 denotesthesolutionsequence
|     |     |     |     |     |     |     |     |     |     |     | 𝑓 (𝑥) 𝑦byminimizing |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- |
(includingintermediatereasoningsteps). Themodellearnsanapproximation 𝜃 ≈
4

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
| empirical | risk over | samples | drawn | from | D   | .   |     |     |     |     |
| --------- | --------- | ------- | ----- | ---- | --- | --- | --- | --- | --- | --- |
train
| Let the | expected | training | risk | be defined |        | as:     |      |          |     |     |
| ------- | -------- | -------- | ---- | ---------- | ------ | ------- | ---- | -------- | --- | --- |
|         |          |          |      | 𝑅          | (𝑓 ) = | 𝔼       | [ℓ(𝑓 | (𝑥),𝑦)], |     | (1) |
|         |          |          |      | train      | 𝜃      | (𝑥,𝑦)∼D |      | 𝜃        |     |     |
train
where ℓ is a task-specific loss function (e.g., cross-entropy, token-level accuracy). At inference time,
given a test input 𝑎 sampled from a potentially different distribution D , the model generates a
|     |     | test |     |     |     |     |     |     | test |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | ---- | --- |
|     | 𝑦   |      |     |     |     |     | D   |     |      |     |
response test conditioned on patterns learned from train . The corresponding expected test risk is:
|     |     |     |     | 𝑅    | (𝑓 ) = | 𝔼       | [ℓ(𝑓 | (𝑥),𝑦)]. |     | (2) |
| --- | --- | --- | --- | ---- | ------ | ------- | ---- | -------- | --- | --- |
|     |     |     |     | test | 𝜃      | (𝑥,𝑦)∼D |      | 𝜃        |     |     |
test
The degree to which the model generalizes from D to D is governed by the distributional
|     |     |     |     |     |     |     | train | test |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | --- | --- |
discrepancy between the two, which we quantify using divergence measures:
D
Definition 3.1 (Distributional Discrepancy). Given training distribution train and test distribution
| D , the | distributional | discrepancy |     | is  | defined | as: |     |     |     |     |
| ------- | -------------- | ----------- | --- | --- | ------- | --- | --- | --- | --- | --- |
test
|     |     |     |     | Δ(D | ,D    | ) =  | H(D   | ∥ D ) |     | (3) |
| --- | --- | --- | --- | --- | ----- | ---- | ----- | ----- | --- | --- |
|     |     |     |     |     | train | test | train | test  |     |     |
where H(· ∥ ·) is a divergence measure (e.g., KL divergence, Wasserstein distance) that quantifies the
| statistical | distance | between | the | two distributions. |     |     |     |     |     |     |
| ----------- | -------- | ------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
Theorem 3.1 (CoT Generalization Bound). Let 𝑓 𝜃 denote a model trained on D with expected
train
|     | 𝑅   | (𝑓 ). |     |     |     | D   |     |     | 𝑅 (𝑓 ) |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | ------ | --- |
training risk train 𝜃 For a test distribution test , the expected test risk test 𝜃 is bounded by:
|     |     |     |     |     |     |     |     | (cid:32)√︂ | (cid:33) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- |
log(1/𝛿)
|     |     | 𝑅    | (𝑓 ) | ≤ 𝑅   | (𝑓 )+Λ·Δ(D |     | ,D    | )+O  |     | (4) |
| --- | --- | ---- | ---- | ----- | ---------- | --- | ----- | ---- | --- | --- |
|     |     | test | 𝜃    | train | 𝜃          |     | train | test | 𝑛   |     |
| Λ   | >   |      |      |       |            |     |       |      |     | 𝑛   |
where 0 is a Lipschitz constant that depends on the model architecture and task complexity, is the
training sample size, and the bound holds with probability 1−𝛿, where 𝛿 is the failure probability.
| The proof | is  | provided | in Appendix |     | A.1 |     |     |     |     |     |
| --------- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Building on this data distribution perspective, we identify three critical dimensions along which
distributional shifts can occur, each revealing different aspects of CoT’s pattern-matching nature:
➊TaskgeneralizationexamineshowwellCoTtransfersacrossdifferenttypesofreasoningtasks.
Novel
tasks may have unique elements and underlying logical structure, which introduces distributional
shifts that challenge the model’s ability to apply learned reasoning patterns. ➋ Length generalization
investigates CoT’s robustness to reasoning chains of varying lengths. Since training data typically
containsreasoningsequenceswithinacertainlengthrange,testcasesrequiringsubstantiallylongeror
shorter reasoning chains represent a form of distributional shift along the sequence length dimension.
This length discrepancy could result from the reasoning step or the text-dependent solution space.
➌
Format generalization explores how sensitive CoT is to variations in prompt formulation and
structure. Due to various reasons (e.g., sophistical training data or diverse background of users), it
is challenging for LLM practitioners to design a golden prompt to elicit knowledge suitable for the
current case. Their detailed definition and implementation are given in subsequent sections.
Each dimension provides a unique lens for understanding the boundaries of CoT’s effectiveness
and the mechanisms underlying its apparent reasoning capabilities. By systematically varying these
dimensions in controlled experimental settings, we can empirically validate our hypothesis that
CoT performance degrades predictably as distributional discrepancy increases, thereby revealing its
fundamental nature as a pattern-matching rather than reasoning system.
5

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
| 4. DataAlchemy: |     |     | An  | Isolated | and | Controlled |     | Environment |     |     |     |     |
| --------------- | --- | --- | --- | -------- | --- | ---------- | --- | ----------- | --- | --- | --- | --- |
To systematically investigate the influence of distributional shifts on CoT reasoning capabilities, we
introduce DataAlchemy, a synthetic dataset framework designed for controlled experimentation.
Thisenvironmentenablesustotrainlanguagemodelsfromscratchunderpreciselydefinedconditions,
allowingforrigorousanalysisofCoTbehavioracrossdifferentOODscenarios. Theoverviewisshown
| in Figure  | 2.            |     |          |     |     |     |     |     |     |     |     |     |
| ---------- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4.1. Basic | Atoms         | and | Elements |     |     |     |     |     |     |     |     |     |
| A =        | {A,B,C,...,Z} |     |          |     |     |     |     |     |     |     |     |     |
Let denotethealphabetof26basicatoms. Anelementeisdefinedasanordered
| sequence | of atoms: |     |     |     |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ℤ+
|     |     |     |     | e = (𝑎 | ,𝑎 ,...,𝑎 |     | ) where | 𝑎   | ∈ A, | 𝑙 ∈ |     | (5) |
| --- | --- | --- | --- | ------ | --------- | --- | ------- | --- | ---- | --- | --- | --- |
|     |     |     |     |        | 0 1       | 𝑙−1 |         |     | 𝑖    |     |     |     |
|A|𝑙)byvarying
ThisdesignprovidesaversatilemanipulationforthesizeofthedatasetD (i.e., |D| =
𝑙
element length to train language models with various capacities. Meanwhile, it also allows us to
| systematically |     | probe | text | length | generalization |     | capabilities. |     |     |     |     |     |
| -------------- | --- | ----- | ---- | ------ | -------------- | --- | ------------- | --- | --- | --- | --- | --- |
4.2. Transformations
|     |     |     |     |     |     |     |     |     | 𝐹   | →   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A transformation is an operation that operates on elements : e eˆ. In this work, we consider two
fundamentaltransformations: theROTTransformationandtheCyclicPositionShift. Toformallydefine
thetransformations,weintroduceabijectivemapping𝜙 : A → ℤ ,whereℤ = {0,1,...,25},such
|     |     |     |     |     |     |     |     |     |     | 26  | 26  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝜙(𝑐)
| that | maps | a character |     | to its | zero-based | alphabetical |     | index. |     |     |     |     |
| ---- | ---- | ----------- | --- | ------ | ---------- | ------------ | --- | ------ | --- | --- | --- | --- |
Definition 4.1 (ROT Transformation). Given an element e = (𝑎 ,...,𝑎 ) and a rotation parameter
|     |     |     |     |     |     |     |     |     | 0   | 𝑙−1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑛 ∈ ℤ, the ROT Transformation 𝑓 produces an element eˆ = (𝑎ˆ ,...,𝑎ˆ𝑙−1 ). Each atom 𝑎ˆ𝑖 is:
|     |     |     |     |     | rot          |     |      |      | 0    |     |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | ---- | ---- | ---- | --- | --- | --- |
|     |     |     |     |     | 𝑎ˆ𝑖 𝜙−1((𝜙(𝑎 |     | )+𝑛) |      |      |     |     |     |
|     |     |     |     |     | =            |     | 𝑖    | (mod | 26)) |     |     | (6) |
𝑛
This operation cyclically shifts each atom positions forward in alphabetical order. For example, if
| e = (A,P,P,L,E) |     | and | 𝑛 = | 13, then | 𝑓 (e,13) | =   | (N,C,C,Y,R). |     |     |     |     |     |
| --------------- | --- | --- | --- | -------- | -------- | --- | ------------ | --- | --- | --- | --- | --- |
rot
Definition 4.2 (Cyclic Position Shift). Given an element e = (𝑎 ,...,𝑎 𝑙−1 ) and a shift parameter 𝑛 ∈ ℤ,
0
|     |     |     | 𝑓   |     |     |     |     | (𝑎ˆ ,...,𝑎ˆ𝑙−1 | ).  |     | 𝑎ˆ𝑖 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
the Cyclic Position Shift pos produces an element eˆ = 0 Each atom is defined by a cyclic
shift of indices:
|     |     |     |     |     |     | 𝑎ˆ𝑖 = | 𝑎     |        |     |     |     | (7) |
| --- | --- | --- | --- | --- | --- | ----- | ----- | ------ | --- | --- | --- | --- |
|     |     |     |     |     |     |       | (𝑖−𝑛) | (mod𝑙) |     |     |     |     |
This transformation cyclically shifts the positions of the atoms within the sequence by 𝑛 positions to the
|            |           |     | (A,P,P,L,E) |     |     | 𝑛   |         | 𝑓   | (e,1) | (E,A,P,P,L). |     |     |
| ---------- | --------- | --- | ----------- | --- | --- | --- | ------- | --- | ----- | ------------ | --- | --- |
| right. For | instance, | if  | e =         |     | and | =   | 1, then |     | =     |              |     |     |
pos
Definition 4.3 (Generalized Compositional Transformation). To model multi-step reasoning, we define
a compositional transformation as the successive application of a sequence of operations. Let 𝑆 =
| (𝑓 , 𝑓 ,..., | 𝑓   |     |     |     |     |     |     | 𝑓   |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 2 𝑘 ) be a sequence of operations, where each 𝑖 is one of the fundamental transformations
F = {𝑓 , 𝑓 } with its respective parameters. The compositional transformation 𝑓 for the sequence𝑆 is
| rot          | pos          |     |     |     |     |     |           |       |     |     | S   |     |
| ------------ | ------------ | --- | --- | --- | --- | --- | --------- | ----- | --- | --- | --- | --- |
| the function | composition: |     |     |     |     |     |           |       |     |     |     |     |
|              |              |     |     |     |     | 𝑓 = | 𝑓 𝑘 ◦ 𝑓 𝑘 | ◦···◦ | 𝑓   |     |     | (8) |
|              |              |     |     |     |     | S   |           |       | 1   |     |     |     |
The resulting element eˆ is obtained by applying the operations sequentially to an initial element e:
|     |     |     |     |     |      | 𝑓 (𝑓  | (...(𝑓 | (e))...)) |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | ----- | ------ | --------- | --- | --- | --- | --- |
|     |     |     |     |     | eˆ = | 𝑘 𝑘−1 |        | 1         |     |     |     | (9) |
6

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
This design enables the construction of arbitrarily complex transformation chains by varying the
type, parameters, order, and length of operations within the sequence. At the sample time, we can
naturally acquire the COT reasoning step by decomposing the intermediate process:
|     |     |     |                                      |           | 𝑓 e(1)                                                                                                                                                                                                                                                                                                                                                           | 𝑓   | e(2)               | −−𝑘−−→1 𝑓                                                                                                                                                                                                                                                                                                                                                        | e(𝑘−1) | −→𝑘 𝑓                                |     |      |
| --- | --- | --- | ------------------------------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------------------------------ | --- | ---- |
|     |     |     | 𝑓 (e)                                | : e       | −→1                                                                                                                                                                                                                                                                                                                                                              | −→2 | ···                |                                                                                                                                                                                                                                                                                                                                                                  |        | eˆ                                   |     | (10) |
|     |     |     | S(cid:32)                            | (cid:32)  | (cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32) |     |                    | (cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32)(cid:32) |        |                                      |     |      |
|     |     |     |                                      | (cid:124) |                                                                                                                                                                                                                                                                                                                                                                  |     | (cid:123)(cid:122) |                                                                                                                                                                                                                                                                                                                                                                  |        | (cid:125)                            |     |      |
|     |     |     | (cid:124)(cid:123)(cid:122)(cid:125) |           |                                                                                                                                                                                                                                                                                                                                                                  |     |                    |                                                                                                                                                                                                                                                                                                                                                                  |        | (cid:124)(cid:123)(cid:122)(cid:125) |     |      |
COTreasoningsteps
|                  |     |         | Query |     |     |     |     |     |     | Answer |     |     |
| ---------------- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
| 4.3. Environment |     | Setting |       |     |     |     |     |     |     |        |     |     |
Through systematic manipulation of elements and transformations, DataAlchemyoffers a flexible
and controllable framework for training LLMs from scratch, facilitating rigorous investigation of
diverse OOD scenarios. Without specification, we employ a decoder-only language model GPT-
2 (Radford et al., 2019) with a configuration of 4 layers, 32 hidden dimensions, and 4 attention
heads. We utilize a Byte-Pair Encoding (BPE) tokenizer. Both LLMs and the tokenizer follow the
general modern LLM pipeline. During the inference time, we set the temperature to 1e-5. For rigor,
we also study LLMs with various parameters, architectures, and temperatures in Section 8. Details
of the implementation are provided in the Appendix B. We consider that each element consists of
4 basic atoms, which produces 456,976 samples for each dataset with varied transformations and
token amounts. We initialize the two transformations 𝑓 = 𝑓 (𝑒,13) and 𝑓 = 𝑓 (𝑒,1). We consider
|     |     |     |     |     |     |     |     | 1   | rot |     | 2 pos |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
the exact match rate, Levenshtein distance (i.e., edit distance) (Yujian and Bo, 2007), and BLEU
score (Papineni et al., 2002) as metrics and evaluate the produced reasoning step, answer, and full
chain. Examples of the datasets and evaluations are shown in Appendix C
| 5. Task | Generalization |     |     |     |     |     |     |     |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TaskgeneralizationrepresentsafundamentalchallengeforCoTreasoning,asitdirectlytestsamodel’s
ability to apply learned concepts and reasoning patterns to unseen scenarios. In our controlled ex-
periments, both transformation and elements could be novel. Following this, we decompose task
generalization into two primary dimensions: element generalization and transformation generaliza-
tion.
Task Generalization Complexity. Guided by the data distribution lens, we first introduce a
| measure | for generalization |     | difficulty: |     |     |     |     |     |     |     |     |     |
| ------- | ------------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Proposition 5.1 (Task Generalization Complexity). For a reasoning chain 𝑓 operating on elements
𝑆
| e = (𝑎 | ,...,𝑎 | ), define: |         |         |     |         |     |         |     |     |     |     |
| ------ | ------ | ---------- | ------- | ------- | --- | ------- | --- | ------- | --- | --- | --- | --- |
| 0      |        | 𝑙−1        |         |         |     |         |     |         |     |     |     |     |
|        |        | 𝑚          |         |         | 𝑛   |         |     |         |     |     |     |     |
|        |        | ∑︁         | (cid:2) | (cid:3) | ∑︁  | (cid:2) |     | (cid:3) |     |     |     |     |
TGC(𝐶) =𝛼 𝕀 𝑎 ∉ E 𝑖 + 𝛽 𝕀 𝑓 ∉ F +𝛾𝕀[(𝑓 , 𝑓 ,..., 𝑓 ) ∉ P ] +𝐶
|     |     |     | 𝑖   |     |     | 𝑗   | train |     | 1   | 2 𝑘 | train 𝑇 | (11) |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ------- | ---- |
t rain
|     |     | 𝑖=1 |     |     | 𝑗=1 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
as a measurement of task discrepancy Δ 𝑡𝑎𝑠𝑘, where 𝛼,𝛽,𝛾 are weighting parameters for different novelty
𝑖
types and𝐶 is task specific constant. E ,F , and P denote the bit-wise element set, relation
|         | 𝑇         |             |     |      | t rain | train     |     | train |     |     |     |     |
| ------- | --------- | ----------- | --- | ---- | ------ | --------- | --- | ----- | --- | --- | --- | --- |
| set and | the order | of relation | set | used | during | training. |     |       |     |     |     |     |
We establish a critical threshold beyond which CoT reasoning fails exponentially:
Theorem 5.1 (Task Generalization Failure Threshold). There exists a threshold 𝜏 such that when
TGC(𝐶) > 𝜏, the probability of correct CoT reasoning drops exponentially:
|     |     |     |     |     | 𝑃(correct|𝐶) |     | ≤ 𝑒−𝛿(TGC(𝐶)−𝜏) |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | --------------- | --- | --- | --- | --- | --- |
(12)
| The | proof | is provided | in Appendix |     | A.2. |     |     |     |     |     |     |     |
| --- | ----- | ----------- | ----------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
7

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
| 5.1. Transformation |     |     | Generalization |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Transformation generalization evaluates the ability of CoT reasoning to effectively transfer when
models encounter novel transformations during testing, which is an especially prevalent scenario in
| real-world   | applications. |        |                     |                   |     |         |     |     |     |     |     |
| ------------ | ------------- | ------ | ------------------- | ----------------- | --- | ------- | --- | --- | --- | --- | --- |
| Experimental |               | Setup. |                     | To systematically |     | eval-   |     |     |     |     |     |
| uate the     | impact        |        | of transformations, |                   |     | we con- |     |     |     |     |     |
1.0
| duct experiments |     |     | by varying |     | transformations |     |     |     |     |     |     |
| ---------------- | --- | --- | ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
0.8 Distribution Shift
betweentrainingandtestingsetswhilekeeping
| other          | factors     | constant     |      | (e.g., | elements,     | length,     | erocS UELB 0.8 |     |     |     |     |
| -------------- | ----------- | ------------ | ---- | ------ | ------------- | ----------- | -------------- | --- | --- | --- | --- |
| and format).   |             | Guided       | by   | the    | intuition     | formal-     |                |     |     |     | 0.6 |
| ized in        | Proposition |              | 5.1, | we     | define        | four incre- | 0.6            |     |     |     |     |
| mentallevelsof |             | distribution |      | shift  | intransforma- |             |                |     |     |     |     |
0.4
| tions as | shown | in  | Figure | 2: (i) | In-Distribution |     |     |     |     |     |     |
| -------- | ----- | --- | ------ | ------ | --------------- | --- | --- | --- | --- | --- | --- |
0.4
| (ID): The | transformations |     |     | in  | the | test set are |     |     |     |     |     |
| --------- | --------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
0.2
identicaltothoseobservedduringtraining,e.g.,
| 𝑓 ◦ 𝑓 | → 𝑓 | ◦ 𝑓 . | (ii) Composition |     |     | (CMP): Test | 0.2 |     |     |     |     |
| ----- | --- | ----- | ---------------- | --- | --- | ----------- | --- | --- | --- | --- | --- |
| 1 1   | 1   | 1     |                  |     |     |             |     |     |     |     |     |
samples comprise novel compositions of pre- 0.0 0.5 1.0 1.5 2.0 2.5 3.0
|                 |             |                |                  |       |         |               | Edit Distance (×10       |     |                        | 1)            |           |
| --------------- | ----------- | -------------- | ---------------- | ----- | ------- | ------------- | ------------------------ | --- | ---------------------- | ------------- | --------- |
| viously         | encountered |                | transformations, |       |         | though        |                          |     |                        |               |           |
| each individual |             | transformation |                  |       | remains | famil-        |                          |     |                        |               |           |
|                 |             |                |                  |       |         |               | Figure 3 | Performance   |     | of                     | CoT reasoning | on trans- |
| iar, e.g.,      | 𝑓           | ◦ 𝑓 , 𝑓        | ◦ 𝑓 ,            | 𝑓 ◦ 𝑓 | →       | 𝑓 ◦ 𝑓 . (iii) |                          |     |                        |               |           |
|                 | 1           | 1              | 1 2              | 2     | 1       | 2 2           |                          |     |                        |               |           |
|                 |             |                |                  |       |         |               | formationgeneralization. |     | EfficacyofCoTreasoning |               |           |
PartialOut-of-Distribution(POOD):Testdatain-
declinesasthedegreeofdistributionaldiscrepancy
| clude compositions |     |     | involving |     | at least | one novel |     |     |     |     |     |
| ------------------ | --- | --- | --------- | --- | -------- | --------- | --- | --- | --- | --- | --- |
increases.
| transformation |     | not | seen     | during              | training, | e.g., |     |     |     |     |     |
| -------------- | --- | --- | -------- | ------------------- | --------- | ----- | --- | --- | --- | --- | --- |
| 𝑓 ◦ 𝑓          | →   | 𝑓 ◦ | 𝑓 . (iv) | Out-of-Distribution |           |       |     |     |     |     |     |
| 1 1            |     | 1   | 2        |                     |           |       |     |     |     |     |     |
(OOD): The test set contains entirely novel transformation types that are unseen in training, e.g.,
| 𝑓 ◦ 𝑓 | → 𝑓 | ◦ 𝑓 . |     |     |     |     |     |     |     |     |     |
| ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 1   | 2   | 2     |     |     |     |     |     |     |     |     |     |
Table 1 | Full chain evaluation under different scenarios for transformation generalization.
Transformation(Train→Test) Scenario ExactMatch EditDistance BLEUScore
|     |     | 𝑓 ◦ | 𝑓 → 𝑓  | ◦ 𝑓      |      | ID        | 100.00% | 0      |     | 1      |     |
| --- | --- | --- | ------ | -------- | ---- | --------- | ------- | ------ | --- | ------ | --- |
|     |     | 1   | 1      | 1 1      |      |           |         |        |     |        |     |
|     |     | {𝑓  | ◦ 𝑓 ,𝑓 | ◦ 𝑓 ,𝑓 ◦ | 𝑓 }→ | 𝑓 ◦ 𝑓 CMP | 0.01%   | 0.1326 |     | 0.6867 |     |
|     |     | 2   | 2 1    | 2 2      | 1    | 1 1       |         |        |     |        |     |
|     |     | 𝑓 ◦ | 𝑓 → 𝑓  | ◦ 𝑓      |      | POOD      | 0.00%   | 0.1671 |     | 0.4538 |     |
|     |     | 1   | 2      | 1 1      |      |           |         |        |     |        |     |
|     |     | 𝑓 ◦ | 𝑓 → 𝑓  | ◦ 𝑓      |      | OOD       | 0.00%   | 0.2997 |     | 0.2947 |     |
|     |     | 2   | 2      | 1 1      |      |           |         |        |     |        |     |
Findings. Figure3illustratestheperformanceofthefullchainunderdifferentdistributiondiscrepan-
ciescomputedbytaskgeneralizecomplexities(normalizedbetween0and1)inDefinition5.1. Wecan
observe that, in general, the effectiveness of CoT reasoning decreases when distribution discrepancy
increases. FortheinstanceshowninTable1,fromin-distributiontocomposition,POOD,andOOD,the
exact match decreases from 1 to 0.01, 0, and 0, and the edit distance increases from 0 to 0.13, 0.17
when tested on data with transformation 𝑓 ◦ 𝑓 . Apart from ID, LLMs cannot produce a correct full
1 1
chaininmostcases,whiletheycanproducecorrectCoTreasoningwhenexposedtosomecomposition
|     |     |     |     |     |     |     | 𝑓   | ◦ 𝑓 | 𝑓 ◦ 𝑓 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
and POOD conditionsby accident. As shownin Table 2, from 1 2 to 2 2 , the LLMs cancorrectly
answer0.1%ofquestions. Acloseexaminationrevealsthatitisacoincidence,e.g.,thequeryelement
is A, N, A, N, which happened to produce the same result for the two operations detailed in the
Appendix D.1. When further analysis is performed by breaking the full chain into reasoning steps
and answers, we observe strong consistency between the reasoning steps and answers. For example,
under the composition generalization setting, the reasoning steps are entirely correct on test data
distribution 𝑓 ◦ 𝑓 and 𝑓 ◦ 𝑓 , but with wrong answers. Probe these insistent cases in Appendix D.1,
|     |     | 1 1 |     | 2 2 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
8

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
we can find that when a novel transformation (say 𝑓 ◦ 𝑓 ) is present, LLMs try to generalize the
|     |     |     |     |     |     |     |     | 1 1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
reasoning paths based on the most similar ones (i.e., 𝑓 ◦ 𝑓 ) seen during training, which leads to
1 2
correct reasoning paths, yet incorrect answer, which echo the example in the introduction. Similarly,
|     |     |     | 𝑓   | ◦ 𝑓 | 𝑓 ◦ | 𝑓   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
generalization from 1 2 to 2 1 or vice versa allows LLMs to produce correct answers that are
attributed to the commutative property between the two orthogonal transformations with unfaithful
reasoning paths. Collectively, the above results indicate that the CoT reasoning fails to generalize to
novel transformations, not even to novel composition transforms. Rather than demonstrating a true
understanding of text, CoT reasoning under task transformations appears to reflect a replication of
| patterns | learned |     | during | training. |     |     |     |     |     |     |     |
| -------- | ------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
Table2 | EvaluationondifferentcomponentsinCoTreasoningontransformationgeneralization. CoT
| reasoning | shows                      |     | inconsistency |     | with | the reasoning |            | steps and | answers. |                  |     |
| --------- | -------------------------- | --- | ------------- | --- | ---- | ------------- | ---------- | --------- | -------- | ---------------- | --- |
|           | Transformation(Train→Test) |     |               |     |      |               | ExactMatch |           |          | EditDistance     |     |
|           |                            |     |               |     |      | Reason        | Answer     | FullChain | Reason   | Answer FullChain |     |
{𝑓 1 ◦ 𝑓 1 ,𝑓 1 ◦ 𝑓 2 ,𝑓 2 ◦ 𝑓 1 }→ 𝑓 2 ◦ 𝑓 2 100.00% 0.01% 0.01% 0.000 0.481 0.133
{𝑓 ◦ 𝑓 ,𝑓 ◦ 𝑓 ,𝑓 ◦ 𝑓 }→ 𝑓 ◦ 𝑓 100.00% 0.01% 0.01% 0.000 0.481 0.133
|               |     | 1 2       | 2 1        | 2 2        | 1         | 1          |         |       |       |             |     |
| ------------- | --- | --------- | ---------- | ---------- | --------- | ---------- | ------- | ----- | ----- | ----------- | --- |
|               | 𝑓   | ◦ 𝑓 →     | 𝑓 ◦ 𝑓      |            |           | 0.00%      | 100.00% | 0.00% | 0.373 | 0.000 0.167 |     |
|               | 1   | 2         | 2 1        |            |           |            |         |       |       |             |     |
|               | 𝑓   | ◦ 𝑓 →     | 𝑓 ◦ 𝑓      |            |           | 0.00%      | 100.00% | 0.00% | 0.373 | 0.000 0.167 |     |
|               | 2   | 1         | 1 2        |            |           |            |         |       |       |             |     |
| Experiment    |     | settings. |            | To further |           | probe when |         |       |       |             |     |
| CoT reasoning |     | can       | generalize |            | to unseen | trans-     |         |       |       |             |     |
   
| formations, |     | we conduct |     | supervised |     | fine-tuning |     |     |     |     |     |
| ----------- | --- | ---------- | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- |
𝜆
| (SFT) | on a | small | portion | of  | unseen | data. | In  |      K F W D 0  W F D [ ( |     |     |     |
| ----- | ---- | ----- | ------- | --- | ------ | ----- | --- | ------------------------------ | --- | --- | --- |
  
| this way, | we      | can | decrease | the      | distribution |      | dis-  |     |     |     |     |
| --------- | ------- | --- | -------- | -------- | ------------ | ---- | ----- | --- | --- | --- | --- |
| crepancy  | between |     | the      | training | and          | test | sets, |     |     |     |     |
  
| which    | might | help | LLMs | to generalize |     | to  | test |      |     |     |     |
| -------- | ----- | ---- | ---- | ------------- | --- | --- | ---- | ---- | --- | --- | --- |
| queries. |       |      |      |               |     |     |      |    |     |     | ID  |
CMP
| Findings.      |     | As shown | in    | Figure  | 4,  | we can       | find |      |     |     |      |
| -------------- | --- | -------- | ----- | ------- | --- | ------------ | ---- | ---- | --- | --- | ---- |
|                |     |          |       |         |     |              |      |    |     |     | POOD |
| that generally |     | a very   | small | portion |     | (𝜆 = 1.5𝑒−4) |      |      |     |     |      |
OOD
| of data | can | make | the model | quickly |     | generalize |     |     |     |     |     |
| ------- | --- | ---- | --------- | ------- | --- | ---------- | --- | --- | --- | --- | --- |
 
to unseen transformations. The less discrep-              
ancybetweenthetrainingandtestingdata,the
|                               |     |     |     |     |               |     |     |     |  6 ) 7  ' D W D  5 D W L R  ×10 |     | 4  |
| ----------------------------- | --- | --- | --- | --- | ------------- | --- | --- | --- | ----------------------------------- | --- | --- |
| quickerthemodelcangeneralize. |     |     |     |     | Thisindicates |     |     |     |                                     |     |     |
that a similar pattern appears in the training Figure 4 | Performance on unseen transformation
data, helping LLMs to generalize to the test using SFT in various levels of distribution shift. In-
dataset.
troducingasmallamountofunseendatahelpsCoT
|              |     |                |     |     |     |     | reasoning |     | to generalize | across different | scenarios. |
| ------------ | --- | -------------- | --- | --- | --- | --- | --------- | --- | ------------- | ---------------- | ---------- |
| 5.2. Element |     | Generalization |     |     |     |     |           |     |               |                  |            |
Elementgeneralizationisanothercriticalfactor
toconsiderwhenLLMstrytogeneralizetonew
tasks.
Experiment settings. Similar to transformation generalization, we fix other factors and consider
three progressive distribution shifts for elements: ID, CMP, and OOD, as shown in Figure 2. It is
noted that in composition, we test if CoT reasoning can be generalized to novel combinations when
seeing all the basic atoms in the elements, e.g., (A,B,C,D) → (B,C,D,A). Based on the atom order
𝑛),
in combination (can be measured by edit distance the CMP can be further developed. While for
OOD, atoms that constitute the elements are totally unseen during the training.
9

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
| Findings. | Similar | to  | transformation |     | generaliza- |     |     |     |     |     |
| --------- | ------- | --- | -------------- | --- | ----------- | --- | --- | --- | --- | --- |
   
tion, the performances degrade sharply when  ' ,                                H U R F 6  8 ( / %
 R L U D Q H F 6
| facing | the distribution |     | shift | consistently |     | across |     |     |     |     |
| ------ | ---------------- | --- | ----- | ------------ | --- | ------ | --- | --- | --- | --- |
 3 0 &
|                                      |      |       |        |            |             |        |           |           |           |     |
| ------------------------------------ | ---- | ----- | ------ | ---------- | ----------- | ------ | ----------------- | ----------------- | ----------------- | ------ |
| alltransformations,asshowninFigure5. |      |       |        |            |             | From   |                   |                   |                   |        |
| IDtoCMPandOOD,theexactmatchdecreases |      |       |        |            |             |        |  ' 2 2            |                   |                   |        |
|                                      |      |       |        |            |             |        |           |           |           |        |
| from 1.0                             | to   | 0 and | 0, for | all cases. | Most        | strik- |                   |                   |                   |     |
|                                      |      |       |        |            |             |        | f1 f2             | f1 f1 f1          | f2 f2 f1 f2 f2    |        |
| ingly, the                           | BLEU | score | is     | 0 when     | transferred | to     |                   |                   |                   |        |
         K F W D 0  W F D [ (
| 𝑓 and | 𝑓 transformations. |     |     | A failure |     | case in |                    |               |               |     |
| ----- | ------------------ | --- | --- | --------- | --- | ------- | ------------------ | ------------- | ------------- | --- |
| 1     | 2                  |     |     |           |     |         |  ' ,         |         |         |     |
 R L U D Q H F 6
| Appendix | D.1 | shows | that | the models | cannot | re- |     |     |     |     |
| -------- | --- | ----- | ---- | ---------- | ------ | --- | --- | --- | --- | --- |
 3 0 &
|          |        |         |         |       |          |         |      |     |     |      |
| -------- | ------ | ------- | ------- | ----- | -------- | ------- | ------ | ----- | ----- | ---- |
| spond    | to any | words   | when    | novel | elements | are     |        |       |       |    |
| present. | We     | further | explore | when  | CoT      | reason- |  ' 2 2 |       |       |      |
|          |        |         |         |       |          |         |      |     |     |      |
ingcangeneralizetonovelelementsbyconduct-
 
|     |     |     |     |     |     |     | f1 f2 | f1 f1 f1 | f2 f2 f1 f2 f2 |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | -------------- | --- |
ingSFT.TheresultsaresummarizedinFigure6.
 7 U D Q V I R U P D W L R Q
Weevaluatetheperformanceunderthreeexact
matchesforthefullchainunderthreescenarios, Figure5|Elementgeneralizationresultsonvarious
CMP based on the edit distance n. The result scenarios and relations.
| is similar | to  | SFT on | transformation. |     |     | The per- |     |     |     |     |
| ---------- | --- | ------ | --------------- | --- | --- | -------- | --- | --- | --- | --- |
𝑛)
formance increases rapidly when presented with similar (a small examples in the training data.
Interestingly, the exact match rate for CoT reasoning aligns with the lower bound of performance
when 𝑛 = 3, which might suggest the generalization of CoT reasoning on novel elements is very
limited, even SFT on the downstream task. When we further analyze the exact match of reasoning,
answer, and token during the training for 𝑛 = 3, as summarized in Figure 6b. We find that there is a
mismatch of accuracy between the answer and the reasoning step during the training process, which
somehow might provide an explanation regarding why CoT reasoning is inconsistent in some cases.
|     |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
 5 H D V R Q L Q J  6 W H S
     K F W D 0  W F D [ (      K F W D 0  W F D [ (  $ Q V Z H U
|    |     |     |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
 ) X O O  & K D L Q
|    |     |     |     |     |     |        |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | ------ | ------ | --- | --- | --- |
|    |     |     |     |     |     |  Q    |     |     |     |     |
 Q   
  
 Q   
   
 Q   
 
   
                                                                           
|     |     |  6 ) 7  ' D W D  5 D W L R |     |     |     |     |     |  6 ) 7  ' D W D  5 D W L R |     |     |
| --- | --- | ---------------------------- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- |
(a)PerformanceonunseenelementviaSFTinvariousCMP (b)EvaluationofCoTreasoninginSFT.
scenarios.
Figure 6 | SFT performances for element generalization. SFT helps to generalize to novel elements.
| 6. Length |     | Generalization |     |     |     |     |     |     |     |     |
| --------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Length generalization examines how CoT reasoning degrades when models encounter test cases that
differinlengthfromtheirtrainingdistribution. Thedifferenceinlengthcouldbeintroducedfromthe
textspaceorthereasoningspaceoftheproblem. Therefore,wedecomposelengthgeneralizationinto
two complementary aspects: text length generalization and reasoning step generalization. Guided by
10

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
| instinct, | we first | propose | to  | measure |     | the length | discrepancy. |     |     |     |
| --------- | -------- | ------- | --- | ------- | --- | ---------- | ------------ | --- | --- | --- |
Length Extrapolation Bound. We establish a power-law relationship for length extrapolation:
Proposition6.1(LengthExtrapolationGaussianDegradation). Foramodeltrainedonchain-of-thought
|     |     |     | 𝐿   |     |     |     |     | 𝐿   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sequences of fixed length , the generalization error at test length follows a Gaussian distribution:
train
|     |     |     |     |     |     |     | (cid:32) | (cid:32) )2 | (cid:33)(cid:33) |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ---------------- | --- |
(𝐿−𝐿
|     |     |     |     | E(𝐿) | = E +(1−E |     | ) · 1−exp | − train |     | (13) |
| --- | --- | --- | --- | ---- | --------- | --- | --------- | ------- | --- | ---- |
|     |     |     |     |      | 0         |     | 0         |         |     |      |
2𝜎2
where E is the in-distribution error at 𝐿 = 𝐿 , 𝜎 is the length generalization width parameter, and 𝐿
|             | 0            |             |               |             |                 | train |              |     |           |     |
| ----------- | ------------ | ----------- | ------------- | ----------- | --------------- | ----- | ------------ | --- | --------- | --- |
| is the test | sequence     | length      |               |             |                 |       |              |     |           |     |
| The         | proof        | is provided |               | in Appendix |                 | A.3.  |              |     |           |     |
| Table 3     | | Evaluation |             | for text      | length      | generalization. |       |              |     |           |     |
|             |              |             | ExactMatch(%) |             |                 |       | EditDistance |     | BLEUScore |     |
Length
FullChain Reason Answer FullChain Reason Answer FullChain Reason Answer
2 0.00% 0.00% 0.00% 0.3772 0.4969 0.5000 0.4214 0.1186 0.0000
3 0.00% 0.00% 0.00% 0.2221 0.3203 0.2540 0.5471 0.1519 0.0000
4 100.00% 100.00% 100.00% 0.0000 0.0000 0.0000 1.0000 1.0000 1.0000
5 0.00% 0.00% 0.00% 0.1818 0.2667 0.2000 0.6220 0.1958 0.2688
6 0.00% 0.00% 0.00% 0.3294 0.4816 0.3337 0.4763 0.1174 0.2077
| 6.1. Text | Length | Generalization |     |     |     |     |     |     |     |     |
| --------- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Text length generalization evaluates how CoT performance varies when the input text length (i.e.,
the element length 𝑙) differs from training examples. Considering the way LLMs process long text,
this aspect is crucial because real-world problems often involve varying degrees of complexity that
manifest as differences in problem statement length, context size, or information density.
| Experiment      |       | settings. | We          | pre-train    |        | LLMs     | on     |     |     |          |
| --------------- | ----- | --------- | ----------- | ------------ | ------ | -------- | ------ | --- | --- | -------- |
| the dataset     | with  | text      | length      | merely       |        | on 𝑙 =   | 4      |     |     |          |
|                 |       |           |             |              |        |          |     |     |     |      |
| while fixing    | other | factors   |             | and evaluate |        | the per- |        |     |     |          |
| formance        | on    | a variety | of lengths. |              | We     | consider |        |     |     |          |
|                 |       |           |             |              |        |          |     |     |     |      |
| three different |       | padding   | strategies  |              | during | the      |        |     |     |          |
 H F Q D W V L '  W L G (
| pre-training: |               | (i) None: | LLMs     |         | do not       | use any  |  H U R F 6  8 ( / % |          |     |          |
| ------------- | ------------- | --------- | -------- | ------- | ------------ | -------- | -------------------- | -------- | --- | -------- |
|               |               |           |          |         |              |          |                   |          |     |      |
| padding.      | (ii) Padding: |           | We       | pad LLM | to           | the max  |                      |          |     |          |
| length        | of the        | context   | window.  |         | (iii) Group: | We       |                      |          |     |          |
|               |               |           |          |         |              |          |                   |          |     |      |
| group         | the text      | and       | truncate | it      | into         | segments |                      |          |     |          |
| with a        | maximum       | length.   |          |         |              |          |                      |  1 R Q H |     |          |
|               |               |           |          |         |              |          |                   |          |     |      |
 * U R X S
| Findings. | As  | illustrated | in  | the Table | 3,  | the CoT |     |     |     |     |
| --------- | --- | ----------- | --- | --------- | --- | ------- | --- | --- | --- | --- |
 3 D G G L Q J
reasoning failed to directly generate two test         
cases even though those lengths present a mild          
 7 H [ W  / H Q J W K
| distribution | shift. | Further, |     | the performance |     |     | de- |     |     |     |
| ------------ | ------ | -------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
clinesasthelengthdiscrepancyincreasesshown Figure7|Performanceoftextlengthgeneralization
𝑙 =
in Figure 7. For instance, from data with 4 acrossvariouspaddingstrategies. Groupstrategies
| to those    | with | 𝑙 = 3    | or 𝑙 = | 5, the    | BLEU     | score |            |                           |     |     |
| ----------- | ---- | -------- | ------ | --------- | -------- | ----- | ---------- | ------------------------- | --- | --- |
|             |      |          |        |           |          |       | contribute | to length generalization. |     |     |
| decreases   | from | 1 to     | 0.55   | and 0.62. | Examples |       |            |                           |     |     |
| in Appendix | D.1  | indicate | that   | LLMs      | attempt  |       | to         |                           |     |     |
11

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
produce CoT reasoning with the same length as the training data by adding or removing tokens
in the reasoning chains. The efficacy of CoT reasoning length generalization deteriorates as the
discrepancy increases. Moreover, we consider using a different padding strategy to decrease the
divergencebetweenthetrainingdataandtestcases. Wefoundthatpaddingtothemaxlengthdoesn’t
contributetolengthgeneralization. However,theperformanceincreaseswhenwereplacethepadding
with text by using the group strategy, which indicates its effectiveness.
6.2. Reasoning Step Generalization
The reasoning step generalization investigates whether models can extrapolate to reasoning chains
requiringdifferentsteps𝑘fromthoseobservedduringtraining. whichisapopularsettinginmulti-step
reasoning tasks.
Experiment settings. Similartotextlengthgeneralization,wefirstpre-traintheLLMwithreasoning
step 𝑘 = 2, and evaluate on data with reasoning step 𝑘 = 1 or 𝑘 = 3.
  
  
  
  
 
                                           
 ' D W D  3 H U F H Q W D J H
     K F W D 0  W F D [ (
  
  
  
  
  
  
  
 N    
  
 N    
 
                                           
 ' D W D  3 H U F H Q W D J H
(a)Reasoningstep.Fromk=2tok=1
     K F W D 0  W F D [ (
 N   
 N   
(b)Reasoningstep.Fromk=2tok=3
Figure8|Testperformanceforreasoning-stepgeneralizationacrossvaryingtrainingdatacompositions.
Performance varies systematically with changes in the distribution of training data components.
Findings. As showcased in Figure 8, CoT reasoning cannot generalize across data requiring different
reasoning steps, indicating the failure of generalization. Then, we try to decrease the distribution
discrepancy introduced by gradually increasing the ratio of unseen data while keeping the dataset
size the same when pre-training the model. And then, we evaluate the performance on two datasets.
As we can observe, the performance on the target dataset increases along with the ratio. At the
same time, the LLMs can not generalize to the original training dataset because of the small amount
of training data. The trend is similar when testing different-step generalization, which follows the
intuition and validates our hypothesis directly.
7. Format Generalization
Format generalization assesses the robustness of CoT reasoning to surface-level variations in test
queries. This dimension is especially crucial for determining whether models have internalized
flexible, transferable reasoning strategies or remain reliant on the specific templates and phrasings
encountered during training.
12

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
Format Alignment Score. We introduce a metric for measuring prompt similarity:
Definition 7.1 (Format Alignment Score). For training prompt distribution 𝑃 𝑡𝑟𝑎𝑖𝑛 and test prompt 𝑝 𝑡𝑒𝑠𝑡:
PAS(𝑝 𝑡𝑒𝑠𝑡 ) = max cos(𝜙(𝑝),𝜙(𝑝 𝑡𝑒𝑠𝑡 )) (14)
𝑝∈𝑃𝑡𝑟𝑎𝑖𝑛
where 𝜙 is a prompt embedding function.
   
   
   
   
   
                
 1 R L V H  / H Y H O    
 H F Q D W V L '  W L G (
 $ O O    
 , Q V H U W L R Q
   
 ' H O H W L R Q
 0 R G L I \
   
   
   
   
                          
 1 R L V H  / H Y H O    
(a)Formatgeneralization.Performanceundervariousper-
turbationmethods.
 H U R F 6  8 ( / %
 1 R Q H
 3 U R P S W
 7 U D Q V I R U P D W L R Q
 ( O H P H Q W
(b)Formatgeneralization.Performancevs.variousapplied
perturbationareas.
Figure 9 | Performance of format generalization. Testing performance varies with different noise
levels and areas where the noise is applied.
Experiment settings. To systematically probe this, we introduce four distinct perturbation modes to
simulate scenario in real-world: (i) insertion, where a noise token is inserted before each original
token;(ii)deletion: itdeletestheoriginaltoken;(iii)modification: itreplacestheoriginaltokenwith
a noise token; and (iv) hybrid mode: it combines multiple perturbations. Each mode is applied for
tokens with probabilities 𝑝, enabling us to quantify the model’s resilience to increasing degrees of
prompt distribution shift.
Findings. As shown in Figure 9a, we found that generally CoT reasoning can be easily affected by
the format changes. No matter insertion, deletion, modifications, or hybrid mode, it creates a format
discrepancy that affects the correctness. Among them, the deletion slightly affects the performance.
While the insertions are relatively highly influential on the results. We further divide the query into
several sections: elements, transformations, and prompt tokens. As shown in Figure 9b, we found
that the elements and transformation play an important role in the format, whereas the changes to
other tokens rarely affect the results.
8. Temperature and Model Size
Temperature and model size generalization explores how variations in sampling temperature and
model capacity can influence the stability and robustness of CoT reasoning. For the sake of rigorous
evaluation, we further investigate whether different choices of temperatures and model sizes may
significantly affect our results.
Experimentsettings. Weexploretheimpactofdifferenttemperaturesonthevalidityofthepresented
results. We adopt the same setting in the transformation generalization.
13

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
Findings. As illustrated in Figure 10a, LLMs tend to generate consistent and reliable CoT reasoning
across a broad range of temperature settings (e.g., from 1e-5 up to 1), provided the values remain
within a suitable range. This stability is maintained even when the models are evaluated under a
| variety of           | distribution          | shifts.                          |                      |        |     |     |
| -------------------- | --------------------- | -------------------------------- | -------------------- | ------ | --- | --- |
|  3 0 & ' 2 2 3 ' 2 2 |                       |                                  |                      |     |     |     |
|                 |             |                   |  H U R F 6  8 ( / % |        |     |     |
 R L U D Q H F 6
    
     K F W D 0  W F D [ (
|       |             |                   |     |    |     |     |
| ---------- | --------------------- | -------------------------------- | --- | ---- | --- | --- |
    
|       |             |                   |     |    |     |     |
| ---------- | --------------------- | -------------------------------- | --- | ---- | --- | --- |
   .
|   H    |          |              |     |      |     |          |
| ---------- | --------------- | ---------------------- | --- | ---- | --- | -------- |
|            |                 |                        |     |    |     |     . |
 3 0 & ' 2 2 3 ' 2 2
                                          H F Q D W V L '  W L G (     0
 R L U D Q H F 6
|            |                       |                                  |          |    |     |    0 |
| ---------- | --------------------- | -------------------------------- | -------- | ---- | --- | ------ |
|       |             |                   |      |      |     |        |
    0
 
|       |             |                   |      |                           |                      |                     |
| ---------- | --------------------- | -------------------------------- | -------- | ------------------------- | -------------------- | ------------------- |
|            |                       |                                  |          |                     |             |            |
|   H    |                |                        |          |                           |                      |                     |
|            |                       |                                  |          |  6 ) 7  5 D W L R  ×10 |                      | 4                  |
 7 H P S H U D W X U H
(a)Influencesofvarioustemperatures. (b)Influencesofvarioussizes.
Figure 10 | Temperature and model size. The findings hold under different temperatures and model
sizes.
Experiment settings. We further examine the influence of model size by employing the same
experimental configuration as used in the novel relation SFT study. In particular, we first pretrain
models of different sizes using the transformation 𝑓 ◦ 𝑓 , and subsequently perform SFT on 𝑓 ◦ 𝑓
|               |         |         |     | 1 1 |     | 2 2 |
| ------------- | ------- | ------- | --- | --- | --- | --- |
| while varying | the SFT | ratios. |     |     |     |     |
Finding. Fig. 10b shows the accuracy of models with different sizes using different SFT ratios, which
closely matches the result of our default model size across all evaluated settings and configurations.
| 9. Discussion | and | Implication |     |     |     |     |
| ------------- | --- | ----------- | --- | --- | --- | --- |
Our investigation, conducted through the controlled environment of DataAlchemy, reveals that
the apparent reasoning prowess of Chain-of-Thought (CoT) is largely a brittle mirage. The findings
across task, length, and format generalization experiments converge on a conclusion: CoT is not
a mechanism for genuine logical inference but rather a sophisticated form of structured pattern
matching, fundamentally bounded by the data distribution seen during training. When pushed
even slightly beyond this distribution, its performance degrades significantly, exposing the superficial
| nature of | the “reasoning” | it produces. |     |     |     |     |
| --------- | --------------- | ------------ | --- | --- | --- | --- |
While our experiments utilized models trained from scratch in a controlled environment, the
principlesuncoveredareextensibletolarge-scalepre-trainedmodels. Wesummarizetheimplications
| for practitioners | as follows. |     |     |     |     |     |
| ----------------- | ----------- | --- | --- | --- | --- | --- |
Guard Against Over-reliance and False Confidence. CoT should not be treated as a “plug-and-
play” module for robust reasoning, especially in high-stakes domains like medicine, finance, or legal
analysis. The ability of LLMs to produce “fluent nonsense”—plausible but logically flawed reasoning
chains—can be more deceptive and damaging than an outright incorrect answer, as it projects a false
aura of dependability. Sufficient auditing from domain experts is indispensable.
14

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
Prioritize Out-of-Distribution (OOD) Testing. Standard validation practices, where the test set
closely mirrors the training set, are insufficient to gauge the true robustness of a CoT-enabled system.
Practitioners must implement rigorous adversarial and OOD testing that systematically probes for
vulnerabilities across task, length, and format variations.
Recognize Fine-Tuning as a Patch, Not a Panacea. Our results show that Supervised Fine-
Tuning(SFT)canquickly“patch”amodel’sperformanceonanew,specificdatadistribution. However,
this should not be mistaken for achieving true generalization. It simply expands the model’s “in-
distribution” bubble slightly. Relying on SFT to fix every OOD failure is an unsustainable and reactive
strategy that fails to address the core issue: the model’s lack of abstract reasoning capability.
10. Conclusion
In this paper, we critically examine the COT reasoning of LLMs through the lens of data distribution,
revealingthattheperceivedstructuredreasoningcapabilitylargelyarisesfrominductivebiasesshaped
by in-distribution training data. We propose a controlled environment, DataAlchemy, allowing
systematic probing of CoT reasoning along three crucial dimensions: task structure, reasoning length,
and query format. Empirical findings consistently demonstrate that CoT reasoning effectively repro-
ducesreasoningpatternscloselyalignedwithtrainingdistributionsbutsufferssignificantdegradation
when faced with distributional deviations. Such observations reveal the inherent brittleness and
superficiality of current CoT reasoning capabilities. We provide insights that emphasize real-world
implications for both practitioners and researchers.
References
O. Bentham, N. Stringham, and A. Marasovic. Chain-of-thought unfaithfulness as disguised accuracy.
TransactionsonMachineLearningResearch,2024. ISSN2835-8856. URLhttps://openreview.
net/forum?id=ydcrP55u2e. Reproducibility Certification.
M. Budnikov, A. Bykova, and I. P. Yamshchikov. Generalization potential of large language models.
Neural Computing and Applications, 37(4):1973–1997, 2025.
Q. Chen, L. Qin, J. Liu, D. Peng, J. Guan, P. Wang, M. Hu, Y. Zhou, T. Gao, and W. Che. Towards
reasoning era: A survey of long chain-of-thought for reasoning large language models. arXiv
preprint arXiv:2503.09567, 2025a.
Y. Chen, J. Benton, A. Radhakrishnan, J. Uesato, C. Denison, J. Schulman, A. Somani, P. Hase,
M. Wagner, F. Roger, et al. Reasoning models don’t always say what they think. arXiv preprint
arXiv:2505.05410, 2025b.
H. Cho, J. Cha, P. Awasthi, S. Bhojanapalli, A. Gupta, and C. Yun. Position coupling: Improving
length generalization of arithmetic transformers using task structure. In The Thirty-eighth Annual
Conference on Neural Information Processing Systems, 2024. URL https://openreview.net/
forum?id=5cIRdGM1uG.
S. Garg, D. Tsipras, P. S. Liang, and G. Valiant. What can transformers learn in-context? a case study
of simple function classes. Advances in neural information processing systems, 35:30583–30598,
2022.
D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, et al.
Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint
arXiv:2501.12948, 2025.
15

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
S. Imani, L. Du, and H. Shrivastava. Mathprompter: Mathematical reasoning using large language
models. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics
| (Volume | 5: Industry | Track), | pages 37–42, | 2023. |
| ------- | ----------- | ------- | ------------ | ----- |
A. Jaech, A. Kalai, A. Lerer, A. Richardson, A. El-Kishky, A. Low, A. Helyar, A. Madry, A. Beutel,
A. Carney, et al. Openai o1 system card. arXiv preprint arXiv:2412.16720, 2024.
S. Kambhampati. Can large language models reason and plan? Annals of the New York Academy of
| Sciences, | 1534(1):15–18, |     | 2024. |     |
| --------- | -------------- | --- | ----- | --- |
S. Kambhampati, K. Stechly, and K. Valmeekam. (how) do reasoning models reason? Annals of the
| New York | Academy | of Sciences, | 1547(1):33–40, | 2025. |
| -------- | ------- | ------------ | -------------- | ----- |
T. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa. Large language models are zero-shot
reasoners. Advances in neural information processing systems, 35:22199–22213, 2022.
T. Lanham, A. Chen, A. Radhakrishnan, B. Steiner, C. Denison, D. Hernandez, D. Li, E. Durmus,
E. Hubinger, J. Kernion, et al. Measuring faithfulness in chain-of-thought reasoning. arXiv preprint
| arXiv:2307.13702, |     | 2023. |     |     |
| ----------------- | --- | ----- | --- | --- |
H. Li, S. Lu, P.-Y. Chen, X. Cui, and M. Wang. Training nonlinear transformers for chain-of-thought
inference: A theoretical generalization analysis. In The Thirteenth International Conference on
https://openreview.net/forum?id=n7n8McETXw.
| Learning | Representations, |     | 2025a. URL |     |
| -------- | ---------------- | --- | ---------- | --- |
Y.Li,Z.Lai,W.Bao,Z.Tan,A.Dao,K.Sui,J.Shen,D.Liu,H.Liu,andY.Kong. Visuallargelanguage
models for generalized and specialized applications. arXiv preprint arXiv:2501.02765, 2025b.
Z. Ling, Y. Fang, X. Li, Z. Huang, M. Lee, R. Memisevic, and H. Su. Deductive verification of chain-of-
thought reasoning. Advances in Neural Information Processing Systems, 36:36407–36433, 2023.
I. Mirzadeh, K. Alizadeh, H. Shahrokhi, O. Tuzel, S. Bengio, and M. Farajtabar. Gsm-symbolic:
Understanding the limitations of mathematical reasoning in large language models. arXiv preprint
| arXiv:2410.05229, |     | 2024. |     |     |
| ----------------- | --- | ----- | --- | --- |
K. Papineni, S. Roukos, T. Ward, and W.-J. Zhu. Bleu: a method for automatic evaluation of machine
translation. InProceedingsofthe40thannualmeetingoftheAssociationforComputationalLinguistics,
| pages 311–318, |     | 2002. |     |     |
| -------------- | --- | ----- | --- | --- |
A.Radford,J.Wu,R.Child,D.Luan,D.Amodei,I.Sutskever,etal. Languagemodelsareunsupervised
| multitask | learners. | OpenAI | blog, 1(8):9, | 2019. |
| --------- | --------- | ------ | ------------- | ----- |
Z. Shen, H. Yan, L. Zhang, Z. Hu, Y. Du, and Y. He. Codi: Compressing chain-of-thought into
continuous space via self-distillation. arXiv preprint arXiv:2502.21074, 2025.
P.Shojaee,I.Mirzadeh,K.Alizadeh,M.Horton,S.Bengio,andM.Farajtabar. Theillusionofthinking:
Understandingthestrengthsandlimitationsofreasoningmodelsviathelensofproblemcomplexity.
| arXiv preprint | arXiv:2506.06941, |     | 2025. |     |
| -------------- | ----------------- | --- | ----- | --- |
J.Song,Z.Xu,andY.Zhong. Out-of-distributiongeneralizationviacomposition: alensthroughinduc-
tion heads in transformers. Proceedings of the National Academy of Sciences, 122(6):e2417182122,
2025.
K. Stechly, K. Valmeekam, and S. Kambhampati. Chain of thoughtlessness? an analysis of cot in
planning. Advances in Neural Information Processing Systems, 37:29106–29141, 2024.
16

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
K. Stechly, K. Valmeekam, A. Gundawar, V. Palod, and S. Kambhampati. Beyond semantics: The
unreasonable effectiveness of reasonless intermediate tokens. arXiv preprint arXiv:2505.13775,
2025.
X. Tang, Z. Zheng, J. Li, F. Meng, S.-C. Zhu, Y. Liang, and M. Zhang. Large language models are
in-context semantic reasoners rather than symbolic reasoners. arXiv preprint arXiv:2305.14825,
2023.
K. Team, A. Du, B. Gao, B. Xing, C. Jiang, C. Chen, C. Li, C. Xiao, C. Du, C. Liao, et al. Kimi k1. 5:
Scaling reinforcement learning with llms. arXiv preprint arXiv:2501.12599, 2025.
Q. Team. Qwq: Reflect deeply on the boundaries of the unknown. Hugging Face, 2024.
L. P.-Y. Ting, C. Zhao, Y.-H. Zeng, Y. J. Lim, and K.-T. Chuang. Beyond rag: Reinforced reasoning
augmented generation for clinical notes. arXiv preprint arXiv:2506.05386, 2025.
Q.Wang,Y.Wang,Y.Wang,andX.Ying.Canin-contextlearningreallygeneralizetoout-of-distribution
tasks? arXiv preprint arXiv:2410.09695, 2024.
X. Wang, J. Wei, D. Schuurmans, Q. V. Le, E. H. Chi, S. Narang, A. Chowdhery, and D. Zhou. Self-
consistency improves chain of thought reasoning in language models. In The Eleventh International
Conference on Learning Representations, 2023. URL https://openreview.net/forum?id=
1PL1NIMMrw.
Y. Wang, F.-C. Chang, and P.-Y. Wu. Chain-of-thought prompting for out-of-distribution samples: A
latent-variable study. arXiv e-prints, pages arXiv–2504, 2025a.
Y.Wang,F.-C.Chang,andP.-Y.Wu. Atheoreticalframeworkforoodrobustnessintransformersusing
gevrey classes. arXiv preprint arXiv:2504.12991, 2025b.
J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, D. Zhou, et al. Chain-of-thought
prompting elicits reasoning in large language models. Advances in neural information processing
systems, 35:24824–24837, 2022.
J. Xu, H. Fei, L. Pan, Q. Liu, M.-L. Lee, and W. Hsu. Faithful logical reasoning via symbolic chain-of-
thought. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 13326–13365, 2024.
J. Yang, K. Zhou, Y. Li, and Z. Liu. Generalized out-of-distribution detection: A survey. International
Journal of Computer Vision, 132(12):5635–5662, 2024.
L. Yang, Y. Song, X. Ren, C. Lyu, Y. Wang, J. Zhuo, L. Liu, J. Wang, J. Foster, and Y. Zhang. Out-of-
distributiongeneralizationinnaturallanguageprocessing: Past,present,andfuture. InProceedings
of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 4533–4559,
2023.
S.Yao,D.Yu,J.Zhao,I.Shafran,T.Griffiths,Y.Cao,andK.Narasimhan. Treeofthoughts: Deliberate
problemsolvingwithlargelanguagemodels. Advancesinneuralinformationprocessingsystems,36:
11809–11822, 2023.
X. Yao, R. Ren, Y. Liao, and Y. Liu. Unveiling the mechanisms of explicit cot training: How chain-of-
thought enhances reasoning generalization. arXiv e-prints, pages arXiv–2502, 2025.
E.Yeo,Y.Tong,M.Niu,G.Neubig,andX.Yue. Demystifyinglongchain-of-thoughtreasoninginllms.
arXiv preprint arXiv:2502.03373, 2025.
17

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
Z. Yu, L. He, Z. Wu, X. Dai, and J. Chen. Towards better chain-of-thought prompting strategies: A
| survey. | arXiv | preprint | arXiv:2310.04959, |     |     | 2023. |     |     |     |     |
| ------- | ----- | -------- | ----------------- | --- | --- | ----- | --- | --- | --- | --- |
L. Yujian and L. Bo. A normalized levenshtein distance metric. IEEE transactions on pattern analysis
| and machine |     | intelligence, |     | 29(6):1091–1095, |     | 2007. |     |     |     |     |
| ----------- | --- | ------------- | --- | ---------------- | --- | ----- | --- | --- | --- | --- |
X. Zhang, C. Du, T. Pang, Q. Liu, W. Gao, and M. Lin. Chain of preference optimization: Improving
chain-of-thoughtreasoninginllms. AdvancesinNeuralInformationProcessingSystems,37:333–356,
2024a.
Y.Zhang,H.Wang,S.Feng,Z.Tan,X.Han,T.He,andY.Tsvetkov. Canllmgraphreasoninggeneralize
beyond pattern memorization? In Findings of the Association for Computational Linguistics: EMNLP
| 2024, | pages | 2289–2305, |     | 2024b. |     |     |     |     |     |     |
| ----- | ----- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- |
Z. Zhang, A. Zhang, M. Li, and A. Smola. Automatic chain of thought prompting in large language
models. In The Eleventh International Conference on Learning Representations, 2023. URL https:
//openreview.net/forum?id=5NTt8GFjUHkr.
Z.Zhang,A.Zhang,M.Li,H.Zhao,G.Karypis,andA.Smola. Multimodalchain-of-thoughtreasoning
in language models. Transactions on Machine Learning Research, 2024, 2024c.
C. Zhao, Z. Tan, C.-W. Wong, X. Zhao, T. Chen, and H. Liu. Scale: Towards collaborative content
analysisinsocialsciencewithlargelanguagemodelagentsandhumanintervention. arXivpreprint
| arXiv:2502.10937, |     |     | 2025. |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
W. X. Zhao, K. Zhou, J. Li, T. Tang, X. Wang, Y. Hou, Y. Min, B. Zhang, J. Zhang, Z. Dong, et al. A
survey of large language models. arXiv preprint arXiv:2303.18223, 2023.
| A. Proof   | of  | Theorems           |     |     |       |     |     |     |     |     |
| ---------- | --- | ------------------ | --- | --- | ----- | --- | --- | --- | --- | --- |
| A.1. Proof | of  | CoT Generalization |     |     | Bound |     |     |     |     |     |
Proof. Let 𝑓 𝜃beamodeltrainedonsamplesfromthedistributionD usingalossfunctionℓ(𝑓 (𝑥),𝑦)
|     |     |     |     |     |     |     |     |     | train | 𝜃   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
Λ-Lipschitz
| that is |     | and | bounded. | The  | expected | test      | risk | is given      | by  |      |
| ------- | --- | --- | -------- | ---- | -------- | --------- | ---- | ------------- | --- | ---- |
|         |     |     |          | 𝑅    | (𝑓 )     | =         |      | [ℓ(𝑓 (𝑥),𝑦)]. |     |      |
|         |     |     |          | test | 𝜃        | 𝔼 (𝑥,𝑦)∼D |      | 𝜃             |     | (15) |
test
| We can | decompose | the | test | risk as |       |         |      |        |         |      |
| ------ | --------- | --- | ---- | ------- | ----- | ------- | ---- | ------ | ------- | ---- |
|        |           |     |      | 𝑅 (𝑓    | ) = 𝑅 | (𝑓 )+(𝑅 |      | (𝑓 )−𝑅 | (𝑓 )).  | (16) |
|        |           |     |      | test 𝜃  | train | 𝜃       | test | 𝜃      | train 𝜃 |      |
To bound the discrepancy between 𝑅 and 𝑅 , we invoke a standard result from statistical
|     |     |     |     |     | test |     | train |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ----- | --- | --- | --- |
learningtheory. Giventhat ℓ is Λ-Lipschitzandthediscrepancymeasure Δ(D ,D ) isanintegral
train test
| probability | metric | (e.g.,    | Wasserstein-1 |       | distance), |         | we have    |       |            |      |
| ----------- | ------ | --------- | ------------- | ----- | ---------- | ------- | ---------- | ----- | ---------- | ---- |
|             |        |           |               | |𝑅 (𝑓 | )−𝑅        | (𝑓      | )| ≤ Λ·Δ(D |       | ,D ).      |      |
|             |        |           |               | test  | 𝜃          | train 𝜃 |            |       | train test | (17) |
| Therefore,  | the    | test risk | satisfies     |       |            |         |            |       |            |      |
|             |        |           |               | 𝑅 (𝑓  | ) ≤ 𝑅      | (𝑓      | )+Λ·Δ(D    |       | ,D ).      | (18) |
|             |        |           |               | test  | 𝜃          | train 𝜃 |            | train | test       |      |
18

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
We next account for the generalization gap between the empirical training risk 𝑅ˆ (𝑓 ) and the
|     |     |     |     |     |     |     |     |     |     |     |     | train 𝜃 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
expected training risk 𝑅 (𝑓 ). By applying a concentration inequality (e.g., Hoeffding’s inequality),
|                  |     |     |       | train | 𝜃   |      |     |            |     |          |     |     |     |
| ---------------- | --- | --- | ----- | ----- | --- | ---- | --- | ---------- | --- | -------- | --- | --- | --- |
| with probability |     | at  | least | 1−𝛿,  | we  | have |     |            |     |          |     |     |     |
|                  |     |     |       |       |     |      |     | (cid:32)√︂ |     | (cid:33) |     |     |     |
log(1/𝛿)
|     |     |     |     |     | 𝑅     | (𝑓 ) ≤ 𝑅ˆ | (𝑓    | )+O |     | ,   |     |     | (19) |
| --- | --- | --- | --- | --- | ----- | --------- | ----- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     | train | 𝜃         | train | 𝜃   | 𝑛   |     |     |     |      |
𝑛
| where     | is the | number |        | of training |        | samples.  |      |              |     |            |          |     |     |
| --------- | ------ | ------ | ------ | ----------- | ------ | --------- | ---- | ------------ | --- | ---------- | -------- | --- | --- |
| Combining |        | the    | above, | we          | obtain | that with | high | probability, |     |            |          |     |     |
|           |        |        |        |             |        |           |      |              |     | (cid:32)√︂ | (cid:33) |     |     |
log(1/𝛿)
|                |     |      | 𝑅              | (𝑓 ) | ≤ 𝑅ˆ  | (𝑓 )+Λ·Δ(D |           | ,D         | )+O |     |     | .   | (20) |
| -------------- | --- | ---- | -------------- | ---- | ----- | ---------- | --------- | ---------- | --- | --- | --- | --- | ---- |
|                |     |      | test           | 𝜃    | train | 𝜃          |           | train test |     |     | 𝑛   |     |      |
| This concludes |     | the  | proof.         |      |       |            |           |            |     |     |     |     | □    |
| A.2. Proof     | of  | Task | Generalization |      |       | Failure    | Threshold |            |     |     |     |     |      |
We establish the exponential decay bound through a probabilistic analysis of reasoning failure modes
| in the presence |     | of  | task | generalization |     | complexity. |     |     |     |     |     |     |     |
| --------------- | --- | --- | ---- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Let Ω denote the sample space of all possible reasoning configurations, and let𝐶 ∈ Ω represent a
specific configuration. We define the following events: 𝐴 as the event that element 𝑎 is novel, i.e.,
|     |     |     |     |     |     |     |     |     | 𝑖   |     |     | 𝑖   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 𝑎 𝑖 | 𝐹   |     |     |     |     |     | 𝑓   |     | 𝑓   |     |     |     |     |
𝑖 ∉ E ; 𝑗 as the event that transformation 𝑗 is novel, i.e., 𝑗 ∉ F train ; and Q as the event that the
t rain
transformation sequence (𝑓 , 𝑓 ,..., 𝑓 ) is novel, i.e., (𝑓 , 𝑓 ,..., 𝑓 ) ∉ P .
|     |     |     |     | 1   | 2   | 𝑘   |     | 1   | 2   | 𝑘 train |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
Here we make the assumption that the reasoning failures induced by novel arguments, functions,
and patterns contribute independently to the overall failure probability and hence we model the
| success | probability |       | as a | product | of           | component-wise |           | success          | rates:          |     |     |     |     |
| ------- | ----------- | ----- | ---- | ------- | ------------ | -------------- | --------- | ---------------- | --------------- | --- | --- | --- | --- |
|         |             |       |      |         |              |                | 𝑚         | 𝑛                |                 |     |     |     |     |
|         |             |       |      |         |              |                | (cid:214) | 𝜌𝕀[𝐴𝑖] (cid:214) | 𝜌𝕀[𝐹𝑗] 𝜌𝕀[Q]𝜌𝐶𝑇 |     |     |     |     |
|         |             |       |      |         | 𝑃(correct|𝐶) | =              | 𝑃         |                  |                 |     |     |     |     |
|         |             |       |      |         |              |                | 0         | 𝑎                | 𝑓               | 𝑝 𝑐 |     |     |     |
|         |             |       |      |         |              |                | 𝑖=1       | 𝑗=1              |                 |     |     |     |     |
|         | 𝑃           | (0,1] |      |         |              |                |           |                  |                 |     |     |     |     |
where ∈ represents the baseline success probability when all components are within the
0
training distribution, and 𝜌 ,𝜌 ,𝜌 ,𝜌 ∈ (0,1) are the degradation factors associated with novel
|     |     |     |     | 𝑎   | 𝑓   | 𝑝 𝑐 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
arguments, functions, patterns, and task-specific complexity, respectively.
|     |     |     |     |     |     | 𝑚   |     | 𝑛   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | ∑︁  |     | ∑︁  |     |     |     |     |     |
ln𝑃(correct | 𝐶) = ln𝑃 + 𝕀[𝐴 ] ln𝜌 + 𝕀[𝐹 ] ln𝜌 +𝕀[Q] ln𝜌 +𝐶 ln𝜌 (21)
|                |     |              |                |     | 0      |         | 𝑖        | 𝑎           | 𝑗   | 𝑓          | 𝑝    | 𝑇 𝑐 |      |
| -------------- | --- | ------------ | -------------- | --- | ------ | ------- | -------- | ----------- | --- | ---------- | ---- | --- | ---- |
|                |     |              |                |     |        | 𝑖=1     |          | 𝑗=1         |     |            |      |     |      |
| For notational |     | convenience, |                | we  | define | the     | positive | constants:  |     |            |      |     |      |
|                |     | 𝜉            | := −ln𝜌        |     | > 0,𝜉  | := −ln𝜌 | >        | 0,𝜉 := −ln𝜌 | >   | 0,𝜉 :=     | −ln𝜌 | >   |      |
|                |     |              | 𝑎              | 𝑎   |        | 𝑓       | 𝑓        | 𝑝           | 𝑝   | 𝑐          |      | 𝑐 0 |      |
| hence          | we  | have:        |                |     |        |         |          |             |     |            |      |     |      |
|                |     |              |                |     |        |         | 𝑚        |             | 𝑛   |            |      |     |      |
|                |     |              |                |     |        |         | ∑︁       |             | ∑︁  |            |      |     |      |
|                |     |              | ln𝑃(correct|𝐶) |     | =      | ln𝑃 −𝜉  |          | 𝕀[𝐴 ] −𝜉    | 𝕀[𝐹 | ] −𝜉 𝑝𝕀[Q] | −𝜉   | 𝐶   | (22) |
|                |     |              |                |     |        | 0       | 𝑎        | 𝑖 𝑓         | 𝑗   |            |      | 𝑐 𝑇 |      |
|                |     |              |                |     |        |         | 𝑖=1      |             | 𝑗=1 |            |      |     |      |
Lemma: RelationshiptoTGC.TheexpressioninequationabovecanbeboundedintermsofTGC(𝐶)
as follows:
|     |     |     |     |     | ln𝑃(correct|𝐶) |     |     | ln𝑃 −𝛿·TGC(𝐶) |     |     |     |     |      |
| --- | --- | --- | --- | --- | -------------- | --- | --- | ------------- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |                |     | ≤   | 0             |     |     |     |     | (23) |
19

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
|       | 𝛿 min( | 𝜉 𝑎, | 𝜉 𝑓, 𝜉 𝑝,𝜉 | ) > |     |     |     |     |     |     |     |     |
| ----- | ------ | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| where | =      |      |            | 𝑐   | 0.  |     |     |     |     |     |     |     |
|       |        | 𝛼    | 𝛽 𝛾        |     |     |     |     |     |     |     |     |     |
TGC(𝐶)
| Proof | of Lemma: |     | From | the    | definition | of  |     | in Eq. | (11), | we     | have: |      |
| ----- | --------- | --- | ---- | ------ | ---------- | --- | --- | ------ | ----- | ------ | ----- | ---- |
|       |           |     |      |        |            | 𝑚   |     | 𝑛      |       |        |       |      |
|       |           |     |      |        |            | ∑︁  |     | ∑︁     |       |        |       |      |
|       |           |     |      | TGC(𝐶) |            | 𝛼   | 𝕀[𝐴 | 𝛽      | 𝕀[𝐹   | +𝛾𝕀[Q] | +𝐶    |      |
|       |           |     |      |        |            | =   | 𝑖 ] | +      | 𝑗 ]   |        | 𝑇     | (24) |
|       |           |     |      |        |            | 𝑖=1 |     | 𝑗=1    |       |        |       |      |
𝛿,
| By the  | definition | of           | each | term        | in  | Eq. (22) | satisfies: |          |     |        |      |      |
| ------- | ---------- | ------------ | ---- | ----------- | --- | -------- | ---------- | -------- | --- | ------ | ---- | ---- |
|         |            |              |      |             |     | 𝑚        |            |          | 𝑚   |        |      |      |
|         |            |              |      |             |     | ∑︁       |            |          | ∑︁  |        |      |      |
|         |            |              |      |             |     | 𝜉        | 𝕀[𝐴        | ] ≥ 𝛿𝛼   | 𝕀[𝐴 | ]      |      |      |
|         |            |              |      |             |     | 𝑎        | 𝑖          |          |     | 𝑖      |      | (25) |
|         |            |              |      |             |     | 𝑖=1      |            |          | 𝑖=1 |        |      |      |
|         |            |              |      |             |     | 𝑛        |            |          | 𝑛   |        |      |      |
|         |            |              |      |             |     | ∑︁       |            |          | ∑︁  |        |      |      |
|         |            |              |      |             |     | 𝜉        | 𝕀[𝐹        | ] ≥ 𝛿𝛽   | 𝕀[𝐹 | ]      |      | (26) |
|         |            |              |      |             |     | 𝑓        | 𝑗          |          |     | 𝑗      |      |      |
|         |            |              |      |             |     | 𝑗=1      |            |          | 𝑗=1 |        |      |      |
|         |            |              |      |             |     |          | 𝜉 𝑝𝕀[Q]    | ≥ 𝛿𝛾𝕀[Q] |     |        |      | (27) |
|         |            |              |      |             |     |          | 𝜉 𝐶        | 𝛿𝐶       |     |        |      |      |
|         |            |              |      |             |     |          | 𝑐          | 𝑇 ≥      | 𝑇   |        |      | (28) |
| Summing | these      | inequalities |      | establishes |     | Eq.      | (23).      |          |     |        |      |      |
|         |            |              |      |             | 𝜏   | ln𝑃      |            |          |     | TGC(𝐶) | > 𝜏, |      |
We now define the threshold := 0. From Eq. (23), when we have:
𝛿
|     |     |     |     |     | ln𝑃(correct |     | | 𝐶) | ≤ ln𝑃 | −𝛿·TGC(𝐶) |     |     | (29) |
| --- | --- | --- | --- | --- | ----------- | --- | ---- | ----- | --------- | --- | --- | ---- |
0
|     |     |     |     |     |     |     |     | = 𝛿(𝜏−TGC(𝐶)) |     |     |     | (30) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | ---- |
−𝛿(TGC(𝐶)−𝜏)
|                |     |        |               |        |     |         |        | =         |     |      |                 | (31) |
| -------------- | --- | ------ | ------------- | ------ | --- | ------- | ------ | --------- | --- | ---- | --------------- | ---- |
|                |     |        |               |        |     |         |        | 𝑃(correct |     | | 𝐶) | ≤ 𝑒−𝛿(TGC(𝐶)−𝜏) |      |
| Exponentiating |     | both   | sides         | yields | the | desired | bound: |           |     |      |                 |      |
| A.3. Proof     | of  | Length | Extrapolation |        |     | Bound   |        |           |     |      |                 |      |
|                |     |        |               |        |     | 𝑓       |        |           |     |      | 𝐿.              |      |
Proof. Consideratransformermodel 𝜃 processingsequencesoflength Themodelimplicitlylearns
position-dependentrepresentationsthroughpositionalencodingsPE(𝑖) ∈ ℝ𝑑 forposition𝑖 ∈ {1,...,𝐿}
(cid:18) (cid:19)
𝑄 𝑖𝐾𝑇
| and attention |     | patterns | 𝐴   | = softmax |     | √ 𝑗 | .   |     |     |     |     |     |
| ------------- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑖𝑗
𝑑
During training on fixed length 𝐿 , the model learns a specific distribution:
train
|       |        |        |              |     |        | 𝑝     | (h) =   | 𝑝(h | 𝐿 | = 𝐿   | )   |     | (32) |
| ----- | ------ | ------ | ------------ | --- | ------ | ----- | ------- | ------- | ----- | --- | --- | ---- |
|       |        |        |              |     |        | train |         |         | train |     |     |      |
| where | h = {ℎ | ,...,ℎ | } represents |     | hidden |       | states. |         |       |     |     |      |
|       |        | 1      | 𝐿            |     |        |       |         |         |       |     |     |      |
|       |        |        |              | 𝐿   | ≠ 𝐿    |       |         |         |       |     |     |      |
For sequences of length train , we encounter distribution shift in two forms: (1) positional
encodingmismatch,wherethemodelhasneverseenpositions 𝑖 > 𝐿 if 𝐿 > 𝐿 ,and(2)attention
|     |     |     |     |     |     |     |     |     |     | train | train |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- |
pattern disruption, where the learned attention patterns are calibrated for length 𝐿 .
train
The KL divergence between training and test distributions can be bounded:
|     |     |     |     |     | 𝐷   | (𝑝      | ∥𝑝    | ) ∝ |𝐿−𝐿 |       | |2  |     |      |
| --- | --- | --- | --- | --- | --- | ------- | ----- | -------- | ----- | --- | --- | ---- |
|     |     |     |     |     |     | 𝐾𝐿 test | train |          | train |     |     | (33) |
This quadratic relationship arises from linear accumulation of positional encoding errors and
quadratic growth in attention pattern misalignment due to pairwise interactions.
| Let | E(𝐿) | be the | prediction |     | error | at length | 𝐿.       | We decompose |       | it as: |     |      |
| --- | ---- | ------ | ---------- | --- | ----- | --------- | -------- | ------------ | ----- | ------ | --- | ---- |
|     |      |        |            |     |       | E(𝐿)      |          | (𝐿)+E        |       | (𝐿)    |     |      |
|     |      |        |            |     |       | =         | E        |              |       |        |     | (34) |
|     |      |        |            |     |       |           | inherent |              | shift |        |     |      |
20

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
where E (𝐿) = E is the inherent model error (constant) and E (𝐿) is the error due to
|              | inherent |        | 0   |     |     |     |     |     | shift |     |     |
| ------------ | -------- | ------ | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
| distribution |          | shift. |     |     |     |     |     |     |       |     |     |
The distribution shift error follows from the Central Limit Theorem. As the error accumulates
| over | sequence | positions, |     | the total | shift | error converges | to:      |                         |     |     |     |
| ---- | -------- | ---------- | --- | --------- | ----- | --------------- | -------- | ----------------------- | --- | --- | --- |
|      |          |            |     |           |       | (cid:18)        | (cid:18) | (𝐿−𝐿 )2(cid:19)(cid:19) |     |     |     |
train
|     |     |     |     | E (𝐿) | =   | (1−E ) · 1−exp | −   |     |     |     | (35) |
| --- | --- | --- | --- | ----- | --- | -------------- | --- | --- | --- | --- | ---- |
|     |     |     |     | shift |     | 0              |     | 2𝜎2 |     |     |      |
This form ensures that E (𝐿 ) = 0 (no shift at training length) and lim E (𝐿) =
|     |     |     |     | shift | train |     |     |     |     | |𝐿−𝐿 |→∞ | shift |
| --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- | -------- | ----- |
train
| 1−E | (maximum | error | bounded |     | by 1). |     |     |     |     |     |     |
| --- | -------- | ----- | ------- | --- | ------ | --- | --- | --- | --- | --- | --- |
0
| The | width | parameter |     | 𝜎 depends | on: |     |     |     |     |     |     |
| --- | ----- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
√︄
𝑑
|     |     |     |     |     |     | 𝜎 = 𝜎 · |     |     |     |     | (36) |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     | 0       | 𝐿   |     |     |     |      |
train
√︁
where𝜎 isamodel-specificconstant, 𝑑 isthemodeldimension,andthe 𝑑/𝐿 factorcapturesthe
|               | 0   |            |       |          |             |           |          |       |                    | train |      |
| ------------- | --- | ---------- | ----- | -------- | ----------- | --------- | -------- | ----- | ------------------ | ----- | ---- |
| concentration |     | of measure |       | in high  | dimensions. |           |          |       |                    |       |      |
| Therefore,    |     | the total  | error | follows: |             |           |          |       |                    |       |      |
|               |     |            |       |          |             | (cid:18)  | (cid:18) | (𝐿−𝐿  | )2(cid:19)(cid:19) |       |      |
|               |     |            |       | E(𝐿)     |             |           |          | train |                    |       |      |
|               |     |            |       | =        | E +(1−E     | ) · 1−exp | −        |       |                    |       | (37) |
|               |     |            |       |          | 0           | 0         |          | 2𝜎2   |                    |       |      |
This Gaussian form naturally emerges from the accumulation of position-dependent errors and
𝐿 𝐿
matches the experimental observation of near-zero error at = with symmetric increase in both
train
| directions.   |     |     |         |     |     |     |     |     |     |     | □   |
| ------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| B. Experiment |     |     | Details |     |     |     |     |     |     |     |     |
ThemodelistrainedusingtheAdamWoptimiserinmixedprecision(FP16). Thedefaultlearningrate
is3×10−3,andtheschedulefollowsacosinedecaywitha10%warm-upratio. Trainingisconducted
for 10 epochs, using a batch size of 1024. A weight decay of 0.01 is applied, and gradient norms are
| clipped         | at                  | 1.0.         |          |                |          |               |       |     |     |     |     |
| --------------- | ------------------- | ------------ | -------- | -------------- | -------- | ------------- | ----- | --- | --- | --- | --- |
| C. Illustration |                     | of           | Datasets |                |          |               |       |     |     |     |     |
| Below           | are                 | the examples | of       | transformation |          | 𝑓 and 𝑓       | :     |     |     |     |     |
|                 |                     |              |          |                |          | 1             | 2     |     |     |     |     |
|                 | Transformation[F1]: |              |          | A A            | F Q      | [F1] <answer> | N N   | S D |     |     |     |
|                 | Transformation[F2]: |              |          | A A            | L P [F2] | <answer>      | A L P | A   |     |     |     |
aside from single transformation, we can composite transformations arbitrarily:
|     | Transformation[F1F2]: |     |     | A   | C I | A [F1] [F2]     | <think> |     |     |     |     |
| --- | --------------------- | --- | --- | --- | --- | --------------- | ------- | --- | --- | --- | --- |
|     |                       |     |     | N   | P V | N [F2] <answer> |         |     |     |     |     |
|     |                       |     |     | P   | V N | N               |         |     |     |     |     |
|     | Transformation[F2F2]: |     |     | N   | O V | S [F2] [F2]     | <think> |     |     |     |     |
<answer>
|     |     |     |     | O   | V S | N [F2] |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
|     |     |     |     | V   | S N | O      |     |     |     |     |     |
weuseexactmatch,editdistanceandBELUscoretomeasurethediscrepancybetweengenerated
tokens and the labels. For more than one transformation examples, we can further measure the
| discrepancy |     | for reasoning |     | and answering |     | seperately. |     |     |     |     |     |
| ----------- | --- | ------------- | --- | ------------- | --- | ----------- | --- | --- | --- | --- | --- |
21

IsChain-of-ThoughtReasoningofLLMsaMirage?ADataDistributionLens
| D. Additional   |           | Experimental   |     |          | Results |             |
| --------------- | --------- | -------------- | --- | -------- | ------- | ----------- |
| D.1. Additional |           | Qualitative    |     | Analysis |         |             |
| D.1.1.          | Orthognal | Transformation |     |          | Caused  | Coincidence |
The following case shows that even if the transformation is different, the model that trained on
transformation 𝑓 ◦ 𝑓 can still provide correct answer through incorrect reasoning:
|            |         | 2         | 1    |            |                |          |
| ---------- | ------- | --------- | ---- | ---------- | -------------- | -------- |
| Prompt:    |         | ’A A      | A B  | [F1]       | [F2] <answer>’ |          |
| Generated: |         | ’B A      | A A  | [F1]       | <answer>       | O N N N’ |
| Expected:  |         | ’O N      | N N’ |            |                |          |
| D.1.2.     | Correct | reasoning |      | but failed | in final       | answer   |
𝑓 ◦ 𝑓 , 𝑓 ◦
The following case shows that the model pretrained on the union of three transformation 1 2 2
| 𝑓 , 𝑓 ◦    | 𝑓 and   | test on       | 𝑓 ◦    | 𝑓    |               |          |
| ---------- | ------- | ------------- | ------ | ---- | ------------- | -------- |
| 1 2        | 2       |               | 1      | 1    |               |          |
| Prompt:    | ’A      | A A           | D [R1] | [R1] | <think>’      |          |
| Generated: |         | ’N N          | N Q    | [R1] | <answer>      | N N Q N’ |
| Expected:  |         | ’N N          | N Q    | [R1] | <answer>      | A A A D’ |
| D.1.3.     | Failure | to generalize |        | to   | novel element |          |
The following case shows that the model trained on element set 𝑎 ∈ [𝐴,𝑀] can not generalize to
𝑖
| unseen     | elements       | such | as N   | or O      |          |              |
| ---------- | -------------- | ---- | ------ | --------- | -------- | ------------ |
| Prompt:    | ’N             | N N  | O [F1] | [F1]      | <think>’ |              |
| Generated: |                | ’R V | Q S    | [F1]      | <answer> | E I D F’     |
| Expected:  |                | ’A A | A B    | [F1]      | <answer> | N N N O’     |
| D.1.4.     | LLM reproduces |      | CoT    | reasoning | at       | seen lengths |
The following case shows that model trained under 𝑓 ◦ 𝑓 tried to reproduce the length in training
1 1
data by adding tokens in the reason chain even prompted with seen transformation 𝑓
1
| Prompt:    | ’A  | A B      | D [f1] | <answer>’ |          |     |
| ---------- | --- | -------- | ------ | --------- | -------- | --- |
| Generated: |     | ’N O     | A Z    | N N       | O Q [f1] |     |
|            |     | <answer> |        | A         | A B D’   |     |
| Expected:  |     | ’N N     | O Q’   |           |          |     |
22