# Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses

**Authors:** Jiahang Lin, Shichun Liu, Chengjun Pan, Lizhi Lin, Shihan Dou, Xuanjing Huang, Hang Yan, Zhenhua Han, Tao Gui
**Date:** April 2026
**Source:** arXiv:2604.25850
**DOI:** 10.48550/arXiv.2604.25850

## Abstract Summary
This paper introduces **Agentic Harness Engineering (AHE)**, a framework for automating the evolution of coding-agent harnesses. It argues that the harness (prompts, tools, middleware) is as critical as the model itself. AHE uses three "observability pillars" to turn harness edits into falsifiable contracts, enabling autonomous, non-random evolution.

## Core Pillars
1.  **Component Observability:** Every editable part of the harness has a file-level representation.
2.  **Experience Observability:** Distills complex agent trajectories into structured evidence for the evolving agent.
3.  **Decision Observability:** Pairs every edit with a prediction that is verified against future outcomes.

## Key Results
- Improved `pass@1` on Terminal-Bench 2 from 69.7% to 77.0%.
- Surpassed human-designed harnesses (Codex-CLI).
- Evolved components show "cross-family transfer," improving performance across different model families (GPT, Claude, etc.).

## Reference
Lin, J., et al. (2026). Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses. arXiv preprint arXiv:2604.25850.
