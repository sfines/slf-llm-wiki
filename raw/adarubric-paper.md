*Response size: ~22K tokens. Consider using zotero_semantic_search to find specific content instead of reading full papers.*

# AdaRubric: Task-Adaptive Rubrics for Reliable LLM Agent Evaluation and Reward Learning

**Type:** webpage

**Item Key:** 4TLDU6XB

**Date:** 2026/03/22

**Authors:** Ding, Liang

**URL:** https://arxiv.org/abs/2603.21362v3



## Abstract

Evaluating LLM agent trajectories is fundamentally task-specific: a code-debugging agent should be judged on Correctness and Error Handling, not on Fluency or Safety. Yet the dominant paradigm -- LLM-as-Judge with a fixed rubric -- applies the same static dimensions regardless of task, producing systematic mis-evaluation. We present AdaRubric, a framework that (i) adaptively generates task-specific evaluation rubrics from task descriptions via LLM, (ii) evaluates agent trajectories step-by-step with confidence-weighted, per-dimension scoring, and (iii) produces dense reward signals for preference learning. Three composable filtering strategies, including the novel DimensionAwareFilter that provably prevents dimension-level quality masking, yield high-quality DPO preference pairs. On WebArena, ToolBench, and AgentBench, AdaRubric achieves Pearson r = 0.79 human correlation (+0.15 over the strongest baseline), with strong reliability (Krippendorff's alpha = 0.83). DPO models trained on AdaRubric-generated pairs improve task success by +6.8-8.5% over the best baseline. AdaRubric also generalises zero-shot to unseen domains (SWE-bench) and extends to multimodal agents (VisualWebArena, OSWorld) without modification. Our code is available at: github.com/alphadl/AdaRubrics

**Notes/Attachments:** 1

---

## Full Text

|     |          |     | ADARUBRIC: |     |       | Task-Adaptive |     | Rubrics |     | for      |     |     |     |
| --- | -------- | --- | ---------- | --- | ----- | ------------- | --- | ------- | --- | -------- | --- | --- | --- |
|     | Reliable |     | LLM        |     | Agent | Evaluation    | and | Reward  |     | Learning |     |     |     |
LiangDing
TheUniversityofSydney
liangding.liam@gmail.com
|     |     | Abstract |     |     |     |     |           |              |     |        |           |     | Ada(Code)         |
| --- | --- | -------- | --- | --- | --- | --- | --------- | ------------ | --- | ------ | --------- | --- | ----------------- |
|     |     |          |     |     |     |     |           | StaticRubric |     |        |           |     | Correctness       |
|     |     |          |     |     |     |     | CodeDebug |              |     |        | CodeDebug |     | Err.Handle r=0.79 |
|     |     |          |     |     |     |     |           | Helpfulness  |     | r=0.47 |           |     | Efficiency        |
6202 yaM 01  ]IA.sc[  3v26312.3062:viXra
Evaluating LLM agent trajectories is funda- Fluency Ada(Search)
|     |     |     |     |     |     |     |     |     | Safety |     |     |     | C o v e ra g e |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | -------------- |
mentallytask-specific: acode-debuggingagent WebSearch r=0.44 WebSearch
|           |                       |        |                |            |               |       |              |                     |         |           |              |            | T o o l A c c . r=0.74 |
| --------- | --------------------- | ------ | -------------- | ---------- | ------------- | ----- | ------------ | ------------------- | ------- | --------- | ------------ | ---------- | ---------------------- |
| should    | be                    | judged | on Correctness |            | and           | Error |              |                     |         |           |              |            | Synthesis              |
|           |                       |        |                |            |               |       |              | (a)StaticEval.      |         |           | (b)ADARUBRIC |            |                        |
| Handling, | not                   | on     | Fluency        | or Safety. | Yet           | the   |              |                     |         |           |              |            |                        |
| dominant  | paradigm—LLM-as-Judge |        |                |            | with          | a     |              |                     |         |           |              |            |                        |
|           |                       |        |                |            |               |       | Figure1:     | Staticevaluationvs. |         |           | ADARUBRIC.   |            | Static                 |
| fixed     | rubric—applies        |        | the            | same       | static dimen- |       |              |                     |         |           |              |            |                        |
|           |                       |        |                |            |               |       | LLM-as-Judge |                     | applies | identical |              | dimensions | to all                 |
sionsregardlessoftask,producingsystematic tasks(r≈0.46). ADARUBRICsynthesisestask-specific
| mis-evaluation. |     | We  | present | ADARUBRIC, |     | a   |     |     |     |     |     |     |     |
| --------------- | --- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rubrics(r≈0.77).
| framework |            | that (i) | adaptively | generates |               | task- |          |           |         |     |      |                |     |
| --------- | ---------- | -------- | ---------- | --------- | ------------- | ----- | -------- | --------- | ------- | --- | ---- | -------------- | --- |
| specific  | evaluation |          | rubrics    | from      | task descrip- |       |          |           |         |     |      |                |     |
|           |            |          |            |           |               |       | steps of | uncertain | quality |     | (Liu | et al., 2023a; | Pan |
| tions     | via LLM,   | (ii)     | evaluates  | agent     | trajecto-     |       |          |           |         |     |      |                |     |
etal.,2024),makingundifferentiatedqualityjudg-
| ries | step-by-step |     | with confidence-weighted, |     |     |     |     |     |     |     |     |     |     |
| ---- | ------------ | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
per-dimension scoring, and (iii) produces ments insufficient for training or deployment. A
|       |        |         |     |            |           |     | key question |     | for the | knowledge-in-LMs |     |     | commu- |
| ----- | ------ | ------- | --- | ---------- | --------- | --- | ------------ | --- | ------- | ---------------- | --- | --- | ------ |
| dense | reward | signals | for | preference | learning. |     |              |     |         |                  |     |     |        |
Three composable filtering strategies, includ- nityis: howshouldanLLMevaluatorleverageits
ingthenovelDimensionAwareFilterthatprov-
knowledgetogeneratetask-appropriateevaluation
ably prevents dimension-level quality mask- criteria,ratherthanapplyingafixed,one-size-fits-
ing, yieldhigh-qualityDPOpreferencepairs.
allrubric?
| On WebArena, |     | ToolBench, |     | and | AgentBench, |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
ADARUBRIC achieves Pearson r=0.79 hu- The static-rubric bottleneck. Two dominant
| man        | correlation |             | (+0.15      | over the | strongest |     |            |           |     |      |     |         |         |
| ---------- | ----------- | ----------- | ----------- | -------- | --------- | --- | ---------- | --------- | --- | ---- | --- | ------- | ------- |
|            |             |             |             |          |           |     | evaluation | paradigms |     | fail | for | complex | agents. |
| baseline), |             | with strong | reliability |          | (Krippen- |     |            |           |     |      |     |         |         |
Reference-basedmetrics(ROUGE-L,BERTScore)
| dorff’s | α=0.83). |     | DPO | models | trained | on  |         |         |         |     |         |       |          |
| ------- | -------- | --- | --- | ------ | ------- | --- | ------- | ------- | ------- | --- | ------- | ----- | -------- |
|         |          |     |     |        |         |     | measure | surface | overlap |     | and are | blind | to goal- |
ADARUBRIC-generatedpairsimprovetasksuc-
|      |               |     |      |     |                |     | directed | reasoning. |     | LLM-as-Judge |     | (Zheng | et al., |
| ---- | ------------- | --- | ---- | --- | -------------- | --- | -------- | ---------- | --- | ------------ | --- | ------ | ------- |
| cess | by +6.8–+8.5% |     | over | the | best baseline. |     |          |            |     |              |     |        |         |
ADARUBRICalsogeneraliseszero-shottoun- 2023;Liuetal.,2023b)appliesfixeddimensions—
seendomains(SWE-bench)andextendstomul- Helpfulness, Fluency, Safety—regardless of task.
timodal agents (VisualWebArena, OSWorld) Thesedimensionsweredesignedforchatassistants,
| withoutmodification. |     |     | Ourcodeisavailableat: |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
notgoal-directedagentsoperatingthroughtooluse
github.com/alphadl/AdaRubrics
andmulti-stepplanning.
| 1 Introduction |     |     |     |     |     |     | Motivating |     | example. |     | A ToolBench |     | API- |
| -------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | --- | ----------- | --- | ---- |
chainingtaskhasmeaningfulqualitydimensions
| LLM now | automates |     | complex | multi-step |     | tasks |     |     |     |     |     |     |     |
| ------- | --------- | --- | ------- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
ofAPISelectionAccuracy,ParameterCorrectness,
| across web | automation |     | (Zhou | et  | al., 2023), | API |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | ----- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
andErrorRecovery—noneappearinginastandard
orchestration(Qinetal.,2023),softwareengineer-
|              |      |         |        |                |             |       | helpfulnessrubric. |           |          | Conversely,afluency-focused |           |     |           |
| ------------ | ---- | ------- | ------ | -------------- | ----------- | ----- | ------------------ | --------- | -------- | --------------------------- | --------- | --- | --------- |
| ing (Jimenez |      | et al., | 2023), | and multimodal |             | envi- |                    |           |          |                             |           |     |           |
|              |      |         |        |                |             |       | rubric             | penalises | agents   | that                        | correctly |     | call APIs |
| ronments     | (Koh | et al., | 2024;  | Xie et         | al., 2024). | As    |                    |           |          |                             |           |     |           |
|              |      |         |        |                |             |       | but produce        |           | compact, | machine-readable            |           |     | output.   |
agentsscale,reliabletrajectoryevaluationbecomes
Staticrubricsintroducesystematicbiasandreward
thecornerstoneofsafety,alignment,anditerative
irrelevantstylisticpropertiesovertasksuccess.
| improvement. |     | Yet | studies | show | that a | substan- |     |     |     |     |     |     |     |
| ------------ | --- | --- | ------- | ---- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
tialfractionofagenttrajectoriesproducedbyfron- AdaRubric. Wepropose ADARUBRIC,builton
tiermodelsonrepresentativebenchmarkscontain theinsight: evaluationdimensionsshouldbeafunc-

tionofthetask,notafixedpropertyoftheevaluator. LLMagentevaluation. WebArena(Zhouetal.,
Given a task description T, ADARUBRIC gener- 2023),ToolBench(Qinetal.,2023),AgentBench
atesaDynamicRubricR(T)comprisingN task- (Liuetal.,2023a),andSWE-bench(Jimenezetal.,
specific, orthogonal evaluation dimensions with 2023) provide task-specific success signals. Pan
calibrated5-pointscoringcriteria. Thisapproach et al. (2024) proposes autonomous evaluation by
directlyleveragestheLLM’sparametricknowledge output comparison. Lu et al. (2025) study agent
abouttaskstructure,successcriteria,anddomain trajectoryqualityfromadifferentangle,showing
conventionstoproduceevaluationsalignedwithhu- thatearly-exitstrategiesreduceredundantstepsin
manexpertjudgment. Figure1showsthecontrast embodied agents and introducing efficiency and
betweenstaticandadaptiveevaluation. progress metrics that are natural reward compo-
|     |     |     |     |     |     |     | nents. Thesesignalsarebinaryorcoarse-grained, |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
Contributions. non-transferableacrosstasks,andoffernoper-step
rewardsignalsuitableforRLtraining—alimitation
| 1. Adaptive | rubric |     | generation | (§3.2): |     | task- |     |     |     |     |     |     |     |
| ----------- | ------ | --- | ---------- | ------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
specific,orthogonalevaluationdimensionswith ADARUBRIC addressesdirectly.
calibratedscoringcriteria,generatedfromtask
|     |     |     |     |     |     |     | RewardsignalsandRLHF/DPO. |     |     |     |     | RLHF(Chris- |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | ----------- | --- |
descriptionsviaLLMs’parametricknowledge.
|     |     |     |     |     |     |     | tiano et | al., 2017; | Ziegler | et  | al., | 2019; | Stiennon |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ------- | --- | ---- | ----- | -------- |
2. Multi-dimensional dense rewards (§3.3): et al., 2020; Ouyang et al., 2022) trains scalar re-
confidence-weighted, per-step, per-dimension ward models; DPO (Rafailov et al., 2023) elim-
|     |     |     |     |     |     |     | inates the | explicit | reward | model |     | entirely. | Tülu |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------ | ----- | --- | --------- | ---- |
scoringforpost-trainingprocess,e.g.,RL/DPO.
(Wangetal.,2023;Ivisonetal.,2023)showsthat
| 3. Reliability |     | quantification |     | (§3.6): | Krippen- |     |     |     |     |     |     |     |     |
| -------------- | --- | -------------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
preferencedataqualitycriticallydeterminesRLHF
dorff’sαprovidesaprincipleddeploymentcri- effectiveness. Process reward models (Lightman
| terion(α      | ≥ 0.80)forLLM-basedevaluators. |                        |         |           |          |       |              |            |            |                  |                |            |           |
| ------------- | ------------------------------ | ---------------------- | ------- | --------- | -------- | ----- | ------------ | ---------- | ---------- | ---------------- | -------------- | ---------- | --------- |
|               |                                |                        |         |           |          |       | et al.,2023; | Cobbeet    |            | al., 2021)assign |                | step-level |           |
|               |                                |                        |         |           |          |       | credits      | for math   | reasoning; |                  | self-rewarding |            | LMs       |
| 4. End-to-end |                                | evaluation-to-training |         |           | pipeline |       |              |            |            |                  |                |            |           |
|               |                                |                        |         |           |          |       | (Yuan et     | al., 2024) | close      | the              | loop.          | Most       | recently, |
| (§3.4):       | composable                     |                        | filters | including | the      | novel |              |            |            |                  |                |            |           |
DRTulu(Shaoetal.,2025)introducesReinforce-
| DimensionAwareFilter |     |     | that | provably | prevents |     |               |     |      |          |         |     |         |
| -------------------- | --- | --- | ---- | -------- | -------- | --- | ------------- | --- | ---- | -------- | ------- | --- | ------- |
|                      |     |     |      |          |          |     | ment Learning |     | with | Evolving | Rubrics |     | (RLER), |
per-dimensionqualitymasking.
|     |     |     |     |     |     |     | where instance-specific, |      |            | search-grounded |     |             | rubrics |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | ---- | ---------- | --------------- | --- | ----------- | ------- |
|     |     |     |     |     |     |     | co-evolve                | with | the policy | during          |     | RL training | for     |
2 RelatedWork
|                         |     |     |     |                  |     |     | long-formdeepresearchtasks. |     |     |                        | ADARUBRIC |     | dif- |
| ----------------------- | --- | --- | --- | ---------------- | --- | --- | --------------------------- | --- | --- | ---------------------- | --------- | --- | ---- |
|                         |     |     |     |                  |     |     | fersinthreekeyrespects:     |     |     | (i)rubricsaregenerated |           |     |      |
| LLM-as-Judgeevaluation. |     |     |     | Zhengetal.(2023) |     |     |                             |     |     |                        |           |     |      |
pertasktype(notperinstance)andcached,making
| established | MT-Bench |     | and Chatbot |     | Arena | using |     |     |     |     |     |     |     |
| ----------- | -------- | --- | ----------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
evaluation>95%cheaper;(ii)rubricsderivefrom
| pairwise | comparison | with | fixed | dimensions. |     | G-  |     |     |     |     |     |     |     |
| -------- | ---------- | ---- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theLLM’sparametricknowledgeratherthanexter-
| Eval (Liu | et al., | 2023b) | employs | GPT-4 | with | ex- |     |     |     |     |     |     |     |
| --------- | ------- | ------ | ------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
plicit criteria for NLG. Prometheus (Kim et al., nalretrieval;(iii)thefocusisagenttrajectoryeval-
uationandrewardsynthesisratherthanlong-form
| 2023) fine-tunes |          | a 13B        | judge | requiring    | labelled |         |                   |                               |        |               |     |         |       |
| ---------------- | -------- | ------------ | ----- | ------------ | -------- | ------- | ----------------- | ----------------------------- | ------ | ------------- | --- | ------- | ----- |
|                  |          |              |       |              |          |         | QAtraining.       | Thetwoapproachesarecomplemen- |        |               |     |         |       |
| training         | data per | task domain. |       | FLASK        | (Ye      | et al., |                   |                               |        |               |     |         |       |
|                  |          |              |       |              |          |         | tary: ADARUBRIC’s |                               |        | task-adaptive |     | rubrics | could |
| 2023) decomposes |          | quality      | into  | fine-grained |          | skill   |                   |                               |        |               |     |         |       |
|                  |          |              |       |              |          |         | serve as          | the initial                   | rubric | framework     |     | that    | RLER  |
sets;JudgeLM(Zhuetal.,2023)trainsjudgesfrom
thenevolvesonlineduringtraining.
| large (question, |     | answer, | judgment) |     | corpora. | Re- |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
wardBench(Lambertetal.,2025)providesasys-
|     |     |     |     |     |     |     | AgentHERandtrajectoryaugmentation. |     |     |     |     |     | One |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
tematicbenchmarkforcomparingrewardmodels
concurrentwork(Ding,2026)relabelsfailedagent
| across task | types, | sharpening |     | the need | for | task- |     |     |     |     |     |     |     |
| ----------- | ------ | ---------- | --- | -------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
trajectoriesviahindsightexperiencereplay,focus-
| sensitive | evaluation | criteria. |     | Lu et | al. (2023) | de- |                        |     |     |     |           |     |         |
| --------- | ---------- | --------- | --- | ----- | ---------- | --- | ---------------------- | --- | --- | --- | --------- | --- | ------- |
|           |            |           |     |       |            |     | ingondataaugmentation. |     |     |     | ADARUBRIC |     | focuses |
composeNLGevaluationintomajorandminorer- onprincipledevaluationandrewardsynthesis,and
roraxes,anearlyinstantiationofstructured,rubric-
thetwoapproachesarenaturallycomplementary.
likescoringthatmotivatesourtask-adaptivedimen-
siondesign. Yetallthesemethodsrelyonfixedor Inter-raterreliability. Krippendorff’sα(Krip-
pre-trained dimensions; ADARUBRIC closes this pendorff,2011)andFleiss’κ(Fleiss,1971)quan-
gap by generating criteria dynamically from the tifyhumanannotationagreement. Weapplythese
taskathand,withoutmanualdesignorfine-tuning. metrics to quantify LLM evaluator consistency

1 Algorithm1: ADARUBRICEvaluationPipeline
S1
TaskT
RubricGen. 2 3 Require: Task T, trajectories {τ }, LLM M,
S2 S3 i
Trajs{τi} Evaluator Filter DPOPairs paramsN,λ,δ min
Ensure: DPOpairsP,scores{S(τ )}
i
Figure2: ADARUBRICpipeline. Stage1synthesises 1. RubricGeneration
a task-adaptive rubric. Stage 2 evaluates trajectories
R(T) ← M(RUBRIC_PROMPT(T)) //
per-step×per-dimension. Stage3appliescomposable
adaptive,cached
filtersandgeneratesDPOpairs.
ValidateR;retryonceonfailure
2. TrajectoryEvaluationforeachτ :
acrossevaluationruns,providingaprincipledcrite- i
fork = 1...K,j = 1...N do
rionfordeployment.
(s ,c ) ←
k,j k,j
3 The ADARUBRIC Framework M(EVAL_PROMPT(t
k
,a
k
,o
k
,d
j
,Γ
j
))
Aggregate: s¯ ← WM(s ,c ,λ)
j ·,j ·,j
3.1 ProblemFormulation (cid:80)
S(τ ) ← w s¯
i j j j
AtaskT = (i,d,c,E)comprisesinstructioni,do-
3. Filtering&PairConstruction
maind,contextc,andexpectedtools/modalitiesE. (cid:0) (cid:1)
F ← DIMAWAREFILTER {τ
i
},{s¯
i,j
},θ
An agent trajectory τ = {(t k ,a k ,o k )}K k=1 con- P ← (cid:8) (τ i +,τ j −) | τ i ,τ j ∈ F, S(τ i )−S(τ j ) ≥
sists of K steps of (thought, action, observation). (cid:9)
δ
min
Staticevaluationmapsτ toascalar; ADARUBRIC
returnP,{S(τ )}
i
producesstructured,task-conditionedevaluations:
f (τ; R(T)) →
(cid:8)
(s , c )
(cid:9)K,N
, (1)
Figure3: CompleteADARUBRICpipeline. Allthree
ada k,j k,j k=1,j=1 stagesaremodular;anyLLMcanserveasM.
where s ∈ {1,...,5} and c ∈ [0,1] is the
k,j k,j
withschema)ensuresparseableoutput(Yangetal.,
confidence(steprelevancetodimensionj).
2024;Grattafiorietal.,2024). Thisstagedirectly
Definition 3.1 (Task-Adaptive Rubric). R(T) =
leveragestheLLM’sknowledgeoftaskstructures,
{(d ,w ,Γ )}N ,whered isadimensionname,
j j j j=1 j domainconventions,andevaluationbestpractices—
w j > 0 with (cid:80) j w j = 1, and Γ j = (γ 1 j,...,γ 5 j) preciselythetypeofknowledgethatKnowFMaims
areverbalizedscoringcriteria. Avalidrubricsat- tounderstandandimprove. Rubricsarecachedper
isfies: (i)Task-relevance: d j derivedfromT’ssuc- task type: generating once for a task description
cess criteria; (ii) Orthogonality: dimensions are andreusingacrossalltrajectorieswithinthattask
semanticallynon-overlapping;(iii)Completeness: familyreducesAPIcostby>95%withnolossin
(cid:83)
j d j covers T’s key success aspects; (iv) Cal- evaluationquality.
ibration: γj =“acceptable”, γj =“broken”,
3 1
γj =“exemplary”. Rubricvalidation. Generatedrubricspassthree
5
automated checks: (i) dimension names are non-
ADARUBRICoperatesthroughthreestages(Fig-
overlapping (> 0.3 cosine distance); (ii) weights
ure2)followedbyrewardsynthesis.
sumto1within1%;(iii)allfivescoringlevelsare
populated. Rubricsfailingvalidationtriggerasin-
3.2 Stage1: AdaptiveRubricGeneration
gleretry;persistentfailuresfallbacktoadomain-
GiventaskT, ADARUBRIC promptsasfollows:
specifictemplaterubric.
(cid:0) (cid:1)
R(T) = LLM RUBRIC_PROMPT(T) , (2)
3.3 Stage2: Confidence-WeightedEvaluation
producing N dimension tuples (d j ,w j ,Γ j ) as For each step k and dimension j, the evaluator
structuredoutput. ThepromptinstructstheLLM LLMreceives(t ,a ,o ,d ,Γ )andreturns:
k k k j j
to (1) identify task-critical success criteria from
itsparametricknowledge,(2)clusterthemintoN s ∈ {1,2,3,4,5}, c ∈ [0,1]. (3)
k,j k,j
orthogonaldimensions(defaultN=5),(3)assign
relativeimportanceweightsw j ,and(4)verbalise Confidencec k,j islowwhenstepkdoesnotdirectly
five scoring levels γj...γj with concrete exam- engagedimensionj (e.g.,apurereasoningstepfor
1 5
plebehaviours. Structuredgeneration(i.e.,JSON theToolAccuracydimension).

Threepluggablestrategiesaggregatestepscores 3.5 RewardSignalSynthesis
toper-dimensionglobalscores:
FromfilteredevaluationssortedbyS(τ),DPOpref-
erencepairsare:
(cid:80)
s ·c ·w
s¯WM = k k,j k,j k , w = eλk/max(K−1,1),
j (cid:80) k w k k P = (cid:8) (τ i +,τ j −,m ij ) (cid:12) (cid:12) m ij = S(τ i )−S(τ j ) ≥ δ min (cid:9) .
(4) (7)
(cid:16) (cid:17)
s¯GM = exp 1 (cid:80) logmax(s ,10−8) , (5) Margin m ij can modulate the DPO loss weight
j K k k,j (Ding, 2026). This yields both quality-assured
s¯M j in = mins k,j . (6) preferredtrajectoriesandinformativedispreferred
k
ones—keypropertiesthatrandompairinglacks.
WeightedMean(WM,default)handlesheteroge-
3.6 ReliabilityQuantification
neousstepimportance; λ ≥ 0isarecency-decay
parameter up-weighting final steps. Geometric To deploy ADARUBRIC in practice, one needs a
Mean(GM)enforcesbalancedcompetencyacross principledstoppingcriterionforrubricquality. We
steps. MinScoreisappropriateforsafety-critical applyKrippendorff’sα(Krippendorff,2011):
taskswhereanystepfailureisdisqualifying. The
globaltrajectoryscoreisS(τ) = (cid:80) w s¯ . α = 1− D o , D = 1 (cid:88)(cid:88) (r −r′ )2,
j j j D o n ij ij
Under an inverse-confidence noise model, e i j>i
confidence-weightedaggregationistheBestLinear (8)
UnbiasedEstimator(BLUE)fortheper-dimension wherer ij andr i ′ j arescoresfromtwoindependent
scorebyGauss-Markov,yieldingstrictlylowervari- evaluation runs (treating each run as an “annota-
ancethanuniformaveraging(seeAppendixB).We tor”) on the same trajectory set. We recommend
note the Gaussian assumption is an idealisation:
deploymentwhenα ≥ 0.80.
empirically (Appendix B), residuals on our held-
4 Experiments
out annotation set are approximately mean-zero
withheavier-than-Gaussiantails,soBLUEshould 4.1 Setup
bereadasamotivatingrationaleratherthanastrict
Benchmarks. WebArena (Zhou et al., 2023):
guarantee.
812web-automationtasksacross5domains. Tool-
Bench(Qinetal.,2023): 500API-chainingtasks
3.4 Stage3: Confidence-FilteredSelection
using real-world APIs. AgentBench (Liu et al.,
4 composable filter primitives: AbsoluteThresh- 2023a): 365 code/OS/database tasks. For hu-
old: S(τ) ≥ θ global . PercentileFilter: top-p% of man correlation, 300 randomly-sampled trajec-
the batch. DimensionAwareFilter: s¯ j ≥ θ j ∀j. tory pairs per benchmark are annotated by three
CompositeFilter: logicalANDofanysubset. annotators; inter-annotator agreement κ > 0.82
Remark 1. An LLM agent trajectory with on all splits. Annotators received a written pro-
(s¯ =5,s¯ =5,s¯ =1) achieves tocol (task description, trajectory transcript, 1–5
Search Extract Reason
S(τ)=3.8 (passing θ=3.5) yet fails at reasoning. rubric, disagreement-resolution rules); we report
DimensionAwareFilterwithθ =3.0correctly 95% bootstrap CIs on Pearson r (±0.02 on av-
Reason
rejectsit. erage) and all ADARUBRIC-vs-baseline gaps are
significantatp<0.01(pairedbootstrap).
For any scalar threshold θ′, there exists a tra-
jectory that passes AbsoluteThreshold while one Models. Evaluator: GPT-4o for ADARUBRIC
dimensionscoresnearzero;DimensionAwareFilter and GPT-4 Direct baselines; Llama-3.1-70B-
closesthisgapbyconstruction(Proposition3.1). Instructforablations. DPObackbone: Qwen2.5-
7B-Instruct (Yang et al., 2024), Llama-3.1-8B-
Proposition3.1(Masking-Prevention). LetN ≥ 2
(cid:80) Instruct(Grattafiorietal.,2024). Fine-tuninguses
dimensions with weights w > 0, w =1, per-
j j j LoRA(Huetal.,2022)withrank16,α=32.
dimensionthresholdsθ ,andθ¯= (cid:80) w θ . Then:
j j j j
(a) F (τ)=1 ⇒ F (τ)=1. (b) For any j∗ Baselines. ROUGE-L(Lin,2004),BERTScore
DA AT
and ϵ > 0, ∃τ∗ with s¯ (τ∗) = ϵ < θ yet (Zhang et al., 2019), G-Eval (Liu et al., 2023b),
j∗ j∗
F (τ∗)=1. (c)Noscalarthresholdθ′ canelimi- Prometheus (Kim et al., 2023), GPT-4 Direct
AT
nate(b). (single-turn, no rubric). To isolate adaptivity

Table 1: Human correlation (Pearson r). Table 2: Multi-benchmark DPO training results.
ADARUBRIC-DA: DimensionAwareFilter vari- WebArena (SR%), ToolBench (TCR%), AgentBench
ant. ∆vs.GPT-4Direct. (SR%). Qwen2.5-7Bbackbone. ∆vs.Prometheus.
| Method |     | WA  | TB  | AB Avg | ∆   |     | Method |     |     | WA  | TB  | AB  |
| ------ | --- | --- | --- | ------ | --- | --- | ------ | --- | --- | --- | --- | --- |
ROUGE-L 0.31 0.26 0.29 0.29 −0.35 Base(zero-shot) 12.3 18.4 15.2
BERTScore 0.43 0.39 0.41 0.41 −0.23 SFT–Successonly 16.7 23.1 20.1
| G-Eval |     | 0.54 | 0.49 | 0.52 0.52 | −0.12 |     | DPO–Random |     |     | 17.4 | 24.8 | 21.3 |
| ------ | --- | ---- | ---- | --------- | ----- | --- | ---------- | --- | --- | ---- | ---- | ---- |
Prometheus 0.61 0.57 0.59 0.59 −0.05 DPO–G-Eval 20.1 27.6 24.5
GPT-4Direct 0.64 0.60 0.62 0.62 — DPO–Prometheus 21.0 29.3 26.4
ADARUBRIC-WM 0.74 0.70 0.72 0.72 +0.10 DPO–ADARUBRIC-WM 24.3 34.2 30.8
+0.12
ADARUBRIC-GM 0.76 0.71 0.74 0.74 DPO–ADARUBRIC-GM 25.1 35.6 31.9
ADARUBRIC-DA 0.79 0.74 0.77 0.77 +0.15 DPO–ADARUBRIC-DA 27.8 37.8 34.1
|                            |     |     |     |                   |     |       | ∆vs.Prom.     |             |     | +6.8            | +8.5 +7.7 |     |
| -------------------------- | --- | --- | --- | ----------------- | --- | ----- | ------------- | ----------- | --- | --------------- | --------- | --- |
| fromextratest-timecompute, |     |     |     | weadditionallyin- |     |       |               |             |     |                 |           |     |
|                            |     |     |     |                   |     | Table | 3: Evaluation | reliability |     | (Krippendorff’s |           | α). |
clude a compute-matched baseline, GPT-4 CoT- WA=WebArena,TB=ToolBench.
| Decomposed,      |     | which        | re-invokes | GPT-4o  | with      |     |        |     |     |     |     |     |
| ---------------- | --- | ------------ | ---------- | ------- | --------- | --- | ------ | --- | --- | --- | --- | --- |
| chain-of-thought |     | and per-step |            | scoring | using the |     |        |     |     |     |     |     |
|                  |     |              |            |         |           |     | Method |     | WA  | TB  | Avg |     |
samestaticHelpfulness/Fluency/Safetyrubricand
|                       |     |     |     |             |       |     | G-Eval(GPT-4o) |     | 0.64 | 0.61 | 0.63 |     |
| --------------------- | --- | --- | --- | ----------- | ----- | --- | -------------- | --- | ---- | ---- | ---- | --- |
| matchesADARUBRIC’sK×N |     |     |     | callbudget. | OnWe- |     |                |     |      |      |      |     |
|                       |     |     |     |             |       |     | Prometheus     |     | 0.71 | 0.68 | 0.70 |     |
bArenaitreachesr=0.68(vs.GPT-4Direct0.64 GPT-4Direct 0.69 0.66 0.68
and ADARUBRIC-DA 0.79), indicating that the ADARUBRIC-WM 0.81 0.79 0.80
|            |     |               |     |              |          |     | ADARUBRIC-GM |     | 0.83 | 0.80 | 0.82 |     |
| ---------- | --- | ------------- | --- | ------------ | -------- | --- | ------------ | --- | ---- | ---- | ---- | --- |
| +0.15 gain | is  | predominantly |     | attributable | to task- |     |              |     |      |      |      |     |
|            |     |               |     |              |          |     | ADARUBRIC-DA |     | 0.85 | 0.82 | 0.84 |     |
adaptiverubricsratherthantoincreasedtest-time
| compute. | ForDPO:randompairing,SFTonsuc- |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4.3 Multi-BenchmarkDPOTraining
cessfultrajectories.
|     |     |     |     |     |     | Table | 2 extends | the | DPO | analysis | to  | all three |
| --- | --- | --- | --- | --- | --- | ----- | --------- | --- | --- | -------- | --- | --------- |
Metrics. Evaluationquality: Pearsonr withex- benchmarks,usingQwen2.5-7Basthesharedback-
| perthumanrankings.          |     | Reliability: |     | Krippendorff’s |      |            |     |                                |     |     |     |     |
| --------------------------- | --- | ------------ | --- | -------------- | ---- | ---------- | --- | ------------------------------ | --- | --- | --- | --- |
|                             |     |              |     |                |      | bonemodel. |     | ADARUBRIC-DAconsistentlydeliv- |     |     |     |     |
| αacrossthreeevaluationruns. |     |              |     | Downstream:    | task |            |     |                                |     |     |     |     |
ersthelargestimprovementsacrosstaskfamilies:
successrate(SR%)ortaskcompletionrate(TCR%)
webautomation,APIorchestration,andOS/code
afterDPOfine-tuning.
tasks. ThegainsarelargestonToolBench(+8.5%),
wheretaskdiversityishighestandstaticrubricmis-
| 4.2 MainResults:      |     | EvaluationQuality |                       |     |     |               |         |         |          |            |        |         |
| --------------------- | --- | ----------------- | --------------------- | --- | --- | ------------- | ------- | ------- | -------- | ---------- | ------ | ------- |
|                       |     |                   |                       |     |     | specification |         | is most | severe.  | AgentBench |        | gains   |
|                       |     |                   |                       |     |     | (+7.7%)       | confirm | thatthe | benefits |            | extend | to code |
| Table1reportsPearsonr |     |                   | betweenevaluatorrank- |     |     |               |         |         |          |            |        |         |
ingsandhumanexpertrankings. ADARUBRIC-DA andOSmanipulationtasks—domainsnotseendur-
achieves r=0.79/0.74/0.77 across benchmarks, ingrubricpromptdesign.
| outperforming |     | all baselines | including |     | GPT-4 Di- |     |     |     |     |     |     |     |
| ------------- | --- | ------------- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
4.4 EvaluationReliability
rect(r=0.64/0.60/0.62).
|                   |     |     |          |            |     | Table       | 3 reports | inter-run  | Krippendorff’s |              |     | α (three |
| ----------------- | --- | --- | -------- | ---------- | --- | ----------- | --------- | ---------- | -------------- | ------------ | --- | -------- |
| Key observations. |     | 1)  | Adaptive | dimensions | are |             |           |            |                |              |     |          |
|                   |     |     |          |            |     | independent |           | evaluation | runs).         | ADARUBRIC-DA |     |          |
theprimarydriver. ThegapbetweenGPT-4Direct achieves α > 0.82 on all benchmarks, meeting
(r=0.64)andADARUBRIC-WM(r=0.74)shows the deployment criterion of α ≥ 0.80. G-Eval
thattask-specificrubricgeneration—notbackbone
(α=0.63)andPrometheus(α=0.70)fallbelowthis
model strength—is the key factor. 2) Dimension- threshold,indicatingunreliablerewardsignals.
AwareFilteraddsmeaningfulimprovement(+0.05
4.5 GeneralisationtoSWE-bench
| r). 3) Surface |     | metrics | are inadequate |     | for agents |     |     |     |     |     |     |     |
| -------------- | --- | ------- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
(ROUGE-L r=0.31, BERTScore r=0.43). The SWE-bench Lite (Jimenez et al., 2023) requires
+0.15 gain over GPT-4 Direct demonstrates that resolving real GitHub issues with executable
adaptive rubric generation is the primary driver. patches—aqualitativelydifferenttaskfromwebau-
Thisconfirmsthatelicitingtask-specificevaluation tomationorAPIchaining. Weapply ADARUBRIC
knowledgefromLLMsthroughstructuredrubric toevaluate300sampledtrajectoriesfromthreerep-
generationismoreeffectivethandirectprompting. resentativeopen-weightagentsystems,usinga5-

