# Manus Backup & Continue Trigger Phrases v3.0

**Version**: 3.0 (Protocol v6.0)  
**Date**: January 1, 2026

---

## Primary Trigger Phrase

```
BACKUP & CONTINUE: Execute the Manus Backup Protocol v6.0:

1. CONTEXTUAL ID: Generate AI-based shorthand (BOOK1, VACATION1, WEBSITE1, etc.) based on task context
2. FOLDER NAME: Use format "YYYY-MM-DD_descriptive-slug" (e.g., 2025-12-31_gatekeepers-v37-fixes) - NO timestamps, NO "BACKUP_" prefix
3. DESTINATION: GitHub repo omarzsalah1/manus-task-backups in backups/ directory
4. REGISTRY: Update sessions/registry.json with new entry (increment category counter, add github_url and notion_url)
5. NOTION: Create record in database "Manus Task Backups" (ID: 33e63115-e073-4137-8f07-318660d56d09) with properties: Backup ID, Session Name, Status, Category, Date, Files, Size, TODO Items, GitHub Path, Restore Command

CONTINUATION.md must include (v3.0 template):
- Contextual shorthand ID
- Everything completed (detailed)
- TODO remaining (High/Medium/Low priority with tables)
- Full file inventory with paths
- Environment capture (pip, npm, apt)
- 🆕 MISTAKES & LESSONS LEARNED (what went wrong, failed approaches, time sinks)
- 🆕 USER INSTRUCTIONS & PREFERENCES (explicit instructions, discovered preferences, decision points)
- 🆕 INSIGHTS & DISCOVERIES (technical insights, domain knowledge, best practices, patterns)
- 🆕 DECISION LOG (all decisions with options, rationale, user approval)
- 🆕 BLOCKERS & WARNINGS (known issues, anti-patterns, edge cases, future problems)
- 🆕 COMMUNICATION SUMMARY (key Q&A, scope changes, clarifications, feedback)

COMPLETION MESSAGE FORMAT (MANDATORY):
✅ {ID} backup complete
Session: "{Descriptive Name}"
Files: X | Size: XKB | TODO: X items
Restore: RESTORE {ID}
GitHub: https://github.com/omarzsalah1/manus-task-backups/tree/master/backups/{FOLDER_NAME}
Notion: {notion_page_url}
```

---

## Restore Commands

### Quick Restore
```
RESTORE {ID}
```
Examples:
- `RESTORE BOOK1`
- `RESTORE SANDBOX2`
- `RESTORE VACATION1`

### Restore Latest
```
RESTORE LATEST
```

### List All Backups
```
LIST BACKUPS
```

---

## Utility Commands

### Show Backup Status
```
BACKUP STATUS
```

### Show Session Registry
```
LIST SESSIONS
```

### Cross-AI Restore (for Claude ↔ Manus)
```
CROSS-RESTORE: Claude Sandbox={CLAUDE_ID} Manus Sandbox={MANUS_ID} Task: {description}
```

---

## What's New in v3.0 (Protocol v6.0)

### 7 New Mandatory Sections

1. **Mistakes & Lessons Learned**
   - What went wrong during the task
   - Failed approaches that were tried
   - Time sinks to avoid in future

2. **User Instructions & Preferences**
   - Explicit instructions given by user
   - Implicit preferences discovered
   - Key decision points with user choices

3. **Insights & Discoveries**
   - Technical insights gained
   - Domain knowledge acquired
   - Best practices learned
   - Patterns identified

4. **Decision Log**
   - All significant decisions
   - Options that were considered
   - Rationale for choices
   - Whether user approved

5. **Blockers & Warnings**
   - Known issues not yet resolved
   - Anti-patterns to avoid
   - Edge cases discovered
   - Potential future problems

6. **Communication Summary**
   - Key questions from user and answers
   - Scope changes during task
   - Important clarifications
   - User feedback received

7. **Enhanced Roadmap Tables**
   - Estimated time for each TODO
   - Dependencies between items
   - Acceptance criteria
   - Risk factors

---

## Categories for Contextual IDs

| Category | Use For | Example ID |
|----------|---------|------------|
| BOOK | Book production, manuscripts | BOOK1 |
| VACATION | Travel planning, itineraries | VACATION1 |
| WEBSITE | Web development, sites | WEBSITE1 |
| API | API development, integrations | API1 |
| DATA | Data analysis, processing | DATA1 |
| REPORT | Reports, documents | REPORT1 |
| EMAIL | Email automation, campaigns | EMAIL1 |
| MEETING | Meeting prep, notes | MEETING1 |
| PROJECT | General projects | PROJECT1 |
| RESEARCH | Research tasks | RESEARCH1 |
| DESIGN | Design work | DESIGN1 |
| CODE | Coding projects | CODE1 |
| DOCS | Documentation | DOCS1 |
| FINANCE | Financial tasks | FINANCE1 |
| HEALTH | Health-related | HEALTH1 |
| TRAVEL | Travel logistics | TRAVEL1 |
| SHOPPING | Shopping, procurement | SHOPPING1 |
| LEARNING | Learning, courses | LEARNING1 |
| AUTOMATION | Automation tasks | AUTOMATION1 |
| SANDBOX | System/infrastructure | SANDBOX1 |
| MISC | Miscellaneous | MISC1 |

---

## Example Usage

### Starting a Backup
```
BACKUP & CONTINUE: Execute the Manus Backup Protocol v6.0...
```

### Restoring a Session
```
RESTORE BOOK1
```

### Expected Output
```
✅ BOOK1 backup complete
Session: "Gatekeepers Society V37 Fixes & Production"
Files: 59 | Size: 152M | TODO: 3 items
Restore: RESTORE BOOK1
GitHub: https://github.com/omarzsalah1/manus-task-backups/tree/master/backups/2025-12-31_gatekeepers-v37-fixes
Notion: https://www.notion.so/2dbff518007781459475fee55b710c56
```

---

## Version History

| Version | Protocol | Changes |
|---------|----------|---------|
| 3.0 | v6.0 | Added 7 institutional knowledge sections |
| 2.0 | v5.1 | Added contextual naming, Notion integration |
| 1.0 | v5.0 | Initial trigger phrase system |

---

*Manus Backup Protocol v6.0 - Preserving Institutional Knowledge*
