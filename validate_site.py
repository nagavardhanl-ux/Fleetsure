# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print(f"Title: {soup.title.string}")

expected_ids = [
    'hero',
    'problem',
    'the-shift',
    'how-it-works',
    'fleet-at-a-glance',
    'three-teams',
    'expiry-alerts',
    'challans',
    'integrations',
    'reporting',
    'compliance-vs-gps',
    'included',
    'faq',
    'contact'
]

print("\n--- CHECKING SECTION IDS ---")
for eid in expected_ids:
    el = soup.find(id=eid)
    if el:
        h_tag = el.find(['h1', 'h2'])
        h_text = h_tag.get_text().strip() if h_tag else "No H1/H2"
        # truncate for clean log
        print(f"  [OK] #{eid}: {h_text[:60]}")
    else:
        print(f"  [MISSING] #{eid}")

print("\n--- CHECKING FAQS ---")
faq_items = soup.find_all('details', class_='faq-item')
print(f"Found {len(faq_items)} FAQ items")
for idx, item in enumerate(faq_items, 1):
    q = item.find('summary').find('span').get_text().strip()
    print(f"  {idx}. {q[:70]}")

print("\n--- CHECKING SCRIPTS & MODALS ---")
demo_modal = soup.find(id='demo-modal')
veh_modal = soup.find(id='vehicle-modal')
print("Demo modal exists:", demo_modal is not None)
print("Vehicle modal exists:", veh_modal is not None)

scripts = soup.find_all('script')
print(f"Total script tags: {len(scripts)}")
