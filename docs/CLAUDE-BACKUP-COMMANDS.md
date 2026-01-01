# 🎯 Claude Backup Commands - Quick Reference

## Mac/iOS Shortcut Commands

Copy these to your Shortcuts app or Text Replacement for instant access.

---

## 🔄 RESTORE Commands

### Restore Specific Backup
```
RESTORE PROJECTX1      # Claude backup
RESTORE VACATIONX2     # Claude backup
RESTORE VACATION1      # Manus backup
RESTORE WEBSITE2       # Manus backup
```
The **X** before the number indicates Claude origin.

### Restore Latest Backup
```
RESTORE LATEST
```
Automatically restores the most recent backup (any category, either source).

---

## 💾 BACKUP Commands

### Full Backup & Continue (Claude)
```
BACKUP & CONTINUE
```
Or use the full checkpoint prompt (`cntN` shortcut):
```
Checkpoint: Back up everything in the sandbox to GitHub manus-task-backups. Analyze task context and select appropriate category (SANDBOX, VACATION, WEBSITE, API, DATA, REPORT, PROJECT, RESEARCH, CODE, DESIGN, FINANCE, HEALTH, LEARNING, AUTOMATION, MISC). Create {CATEGORY}X{N} entry in registry.json (X denotes Claude origin). Generate CONTINUATION.md with: (1) contextual shorthand ID, (2) everything done this session, (3) what remains (TODO High/Medium/Low), (4) all file paths, (5) files user must re-upload, (6) environment snapshot, (7) continuation suggestions. Push all sandbox files. Sync to Notion. Return the {CATEGORY}X{N} ID and restore command.
```

**Completion Message Format:**
```
✅ PROJECTX1 backup complete
Source: Claude
Category: PROJECT
Session: "Florence Investor Deck Refinement"
Files: 8 | Size: 2.4MB | TODO: 5 items
Restore: RESTORE PROJECTX1
```

---

## 📋 LIST Commands

### List All Backups
```
LIST BACKUPS
```
Shows all backups from both Claude (X) and Manus:
```
┌─────────────┬─────────────────────────────────┬────────────┬──────────┐
│ ID          │ Name                            │ Date       │ Source   │
├─────────────┼─────────────────────────────────┼────────────┼──────────┤
│ SANDBOX1    │ Backup Skill Setup              │ 2025-12-31 │ Manus    │
│ SANDBOXX1   │ Checkpoint Skill Development    │ 2026-01-01 │ Claude   │
│ VACATION1   │ Hawaii Trip Planning            │ 2026-01-15 │ Manus    │
│ PROJECTX1   │ Investor Deck Refinement        │ 2026-01-01 │ Claude   │
│ APIX1       │ Florence API Integration        │ 2026-01-02 │ Claude   │
└─────────────┴─────────────────────────────────┴────────────┴──────────┘
```

---

## 🏷️ Category Reference

Claude uses the same categories as Manus, with **X** suffix:

| Category | Claude ID | Manus ID | Use For |
|----------|-----------|----------|----------|
| SANDBOX | SANDBOXX1 | SANDBOX1 | System tools, infrastructure |
| VACATION | VACATIONX1 | VACATION1 | Travel, trips, bookings |
| WEBSITE | WEBSITEX1 | WEBSITE1 | Web development |
| API | APIX1 | API1 | API integrations |
| DATA | DATAX1 | DATA1 | Data analysis |
| REPORT | REPORTX1 | REPORT1 | Reports, presentations |
| PROJECT | PROJECTX1 | PROJECT1 | Project management |
| RESEARCH | RESEARCHX1 | RESEARCH1 | Research, investigations |
| CODE | CODEX1 | CODE1 | General coding |
| DESIGN | DESIGNX1 | DESIGN1 | UI/UX, graphics |
| FINANCE | FINANCEX1 | FINANCE1 | Budgets, invoices |
| HEALTH | HEALTHX1 | HEALTH1 | Health tracking |
| LEARNING | LEARNINGX1 | LEARNING1 | Education, courses |
| AUTOMATION | AUTOMATIONX1 | AUTOMATION1 | Workflows |
| MISC | MISCX1 | MISC1 | Everything else |

---

## 📱 iOS/macOS Text Replacements

| Shortcut | Expands To |
|----------|------------|
| `cntN` | Full checkpoint prompt (see above) |
| `rr` | `RESTORE ` |
| `rsl` | `RESTORE LATEST` |
| `lsb` | `LIST BACKUPS` |
| `bkc` | `BACKUP & CONTINUE` |

**Usage:** Type `rr` → expands to `RESTORE ` → then type `PROJECTX1`

---

## 🔗 Resources

- **GitHub:** https://github.com/omarzsalah1/manus-task-backups
- **Notion Database:** https://www.notion.so/1337a26936fd4f4a9e82a30eea20c78d

---

## Quick Reference Card

```
╔═══════════════════════════════════════════════════════════════╗
║        CLAUDE BACKUP SYSTEM - CONTEXTUAL NAMING v4.0          ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  💾 BACKUP                                                    ║
║  ─────────────────────────────────────────────────────────── ║
║  cntN (shortcut)       Full checkpoint → PROJECTX1, etc.     ║
║  BACKUP & CONTINUE     Same as above                          ║
║                                                               ║
║  🔄 RESTORE                                                   ║
║  ─────────────────────────────────────────────────────────── ║
║  RESTORE PROJECTX1     Claude backup (X = Claude)             ║
║  RESTORE VACATION1     Manus backup (no X = Manus)            ║
║  RESTORE LATEST        Most recent (either source)            ║
║                                                               ║
║  📋 LIST                                                      ║
║  ─────────────────────────────────────────────────────────── ║
║  LIST BACKUPS          All backups (both Claude & Manus)      ║
║                                                               ║
║  🏷️ ID FORMAT                                                 ║
║  ─────────────────────────────────────────────────────────── ║
║  Claude: {CATEGORY}X{N}  →  PROJECTX1, APIX2, VACATIONX1     ║
║  Manus:  {CATEGORY}{N}   →  PROJECT1, API2, VACATION1        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

*Claude Checkpoint System v4.0 - Integrated with Manus*