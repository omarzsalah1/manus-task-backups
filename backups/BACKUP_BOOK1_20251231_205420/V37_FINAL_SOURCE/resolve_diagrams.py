#!/usr/bin/env python3
"""Resolve diagram INSERT markers with actual image references"""

from pathlib import Path

# Diagram INSERT mappings
DIAGRAM_MAP = {
    '{{INSERT:KUMAR_TAXONOMY}}': '![Kumar Taxonomy Ring](../Gatekeepers_REPO/images/scheduling_artifacts/VIZ_1.1_Kumar_Taxonomy_Ring.png)',
    '{{INSERT:REQUEST_FUNNEL}}': '![Request Funnel](../Gatekeepers_REPO/images/scheduling_artifacts/VIZ_4.1_Request_Funnel.png)',
    '{{INSERT:TRUMP_ANALYSIS}}': '''![Trump Schedule Analysis - Pie Chart](../Gatekeepers_REPO/images/scheduling_artifacts/VIZ_2.1A_Trump_Schedule_Pie.png)

![Trump Late Night Tweets - Bar Chart](../Gatekeepers_REPO/images/scheduling_artifacts/VIZ_2.1B_LateNight_Tweet_Bar.png)

![Administration Comparison Table](../Gatekeepers_REPO/images/scheduling_artifacts/VIZ_2.2_Admin_Comparison_Table.png)''',
    '{{INSERT:REAGAN_PHOTO}}': '![President Reagan Recovery](../Gatekeepers_REPO/images/scheduling_artifacts/Reagan_Recovery_Pencil_FINAL.png)',
    '{{INSERT:FOUR_ERAS}}': '![Four Eras Timeline](../Gatekeepers_REPO/images/scheduling_artifacts/VIZ_5.1_Four_Eras_Timeline.png)',
    '{{INSERT:BIDEN_PHOTO}}': '![President Biden PDB](../Gatekeepers_REPO/images/scheduling_artifacts/Biden_PDB_Pencil_CORRECTED.png)',
    '{{INSERT:CIRCADIAN_RHYTHM}}': '![Circadian Function Line](../Gatekeepers_REPO/images/scheduling_artifacts/VIZ_3.1_Circadian_Function_Line.png)',
    '{{INSERT:DECISION_FATIGUE}}': '![Decision Fatigue Index](../Gatekeepers_REPO/images/scheduling_artifacts/VIZ_6.1_Decision_Fatigue_Index.png)',
}

master_file = Path('/home/ubuntu/V37_FINAL/THE_GATEKEEPERS_SOCIETY_V37_MASTER.md')

print("Resolving diagram INSERT markers...")
print("=" * 70)

with open(master_file, 'r') as f:
    content = f.read()

replacements = 0
for marker, image_ref in DIAGRAM_MAP.items():
    if marker in content:
        content = content.replace(marker, image_ref)
        replacements += 1
        print(f"✅ Resolved: {marker}")

with open(master_file, 'w') as f:
    f.write(content)

print("=" * 70)
print(f"✅ Resolved {replacements} diagram markers")

# Check for remaining markers
remaining = content.count('{{INSERT:')
if remaining > 0:
    print(f"⚠️  {remaining} unresolved markers remaining")
else:
    print("✅ All markers resolved!")
