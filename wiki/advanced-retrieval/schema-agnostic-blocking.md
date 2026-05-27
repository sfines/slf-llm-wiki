# Schema-Agnostic Blocking

Schema-agnostic blocking methods are Entity Resolution candidate selection techniques that make no assumptions about the input data's schema. Instead of extracting blocking keys from specific attributes (like a "name" or "zip_code" column), they extract blocks from all available attribute values.

This makes schema-agnostic blocking highly suitable for highly heterogeneous, loosely structured entity profiles, such as data stemming from the Web of Data, or instances with significant noise in both attribute names and values.

Key approaches include:
* **Token Blocking (TB)**: Extracts all tokens from all attribute values of an entity. Two entities co-occur in a block if they share at least one token, regardless of the attribute names.
* **Attribute Clustering Blocking**: Groups syntactically similar attributes and demands common tokens appear in similar attribute clusters.
* **Semantic Graph Blocking**: Relies entirely on relational links (like RDF edges or foreign keys) to form blocks, disregarding textual attribute values.

## References
- [A Survey of Blocking and Filtering Techniques for Entity Resolution](../../raw/entity-resolution-survey.md)