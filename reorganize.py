import os
import re
import shutil

wiki_dir = '/Users/sfines/workspace/slf-llm-wiki/wiki'
index_file = os.path.join(wiki_dir, 'index.md')

with open(index_file, 'r') as f:
    lines = f.readlines()

# Map file -> category folder
file_to_folder = {}
current_category = None

in_catalog = False
for line in lines:
    if "## 📚 Complete Catalog" in line:
        in_catalog = True
    if in_catalog and line.startswith('- ['):
        # Top-level category
        match = re.match(r'- \[([^\]]+)\]', line)
        if match:
            cat_name = match.group(1).lower().replace(' ', '-').replace('(', '').replace(')', '')
            current_category = cat_name
            # If the category itself links to a file, map that file
            link_match = re.search(r'\]\(([^)]+\.md)(?:#[^)]+)?\)', line)
            if link_match:
                filename = link_match.group(1)
                file_to_folder[filename] = current_category
    elif in_catalog and current_category and line.strip().startswith('- ['):
        link_match = re.search(r'\]\(([^)]+\.md)(?:#[^)]+)?\)', line)
        if link_match:
            filename = link_match.group(1)
            file_to_folder[filename] = current_category

# Cleanup category names manually for better aesthetics
category_overrides = {
    'core-concepts': 'core-concepts',
    'agentic-domain-driven-design': 'agentic-ddd',
    'agent-memory': 'agent-memory',
    'advanced-retrieval-rag': 'advanced-retrieval',
    'agentic-harness-engineering': 'agentic-harness',
    'confucius-code-agent': 'confucius',
    'agyn-team-based-engineering': 'agyn',
    'apwa-distributed-workloads': 'apwa',
    'gambit-adversarial-robustness': 'gambit',
    'automating-domain-driven-design': 'automating-ddd',
    'system-logs': None # Don't move log.md
}

for file, cat in list(file_to_folder.items()):
    if cat in category_overrides:
        if category_overrides[cat] is None:
            del file_to_folder[file]
        else:
            file_to_folder[file] = category_overrides[cat]

# Ensure we map all .md files (if some are missed but we still need to calculate paths)
all_md_files = [f for f in os.listdir(wiki_dir) if f.endswith('.md')]

# Map original filename to its new relative path (from wiki root)
new_paths = {}
for f in all_md_files:
    if f in file_to_folder:
        new_paths[f] = f"{file_to_folder[f]}/{f}"
    else:
        new_paths[f] = f

def get_rel_path(from_file_new_path, to_file_new_path):
    from_dir = os.path.dirname(from_file_new_path)
    if not from_dir:
        from_dir = '.'
    
    to_path = to_file_new_path
    
    # Use os.path.relpath to calculate
    rel = os.path.relpath(to_path, from_dir)
    return rel

# Let's process each file
for filename in all_md_files:
    filepath = os.path.join(wiki_dir, filename)
    with open(filepath, 'r') as f:
        content = f.read()
    
    # We need to find all markdown links. 
    # Example: [text](target.md) or [text](target.md#anchor)
    def link_replacer(match):
        text = match.group(1)
        link = match.group(2)
        
        # Parse link into path and anchor
        if '#' in link:
            target_path, anchor = link.split('#', 1)
            anchor = '#' + anchor
        else:
            target_path = link
            anchor = ''
            
        # Ignore external links
        if target_path.startswith('http') or not target_path.endswith('.md'):
            return f"[{text}]({link})"
            
        # Extract filename (might already have some relative path, though they are flat right now)
        target_file = os.path.basename(target_path)
        
        if target_file in new_paths:
            new_rel = get_rel_path(new_paths[filename], new_paths[target_file])
            return f"[{text}]({new_rel}{anchor})"
        else:
            return f"[{text}]({link})"
            
    new_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link_replacer, content)
    
    # Write back the new content to the *current* location first
    with open(filepath, 'w') as f:
        f.write(new_content)

# Now move the files to their new locations
for filename, folder in file_to_folder.items():
    source = os.path.join(wiki_dir, filename)
    target_dir = os.path.join(wiki_dir, folder)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    target = os.path.join(target_dir, filename)
    shutil.move(source, target)
    print(f"Moved {filename} -> {folder}/{filename}")

print("Done reorganizing and updating links.")