Table4: SWE-benchLiteevaluation. Pearsonrwith Table6: Backbonegeneralisation(WebArena). Adap-
pass/fail oracle and resolve rate (%) after DPO fine- tiverubricsoutperformGPT-4Directevenwithsmaller
| tuningofLlama-3.1-8B-Instruct. |     |     | ADARUBRICgener- |     | models. |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
alisestocode-repairtaskswithzerorubricengineering.
|     |                |      |      |       |     | Backbone        |     | r    | α    | SR%  |     |
| --- | -------------- | ---- | ---- | ----- | --- | --------------- | --- | ---- | ---- | ---- | --- |
|     | Method         | r    | α    | Res.% |     |                 |     |      |      |      |     |
|     |                |      |      |       |     | GPT-4Direct     |     | 0.64 | 0.69 | —    |     |
|     | G-Eval(GPT-4o) | 0.51 | 0.63 | 8.2   |     | Prometheus(13B) |     | 0.61 | 0.71 | 21.0 |     |
|     | Prometheus     | 0.56 | 0.70 | 9.1   |     |                 |     |      |      |      |     |
|     |                |      |      |       |     | AR/GPT-4o       |     | 0.79 | 0.85 | 27.8 |     |
|     | GPT-4Direct    | 0.59 | 0.68 | 9.8   |     |                 |     |      |      |      |     |
|     |                |      |      |       |     | AR/Llama-70B    |     | 0.75 | 0.82 | 25.9 |     |
|     |                |      |      |       |     | AR/Llama-8B     |     | 0.68 | 0.77 | 23.2 |     |
|     | ADARUBRIC-WM   | 0.72 | 0.82 | 12.4  |     |                 |     |      |      |      |     |
|     | ADARUBRIC-DA   | 0.77 | 0.84 | 14.7  |     |                 |     |      |      |      |     |
Table5: AblationonWebArena. GPT-4oevaluator. aholisticGPT-4Direct-likeevaluation(r=0.61);
N>6
|     |                       |     |      |      |                                                | shows diminishing |       | returns,   |     | consistent | with |
| --- | --------------------- | --- | ---- | ---- | ---------------------------------------------- | ----------------- | ----- | ---------- | --- | ---------- | ---- |
|     | Variant               |     | r    | SR%  | evaluatorinstruction-followingsaturationathigh |                   |       |            |     |            |      |
|     |                       |     |      |      | dimension                                      | counts,           | where | dimensions |     | become     | in-  |
|     | Fixed(generic)        |     | 0.51 | 19.1 |                                                |                   |       |            |     |            |      |
|     | Fixed(domaintemplate) |     | 0.65 | 22.4 | creasinglyoverlapping.                         |                   |       |            |     |            |      |
|     | Adaptive,noconf.wt.   |     | 0.72 | 24.0 |                                                |                   |       |            |     |            |      |
|     | Adaptive,noDAFilter   |     | 0.75 | 25.2 |                                                |                   |       |            |     |            |      |
5.3 BackboneGeneralisation
|     | ADARUBRIC-DA(full) |     | 0.79 | 27.8 |     |     |     |     |     |     |     |
| --- | ------------------ | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
Table6evaluatesADARUBRICwheninstantiated
dimensionalrubricgeneratedfromtheSWE-bench withopen-weightmodels,assessingindependence
|     |     |     | Issue | Understand- |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
task description (dimensions: fromGPT-4o. The+0.11gap(Pearsonr)between
ing,RepositoryNavigation,CodeCorrectness,Test GPT-4oandLlama-3.1-8Bvariantsissmallerthan
Coverage,PatchMinimality). the +0.15 gap between GPT-4 Direct and any
ADARUBRIC-DA achieves r=0.77 against the ADARUBRIC variant (i.e., switching from static
binaryoracleonSWE-bench—only0.02belowits
|     |     |     |     |     | to adaptive | rubric | adds | +0.15, | while | switching |     |
| --- | --- | --- | --- | --- | ----------- | ------ | ---- | ------ | ----- | --------- | --- |
WebArena performance—showing that the adap- from GPT-4o to Llama-3.1-8B backbone costs
tive rubric approach generalises to unseen task only −0.11), confirming adaptive rubric genera-
types with no additional engineering. The DPO tioncontributesmorethanbackbonemodel’scapa-
resolverateof14.7%representsa+4.9%improve- bility. Thisfindingisparticularlyrelevantforthe
mentoverGPT-4Direct—asignificantadvanceon KnowFMcommunity: itsuggeststhatstructured
thischallengingbenchmark(Table4). knowledgeelicitation(viarubricprompts)unlocks
evaluationcapabilitieseveninsmallermodels.
5 Analysis
5.4 Cross-DomainTransfer
5.1 AblationStudy
Table5ablateskeydesignchoicesonWebArena. ApracticalquestioniswhetherADARUBRICpref-
Each component contributes positively. Switch- erencepairsgeneratedononebenchmarkcanim-
ingfromgenericfixeddimensionstodomaintem- proveperformanceonadifferent benchmark. Ta-
ble7evaluatesthiscross-domainscenario.
| plates | adds +0.14 r; | further | replacing | templates |     |     |     |     |     |     |     |
| ------ | ------------- | ------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
withadaptivegenerationadds+0.07,confirming ADARUBRIC cross-domainperformance(31.2
that task-specific rubric design is the core contri- TB, 24.6 WA) substantially exceeds Prometheus
bution. Confidence weighting adds +0.03; Di- in-domain performance (21.4, 21.0), demonstrat-
mensionAwareFilteradds+0.04. Overall,thefull ing that adaptive rubric scoring teaches gener-
pipeline achieves a cumulative +0.28 r improve- alisable quality preferences that transfer across
mentoverthegenericfixedbaseline,showingthat task families. The combined training setting
allcomponentscontributemeaningfully. (WA+TB→AB:32.7%)approachesin-domainper-
|     |     |     |     |     | formance | (34.1%), | confirming |     | that | multi-source |     |
| --- | --- | --- | --- | --- | -------- | -------- | ---------- | --- | ---- | ------------ | --- |
5.2 NumberofDimensionsN
adaptiverubricsignalsarecomplementaryrather
WeevaluateADARUBRICperformanceasafunc- than conflicting. This is a direct consequence of
tionofthenumberofdimensionsN onWebArena the rubric generation from task descriptions: the
andToolBench. Optimalperformanceisachieved evaluatorlearnstoassessgoal-directedreasoning
at N=5, confirming the default. N=1 recovers qualityregardlessofdomain.

