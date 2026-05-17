# OpenCode Instructions for SLF LLM Wiki

This repository is an "LLM Wiki" (plain markdown, semantic relative links, no frontmatter) acting as a knowledge graph for Agentic Engineering. Your primary job is reading papers, summarizing concepts, and interlinking knowledge.

## Repo Architecture & Boundaries
- `raw/`: Immutable source texts (papers, articles). Never modify existing raw files.
- `wiki/`: LLM-generated markdown concept pages. These are grouped into logical subdirectories (e.g., `wiki/agentic-ddd/`, `wiki/agent-memory/`).
- `wiki/index.md`: The central taxonomy map. **Every** markdown file in `wiki/` must be categorized and linked here.
- `wiki/log.md`: The chronological record. Append a brief summary here after any significant batch of changes.

## Exact Verification Commands
Run these to verify graph integrity after creating, renaming, or modifying files. This is **mandatory**.
- `python lint_wiki.py` : Finds broken relative links anywhere, and lists files missing from `wiki/index.md`.
- `python lint_raw.py` : Finds files in `raw/` that have not been referenced by any file in `wiki/`.

*Command order:* `python lint_wiki.py && python lint_raw.py`

## Ingestion Workflow & Quirks
- **Full Text Sourcing:** When pulling from Zotero or external sources, fetch the *full* article text to build the `raw/` document. Do not rely solely on the abstract. Do not attempt to read local PDFs directly; use the URL to fetch the content.
- **Incremental Slicing:** A single raw paper should usually spawn or update multiple (e.g., 10-15) highly-focused concept files in `wiki/`, rather than generating one giant summary.
- **Format:** Pure Markdown only. Do not use YAML/JSON frontmatter.
- **Linking:** Always use explicit relative paths for links (e.g., `[Concept](../core-concepts/concept.md)`). Avoid absolute paths.

## Reference Files
- `GEMINI.md`: Contains the original foundational project instructions and design mandates.
