# 🎯 Backup Commands - Quick Reference

## Mac/iOS Shortcut Commands

Copy these to your Shortcuts app for instant access.

---

## 🔄 RESTORE Commands

### Restore Specific Backup
```
RESTORE VACATION1
RESTORE WEBSITE2
RESTORE API1
```
Restores the backup with the specified contextual ID. The ID reflects what the task was about.

### Restore Latest Backup
```
RESTORE LATEST
```
Automatically restores the most recent backup (any category) without needing to remember the ID.

---

## 💾 BACKUP Commands

### Full Backup & Continue
```
BACKUP & CONTINUE
```
Creates a comprehensive backup with:
- **AI-generated contextual ID** (VACATION1, WEBSITE2, API1, etc.) based on what your task is about
- Full sandbox file snapshot
- Environment capture (pip, npm, apt packages)
- TODO/Roadmap tracking
- Notion database entry
- GitHub push

**Completion Message Format:**
```
✅ VACATION1 backup complete
Session: "Hawaii Trip Planning - Flight & Hotel"
Files: 12 | Size: 85KB | TODO: 3 items
Restore: RESTORE VACATION1
```

### Quick Checkpoint
```
CHECKPOINT
```
Fast snapshot without full documentation. Good for mid-task saves.

### Error Recovery Backup
```
ERROR BACKUP
```
Creates a detailed recovery package when something goes wrong.

---

## 📋 LIST Commands

### List All Backups
```
LIST BACKUPS
```
Shows all available backups across all categories:
```
┌────────────┬─────────────────────────────────┬────────────┬──────────┐
│ ID         │ Name                            │ Date       │ Status   │
├────────────┼─────────────────────────────────┼────────────┼──────────┤
│ SANDBOX1   │ Backup Skill Setup              │ 2025-12-31 │ ✅       │
│ SANDBOX2   │ System v2 Enhancement           │ 2025-12-31 │ ✅       │
│ VACATION1  │ Hawaii Trip Planning            │ 2026-01-15 │ 🔄       │
│ WEBSITE1   │ Portfolio Site Redesign         │ 2026-01-10 │ ✅       │
└────────────┴─────────────────────────────────┴────────────┴──────────┘
```

---

## 🏷️ Category Reference

The AI automatically selects the appropriate category based on your task:

| Category | When It's Used | Example ID |
|----------|----------------|------------|
| `SANDBOX` | System tools, Manus configuration, backup infrastructure | SANDBOX1 |
| `VACATION` | Travel planning, flight tickets, hotel bookings, trip itineraries | VACATION1 |
| `WEBSITE` | Web development, site redesign, landing pages | WEBSITE1 |
| `API` | API integrations, backend development, webhooks | API1 |
| `DATA` | Data analysis, spreadsheets, visualizations | DATA1 |
| `REPORT` | Reports, presentations, documents | REPORT1 |
| `EMAIL` | Email campaigns, newsletters, templates | EMAIL1 |
| `MEETING` | Meeting prep, agendas, notes | MEETING1 |
| `PROJECT` | Project management, planning | PROJECT1 |
| `RESEARCH` | Research, investigations, analysis | RESEARCH1 |
| `DESIGN` | UI/UX, graphics, branding | DESIGN1 |
| `CODE` | General coding, scripts | CODE1 |
| `DOCS` | Documentation, guides, manuals | DOCS1 |
| `FINANCE` | Financial tasks, budgets, invoices | FINANCE1 |
| `HEALTH` | Health tracking, wellness, fitness | HEALTH1 |
| `LEARNING` | Courses, tutorials, education | LEARNING1 |
| `AUTOMATION` | Workflow automation, scripts | AUTOMATION1 |
| `MISC` | Anything else | MISC1 |

---

## 📱 iOS/macOS Shortcuts Setup

### Option 1: Text Replacement (Fastest)
1. Go to **Settings > General > Keyboard > Text Replacement**
2. Add these:

| Shortcut | Phrase |
|----------|--------|
| `rr` | `RESTORE ` |
| `rsl` | `RESTORE LATEST` |
| `lsb` | `LIST BACKUPS` |
| `bkc` | `BACKUP & CONTINUE` |

**Usage:** Type `rr` → expands to `RESTORE ` → then type `VACATION1`

### Option 2: Shortcuts App
1. Open **Shortcuts** app
2. Create new shortcut for each command
3. Add action: **Text** → paste command
4. Add action: **Copy to Clipboard**
5. Add to Home Screen or Menu Bar

---

## 📝 Full iOS Shortcut (Copy This)

```
BACKUP & CONTINUE: Create a comprehensive continuation package with AI-generated contextual shorthand ID based on task context (e.g., VACATION1 for travel, WEBSITE2 for web dev, API1 for integrations). Back up ALL sandbox files to GitHub (omarzsalah1/manus-task-backups), generate a detailed CONTINUATION.md with:
1. Contextual shorthand ID (VACATION1, WEBSITE2, API1, etc.) based on what this task is about
2. Explicit details of everything completed
3. What remains to be done (TODO: High/Medium/Low priority)
4. Full file inventory with paths
5. GitHub pull instructions: RESTORE {ID}
6. Environment/dependency capture (pip, npm, apt packages)
7. Notion database sync with full metadata
8. Any suggestions for seamless continuation

Push everything to a dated folder in backups/ directory. Report completion as:
✅ {CATEGORY}{N} backup complete
Session: "[AI-generated descriptive name]"
Files: X | Size: XKB | TODO: X items
Restore: RESTORE {CATEGORY}{N}
```

---

## 🗂️ Current Backups

| ID | Category | Name | Date | Restore Command |
|----|----------|------|------|-----------------|
| SANDBOX1 | SANDBOX | Backup & Continue Skill Setup | 2025-12-31 | `RESTORE SANDBOX1` |
| SANDBOX2 | SANDBOX | System v2.0 Enhancement | 2025-12-31 | `RESTORE SANDBOX2` |

---

## 🔗 Resources

- **GitHub:** https://github.com/omarzsalah1/manus-task-backups
- **Notion Database:** https://www.notion.so/1337a26936fd4f4a9e82a30eea20c78d
- **Notion Parent Page:** https://www.notion.so/2dbff518007781239528f3298aaecd79

---

## How It Works

1. **BACKUP & CONTINUE** → AI analyzes task context
2. **Selects category** → VACATION for travel, WEBSITE for web dev, etc.
3. **Increments category counter** → VACATION1, VACATION2, etc.
4. **Creates dual ID** → Quick ID (VACATION1) + descriptive name
5. **Notion synced** with all metadata
6. **GitHub pushed** automatically

---

*Manus Task Backup System v4.0 - Contextual Naming Edition*
