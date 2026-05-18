# Verified Inference-Time Skills

Inference-time skills are reusable, prompt-level interventions that modify the behavior of a base agent to improve its task performance without altering the underlying model weights. Verified inference-time skills are skills that have been empirically tested to ensure they provide a net positive effect.

## Auditable Artifacts

Unlike weight updates or opaque prompt searches, these skills are human-readable artifacts. They allow practitioners to inspect the encoded procedures, direct instructions, and task-specific guidance before they are deployed to an agent.

## Skill Structure

A typical skill intervention consists of:
- A structured prompt defining task context, success procedures, and failure avoidance.
- Task metadata describing the operational environment.
- Optional executable scripts and auxiliary reference documents for tool-intensive tasks.

## See Also
- [SkillGen Framework](./skillgen-framework.md)
- [Causal Evaluation of Skill Interventions](./causal-evaluation-of-skill-interventions.md)
- [Cross-Model Skill Transfer](./cross-model-skill-transfer.md)
- [../core-concepts/autonomous-agents.md](../core-concepts/autonomous-agents.md)
- [Raw Source: SkillGen Paper](../../raw/skillgen-paper.md)