# Challenges and Research Directions for Large Language Model Inference Hardware

**Type:** preprint

**Item Key:** 4M8TA9RZ

**Date:** 2026-01-08

**Authors:** Ma, Xiaoyu; Patterson, David

**DOI:** 10.1109/MC.2026.3652916

**URL:** http://arxiv.org/abs/2601.05047

## Extra
arXiv:2601.05047 [cs]

## Abstract
Large Language Model (LLM) inference is hard. The autoregressive Decode phase of the underlying Transformer model makes LLM inference fundamentally different from training. Exacerbated by recent AI trends, the primary challenges are memory and interconnect rather than compute. To address these challenges, we highlight four architecture research opportunities: High Bandwidth Flash for 10X memory capacity with HBM-like bandwidth; Processing-Near-Memory and 3D memory-logic stacking for high memory bandwidth; and low-latency interconnect to speedup communication. While our focus is datacenter AI, we also review their applicability for mobile devices.

## Full Text

Challenges and Research Directions for Large Language Model Inference Hardware
Xiaoyu Ma and David Patterson, Google

Large Language Model (LLM) inference is hard. The autoregressive Decode phase of the underlying Transformer model makes LLM inference fundamentally different from training. Exacerbated by recent AI trends, the primary challenges are memory and interconnect rather than compute. To address these challenges, we highlight four architecture research opportunities: High Bandwidth Flash for 10X memory capacity with HBM-like bandwidth; Processing-Near-Memory and 3D memory-logic stacking for high memory bandwidth; and low-latency interconnect to speedup communication. While our focus is datacenter AI, we also review their applicability for mobile devices.

INTRODUCTION
When one author started his career in 1976, ~40% of the papers at computer architecture conferences were from industry. Their share fell below 4% at ISCA 2025, suggesting a near disconnect between research and practice. To help restore their historic bond, we propose research directions that, if pursued, address some of the biggest hardware challenges that the AI industry faces.

Large language model (LLM) inference is a crisis. Rapidly improving hardware enables AI advances. Projections of inference chip annual sales are 4X-6X over the next 5-8 years. While training demonstrates remarkable AI breakthroughs, the cost of inference determines economic viability. Companies find it costly to serve state-of-the-art models as usage of these models dramatically increases.

New trends make inference harder. Recent advances in LLMs require more resources for inference:
- Mixture of Experts (MoE). Rather than a single dense feedforward block, MoE uses tens to hundreds of experts—256 for DeepSeekv3— invoked selectively. This sparsity allows model size to grow significantly for higher quality, despite a modest increase in training cost. While helping training, MoE exacerbates inference by expanding memory and communication.
- Reasoning models. Reasoning is a think-before-act technique to improve quality. An extra “thinking” step generates a long sequence of “thoughts” before the final answer, similar to people solving a problem step-by-step. Thinking greatly increases generation latency, and the long sequence of thought tokens strains memory.
- Multimodal. LLMs have evolved from text to image, audio, and video generation. Larger data types demand more than text generation.
- Long context. A context window refers to the amount of information the LLM model can look at when generating an answer. Longer context helps quality, but increases compute and memory demands.
- Retrieval-Augmented Generation (RAG). RAG accesses a user-specific knowledge database to obtain relevant information as extra context to improve LLM results, increasing resource demands.
- Diffusion. In contrast to the autoregressive method that generates tokens sequentially, the novel diffusion method generates all tokens (e.g., an entire image) in one step and then iteratively denoises the image to reach desired quality. Unlike above, diffusion only increases compute demands.

The growing market and challenges of LLM inference suggest a great opportunity and need for innovation!

CURRENT LLM INFERENCE HARDWARE AND ITS INEFFICIENCIES
We first review LLM inference basics and its primary bottlenecks on mainstream AI architectures, focusing on LLMs in the datacenter. LLMs on mobile devices have different restrictions and thus different options (e.g., HBM is infeasible).

LLMs, whose heart is Transformer, have two inference phases with very different characteristics: Prefill and Decode. Prefill is similar to training by processing all tokens of the input sequence simultaneously, so it is inherently parallel and often compute bound. In contrast, Decode is inherently sequential, as each step generates one output token (“autoregressive”), making it memory bound. The Key Value (KV) Cache connects the two phases, with its size proportional to the input+output sequence length. Prefill and Decode are not tightly coupled, and often run on different servers. Disaggregated inference allows software optimizations like batching to make Decode be less memory bound. A survey for efficient LLM inference reviews many software optimizations.

