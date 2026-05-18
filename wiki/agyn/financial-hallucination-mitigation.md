# Financial Hallucination Mitigation

Financial Hallucination Mitigation focuses on preventing Large Language Models from generating plausible but factually incorrect financial figures. In due diligence, fabricated data is unacceptable, requiring strict structural constraints over model output and an emphasis on data provenance.

## Key Strategies

- **Grounding in Official Data**: Utilizing real-time retrieval from authoritative business registries and auditable filings.
- **Explicit Data Gaps**: Writing a "Not Found" flag directly into reports when data is unavailable, making the gap auditable rather than guessing figures.
- **Preserved Citations**: Enforcing inline citations and linking directly to source PDFs and page numbers to enable human verification.

## See Also

- [Multi-Agent Structural Fallback Mechanism](multi-agent-structural-fallback-mechanism.md)
- [Retrieval-Augmented Generation for Finance](retrieval-augmented-generation-for-finance.md)
- [Raw Source: VC Due Diligence Paper](../../raw/multi-agent-vc-due-diligence-paper.md)
