# Project Instructions: slf-llm-wiki

This project follows the **LLM Wiki** pattern for incremental knowledge building.

## Architecture

1. **Raw Sources (`/raw`)**: Immutable source documents (articles, papers, data files).
2. **The Wiki (`/wiki`)**: LLM-generated markdown files, entity pages, and concept summaries.
3. **Assets (`/raw/assets`)**: Local images and media referenced by the wiki.

## Source Handling

1. When ingesting sources using Zotero or other library managers, do not rely solely on the abstract, but fetch the full paper and perform the ingestion upon the full contents of the file. 
2. If there are multiple versions of the same source, Ask the user which version they would like to use.
3. Do not attempt to read pdfs from the Zotero library directly. Use the URL attribute for the Zotero entry to fetch the full Paper / Article

## Navigation

- **Index (`/wiki/index.md`)**: Categorized catalog of all wiki pages.
- **Log (`/wiki/log.md`)**: Chronological record of activities.

## Workflows

### Incremental Ingestion

### Synthesis Maintenance
Each area directory contains an `<area>-synthesis.md` file. Whenever you ingest a new source into an area, you **must** update its corresponding synthesis file. The update should:
- Weave the new insights into the "State of Current Thought" section to highlight the most current thinking.
- Explicitly outline any new or existing debates in the "Areas of Controversy / Ongoing Conversation" section so they can be understood as areas of ongoing conversation.

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