Table 7: Cross-domain transfer. “Train→Test” de- Table 8: PPO training with ADARUBRIC reward.
noteswhichbenchmark’sDPOpairsareusedforfine- WebArena SR% after 1K, 3K, and 5K rollout steps.
tuningandwhichistheevaluationtarget. ADARUBRIC Denseper-dimensionrewardssubstantiallyaccelerate
| cross-domainexceedsPrometheusin-domain. |                                  |     |        |      | convergence. |              |     |         |       |        |      |        |
| --------------------------------------- | -------------------------------- | --- | ------ | ---- | ------------ | ------------ | --- | ------- | ----- | ------ | ---- | ------ |
|                                         | TrainSource                      |     | WA TB  | AB   |              | Reward       |     |         | 1K    | 3K     | 5K   |        |
|                                         | Prometheusbaseline(staticrubric) |     |        |      |              | GPT-4Scalar  |     |         | 14.2  | 18.7   | 21.3 |        |
|                                         | WA→WA(in-dom.)                   |     | 21.0 — | —    |              | Prometheus   |     |         | 15.8  | 21.2   | 23.6 |        |
|                                         | WA→TB(cross)                     |     | — 21.4 | —    |              |              |     |         |       |        |      |        |
|                                         | TB→WA(cross)                     |     |        |      |              | ADARUBRIC-WM |     |         | 18.3  | 24.9   | 27.1 |        |
|                                         |                                  |     | 18.3 — | —    |              |              |     |         |       |        |      |        |
|                                         |                                  |     |        |      |              | ADARUBRIC-DA |     |         | 20.1  | 27.4   | 30.2 |        |
|                                         | TB→TB(in-dom.)                   |     | — 29.3 | —    |              |              |     |         |       |        |      |        |
|                                         | AB→AB(in-dom.)                   |     | — —    | 26.4 |              |              |     |         |       |        |      |        |
|                                         |                                  |     |        |      | Table        | 9: Rubric    |     | quality | human | study. |      | Scores |
ADARUBRIC-DA(adaptiverubric) are mean Likert (1–5). Inter-annotator agreement
WA→WA(in-dom.) 27.8 — — κ=0.79. ADARUBRIC-generated rubrics approach
|     | WA→TB(cross) |     | — 31.2 | —   |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
expert-designedquality.
|                               | TB→WA(cross)               |     | 24.6 —          | —    |                            |     |     |     |      |       |       |     |
| ----------------------------- | -------------------------- | --- | --------------- | ---- | -------------------------- | --- | --- | --- | ---- | ----- | ----- | --- |
|                               | TB→TB(in-dom.)             |     | — 37.8          | —    |                            |     |     |     |      |       |       |     |
|                               | AB→AB(in-dom.)             |     | — —             | 34.1 | RubricSource               |     |     |     | Rel. | Orth. | Comp. |     |
|                               | WA+TB→AB(comb.)            |     | — —             | 32.7 |                            |     |     |     |      |       |       |     |
|                               |                            |     |                 |      | Generic(Help./Safety/Flu.) |     |     |     | 2.1  | 3.8   |       | 1.6 |
|                               |                            |     |                 |      | Domaintemplate(manual)     |     |     |     | 3.9  | 3.6   |       | 3.7 |
| 5.5                           | ExtensiontoMultimodalTasks |     |                 |      | Expert-designed            |     |     |     | 4.6  | 4.4   |       | 4.5 |
|                               |                            |     |                 |      | ADARUBRIC-generated        |     |     |     | 4.3  | 4.2   |       | 4.1 |
| ADARUBRICismodality-agnostic: |                            |     | itsrubricgener- |      |                            |     |     |     |      |       |       |     |
atorautomaticallyincludesvisual-specificdimen-
sions (Visual Grounding, Screenshot Interpreta- Orthogonality,andCompleteness(doesthefullset
tion)whenthetaskdescriptioninvolvesvisualob- of dimensions cover the task’s success criteria?).
|             |     |                                 |     |     | We  | compare | against | expert-designed |     |     | rubrics | and |
| ----------- | --- | ------------------------------- | --- | --- | --- | ------- | ------- | --------------- | --- | --- | ------- | --- |
| servations. |     | OnVisualWebArena(Kohetal.,2024) |     |     |     |         |         |                 |     |     |         |     |
genericfixedrubrics(Table9).
| and | OSWorld | (Xie | et al., 2024), ADARUBRIC- |     |     |     |     |     |     |     |     |     |
| --- | ------- | ---- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DAachievesr=0.76/0.73,outperformingGPT-4V ADARUBRIC-generatedrubricsscore4.3/4.2/4.1
Direct by +0.14/+0.14, and DPO training yields on relevance, orthogonality, and completeness,
within0.2–0.4ofexpert-designedrubricsoneach
+5.8%SRgain—allwithoutmultimodal-specific
engineering(Table12inAppendixD). dimension,asmallgapforfullyautomatedgenera-
tion. Genericfixedrubricsscorecriticallylowon
5.6 PPOIntegration completeness(1.6),confirmingthatstandardchat-
|        |      |           |        |               | assistant | dimensions |     | leave | large | portions |     | of the |
| ------ | ---- | --------- | ------ | ------------- | --------- | ---------- | --- | ----- | ----- | -------- | --- | ------ |
| Beyond | DPO, | ADARUBRIC | scores | can serve di- |           |            |     |       |       |          |     |        |
rectlyasarewardfunctionforPPO-styleonlineRL agenttaskqualityunmeasured. Themaingapfrom
(Schulman et al., 2017). We train a Qwen2.5-7B expert-designedrubricsisonedge-casecoverage:
|     |     |     |     |     | experts | include | dimensions |     | like | CAPTCHA |     | Han- |
| --- | --- | --- | --- | --- | ------- | ------- | ---------- | --- | ---- | ------- | --- | ---- |
policywithADARUBRIC-DAastherewardmodel
for1,000rolloutsonWebArenatrainingtasksand dlingorRate-LimitAwarenessthat ADARUBRIC
compareto(i)aGPT-4scalarrewardbaselineand occasionallymissesforspecialisedtasks.
| (ii) | a Prometheus-based |     | reward. Table | 8 reports |     |     |     |     |     |     |     |     |
| ---- | ------------------ | --- | ------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
5.8 FilterStrategyComparison
resultsat1K,3K,and5Krolloutsteps.
ADARUBRIC-DA achieves 30.2% SR at 5K Table 10 compares four filter strategies on We-
steps, +6.6% above Prometheus. Crucially, the bArena. DimensionAwareFilterachievesthebest
|     |     |     |     |     |     |     | (27.8) |     |     |     | 61.5% |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ----- | --- |
1K-step gap (+4.3%) shows faster convergence: DPO SR% while retaining only of
dense,per-dimensionrewardsprovidericherlearn- pairs. CompositeFilter (all strategies combined)
ingsignalthanscalarfeedback,reducingthesam- removestoomanyborderline-goodtrajectoriesand
plecomplexityofRLtraining. under-performs (26.9), confirming that selective
filteringbydimension-levelqualityissuperiorto
| 5.7 | RubricQuality: |     | HumanStudy |     |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
aggressivemulti-filterstacking.
| We  | assess | the quality | of ADARUBRIC-generated |     |     |     |     |     |     |     |     |     |
| --- | ------ | ----------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5.9 RecencyDecayλ
rubricsthroughahumanstudywithfivedomainex-
pertsacross60tasks(20WebArena,20ToolBench, Table 11 reports sensitivity to recency-decay λ.
20 AgentBench). Each expert rates every dimen- λ=0.5 is consistently optimal across both bench-
siononthreecriteria(1–5Likert): Task-Relevance, marks: up-weightinglaterstepscapturesgoalcom-

