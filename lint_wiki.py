import os
import re

wiki_dir = 'wiki'
index_file = os.path.join(wiki_dir, 'index.md')

md_files = []
for root, dirs, files in os.walk(wiki_dir):
    for f in files:
        if f.endswith('.md'):
            # Store relative paths from wiki_dir for index comparison
            rel_path = os.path.relpath(os.path.join(root, f), wiki_dir)
            md_files.append(rel_path)

with open(index_file, 'r') as f:
    index_content = f.read()

linked_in_index = set(re.findall(r'\]\(([^)]+\.md)(?:#[^)]+)?\)', index_content))

orphans_from_index = [f for f in md_files if f not in linked_in_index and f != 'index.md' and f != 'log.md']

print("Orphan files not in index.md:")
for o in sorted(orphans_from_index):
    print(f"  - {o}")

broken_links = []

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.obsidian' in root:
        continue
    for file_name in files:
        if file_name.endswith('.md'):
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r') as fh:
                content = fh.read()
                links = re.findall(r'\]\(([^)]+)\)', content)
                for link in links:
                    if link.startswith('http://') or link.startswith('https://'):
                        continue
                    link_path = link.split('#')[0]
                    if not link_path:
                        continue
                    
                    target_path = os.path.normpath(os.path.join(os.path.dirname(file_path), link_path))
                    
                    if not os.path.exists(target_path):
                        broken_links.append((file_path, link))

print("\nBroken links:")
for file, link in broken_links:
    print(f"  - {file}: {link}")
