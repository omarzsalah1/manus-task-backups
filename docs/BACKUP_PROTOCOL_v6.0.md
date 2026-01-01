# Manus Backup Protocol v6.0

**Version**: 6.0  
**Date**: January 1, 2026  
**Status**: PROPOSED  
**Previous Version**: 5.1

---

## Overview

The Manus Backup Protocol v6.0 enhances the backup system with **Institutional Knowledge Capture** - ensuring that insights, mistakes, user instructions, and detailed roadmaps are preserved alongside files and environment state.

---

## What's New in v6.0

### New Mandatory Sections in CONTINUATION.md

| Section | Purpose | v5.1 | v6.0 |
|---------|---------|------|------|
| Mistakes & Lessons Learned | Capture what went wrong and why | ❌ | ✅ |
| User Instructions & Preferences | Document explicit/implicit user guidance | ❌ | ✅ |
| Insights & Discoveries | Technical and domain knowledge gained | ❌ | ✅ |
| Detailed Roadmap (with tables) | Est. time, dependencies, acceptance criteria | Partial | ✅ |
| Decision Log | All decisions with rationale | ❌ | ✅ |
| Blockers & Warnings | Known issues, anti-patterns, edge cases | Partial | ✅ |
| Communication Summary | Key Q&A, scope changes, feedback | ❌ | ✅ |

---

## Trigger Phrase

```
BACKUP & CONTINUE: Execute the Manus Backup Protocol v6.0
```

---

## Protocol Steps

### Step 1: CONTEXTUAL ID
Generate AI-based shorthand ID based on task context:
- Format: `{CATEGORY}{N}` (e.g., BOOK1, VACATION1, WEBSITE1)
- Categories: BOOK, VACATION, WEBSITE, API, DATA, REPORT, EMAIL, MEETING, PROJECT, RESEARCH, DESIGN, CODE, DOCS, FINANCE, HEALTH, TRAVEL, SHOPPING, LEARNING, AUTOMATION, SANDBOX, MISC
- Increment counter in registry.json

### Step 2: FOLDER NAME
Create backup folder with format:
- `YYYY-MM-DD_descriptive-slug`
- Example: `2025-12-31_gatekeepers-v37-fixes`
- NO timestamps, NO "BACKUP_" prefix

### Step 3: DESTINATION
Push to GitHub repository:
- Repo: `omarzsalah1/manus-task-backups`
- Path: `backups/{FOLDER_NAME}/`

### Step 4: REGISTRY UPDATE
Update `sessions/registry.json`:
```json
{
  "shorthand_id": "BOOK1",
  "source": "manus",
  "category": "BOOK",
  "session_name": "Descriptive Session Name",
  "created_date": "2025-12-31",
  "backup_folder": "2025-12-31_descriptive-slug",
  "status": "complete|active|incomplete",
  "github_url": "https://github.com/...",
  "notion_url": "https://www.notion.so/...",
  "files_count": 59,
  "total_size": "152M",
  "todo_items": 3,
  "completion_pct": 0.85
}
```

### Step 5: NOTION RECORD
Create/update record in Notion database "Manus Task Backups":
- Database ID: `33e63115-e073-4137-8f07-318660d56d09`
- Properties: Backup ID, Session Name, Status, Category, Date, Files, Size, TODO Items, GitHub Path, Restore Command, Completion %

### Step 6: CONTINUATION.md (v3.0 Template)
Create comprehensive CONTINUATION.md with ALL sections:

#### Required Sections (v6.0)

1. **Header** - Session ID, Name, Date, Type, GitHub, Notion
2. **Quick Restore** - One-command and manual restore instructions
3. **Task Objective** - Clear statement of goal
4. **Completed Work** - Detailed by phase
5. **🆕 Detailed Roadmap** - Tables with Est. Time, Dependencies, Acceptance Criteria, Risk
6. **🆕 Mistakes & Lessons Learned** - What went wrong, failed approaches, time sinks
7. **🆕 User Instructions & Preferences** - Explicit instructions, discovered preferences, decision points
8. **🆕 Insights & Discoveries** - Technical insights, domain knowledge, best practices, patterns
9. **🆕 Decision Log** - All decisions with options, rationale, user approval
10. **🆕 Blockers & Warnings** - Known issues, anti-patterns, edge cases, future problems
11. **🆕 Communication Summary** - Key Q&A, scope changes, clarifications, feedback
12. **File Inventory** - Project files, config, assets, key files
13. **Environment Snapshot** - Python, Node, System packages, env vars
14. **External Resources** - APIs, docs, related sessions
15. **Continuation Suggestions** - First steps, what to review, pitfalls, alternatives
16. **Session Metadata** - Stats table
17. **Context for AI Continuation** - Task context, accomplishments, user needs, success factors, issues to watch
18. **Quick Reference** - Summary block