| Table | 10: | Filter | strategy | comparison | (WebArena). |     |             |      |          |          |     |               |     |
| ----- | --- | ------ | -------- | ---------- | ----------- | --- | ----------- | ---- | -------- | -------- | --- | ------------- | --- |
|       |     |        |          |            |             |     | elicitation | is a | powerful | paradigm |     | for improving |     |
DimensionAwareFilter achieves the best trade-off be- LLM reliability. The two-step process (generate
tweenqualityandpairretention.
|     |     |     |     |     |     |     | rubric → | evaluate | against | it) | decomposes |     | a com- |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------- | --- | ---------- | --- | ------ |
plexjudgmentintomanageablesub-tasks,reducing
Filter r SR% Retained thecognitiveloadontheevaluatorandproducing
|     | None              |     |     | 0.71 | 21.7 | 100%  | morecalibratedassessments. |     |           |     |           |     |        |
| --- | ----------------- | --- | --- | ---- | ---- | ----- | -------------------------- | --- | --------- | --- | --------- | --- | ------ |
|     | AbsoluteThreshold |     |     | 0.74 | 24.0 | 72.3% |                            |     |           |     |           |     |        |
|     |                   |     |     |      |      |       | (2) Evaluation             |     | knowledge |     | transfers |     | across |
|     | PercentileFilter  |     |     | 0.73 | 23.4 | 80.0% |                            |     |           |     |           |     |        |
DimensionAwareFilter 0.79 27.8 61.5% domains. Cross-domain DPO results (Table 7)
CompositeFilter 0.78 26.9 47.2% showthattask-adaptiverubricscapturegeneralis-
ablequalitysignals,notdomain-specificheuristics.
| Table | 11:      | Effect | of recency | decay   | λ (WebArena). |            |                                         |     |     |     |     |     |     |
| ----- | -------- | ------ | ---------- | ------- | ------------- | ---------- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
| λ=0.5 |          |        |            |         |               |            | ADARUBRICtrainedonWebArenapairsachieves |     |     |     |     |     |     |
|       | provides |        | optimal    | balance | between       | recent and |                                         |     |     |     |     |     |     |
31.2%onToolBench—exceedingPrometheusin-
earlysteps.
domain(29.3%)—suggestingthatthequalitycon-
|     |     | λ   |     | r   | SR% |     | ceptslearnedthroughrubric-guidedevaluationare |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
transferable.
|     |     | 0(uniform) |     | 0.71 | 23.5 |     |             |     |        |         |                |     |     |
| --- | --- | ---------- | --- | ---- | ---- | --- | ----------- | --- | ------ | ------- | -------------- | --- | --- |
|     |     |            |     |      |      |     | (3) Smaller |     | models | benefit | disproportion- |     |     |
|     |     | 0.25       |     | 0.75 | 25.4 |     |             |     |        |         |                |     |     |
0.5(default) 0.79 27.8 ately. Rubric-guided evaluation with Llama-8B
|     |     | 1.0 |     | 0.77 | 26.9 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
(r=0.68)outperformsunstructuredGPT-4evalua-
|     |     | 2.0 |     | 0.72 | 24.8 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
(r=0.64),
|     |     |     |     |     |     |     | tion             |     | suggesting | that      | structured |     | knowl- |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | --------- | ---------- | --- | ------ |
|     |     |     |     |     |     |     | edge scaffolding |     | can        | partially | compensate |     | for    |
pletioninformationwithoutdiscardingearlyplan-
|                    |     |     |                           |     |     |     | modelscale. | Thishaspracticalimplicationsforthe |            |          |     |               |     |
| ------------------ | --- | --- | ------------------------- | --- | --- | --- | ----------- | ---------------------------------- | ---------- | -------- | --- | ------------- | --- |
| ningstepsentirely. |     |     | Extremelyhighλ(=2.0)over- |     |     |     |             |                                    |            |          |     |               |     |
|                    |     |     |                           |     |     |     | deployment  | of                                 | evaluation | systems: |     | organisations |     |
concentratesontheterminalstep,losinginforma-
withlimitedcomputebudgetscanuseADARUBRIC
tionfromthereasoningchain(r=0.72vs.0.79).
|     |     |     |     |     |     |     | with smaller | open-weight |     | models |     | while | still ex- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --- | ------ | --- | ----- | --------- |
ceedingthequalityofdirectevaluationbyfrontier
5.10 CalibrationandErrorAnalysis
models.
| ADARUBRIC |     |     | score buckets |     | correlate | strongly |     |     |     |     |     |     |     |
| --------- | --- | --- | ------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
with human percentile ranks (Spearman ρ=0.98, RelationtoTülu,DRTulu,andpreferencedata
|           |     |            |     |          |           |          | quality. | Tülu | (Wang | et al., | 2023; | Ivison | et al., |
| --------- | --- | ---------- | --- | -------- | --------- | -------- | -------- | ---- | ----- | ------- | ----- | ------ | ------- |
| p<0.001), |     | confirming |     | that the | 1–5 scale | is mean- |          |      |       |         |       |        |         |
ingfully calibrated. Manual inspection of 50 2023) demonstrates that preference data quality
disagreement cases reveals three failure modes: criticallydeterminesRLHFeffectiveness. DRTulu
long-horizonbinarygoals(32%),implicitdomain (Shaoetal.,2025)extendsthislinebyco-evolving
conventions (28%), and ambiguous observations instance-specific,search-groundedrubricswiththe
(24%)—alladdressableviarichertaskdescriptions policy during RL training for long-form deep re-
(detailsinAppendixC). search. ADARUBRIC occupies a complementary
|     |             |     |                |     |     |     | niche:     | it generates |     | task-type-level |           | rubrics   | from |
| --- | ----------- | --- | -------------- | --- | --- | --- | ---------- | ------------ | --- | --------------- | --------- | --------- | ---- |
| 6   | Discussion: |     | KnowledgeinLLM |     |     |     |            |              |     |                 |           |           |      |
|     |             |     |                |     |     |     | parametric | knowledge    |     | before          | training, | providing |      |
Evaluation
high-qualitypreferencesignalsforagenttrajectory
|      |          |     |           |               |         |           | evaluation | without | requiring  |            | retrieval    | infrastruc- |       |
| ---- | -------- | --- | --------- | ------------- | ------- | --------- | ---------- | ------- | ---------- | ---------- | ------------ | ----------- | ----- |
| Our  | proposed |     | ADARUBRIC |               | reveals | an impor- |            |         |            |            |              |             |       |
|      |          |     |           |               |         |           | ture or    | online  | rubric     | evolution. | The          | DPO         | gains |
| tant | aspect   | of  | knowledge | in foundation |         | models:   |            |         |            |            |              |             |       |
|      |          |     |           |               |         |           | observed   | across  | benchmarks |            | (+6.8–+8.5%) |             | are   |
LLMspossessrich,implicitevaluationknowledge—
consistentwithTülu’sfindingthatbetterpreference
| understanding |     |     | of what | constitutes | success | across |     |     |     |     |     |     |     |
| ------------- | --- | --- | ------- | ----------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
datatranslatesdirectlytoimprovedmodelperfor-
| diverse | task | domains—that |     | can | be externalised |     |     |     |     |     |     |     |     |
| ------- | ---- | ------------ | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
mance. AnaturalextensionistoinitialiseDRTulu-
throughstructuredpromptingintoexplicit,reusable
|     |     |     |     |     |     |     | style evolving |     | rubrics | with | ADARUBRIC’s |     | task- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | ---- | ----------- | --- | ----- |
evaluationrubrics.
adaptiverubrics,combiningparametricknowledge
|     | Three | findings | are | particularly | relevant | to the |     |     |     |     |     |     |     |
| --- | ----- | -------- | --- | ------------ | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
scaffoldingwithonlinesearchgrounding.
KnowFMcommunity:
|     | (1) Knowledge |     | externalisation |     | outperforms |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | --------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
7 Conclusion
| directapplication. |     |     | AskinganLLMtofirstgener- |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ateanexplicitrubric,thenevaluateagainstit,sub- WepresentedADARUBRIC,aframeworkthatadap-
stantially outperforms direct evaluation (r=0.79 tivelygeneratestask-specificevaluationrubricsfor
vs.0.64). Thissuggeststhatstructuredknowledge LLM agent trajectories by leveraging the LLM’s

