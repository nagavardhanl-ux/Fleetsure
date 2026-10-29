import json
from bs4 import BeautifulSoup

with open('fleetsure_content.json', 'r', encoding='utf-8') as f:
    C = json.load(f)

with open('index.html', 'r', encoding='utf-8') as f:
    html_text = f.read()

missing_items = []
present_count = 0

for row in C['rows']:
    sec, elem, content, layout = row
    if sec in ['APPROVED STORYLINE', 'KEPT OFF THE PAGE UNTIL CONFIRMED', 'SEO SETUP']:
        continue
    if content:
        # Check snippet
        snippet = content[:35]
        if snippet in html_text:
            present_count += 1
        else:
            missing_items.append((sec, elem, snippet))

print(f"Total checked: {present_count + len(missing_items)}")
print(f"Present: {present_count}")
print(f"Missing count: {len(missing_items)}")
for m in missing_items:
    print("  Missing:", m)