GPUs and TPUs are popular datacenter accelerators for both training and inference. Historically, inference versions were scaled-down from training systems, such as with fewer chips or a smaller chip with less memory or performance. Thus far, no GPU/TPU was designed solely for LLM inference. Because Prefill is similar to training whereas Decode differs significantly, two challenges make GPUs/TPUs inefficient for Decode.

Decode Challenge #1: Memory
The autoregressive Decode makes inference inherently memory bound, with new software trends heightening this challenge. In contrast, the hardware trends go in a completely different direction.

AI processors face a Memory Wall. Current datacenter GPUs/TPUs rely on High Bandwidth Memory (HBM), and connect several HBM stacks to a single monolithic accelerator ASIC. Nevertheless, memory bandwidth improves more slowly than compute FLOPS. For example, NVIDIA GPU 64-bit FLOPS rose by 80X from 2012 to 2022, but bandwidth grew only 17X. This gap will continue expanding.

HBM is increasingly expensive. Looking at one HBM stack, the normalized price of capacity ($/GB) and bandwidth ($/GBps) increases over time. Both grew 1.35x higher from 2023-2025. This rise is because manufacturing and packaging difficulties increase with dies per HBM stack and DRAM density growth. In contrast, the equivalent costs for standard DDR4 DRAM decrease over time. From 2022-2025, capacity cost shrank to 0.54x and bandwidth cost to 0.45x. While prices of all memory and storage devices surged in 2026 due to unexpected demand, we believe long term that the diverging pricing trends of HBM and DRAM will hold.

DRAM density growth is decelerating. For an individual DRAM die, scaling is also worrisome. Fourfold growth from 8-gigabit DRAM dies that debuted in 2014 will take over 10 years. Fourfold gains occurred every 3-6 years previously.

SRAM-only solutions are insufficient. Cerebras and Groq tried using full reticle chips filled with SRAM to avoid DRAM and HBM challenges. (Cerebras even used wafer scale integration.) While plausible when the companies were founded a decade ago, LLMs soon overwhelmed on-chip SRAM capacity. Both had to later retrofit external DRAM.

Decode Challenge #2: End-to-End Latency
User-facing implies low latency. Unlike training that takes weeks, inference is tied to real-time requests, needing a response in seconds or less. Low latency is critical for user-facing inference. (Batch or offline inference does not have a low latency requirement.) Depending on the application, latency is measured as time-to-completion of all output tokens or time-to-first-token. Both have challenges:
- Time-to-completion challenge. Decode produces one token at a time, so the longer the output, the longer the latency. Long output sequences stretch latency, but long input sequences are also slower because accessing the KV Cache during Decode and Prefill takes more time. Each Decode iteration has high memory access latency because it is memory bound.
- Time-to-first-token challenge. Long input sequences and RAG increase the amount of work before generation and hence the time-to-first-token. Reasoning models also increase this latency as they generate many “thought” tokens before the first user-visible token.

Interconnect latency outweighs bandwidth. Before LLMs, in datacenter inference usually ran on one chip, while training needed a supercomputer. The supercomputer interconnect understandably aimed much more at bandwidth than latency. LLM inference changes the game:
- Because of big weights, LLM inference now needs a multi-chip system, with software sharding that implies frequent communication. MoE and long sequence models further increase the system size to accommodate larger memory capacity requirements.
- Unlike training, the size of network messages is often small, given the small batch size of Decode. Latency trumps bandwidth for frequent, small messages in a big network.

Only Diffusion needs increased compute—relatively easy to deliver—as it is fundamentally unlike Transformer Decode. Thus, we focus on promising directions for improving memory and interconnect latency but not compute. 

FOUR RESEARCH OPPORTUNITIES TO RE-THINK LLM INFERENCE HARDWARE
Performance/cost metrics measure the efficiency of AI systems. Modern metrics—which emphasize realistic performance normalized, Total Cost of Ownership (TCO), average power consumption, and carbon dioxide equivalent emissions (CO2e)—offer new targets for designing systems:
- Performance must be meaningful. For LLM Decode inference, high FLOPS on a giant die does not necessarily mean high performance. Instead, we need to scale memory bandwidth and capacity efficiently, and optimize interconnect speed.
- Performance must be delivered within datacenter capacity, often constrained by power, space, and CO2e budgets.
- Power and CO2e are first-order optimization targets. Power affects TCO and datacenter capacity. Power and energy cleanliness determine operational CO2e. Manufacturing yield and life cycle set embodied CO2e.