### Step 7: ENVIRONMENT CAPTURE
Run environment capture scripts:
```bash
pip3 freeze > requirements.txt
npm list -g --depth=0 > npm-global-packages.txt
dpkg --get-selections | grep -v deinstall > apt-packages.txt
```

### Step 8: COMPLETION MESSAGE
Output in mandatory format:
```
✅ {ID} backup complete
Session: "{Descriptive Name}"
Files: X | Size: XKB | TODO: X items
Restore: RESTORE {ID}
GitHub: https://github.com/omarzsalah1/manus-task-backups/tree/master/backups/{FOLDER_NAME}
Notion: {notion_page_url}
```

---

## Restore Protocol

### Quick Restore
```
RESTORE {ID}
```

### What Restore Does
1. Clone/pull backup repository
2. Copy sandbox files to home directory
3. Run restore-env.sh to reinstall packages
4. Display confirmation with TODO summary

---

## Institutional Knowledge Capture Guidelines

### Mistakes & Lessons Learned
**Capture these during the task:**
- Every error message and its resolution
- Approaches that didn't work
- Time spent on dead ends
- Root causes discovered

**Format:**
| Mistake | What Happened | Lesson Learned | Time Lost |
|---------|---------------|----------------|-----------|
| Edited PDF directly | Changes didn't persist | Must edit source markdown, then rebuild | 30 min |

### User Instructions & Preferences
**Capture these during the task:**
- Explicit instructions given by user
- Implicit preferences discovered
- Style/format preferences
- Priority preferences

**Format:**
| Preference | How Discovered | Application |
|------------|----------------|-------------|
| Prefers V32 design aesthetic | User mentioned "match V32 quality" | Use antique gold, specific typography |

### Insights & Discoveries
**Capture these during the task:**
- Technical solutions found
- Workarounds discovered
- Best practices learned
- Patterns identified

**Format:**
| Insight | Context | Future Application |
|---------|---------|-------------------|
| WeasyPrint needs PNG not SVG | Clock-star images failed | Always convert SVG to PNG before build |

### Decision Log
**Capture these during the task:**
- Every significant decision
- Options considered
- Why the choice was made
- Whether user approved

**Format:**
| Date | Decision | Options Considered | Rationale | User Approved |
|------|----------|-------------------|-----------|---------------|
| 12/31 | Use 300 DPI | 150 DPI (smaller), 300 DPI (print quality) | User prioritizes print | Yes |

---

## Migration from v5.1 to v6.0

### For Existing Backups
1. Existing CONTINUATION.md files remain valid
2. New backups will use v3.0 template
3. No retroactive updates required

### For New Backups
1. Use v3.0 template for CONTINUATION.md
2. Include all 7 new sections
3. Use table format for structured data

---

## Validation Checklist

Before completing backup, verify:

- [ ] Contextual ID generated and counter incremented
- [ ] Folder name follows format (no timestamps, no BACKUP_ prefix)
- [ ] All files copied to backup folder
- [ ] CONTINUATION.md includes ALL 18 sections
- [ ] Mistakes & Lessons section populated (if any)
- [ ] User Instructions section populated
- [ ] Insights section populated
- [ ] Decision Log populated
- [ ] Blockers & Warnings section populated
- [ ] Communication Summary populated
- [ ] Registry.json updated
- [ ] Notion record created/updated
- [ ] GitHub push successful
- [ ] Completion message in correct format

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 6.0 | 2026-01-01 | Added 7 institutional knowledge sections |
| 5.1 | 2025-12-31 | Added contextual naming, Notion integration |
| 5.0 | 2025-12-31 | Added environment capture, restore scripts |
| 4.0 | 2025-12-31 | Added registry.json, dual ID system |
| 3.0 | 2025-12-30 | Added TODO tracking |
| 2.0 | 2025-12-30 | Added GitHub integration |
| 1.0 | 2025-12-29 | Initial version |

---

*Manus Backup Protocol v6.0 - Preserving Institutional Knowledge*
