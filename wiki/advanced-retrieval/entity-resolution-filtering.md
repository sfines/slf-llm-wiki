# Entity Resolution Filtering

Filtering is a technique used in Entity Resolution to quickly identify entity pairs that are likely to satisfy a predetermined similarity threshold (i.e., a similarity join), thereby excluding pairs guaranteed not to match. 

Unlike Blocking—which operates without knowledge of the matching function and produces approximate candidate blocks—Filtering follows a strict **filter-verification** framework:
1. **Filtering**: Computes a set of candidates by pruning all true negatives (pairs that mathematically cannot reach the threshold) while allowing some false positives.
2. **Verification**: Computes the exact similarity score between the candidates to remove the false positives.

Common filtering string similarity joins (e.g., based on Edit Distance, Jaccard, Cosine, or Dice similarities) typically rely on transforming string comparisons into equivalent set overlap thresholds. Filtering acts as an exact procedure that produces no false negatives, making it complementary to the approximate nature of Blocking.

## References
- [A Survey of Blocking and Filtering Techniques for Entity Resolution](../../raw/entity-resolution-survey.md)