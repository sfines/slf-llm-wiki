# Block Processing

Block Processing is an optional optimization stage in Entity Resolution that occurs between Block Building and Matching. Its goal is to refine the initial block collection to significantly increase precision (Pairs Quality) with a negligible cost in recall (Pair Completeness).

Block Processing optimizations generally fall into two categories:
* **Block Cleaning**: Discarding entire blocks that primarily contain unnecessary comparisons. For example, a block corresponding to the highly frequent token "the" would be eliminated.
* **Comparison Cleaning**: Discarding individual redundant or superfluous comparisons within certain blocks. Since blocking schemes often map entities to multiple overlapping blocks (redundancy-positive), Comparison Cleaning ensures that a pair of entities is compared only once.

## References
- [A Survey of Blocking and Filtering Techniques for Entity Resolution](../../raw/entity-resolution-survey.md)