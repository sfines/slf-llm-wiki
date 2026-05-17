# GAMBIT Overview

**GAMBIT** is a state-of-the-art benchmark for evaluating the **Adversarial Robustness** of [Multi-Agent Systems (MAS)](multi-agent-systems.md), with a focus on detecting **adaptive imposters**.

## Core Philosophy: The Security of Collectives
The fundamental thesis of GAMBIT is that the gains of an agentic AI collective—such as [Team-Based SE](team-based-software-engineering.md) or [Strategic Orchestration](agyn-framework.md)—can be nullified by a single deceptive agent. To secure these systems, developers must move beyond static defenses and embrace **adaptive resilience**.

## Key Tenets
### 1. [Three-Mode Evaluation](gambit-three-mode-benchmark.md)
GAMBIT shifts the focus from simple detection accuracy to **adaptation speed**, measuring how quickly a system can recalibrate to novel threats.

### 2. [Adaptive Imposter Dynamics](gambit-adaptive-imposter.md)
The benchmark introduces an evolutionary framework where imposter agents learn to bypass active detectors while still achieving their malicious objectives.

### 3. [Fast Recalibration](gambit-fast-recalibration.md)
A critical engineering pillar focused on updating defenses with minimal data (as few as 20 labeled examples) using techniques like meta-learning.

## Evaluation Substrate: Chess as Reasoning
GAMBIT uses **Chess** as its substrate problem. This provides a deep reasoning space with verifiable performance metrics, allowing for clear measurement of how an imposter "collapses" the performance of a benign collective.

## See Also
- [Multi-Agent Adversarial Robustness](adversarial-robustness-mas.md)
- [Imposter Detector Evaluation](gambit-detector-evaluation.md)
- [Raw Source: GAMBIT Paper](../raw/gambit-paper.md)

---
[🏠 Back to Home](index.md)