parametricknowledgeoftaskstructuresandevalu- Future directions. ADARUBRIC complements
ationcriteria. Onfivebenchmarks, ADARUBRIC trajectory augmentation approaches like Agen-
achieves Pearson r=0.79 (+0.15 over the best tHER (Ding, 2026): ADARUBRIC evaluations
baseline)withstrongreliability(α=0.83),andpro- canvalidaterelabelledtrajectories,improvingdata
ducesDPOpreferencepairsthatimproveagenttask quality. Extensiontomultimodaltrajectoriesand
successbyupto+8.5%. Critically, ADARUBRIC tighteronlineRLintegrationarenaturalnextsteps.
generalisestounseentasktypes(SWE-benchcode
repair: r=0.77,+4.9%DPOgain)andaccelerates
References
| PPO-based | online | RL  | training | by +6.6% at 5K |     |     |     |     |     |     |     |
| --------- | ------ | --- | -------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
steps. Cross-domaintransfer,zero-shotgeneralisa- PaulFChristiano,JanLeike,TomBrown,MiljanMar-
|     |     |     |     |     | tic, Shane | Legg, | and | Dario | Amodei. | 2017. | Deep |
| --- | --- | --- | --- | --- | ---------- | ----- | --- | ----- | ------- | ----- | ---- |
tion,andmodality-agnosticextensiondemonstrate
|             |        |           |       |            | reinforcementlearningfromhumanpreferences. |     |     |     |     |     | Ad- |
| ----------- | ------ | --------- | ----- | ---------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
| the breadth | of the | approach. | Human | evaluation |                                            |     |     |     |     |     |     |
vancesinneuralinformationprocessingsystems,30.
| of generated | rubrics | shows | quality | approaching |     |     |     |     |     |     |     |
| ------------ | ------- | ----- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
expert-designedrubrics(relevance: 4.3/5),validat- Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
MarkChen,HeewooJun,LukaszKaiser,Matthias
| ingthegenerationmechanism. |            |           | Fortheknowledge- |              |           |       |           |       |          |     |           |
| -------------------------- | ---------- | --------- | ---------------- | ------------ | --------- | ----- | --------- | ----- | -------- | --- | --------- |
|                            |            |           |                  |              | Plappert, | Jerry | Tworek,   | Jacob | Hilton,  |     | Reiichiro |
| in-LMs                     | community, | ADARUBRIC |                  | demonstrates |           |       |           |       |          |     |           |
|                            |            |           |                  |              | Nakano,   | and   | 1 others. | 2021. | Training |     | verifiers |
thatstructuredelicitationofevaluationknowledge— to solve math word problems. arXiv preprint
arXiv:2110.14168.
aformofknowledgeexternalisation—isapromis-
ingdirectionforbuildingmorereliableandadap-
|     |     |     |     |     | Liang Ding. | 2026. | Agenther: |     | Hindsight | experience |     |
| --- | --- | --- | --- | --- | ----------- | ----- | --------- | --- | --------- | ---------- | --- |
tiveAIsystems.
|     |     |     |     |     | replay | for llm | agent | trajectory | relabeling. |     | arXiv |
| --- | --- | --- | --- | --- | ------ | ------- | ----- | ---------- | ----------- | --- | ----- |
preprintarXiv:2603.21357.
|                                                 |                              |     |     |     | JosephLFleiss.1971. |       | Measuringnominalscaleagree- |     |               |     |           |
| ----------------------------------------------- | ---------------------------- | --- | --- | --- | ------------------- | ----- | --------------------------- | --- | ------------- | --- | --------- |
| Limitations.                                    | RubricqualitydependsonLLMca- |     |     |     |                     |       |                             |     |               |     |           |
|                                                 |                              |     |     |     | ment                | among | many raters.                |     | Psychological |     | bulletin, |
| pability;taskswithvagueorunderspecifieddescrip- |                              |     |     |     | 76(5):378.          |       |                             |     |               |     |           |
tionsmayyieldincompleteoroverlappingdimen-
AaronGrattafiori,AbhimanyuDubey,AbhinavJauhri,
| sions, and | rubric | generation | can | miss specialised |         |         |          |     |         |       |     |
| ---------- | ------ | ---------- | --- | ---------------- | ------- | ------- | -------- | --- | ------- | ----- | --- |
|            |        |            |     |                  | Abhinav | Pandey, | Abhishek |     | Kadian, | Ahmad | Al- |
criteria (e.g., CAPTCHA Handling, Rate-Limit Dahle,AieshaLetman,AkhilMathur,AlanSchelten,
Awareness)whenparametricknowledgeofthedo- AlexVaughan,and1others.2024. Thellama3herd
|             |                                |     |     |     | ofmodels. | arXivpreprintarXiv:2407.21783. |     |     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --------- | ------------------------------ | --- | --- | --- | --- | --- |
| mainisthin. | Becauserubricsaregeneratedfrom |     |     |     |           |                                |     |     |     |     |     |
thetaskdescription,adversariallycrafteddescrip-
|     |     |     |     |     | Edward | J Hu, | Yelong | Shen, | Phillip | Wallis, | Zeyuan |
| --- | --- | --- | --- | --- | ------ | ----- | ------ | ----- | ------- | ------- | ------ |
tionscouldinprinciplebiasevaluation;inourpilot Allen-Zhu, Yuanzhi Li, Shean Wang, Liang Wang,
|     |     |     |     |     | WeizhuChen,and1others.2022. |     |     |     |     | Lora: Low-rank |     |
| --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | -------------- | --- |
with30perturbeddescriptions,rdegradesby0.04–
|     |     |     |     |     | adaptationoflargelanguagemodels. |     |     |     |     | Iclr,1(2):3. |     |
| --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | ------------ | --- |
0.06,indicatingnon-trivialbutboundedsensitivity
that motivates future work on description-robust Hamish Ivison, Yizhong Wang, Valentina Pyatkin,
|                    |     |            |     |                 | Nathan | Lambert, | Matthew |     | Peters, | Pradeep | Dasigi, |
| ------------------ | --- | ---------- | --- | --------------- | ------ | -------- | ------- | --- | ------- | ------- | ------- |
| rubric generation. |     | Confidence |     | scores are LLM- |        |          |         |     |         |         |         |
JoelJang,DavidWadden,NoahASmith,IzBeltagy,
| predicted                            | and may | require | post-hoc | recalibration     |                                 |     |                           |     |     |               |     |
| ------------------------------------ | ------- | ------- | -------- | ----------------- | ------------------------------- | --- | ------------------------- | --- | --- | ------------- | --- |
|                                      |         |         |          |                   | and1others.2023.                |     | Camelsinachangingclimate: |     |     |               |     |
| forstronglyout-of-distributiontasks. |         |         |          | Computation-      |                                 |     |                           |     |     |               |     |
|                                      |         |         |          |                   | Enhancinglmadaptationwithtulu2. |     |                           |     |     | arXivpreprint |     |
| ally, ADARUBRICcostsK×N              |         |         |          | evaluatorcallsper | arXiv:2311.10702.               |     |                           |     |     |               |     |
trajectory(≈40forWebArena)with3–5×thewall-
|          |       |         |        |                   | Carlos E | Jimenez, | John  | Yang,     | Alexander |     | Wettig, |
| -------- | ----- | ------- | ------ | ----------------- | -------- | -------- | ----- | --------- | --------- | --- | ------- |
| clock of | GPT-4 | Direct; | rubric | caching amortises |          |          |       |           |           |     |         |
|          |       |         |        |                   | Shunyu   | Yao,     | Kexin | Pei, Ofir | Press,    | and | Karthik |
thegenerationcostacrossataskfamilybutnotthe Narasimhan.2023. Swe-bench: Canlanguagemod-
|                                            |     |     |                          |     | elsresolvereal-worldgithubissues? |     |     |     |     | arXivpreprint |     |
| ------------------------------------------ | --- | --- | ------------------------ | --- | --------------------------------- | --- | --- | --- | --- | ------------- | --- |
| per-stepevaluationcost.                    |     |     | Finally,thehumancorrela- |     |                                   |     |     |     |     |               |     |
| tionstudyuses300pairsperbenchmarkwiththree |     |     |                          |     | arXiv:2310.06770.                 |     |     |     |     |               |     |
annotators,andthemultimodal/PPO/SWE-bench
|     |     |     |     |     | Seungone | Kim, | Jamin | Shin, | Yejin | Cho, Joel | Jang, |
| --- | --- | --- | --- | --- | -------- | ---- | ----- | ----- | ----- | --------- | ----- |
sections are kept deliberately compact—we treat Shayne Longpre, Hwaran Lee, Sangdoo Yun,
SeongjinShin,SungdongKim,JamesThorne,and
themasgeneralisationevidenceratherthanastheir
|                    |     |                            |     |     | 1others.2023. |            | Prometheus: |             | Inducingfine-grained |         |        |
| ------------------ | --- | -------------------------- | --- | --- | ------------- | ---------- | ----------- | ----------- | -------------------- | ------- | ------ |
| ownprimarystudies. |     | Single-passevaluationcould |     |     |               |            |             |             |                      |         |        |
|                    |     |                            |     |     | evaluation    | capability |             | in language |                      | models. | In The |
beimprovedbymulti-roundverification,thoughat TwelfthInternationalConferenceonLearningRepre-
| highercomputationalcost. |     |     | Allrubric,evaluation, |     | sentations. |     |     |     |     |     |     |
| ------------------------ | --- | --- | --------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
andfilterprompttemplatesusedinthispaperare
|     |     |     |     |     | Jing Yu | Koh, | Robert | Lo, Lawrence |     | Jang, | Vikram |
| --- | --- | --- | --- | --- | ------- | ---- | ------ | ------------ | --- | ----- | ------ |
releasedinthesupplementarymaterialtosupport
|              |     |     |     |     | Duvvur,                                    | Ming | Lim, | Po-Yu | Huang, | Graham | Neu- |
| ------------ | --- | --- | --- | --- | ------------------------------------------ | ---- | ---- | ----- | ------ | ------ | ---- |
| replication. |     |     |     |     | big,ShuyanZhou,RussSalakhutdinov,andDaniel |      |      |       |        |        |      |

