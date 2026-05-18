import os

files_to_update = ['/Users/sfines/workspace/slf-llm-wiki/AGENTS.md', '/Users/sfines/workspace/slf-llm-wiki/GEMINI.md']

synthesis_instruction = """
### Synthesis Maintenance
Each area directory contains an `<area>-synthesis.md` file. Whenever you ingest a new source into an area, you **must** update its corresponding synthesis file. The update should:
- Weave the new insights into the "State of Current Thought" section to highlight the most current thinking.
- Explicitly outline any new or existing debates in the "Areas of Controversy / Ongoing Conversation" section so they can be understood as areas of ongoing conversation.
"""

for filepath in files_to_update:
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r') as f:
        content = f.read()
        
    if "Synthesis Maintenance" not in content:
        if "## Ingestion Workflow & Quirks" in content:
            # For AGENTS.md
            content = content.replace("## Ingestion Workflow & Quirks", "## Ingestion Workflow & Quirks\n" + synthesis_instruction)
        elif "### Incremental Ingestion" in content:
            # For GEMINI.md
            content = content.replace("### Incremental Ingestion", "### Incremental Ingestion\n" + synthesis_instruction)
            
        with open(filepath, 'w') as f:
            f.write(content)
