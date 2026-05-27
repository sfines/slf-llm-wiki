# Entity Resolution Blocking

Blocking is a candidate selection technique in Entity Resolution designed to reduce the number of expensive pairwise comparisons by clustering potentially matching entities into blocks. Only entities sharing at least one block are compared.

Blocking trades slightly lower effectiveness (missing some matches) for significantly higher efficiency. A blocking scheme is evaluated by three main metrics:
* **Pair Completeness (PC)**: Recall; the portion of actual duplicates that share at least one block.
* **Pairs Quality (PQ)**: Precision; the portion of executed comparisons that actually correspond to real duplicates.
* **Reduction Ratio (RR)**: The reduction in the number of comparisons relative to a brute-force approach.

Blocking schemes consists of a *transformation function* (extracting signatures/keys) and an *assignment function* (mapping keys to blocks). Methods can be redundancy-free (disjoint blocks) or redundancy-positive (overlapping blocks), and schema-aware or schema-agnostic.

## References
- [A Survey of Blocking and Filtering Techniques for Entity Resolution](../../raw/entity-resolution-survey.md)