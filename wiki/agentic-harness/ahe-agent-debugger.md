# AHE Agent Debugger Pipeline

The **Agent Debugger** is the technical implementation of the [Experience Observability](ahe-experience-observability.md) pillar in the [AHE framework](agentic-harness-engineering.md).

## Distillation Workflow
The pipeline processes multi-million-token trajectories through a three-stage distillation:
1.  **Event Extraction:** Identifying high-level actions (e.g., "Edited file X", "Ran test Y") and discarding redundant model output.
2.  **Trajectory Layering:** Organizing events into a "drill-down" hierarchy, from global task goals to granular shell commands.
3.  **Root-Cause Attribution:** A specialized "debugger agent" analyzes the distilled trajectory to identify exactly which harness component (or lack thereof) contributed to a failure.

## Evidence Corpus
The output of the debugger is a **Structured Evidence Corpus**. Instead of reading raw logs, the "evolving agent" consumes these structured lessons to inform its next harness edit.

## Technical Stack
- **E2B Sandboxes:** Used for isolated execution of agent actions.
- **LLM-Based Debuggers:** Independent models used to analyze the trajectories of the primary agent.

## See Also
- [AHE Pillar: Experience Observability](ahe-experience-observability.md)
- [Agentic Harness Engineering (AHE)](agentic-harness-engineering.md)
