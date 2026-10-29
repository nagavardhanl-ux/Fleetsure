# -*- coding: utf-8 -*-
"""
Main Builder: Combines all modules and generates index.html
"""

import json
from css_styles import get_css
import sections_html
import sections_html_part1
import sections_html_part2
import sections_html_part3
from app_js import get_js

# Load content
with open('fleetsure_structured.json', 'r', encoding='utf-8') as f:
    C = json.load(f)

with open('site_schema.json', 'r', encoding='utf-8') as f:
    schema_json_ld = f.read()

# Extract 12 FAQs
faqs = []
for i in range(1, 13):
    q = C['13. FAQ'][f'FAQ {i} - Question']['content']
    a = C['13. FAQ'][f'FAQ {i} - Answer']['content']
    faqs.append({"q": q, "a": a})

title = C['SEO SETUP']['Title tag']['content']
meta_desc = C['SEO SETUP']['Meta description']['content']
og_title = C['SEO SETUP']['OG title']['content']
og_desc = C['SEO SETUP']['OG description']['content']
canonical_url = "https://" + C['SEO SETUP']['URL']['content']

html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_desc}">
  
  <!-- Keywords -->
  <meta name="keywords" content="fleet compliance software, fleet compliance management, vehicle compliance management, challan management software, vehicle document management software, fleet document tracking, vehicle document expiry alerts, RC insurance PUC tracking, driver licence expiry tracking, road tax renewal, fleet compliance dashboard, multi-location fleet management, challan tracking across states">

  <!-- Open Graph -->
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{og_desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical_url}">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
{schema_json_ld}
  </script>

  <style>
{get_css()}
  </style>
</head>
<body>

  {sections_html.get_header_html()}

  <main>
    {sections_html.get_hero_html(C)}
    {sections_html_part1.get_problem_html(C)}
    {sections_html_part1.get_shift_html(C)}
    {sections_html_part1.get_how_it_works_html(C)}
    {sections_html_part2.get_glance_html(C)}
    {sections_html_part2.get_teams_html(C)}
    {sections_html_part2.get_alerts_html(C)}
    {sections_html_part2.get_challans_html(C)}
    {sections_html_part2.get_systems_html(C)}
    {sections_html_part3.get_views_html(C)}
    {sections_html_part3.get_compare_html(C)}
    {sections_html_part3.get_included_html(C)}
    {sections_html_part3.get_faq_html(C, faqs)}
    {sections_html_part3.get_final_cta_html(C)}
  </main>

  {sections_html_part3.get_footer_html(C)}

  {sections_html_part3.get_modals_html()}

  <script>
{get_js()}
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_doc)

print(f"Successfully generated index.html (size: {len(html_doc)} bytes)")