Fried.2024. Visualwebarena:Evaluatingmultimodal YujiaQin,ShihaoLiang,YiningYe,KunlunZhu,Lan
agentsonrealisticvisualwebtasks. InProceedings Yan,YaxiLu,YankaiLin,XinCong,XiangruTang,
of the 62nd Annual Meeting of the Association for BillQian,and1others.2023. Toolllm: Facilitating
ComputationalLinguistics(Volume1: LongPapers), largelanguagemodelstomaster16000+real-world
| pages881–905.           |     |     |                         |     |     |     | apis. arXivpreprintarXiv:2307.16789. |     |     |     |     |     |
| ----------------------- | --- | --- | ----------------------- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
| KlausKrippendorff.2011. |     |     | Computingkrippendorff’s |     |     |     |                                      |     |     |     |     |     |
RafaelRafailov,ArchitSharma,EricMitchell,Christo-
alpha-reliability.
pherDManning,StefanoErmon,andChelseaFinn.
2023. Directpreferenceoptimization:Yourlanguage
| Nathan | Lambert, | Valentina | Pyatkin, |     | Jacob | Morrison, |     |     |     |     |     |     |
| ------ | -------- | --------- | -------- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- |
Advancesinneural
LesterJamesValidadMiranda,BillYuchenLin,Khy- modelissecretlyarewardmodel.
informationprocessingsystems,36:53728–53741.
athiChandu,NouhaDziri,SachinKumar,TomZick,
| YejinChoi,and1others.2025. |        |        |     | Rewardbench: |           | Eval- |                |     |               |         |          |           |
| -------------------------- | ------ | ------ | --- | ------------ | --------- | ----- | -------------- | --- | ------------- | ------- | -------- | --------- |
|                            |        |        |     |              |           |       | John Schulman, |     | Filip Wolski, |         | Prafulla | Dhariwal, |
| uating                     | reward | models | for | language     | modeling. | In    |                |     |               |         |          |           |
|                            |        |        |     |              |           |       | Alec Radford,  |     | and Oleg      | Klimov. | 2017.    | Proxi-    |
FindingsoftheAssociationforComputationalLin-
arXivpreprint
guistics: NAACL2025,pages1755–1797. malpolicyoptimizationalgorithms.
arXiv:1707.06347.
HunterLightman,VineetKosaraju,YuriBurda,Harri-
sonEdwards,BowenBaker,TeddyLee,JanLeike, RulinShao,AkariAsai,ShannonZejiangShen,Hamish
Ivison,VarshaKishore,JingmingZhuo,XinranZhao,
| John | Schulman, | Ilya | Sutskever, |     | and Karl | Cobbe. |     |     |     |     |     |     |
| ---- | --------- | ---- | ---------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- |
MollyPark,SamuelGFinlayson,DavidSontag,and
| 2023. | Let’sverifystepbystep. |     |     | InThetwelfthinter- |     |     |     |     |     |     |     |     |
| ----- | ---------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
nationalconferenceonlearningrepresentations. 1others.2025. Drtulu: Reinforcementlearningwith
|                   |     |            |        |                      |               |     | evolving          | rubrics | for deep | research. | arXiv | preprint |
| ----------------- | --- | ---------- | ------ | -------------------- | ------------- | --- | ----------------- | ------- | -------- | --------- | ----- | -------- |
| Chin-YewLin.2004. |     |            | Rouge: | Apackageforautomatic |               |     | arXiv:2511.19399. |         |          |           |       |          |
| evaluation        | of  | summaries. |        | In Text              | summarization |     |                   |         |          |           |       |          |
branchesout,pages74–81. Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel
|     |     |     |     |     |     |     | Ziegler, | Ryan | Lowe, Chelsea |     | Voss, Alec | Radford, |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------------- | --- | ---------- | -------- |
XiaoLiu,HaoYu,HanchenZhang,YifanXu,Xuanyu
|            |        |         |               |         |        |        | DarioAmodei,andPaulFChristiano.2020. |     |     |     |     | Learn-   |
| ---------- | ------ | ------- | ------------- | ------- | ------ | ------ | ------------------------------------ | --- | --- | --- | --- | -------- |
| Lei, Hanyu |        | Lai, Yu | Gu, Hangliang |         | Ding,  | Kaiwen |                                      |     |     |     |     |          |
|            |        |         |               |         |        |        | ingtosummarizewithhumanfeedback.     |     |     |     |     | Advances |
| Men,       | Kejuan | Yang,   | and 1         | others. | 2023a. | Agent- |                                      |     |     |     |     |          |
inneuralinformationprocessingsystems,33:3008–
| bench: | Evaluating |     | llms as | agents. | arXiv | preprint |     |     |     |     |     |     |
| ------ | ---------- | --- | ------- | ------- | ----- | -------- | --- | --- | --- | --- | --- | --- |
3021.
arXiv:2308.03688.
Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang, Yizhong Wang, Hamish Ivison, Pradeep Dasigi, Jack
RuochenXu, andChenguangZhu.2023b. G-eval: Hessel,TusharKhot,KhyathiChandu,DavidWad-
den,KelseyMacMillan,NoahASmith,IzBeltagy,
Nlgevaluationusinggpt-4withbetterhumanalign-
|       |                |     |     |          |            |     | and1others.2023. |     | Howfarcancamelsgo? |     |     | explor- |
| ----- | -------------- | --- | --- | -------- | ---------- | --- | ---------------- | --- | ------------------ | --- | --- | ------- |
| ment. | In Proceedings |     | of  | the 2023 | conference | on  |                  |     |                    |     |     |         |
empiricalmethodsinnaturallanguageprocessing, ingthestateofinstructiontuningonopenresources.
pages2511–2522. AdvancesinNeuralInformationProcessingSystems,
36:74764–74786.
| Qingyu | Lu, Liang | Ding, | Siyi | Cao, | Xuebo | Liu, Kan- |     |     |     |     |     |     |
| ------ | --------- | ----- | ---- | ---- | ----- | --------- | --- | --- | --- | --- | --- | --- |
jian Zhang, Jinxia Zhang, and Dacheng Tao. 2025. TianbaoXie,DanyangZhang,JixuanChen,Xiaochuan
| Runawayisashamed,buthelpful: |     |     |     |     | Ontheearly-exit |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
Li,SihengZhao,RuishengCao,TohJHua,Zhoujun
behavioroflargelanguagemodel-basedagentsinem- Cheng, Dongchan Shin, Fangyu Lei, and 1 others.
bodiedenvironments. InFindingsoftheAssociation 2024. Osworld: Benchmarkingmultimodalagents
forComputationalLinguistics: EMNLP2025,pages foropen-endedtasksinrealcomputerenvironments.
| 24014–24027. |     |     |     |     |     |     | AdvancesinNeuralInformationProcessingSystems, |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- |
37:52040–52094.
| Qingyu | Lu, Liang | Ding, | Liping  | Xie, | Kanjian | Zhang, |          |         |       |         |        |         |
| ------ | --------- | ----- | ------- | ---- | ------- | ------ | -------- | ------- | ----- | ------- | ------ | ------- |
| Derek  | F Wong,   | and   | Dacheng | Tao. | 2023.   | Toward |          |         |       |         |        |         |
|        |           |       |         |      |         |        | An Yang, | Baosong | Yang, | Beichen | Zhang, | Binyuan |
human-likeevaluationfornaturallanguagegenera-
|                        |     |     |                        |     |     |     | Hui, Bo | Zheng,   | Bowen  | Yu,    | Chengyuan | Li, Day-      |
| ---------------------- | --- | --- | ---------------------- | --- | --- | --- | ------- | -------- | ------ | ------ | --------- | ------------- |
| tionwitherroranalysis. |     |     | InProceedingsofthe61st |     |     |     |         |          |        |        |           |               |
|                        |     |     |                        |     |     |     | iheng   | Liu, Fei | Huang, | Haoran | Wei,      | and 1 others. |
AnnualMeetingoftheAssociationforComputational 2024. Qwen2.5 technical report. arXiv preprint
| Linguistics | (Volume |     | 1: Long | Papers), | pages | 5892– |     |     |     |     |     |     |
| ----------- | ------- | --- | ------- | -------- | ----- | ----- | --- | --- | --- | --- | --- | --- |
arXiv:2412.15115.
5907.
|     |     |     |     |     |     |     | Seonghyeon | Ye, | Doyoung | Kim, | Sungdong | Kim, |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | ---- | -------- | ---- |
LongOuyang,JeffreyWu,XuJiang,DiogoAlmeida,
|     |     |     |     |     |     |     | Hyeonbin | Hwang, | Seungone |     | Kim, | Yongrae Jo, |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | -------- | --- | ---- | ----------- |
CarrollWainwright,PamelaMishkin,ChongZhang,
|     |     |     |     |     |     |     | James | Thorne, | Juho Kim, | and | Minjoon | Seo. 2023. |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | --------- | --- | ------- | ---------- |
SandhiniAgarwal,KatarinaSlama,AlexRay,and1
others.2022. Traininglanguagemodelstofollowin- Flask: Fine-grained language model evaluation
structionswithhumanfeedback. Advancesinneural based on alignment skill sets. arXiv preprint
arXiv:2307.10928.
informationprocessingsystems,35:27730–27744.
JiayiPan,YichiZhang,NicholasTomlin,YifeiZhou, WeizheYuan,RichardYuanzhePang,KyunghyunCho,
SergeyLevine,andAlaneSuhr.2024. Autonomous Xian Li, Sainbayar Sukhbaatar, Jing Xu, and Ja-
evaluation and refinement of digital agents. arXiv sonWeston.2024. Self-rewardinglanguagemodels.
| preprintarXiv:2404.06474. |     |     |     |     |     |     | arXivpreprintarXiv:2401.10020. |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |

Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q Empirical validation of the noise model. On
Weinberger,andYoavArtzi.2019. Bertscore: Eval- 300WebArenatrajectorypairswith3independent
uating text generation with bert. arXiv preprint
evaluator runs, we compute residuals s −s¯
arXiv:1904.09675. k,j k,j
and find the distribution is approximately mean-
LianminZheng,Wei-LinChiang,YingSheng,Siyuan zero(bias≤ 0.07onthe1–5scale)butleptokurtic
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, (excess kurtosis ≈1.4) with a mild negative cor-
Zhuohan Li, Dacheng Li, Eric Xing, and 1 others.
relationbetween|s−s¯|andc(Spearman−0.31).
2023. Judging llm-as-a-judge with mt-bench and
Theinverse-confidencescalingdirectiontherefore
chatbotarena. Advancesinneuralinformationpro-
cessingsystems,36:46595–46623. holds in practice, while the Gaussian tails do
not; BLUE should be treated as a motivating ap-
Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou, proximation,andtheempiricalvariancereduction
RobertLo,AbishekSridhar,XianyiCheng,Tianyue
ofconfidence-weightingvs.uniformaveragingis
Ou, Yonatan Bisk, Daniel Fried, and 1 others.
18−24%acrossbenchmarks.
2023. Webarena: A realistic web environment
for building autonomous agents. arXiv preprint
arXiv:2307.13854. C CalibrationandErrorAnalysis
Lianghui Zhu, Xinggang Wang, and Xinlong Wang. ADARUBRIC score buckets correlate strongly
2023. Judgelm: Fine-tuned large language with human percentile ranks (Spearman ρ=0.98,
models are scalable judges. arXiv preprint
p<0.001),withrating-5trajectorieslandingatthe
arXiv:2310.17631.
91sthumanpercentileonaverage. Thenear-linear
DanielMZiegler,NisanStiennon,JeffreyWu,TomB relationshipconfirmsthatthe1–5scaleismeaning-
Brown, Alec Radford, Dario Amodei, Paul Chris- fullycalibrated.
tiano, and Geoffrey Irving. 2019. Fine-tuning lan-
Manual inspection of 50 disagreement cases
guage models from human preferences. arXiv
(|r −r |>1)onWebArenarevealsthreemain
preprintarXiv:1909.08593. ada human
failure modes: (1) long-horizon binary goals
A ImplementationDetails (32%)—ADARUBRICover-creditspartialcomple-
tion in multi-hop tasks where final outcome is
Hyperparameters. Default: N=5 dimensions, binary; (2) implicit domain conventions (28%)—
recency-decayλ=0.5,minimummarginδ min =0.5, ADARUBRICfailstopenaliseviolationsofwebsite-
DimAware threshold θ j =2.5, percentile filter specific norms (e.g., wrong date format); (3) am-
p=80. biguousobservations(24%)—HTMLartefactsor
APIerrorcodesconfuseper-stepscoring. Allare
Computationalcost. ADARUBRICrunsK×N
addressable via richer task descriptions or obser-
LLM calls per trajectory (plus one rubric gener-
vation pre-processing. In 16% of cases, the hu-
ation call per task type). For WebArena (K≈8,
manrater’sjudgmentwasarguablyincorrect,and
N=5): 40 calls vs. 1 for GPT-4 Direct. With
ADARUBRIC’sevaluationwasdefensible.
cachingandbatching,totallatencyis3–5×GPT-4
Direct. D AdditionalResults
B ProofofProposition3.1 PPO training details. We train a Qwen2.5-
7B policy with ADARUBRIC-DA as the reward
(cid:80)
(a) If all s¯ ≥ θ , then S(τ) = w s¯ ≥
j j j j j model for 1,000 rollouts on WebArena training
(cid:80) j w j θ j = θ¯ . (b) Set s¯ j∗ = ϵ and s¯ j = (θ¯− tasks. WebArena’s training split (N=80 tasks)
w j∗ ϵ)/(1−w j∗ )forj ̸= j∗,givingS(τ∗) = θ¯ . (c) is used for online RL; the held-out 732 tasks
Constructiongeneralisestoanyθ′. serve as the test set. Results at 1K/3K/5K roll-
outs: GPT-4 Scalar: 14.2/18.7/21.3; Prometheus:
BLUE of confidence-weighted aggregation.
15.8/21.2/23.6; ADARUBRIC-WM:18.3/24.9/27.1;
Underanoisemodels = s∗ +ε withε ∼
k,j k,j k,j k,j ADARUBRIC-DA:20.1/27.4/30.2.
N(0,σ2/c ),theconfidence-weightedestimator
k,j
µˆ = (cid:80) c k,j s isBLUEbyGauss-Markov, Multimodalresults. Table12reportsfullmulti-
w j ithVar k [µˆ (cid:80) ] k′ = c k′ σ ,j 2/ k (cid:80) ,j c ≤ σ2(cid:80) c−1/K2 = modalevaluationresults.
j k k,j k k,j
Var[s¯uniform] (Cauchy-Schwarz), with equality iff Rubricqualityhumanstudy. Fivedomainex-
j
allc areequal. pertsrate60rubrics(20perbenchmark)on1–5Lik-
k,j

Table12:Multimodalagentevaluation.Pearsonrand
DPOSR%onVisualWebArena(VWA)andOSWorld.
|              |                                      | VWA                  | OSWorld      |         |
| ------------ | ------------------------------------ | -------------------- | ------------ | ------- |
| Method       |                                      | r                    | SR% r        | SR%     |
| G-Eval       |                                      | 0.48                 | — 0.44       | —       |
| GPT-4VDirect |                                      | 0.62                 | — 0.59       | —       |
| ADARUBRIC-DA |                                      | 0.76                 | 26.3 0.73    | 22.8    |
| ertscales.   | Generic(Helpfulness/Safety/Fluency): |                      |              |         |
| 2.1/3.8/1.6. | Domaintemplate:                      |                      | 3.9/3.6/3.7. | Expert- |
| designed:    | 4.6/4.4/4.5.                         | ADARUBRIC-generated: |              |         |
| 4.3/4.2/4.1. | Inter-annotatoragreementκ=0.79.      |                      |              |         |