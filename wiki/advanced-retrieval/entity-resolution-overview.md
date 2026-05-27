# Entity Resolution (ER)

Entity Resolution (ER) is the task of identifying different entity profiles that describe the same real-world object. It is a core task in Data Integration, applicable to structured databases, semi-structured data (like Linked Open Data), and unstructured entities from text. 

The primary challenge of Entity Resolution is its inherently quadratic time complexity ($O(n^2)$), as exhaustive pairwise comparisons between all profiles do not scale to large datasets. To address this, the process is generally split into:
1. **Candidate Selection**: Quickly filtering out obvious non-matches using techniques like Blocking and Filtering.
2. **Candidate Matching**: Applying computationally expensive similarity measures to the remaining candidate pairs.

Modern approaches tackle Big Data volume via parallelization and schema-agnostic strategies.

## References
- [A Survey of Blocking and Filtering Techniques for Entity Resolution](../../raw/entity-resolution-survey.md)