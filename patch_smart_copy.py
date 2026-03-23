import os
import codecs

base_dir = r"c:\Users\Mahir\Desktop\Locy"

for root, _, files in os.walk(base_dir):
    if "node_modules" in root or ".git" in root: continue
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with codecs.open(path, "r", "utf-8") as f:
                content = f.read()
            
            replacements = [
                (
                    '<a href="mailto:hi@locy.ai?subject=Enterprise%20Inquiry" class="btn btn-outlined"',
                    '<a href="mailto:hi@locy.ai?subject=Enterprise%20Inquiry" class="btn btn-outlined btn-smart-copy" data-copy="hi@locy.ai"'
                ),
                (
                    '<a href="mailto:hi@locy.ai" class="btn btn-outlined"',
                    '<a href="mailto:hi@locy.ai" class="btn btn-outlined btn-smart-copy" data-copy="hi@locy.ai"'
                ),
                (
                    '<a href="mailto:legal@locy.ai?subject=DPA%20Request" class="btn btn-outlined"',
                    '<a href="mailto:legal@locy.ai?subject=DPA%20Request" class="btn btn-outlined btn-smart-copy" data-copy="legal@locy.ai"'
                ),
                (
                    '<a href="mailto:hi@locy.ai?subject=Enterprise%20Compliance%20Inquiry" class="btn btn-outlined"',
                    '<a href="mailto:hi@locy.ai?subject=Enterprise%20Compliance%20Inquiry" class="btn btn-outlined btn-smart-copy" data-copy="hi@locy.ai"'
                )
            ]
            
            modified = False
            for old, new in replacements:
                if old in content:
                    content = content.replace(old, new)
                    modified = True
            
            if modified:
                with codecs.open(path, "w", "utf-8") as f:
                    f.write(content)
                print(f"Patched {path}")
