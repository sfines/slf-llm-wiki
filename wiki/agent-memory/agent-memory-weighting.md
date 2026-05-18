# Agent Memory Weighting

Agent Memory Weighting is the analytical process of adjusting the influence of historical data versus current contextual information when an agent forms a decision. 

## Decaying Historical Impact
In realistic economic modeling, equal weighting of all past events leads to behavioral rigidity. Memory weighting introduces a decay function to the impact of historical economic data. As events recede into the past, their direct influence on the agent's immediate choices diminishes. This prevents agents from experiencing excessive, prolonged reactions to short-term economic shocks that have already been resolved.

## Balancing Objective and Subjective Data
Memory weighting does not act alone; it works in tandem with the agent's subjective confidence (such as the Economic Sentiment Index). By explicitly weighting between objectively remembered history and the agent's current emotional context, the decision-making module can modulate responses dynamically. This results in agents that are both historically grounded and highly adaptive to evolving environments.

## See Also
- [Agent Event Memory Perception](agent-event-memory-perception.md)
- [Economic Sentiment Indexing](economic-sentiment-indexing.md)
- [Raw Source: EconAI Paper](../../raw/econai-paper.md)