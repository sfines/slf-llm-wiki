# Multi-Agent Structural Fallback Mechanism

A Structural Fallback Mechanism is a hard constraint designed within a multi-agent workflow to handle missing or inaccessible primary data sources safely. It deliberately shifts from primary retrieval to secondary sources or explicit failure states to prevent hallucination.

## Execution Flow

- **Primary Retrieval**: Agents attempt to fetch data from high-authority sources, such as official corporate business registries.
- **Secondary Fallback**: If primary data is unavailable (e.g., missing registry number due to foreign incorporation), the system dynamically routes queries to third-party commercial databases like Crunchbase or Dealroom.
- **Explicit Gap Flagging**: If all sources fail, the agent outputs an explicit "Not Found" flag instead of generating an estimate, surfacing the true epistemic state to the analyst.

## See Also

- [Financial Hallucination Mitigation](financial-hallucination-mitigation.md)
- [Autonomous Financial API Routing](autonomous-financial-api-routing.md)
- [Raw Source: VC Due Diligence Paper](../../raw/multi-agent-vc-due-diligence-paper.md)