Next, we describe four promising research directions to address the Decode challenges. Although described independently, they are synergistic; an architecture can usefully combine many of them. All improve performance/TCO, performance/CO2e, and performance/power.

① High Bandwidth Flash for 10X capacity
High Bandwidth Flash (HBF) combines HBM bandwidth with flash capacity by stacking flash dies like HBM. HBF delivers 10X memory capacity per node to reduce system size to save power, TCO, CO2e, and network overhead. The weaknesses of alternatives are bandwidth for DDR5, capacity for HBM, and write limits and high read latency for HBF. Another HBF benefit is sustainable capacity scaling; flash capacity continues to double every three years while DRAM growth decelerates.

Two well-known flash memory restrictions must be addressed:
- Limited write endurance. Write/erase cycles can wearout flash. Therefore, HBF must hold infrequently-updated data, such as weights at inference time or slow-changing context.
- Page-based reads with high latency. Flash reads are at page granularity (10s KBs) with a latency substantially worse than DRAM (10s microseconds). Small reads reduce effective bandwidth.
These issues mean HBF cannot replace all HBM; a system still needs normal DRAM for data unsuitable for HBF.

The addition of HBF enables exciting capabilities for LLM inference:
- 10X weight memory. Weights are frozen during inference, so HBF’s 10X capacity could host many more weights—such as giant MoEs—to enable much bigger models than affordable today.
- 10X context memory. Limited write endurance makes HBF infeasible for KV Cache data updated for every query or generation token. However, it works for a slow-changing context. For example: A web corpus, used by LLM search; A code database, used by AI coding; A paper corpus, used by AI tutoring.
- Smaller inference system. Memory capacity determines the minimum hardware to hold a model. HBF downsizes the system, helping communication, reliability, and resource allocation.
- Greater resource capacity. HBF would reduce dependency on HBM-only architectures and alleviate the global shortage of mainstream memory devices.

② Processing-Near-Memory for high bandwidth
Processing-in-Memory (PIM), conceived by the 1990s, obtains high bandwidth by augmenting memory dies with small, low-power processors attached to memory banks. While PIM offers extraordinary bandwidth, key challenges are software sharding and memory-logic coupling. The former limits the number of software kernels that can run well on PIM. The latter hurts power and area efficiency of compute logic. In contrast, Processing-Near-Memory (PNM) is a technique that places memory and logic nearby but still uses separate dies. One version of PNM is 3D compute-logic stacking.

Unfortunately, some recent papers blur the distinction between PIM and PNM. We go here with a simple but sharp distinction: PIM refers to designs where the processor and memory are in the same die and PNM means they are on nearby but separate dies. This distinction makes PIM and PNM unambiguous.

Hardware advantages are irrelevant if it’s too hard for software to use, which is our experience for PIM and datacenter LLMs. PNM is better than PIM for LLM inference, despite weaknesses in bandwidth and power. Specifically, PIM requires software to shard memory structures of LLMs into many small pieces that rarely interact to fit into 32-64MB memory banks; shards in PNM can be 1000x larger, making it much easier to partition LLMs with a low communication overhead. It is also unclear if the compute can be sufficient in PIM given the very limited budget for power and thermal of a DRAM technology process node.

While PNM is better than PIM for datacenter LLMs, the comparison is not as clear for mobile devices. Mobile devices are more energy-constrained and run LLMs with many fewer weights, shorter context, smaller data types, and smaller batch sizes due to a single user. These differences simplify sharding, reduce the compute and thermal need, making PIM weaknesses less problematic and so plausibly viable for mobile devices.

③ 3D memory-logic stacking for high bandwidth
Unlike 2D hardware, where memory IOs reside on the shoreline, 3D stacking uses vertical through silicon vias (TSVs) to get a wide-and-dense memory interface for high bandwidth at low power.

3D memory-logic stacking has two versions:
1. Compute-on-HBM-base-die reuses HBM designs by inserting the compute logic into the HBM base die. Because the memory interface is unchanged, bandwidth is the same as HBM, while power is 2–3X lower because of the shortened data path.
2. Custom 3D solutions enable bandwidth and bandwidth-per-watt higher than reusing HBM through using a wider-and-denser memory interface and more advanced packaging technologies.

Despite better bandwidth and power, 3D stacking faces challenges:
1. Thermal. Cooling a 3D design is harder than 2D as there is less surface area. One solution is to limit FLOPS of the compute logic by running at a low clock speed and voltage, as LLM Decode inference already has low arithmetic intensity.
2. Memory-logic coupling. An industry standard may be required for the memory interface of 3D compute-logic stacking.

