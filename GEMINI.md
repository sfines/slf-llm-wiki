# Project Instructions: slf-llm-wiki

This project follows the **LLM Wiki** pattern for incremental knowledge building.

## Architecture

1. **Raw Sources (`/raw`)**: Immutable source documents (articles, papers, data files).
2. **The Wiki (`/wiki`)**: LLM-generated markdown files, entity pages, and concept summaries.
3. **Assets (`/raw/assets`)**: Local images and media referenced by the wiki.

## Navigation

- **Index (`/wiki/index.md`)**: Categorized catalog of all wiki pages.
- **Log (`/wiki/log.md`)**: Chronological record of activities.

## Workflows

### Incremental Ingestion
When adding a new source to `/raw`:
1. Analyze the source.
2. Update `/wiki/index.md` if a new category is needed.
3. Create or update 10-15 relevant files in `/wiki` to integrate the knowledge.
4. Record the action in `/wiki/log.md`.

### Compounding Knowledge
- Save insights from queries back into the wiki as new pages.
- Link new pages to existing ones to maintain the knowledge graph.

### Automated Maintenance
- Periodically check for contradictions, stale claims, orphan pages, and missing cross-references.
- Ensure all pages are listed in `/wiki/index.md`.

## Conventions
- Use Markdown for all content.
- Prefer descriptive filenames (e.g., `quantum-computing-fundamentals.md`).
- Use relative links between wiki pages.
- Avoid absolute paths.
