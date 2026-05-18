# Macro-Micro Economic Unified Modeling

Macro-Micro Economic Unified Modeling is an approach to Agent-Based Modeling (ABM) that bridges the gap between individual, household-level decision-making (microeconomics) and aggregate, society-wide trends (macroeconomics) within a single, cohesive framework.

## Bridging the Gap
Historically, macroeconomic modeling relies on closed-form frameworks (like DSGE) with strong equilibrium assumptions, which struggle to represent out-of-equilibrium dynamics and heterogeneous agents. Conversely, micro-level ABMs often scale poorly and require intense re-calibration. Frameworks like EconAI bypass this dichotomy by using a unified large language model (LLM) backbone. 

## Interacting Layers
In this unified model, the macro-level regularities naturally emerge from the interaction of micro-level actors:
- **Micro-Level (Households)**: Agents make individualized decisions regarding labor participation, consumption, and savings based on personal income and sentiment.
- **Macro-Level (Firms, Government, Financial Markets)**: Firms handle goods production and pricing, the government applies progressive taxation and wealth redistribution, and financial institutions adjust interest rates (e.g., via a modified Taylor rule) based on aggregate inflation and unemployment.

By coupling these layers, the simulation can accurately recover textbook economic regularities—such as the Phillips curve and Okun's law—without requiring hard-coded aggregate rules.

## See Also
- [EconAI Framework](econai-framework.md)
- [Household vs Firm Agent Roles](household-vs-firm-agent-roles.md)
- [Long-Term Strategic Economic Planning](long-term-strategic-economic-planning.md)
- [Raw Source: EconAI Paper](../../raw/econai-paper.md)