④ Low-latency interconnect
Techniques ①–③ help latency as well as throughput: higher memory bandwidth reduces latency of every Decode iteration and higher memory capacity per accelerator chip reduces system size, saving communication overhead. Another promising latency direction for datacenters is to rethink the network latency-bandwidth tradeoff since inference is more sensitive to interconnect latency. For example:
- High-connectivity topology. Topologies with high connectivity—such as tree, dragonfly, and high-dimensional tori—require fewer hops, reducing latency. These topologies may diminish bandwidth but improve latency.
- Processing-in-network. Communication collectives used by LLMs—broadcast, all-reduce, MoE dispatch and collect—are well suited for in-network acceleration to improve both bandwidth and latency, e.g., a tree topology with in-network aggregation enables both low-latency and high-throughput all-reduce.
- AI chip optimization. The latency focus influences chip design with several possible optimizations: Storing small arriving packets directly into on-chip SRAM instead of off-chip DRAM; Placing the compute engine close to the network interface to reduce transportation time.
- Reliability. Codesigning reliability and interconnect can help both: A local standby spare reduces system failures and the latency and throughput consequences of migrating the failed job to a new healthy node somewhere when there are no standby spares. If perfect communication is unnecessary for LLM inference, one can reduce latency yet deliver satisfactory quality results by using fake data or a prior result when message timeout expires, rather than waiting for straggler messages to arrive.

RELATED WORK
High Bandwidth Flash. SanDisk first proposed HBF, an HBM-like architecture for flash to overcome its bandwidth limit. Microsoft researchers proposed a new class of memory that focuses on read performance and high density instead of write performance and retention time for AI inference. Another research paper proposed integrating flash into mobile processors for on-device LLM inference enhanced with an LPDDR interface for the low bandwidth need of Prefill and Processing-Near-Flash for the high bandwidth need of Decode.

Processing-Near-Memory. 3D compute-logic stacking has gained increasing attention as a technique for bandwidth higher than HBM, such as compute-on-HBM-base-die proposals and an AMD concept. In the non-3D space, Samsung AXDIMM and Marvell Structera-A attach processors to commercial DDR DRAM. The former integrated compute logic in the DIMM buffer chip. The latter leveraged the CXL interface for improved programmability and ease of system integration. Many papers discuss using PIM/PNM in mobile devices, not the main focus of this paper.

Low-latency interconnect. Numerous papers describe low hop count network topologies including trees, dragonfly, and high-dimensional Tori. Examples of commercial processing-in-network are NVIDIA NVLink and Infiniband switches that support in-switch reduction, and multicast acceleration through SHARP. Similar capabilities for AI workloads appeared recently in Ethernet switches.

Software Innovations. Besides this paper’s focus on hardware innovations, there is a rich space of software-hardware codesign for algorithmic and software innovations to improve LLM inference. For example, a root cause is the autoregressive nature of Transformer Decode. A new algorithm that avoided autoregressive generation—such as Diffusion for image generation—could dramatically simplify AI inference hardware.

CONCLUSION
The increasing importance and difficulty of inference for LLMs—which desperately need lower cost and latency—is an attractive research target. Autoregressive Decode is already a major challenge for memory and interconnect latency, which is exacerbated by MoE, reasoning, multimodal data, RAG, and long input/output sequences.

The computer architecture community has made great contributions on challenges when a realistic simulator was available, as it has previously for branch prediction and cache design. Since primary bottlenecks of LLM inference are memory and latency, a roofline-based performance simulator could be useful to provide first-order estimates in many scenarios. Additionally, such a framework should track memory capacity, explore various sharding techniques that are critical to performance, and use modern performance/cost metrics. We hope academic researchers will respond to this opportunity to accelerate AI research.

The current AI hardware philosophy—full-reticle die with high FLOPS, many HBM stacks, and bandwidth-optimized interconnect—is a mismatch to LLM Decode inference. While many researchers explore compute for datacenters, we recommend instead improving memory and network along four directions: HBF, PNM, 3D stacking, and low latency interconnect. Moreover, novel performance/cost metrics that focus on datacenter capacity, system power, and carbon footprint offer new opportunities versus conventional measures. Constrained versions of HBF, PNM, PIM, and 3D stacking also might work well for mobile device LLMs.

Such advances would unlock collaborative work towards important and urgent innovations that the world needs for delivering affordable AI inference.
