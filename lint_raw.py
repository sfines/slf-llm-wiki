import os
import re

wiki_dir = 'wiki'
raw_dir = 'raw'

raw_files = set(f for f in os.listdir(raw_dir) if f.endswith('.md'))
referenced_raw = set()

for root, dirs, files in os.walk(wiki_dir):
    for file_name in files:
        if file_name.endswith('.md'):
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r') as fh:
                content = fh.read()
                # Find markdown links: [text](link)
                links = re.findall(r'\]\(([^)]+)\)', content)
                for link in links:
                    if '../raw/' in link:
                        referenced_raw.add(os.path.basename(link.split('#')[0]))

unreferenced = raw_files - referenced_raw

print("Raw files not referenced in wiki:")
for u in sorted(list(unreferenced)):
    print(f"  - {u}")
