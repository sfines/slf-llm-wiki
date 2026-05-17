# User Experience (UX) for Autonomy

**User Experience (UX)** in the [Confucius SDK](confucius-code-agent.md) focuses on the human developer's ability to monitor, control, and trust the [Autonomous Agent](../core-concepts/autonomous-agents.md).

## Beyond Traditional UI
UX for autonomous systems must address unique challenges:
- **Transparency:** The user must be able to "look under the hood" at the agent's reasoning and tool usage.
- **Controllability:** Providing "steering" mechanisms that allow the user to adjust the agent's path without micro-managing.
- **Trust:** Building confidence through consistent performance and clear communication of uncertainty.

## Mechanisms in Confucius
- **Observability Dashboards:** Visualizing agent trajectories and decision points.
- **Human-in-the-loop (HITL) Checkpoints:** Defined moments where the agent must pause for user approval (e.g., before a major PR merge).
- **Explanation Generation:** The agent provides natural language summaries of "why" it took a specific action.

## See Also
- [Confucius SDK Perspectives](confucius-sdk-perspectives.md)
- [Agent Experience (AX) Design](confucius-ax-design.md)
- [Developer Experience (DX) in Agents](confucius-dx-design.md)
