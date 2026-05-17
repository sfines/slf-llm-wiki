import os
import re

root_dir = '/Users/sfines/workspace/slf-llm-wiki'
wiki_dir = os.path.join(root_dir, 'wiki')

# First, let's build a map of all markdown files and their absolute paths
all_md_paths = {}
for current_root, dirs, files in os.walk(root_dir):
    if '.git' in current_root or '.obsidian' in current_root:
        continue
    for f in files:
        if f.endswith('.md'):
            # Just store basename -> absolute path
            # Assuming filenames are unique across the whole repo for this simple fix
            all_md_paths[f] = os.path.join(current_root, f)

def get_rel_path(from_file_abs, to_file_abs):
    from_dir = os.path.dirname(from_file_abs)
    return os.path.relpath(to_file_abs, from_dir)

broken_links_fixed = 0

for current_root, dirs, files in os.walk(root_dir):
    if '.git' in current_root or '.obsidian' in current_root:
        continue
    for f in files:
        if f.endswith('.md'):
            file_abs = os.path.join(current_root, f)
            with open(file_abs, 'r') as fh:
                content = fh.read()
                
            def link_replacer(match):
                global broken_links_fixed
                text = match.group(1)
                link = match.group(2)
                
                if link.startswith('http') or not link.split('#')[0].endswith('.md'):
                    return match.group(0)
                    
                target_path, *anchor_parts = link.split('#', 1)
                anchor = '#' + anchor_parts[0] if anchor_parts else ''
                
                # Check if the current link is broken
                target_abs = os.path.normpath(os.path.join(os.path.dirname(file_abs), target_path))
                
                if not os.path.exists(target_abs):
                    # It's broken. Let's find the correct target file based on its basename
                    target_basename = os.path.basename(target_path)
                    if target_basename in all_md_paths:
                        correct_abs = all_md_paths[target_basename]
                        new_rel = get_rel_path(file_abs, correct_abs)
                        broken_links_fixed += 1
                        return f"[{text}]({new_rel}{anchor})"
                
                return match.group(0)

            new_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link_replacer, content)
            if new_content != content:
                with open(file_abs, 'w') as fh:
                    fh.write(new_content)

print(f"Fixed {broken_links_fixed} broken links.")
