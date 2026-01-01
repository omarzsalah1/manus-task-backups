# Manus Task Backups v4.1

**Unified backup and continuation system for Manus AI and Claude AI tasks.**

This repository stores sandbox snapshots, environment configurations, and continuation prompts for seamless task resumption across sessions.

## 🆕 What's New in v4.1

- **Contextual Naming:** AI-generated category IDs (VACATION1, WEBSITE2, API1, etc.)
- **Unified System:** Both Manus and Claude backups in one repo
- **Source Identification:** Manus = `{CATEGORY}{N}`, Claude = `{CATEGORY}X{N}`
- **Multi-Category Counters:** Each category tracks its own sequence
- **Notion Integration:** Automatic documentation and TODO task creation
- **Environment Capture:** Full pip, npm, and apt package snapshots

## 🏷️ ID Convention

| Source | Format | Examples |
|--------|--------|----------|
| **Manus** | `{CATEGORY}{N}` | VACATION1, PROJECT2, API1 |
| **Claude** | `{CATEGORY}X{N}` | VACATIONX1, PROJECTX2, APIX1 |

The **X** before the number denotes Claude origin.

## 📂 Available Categories

| Category | Use For |
|----------|---------|
| `SANDBOX` | System tools, backup infrastructure |
| `VACATION` | Travel planning, trips, bookings |
| `WEBSITE` | Web development, landing pages |
| `API` | API integrations, webhooks |
| `DATA` | Data analysis, spreadsheets |
| `REPORT` | Reports, presentations |
| `PROJECT` | Project management, planning |
| `RESEARCH` | Research, investigations |
| `CODE` | General coding, scripts |
| `DESIGN` | UI/UX, graphics, branding |
| `FINANCE` | Budgets, invoices, expenses |
| `HEALTH` | Health tracking, wellness |
| `LEARNING` | Education, courses |
| `AUTOMATION` | Workflow automation |
| `MISC` | Everything else |

## 🚀 Commands

| Command | Description |
|---------|-------------|
| `BACKUP & CONTINUE` | Full backup with AI-selected category |
| `RESTORE VACATION1` | Restore specific Manus backup |
| `RESTORE VACATIONX1` | Restore specific Claude backup |
| `RESTORE LATEST` | Restore most recent (any source) |
| `LIST BACKUPS` | Show all available backups |

## 📁 Repository Structure

```
manus-task-backups/
├── backups/                          # Task backup folders
│   └── YYYY-MM-DD_session-name/      # Individual task backup
│       ├── sandbox/                  # Full sandbox file snapshot
│       ├── CONTINUATION.md           # Detailed continuation prompt
│       ├── manifest.json             # File inventory and metadata
│       └── restore-env.sh            # Environment restoration script
├── sessions/
│   └── registry.json                 # Multi-category counter registry
├── docs/
│   ├── BACKUP-COMMANDS.md            # Manus quick reference
│   └── CLAUDE-BACKUP-COMMANDS.md     # Claude quick reference
├── config/
│   └── notion-integration.json       # Notion sync settings
└── templates/
    └── continuation-template-v2.md   # CONTINUATION.md template
```

## 📥 How to Resume a Task

### Restore Command
```
RESTORE VACATION1      # Manus backup
RESTORE VACATIONX1     # Claude backup
RESTORE LATEST         # Most recent
```

### Manual Restoration
```bash
gh repo clone omarzsalah1/manus-task-backups ~/manus-task-backups
cp -r ~/manus-task-backups/backups/[backup-folder]/sandbox/* ~/
```

## ⌨️ iOS/macOS Shortcuts

| Shortcut | Expands To |
|----------|------------|
| `rr` | `RESTORE ` |
| `rsl` | `RESTORE LATEST` |
| `lsb` | `LIST BACKUPS` |
| `bkc` | `BACKUP & CONTINUE` |
| `cntN` | Full Claude checkpoint prompt |

## 🔗 Resources

- **GitHub:** https://github.com/omarzsalah1/manus-task-backups
- **Notion Database:** https://www.notion.so/1337a26936fd4f4a9e82a30eea20c78d
- **Notion Parent:** https://www.notion.so/2dbff518007781239528f3298aaecd79

---

*Unified Backup System v4.1 - Manus + Claude Integration*
