#!/usr/bin/env python3
"""Build V37 MASTER from GitHub chapters with all assets"""

from pathlib import Path

chapters = [
    'GK_CH00_Introduction/GK_CH00_Introduction_FINAL.md',
    'GK_CH01_Sacred_Hour/GK_CH01_Sacred_Hour_FINAL.md',
    'GK_CH02_The_Vacation_Wars/GK_CH02_Vacation_Wars_FINAL.md',
    'GK_CH03_Breaking_Point/GK_CH03_Breaking_Point_FINAL.md',
    'GK_CH04_Crisis_Day/GK_CH04_Crisis_Day_FINAL.md',
    'GK_CH05_Handoff/GK_CH05_Handoff_FINAL.md',
    'GK_CH06_Playbook/GK_CH06_Playbook_FINAL.md',
    'GK_CH07_Bodys_Needs/GK_CH03_Bodys_Needs_FINAL.md',
    'GK_CH08_Machinery_of_Access/GK_CH08_Machinery_of_Access_FINAL.md',
    'GK_CH09_Family_Firewall/GK_CH04_Family_Firewall_FINAL.md',
    'GK_CH10_Guilty_Pleasures/GK_CH05_Guilty_Pleasures_FINAL.md',
    'GK_CH11_Conclusion/GK_CH08_Conclusion_FINAL.md',
    'GK_CH12_Weight_of_Friendship/GK_CH12_Weight_of_Friendship_FINAL.md'
]

github_base = Path('/home/ubuntu/Gatekeepers_REPO/book_source/chapters')
output_file = Path('/home/ubuntu/V37_FINAL/THE_GATEKEEPERS_SOCIETY_V37_MASTER.md')

print("Building V37 MASTER from GitHub chapters...")
print("=" * 70)

master_content = []
for i, chapter_path in enumerate(chapters, 1):
    full_path = github_base / chapter_path
    print(f"{i:2d}. {chapter_path}")
    
    if not full_path.exists():
        print(f"    ❌ ERROR: File not found!")
        continue
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    master_content.append(content)
    master_content.append('\n\n')
    
    # Count assets
    portraits = content.count('<div class="portrait">')
    diagrams = content.count('{{INSERT:')
    tables = content.count('|')
    
    print(f"    ✅ {len(content):,} chars | {portraits} portraits | {diagrams} diagrams | {tables} table lines")

# Write master file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(master_content))

print("=" * 70)
print(f"✅ V37 MASTER created: {output_file}")
print(f"   Total size: {output_file.stat().st_size:,} bytes")

# Count total assets
with open(output_file, 'r') as f:
    full_content = f.read()
    total_portraits = full_content.count('<div class="portrait">')
    total_diagrams = full_content.count('![')
    total_tables = full_content.count('|')
    
print(f"   📊 Total portraits: {total_portraits}")
print(f"   📊 Total images: {total_diagrams}")
print(f"   📊 Total table lines: {total_tables}")
