# 📋 Full Implementation Plan: Manus Backup & Restore System v3.0

## Table of Contents
1. [System Overview](#1-system-overview)
2. [Architecture](#2-architecture)
3. [AI-Generated Shorthand Task Title Mechanism](#3-ai-generated-shorthand-task-title-mechanism)
4. [Backup Workflow](#4-backup-workflow)
5. [Restore Workflow](#5-restore-workflow)
6. [List Workflow](#6-list-workflow)
7. [File Structure](#7-file-structure)
8. [Notion Database Schema](#8-notion-database-schema)
9. [Command Reference](#9-command-reference)
10. [iOS/macOS Shortcuts](#10-iosmacos-shortcuts)
11. [Quick Reference Card](#11-quick-reference-card)

---

## 1. System Overview

The Manus Backup & Restore System provides seamless task continuity across sessions through:

- **Auto-generated shorthand IDs** (SANDBOX1, SANDBOX2, etc.)
- **Full sandbox file backup** to GitHub
- **Environment capture & restoration** (pip, npm, apt packages)
- **Notion integration** for structured documentation
- **TODO/Roadmap tracking** for incomplete work
- **Simple restore commands** for Mac/iOS Shortcuts

### Key Benefits

| Feature | Benefit |
|---------|---------|
| SANDBOX IDs | Easy to remember, type, and share |
| Dual ID System | Quick access (SANDBOX2) + descriptive name |
| Environment Capture | Full restoration including all packages |
| Notion Sync | Searchable, filterable backup database |
| TODO Tracking | Never lose track of incomplete work |
| One-Command Restore | `RESTORE SANDBOX2` - that's it |

---

## 2. Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER INTERFACE                               │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────────────┐ │
│  │ BACKUP &    │  │ RESTORE      │  │ LIST SANDBOXES          │ │
│  │ CONTINUE    │  │ SANDBOX{N}   │  │                         │ │
│  └──────┬──────┘  └──────┬───────┘  └────────────┬────────────┘ │
└─────────┼────────────────┼──────────────────────┼───────────────┘
          │                │                      │
          ▼                ▼                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                     MANUS AI PROCESSING                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 1. Parse command (BACKUP/RESTORE/LIST)                      ││
│  │ 2. Read registry.json for session data                      ││
│  │ 3. Execute appropriate workflow                             ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
          │                │                      │
          ▼                ▼                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                     STORAGE LAYER                                │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │ GitHub Repo     │  │ Notion Database │  │ Local Registry  │  │
│  │ manus-task-     │  │ Backup Sessions │  │ registry.json   │  │
│  │ backups         │  │ Registry        │  │                 │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **User triggers command** → Manus parses intent
2. **Manus reads registry** → Gets session data and counter
3. **Executes workflow** → Backup/Restore/List
4. **Updates storage** → GitHub + Notion + Registry
5. **Reports to user** → Confirmation with details

---

## 3. AI-Generated Shorthand Task Title Mechanism

### 3.1 ID Generation Process

When `BACKUP & CONTINUE` is triggered:

```
Step 1: Read registry.json
        → Get current counter: next_sandbox_number = 3

Step 2: Generate shorthand ID
        → shorthand_id = "SANDBOX" + counter = "SANDBOX3"

Step 3: AI generates descriptive session name
        → Analyze task context, objectives, and work done
        → Generate concise name: "API Integration Project"

Step 4: Increment counter
        → next_sandbox_number = 4 (saved to registry)

Step 5: Create dual-ID entry
        → shorthand_id: "SANDBOX3"
        → session_id: "api-integration-project"
        → session_name: "API Integration Project"
```

### 3.2 Registry Structure

```json
{
  "schema_version": "3.0",
  "counter": {
    "next_sandbox_number": 3,
    "description": "Auto-incrementing, never decreases"
  },
  "sessions": [
    {
      "shorthand_id": "SANDBOX1",
      "session_id": "continuation-skill-v1",
      "session_name": "Backup & Continue Skill Setup",
      "created_date": "2025-12-31",
      "backup_folder": "2025-12-31_continuation-skill-setup",
      "status": "complete",
      "total_files": 6,
      "todo_count": 0
    },
    {
      "shorthand_id": "SANDBOX2",
      "session_id": "backup-system-v2-enhancement",
      "session_name": "Backup & Continue System v2.0 Enhancement",
      "created_date": "2025-12-31",
      "backup_folder": "2025-12-31_backup-system-v2-enhancement",
      "status": "complete",
      "total_files": 15,
      "todo_count": 8
    }
  ],
  "commands": {
    "restore": "RESTORE SANDBOX{N}",
    "restore_latest": "RESTORE LATEST",
    "list": "LIST SANDBOXES",
    "backup": "BACKUP & CONTINUE"
  }
}
```

### 3.3 Collision Prevention

The counter in `registry.json`:
- **Never decreases** - only increments
- **Persists across sessions** - stored in GitHub
- **Pulled before each backup** - ensures latest counter
- **Atomic increment** - backup fails if push fails

---

## 4. Backup Workflow

### 4.1 Trigger Command

```
BACKUP & CONTINUE
```

### 4.2 Full Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ BACKUP & CONTINUE WORKFLOW                                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. GENERATE IDs                                                 │
│     ├─ Read counter from registry.json                          │
│     ├─ Create shorthand: SANDBOX{N}                             │
│     ├─ AI generates descriptive session_name                    │
│     └─ Increment counter                                        │
│                                                                  │
│  2. CREATE BACKUP FOLDER                                         │
│     └─ backups/{DATE}_{session_id}/                             │
│         ├─ sandbox/           (all user files)                  │
│         ├─ CONTINUATION.md    (restore prompt)                  │
│         ├─ manifest.json      (file inventory)                  │
│         ├─ environment.json   (packages list)                   │
│         └─ restore-env.sh     (restoration script)              │
│                                                                  │
│  3. CAPTURE ENVIRONMENT                                          │
│     ├─ pip3 freeze > requirements.txt                           │
│     ├─ npm list --json > package-list.json                      │
│     └─ dpkg --get-selections > apt-packages.txt                 │
│                                                                  │
│  4. COPY SANDBOX FILES                                           │
│     └─ cp -r /home/ubuntu/* → backup/sandbox/                   │
│         (excluding .git, .nvm, .cache, node_modules)            │
│                                                                  │
│  5. GENERATE CONTINUATION.md                                     │
│     ├─ Task objective                                           │
│     ├─ Completed work summary                                   │
│     ├─ TODO/Roadmap (High/Medium/Low priority)                  │
│     ├─ File inventory table                                     │
│     ├─ Environment snapshot                                     │
│     └─ Restore command: RESTORE SANDBOX{N}                      │
│                                                                  │
│  6. UPDATE REGISTRY                                              │
│     └─ Add new session entry to sessions[]                      │
│                                                                  │
│  7. SYNC TO NOTION                                               │
│     └─ Create database entry with all metadata                  │
│                                                                  │
│  8. PUSH TO GITHUB                                               │
│     └─ git add -A && git commit && git push                     │
│                                                                  │
│  9. REPORT COMPLETION                                            │
│     ┌─────────────────────────────────────────────────────────┐ │
│     │ ✅ SANDBOX3 backup complete                              │ │
│     │ Session: "API Integration Project"                       │ │
│     │ Files: 25 | Size: 150KB | TODO: 5 items                  │ │
│     │ Restore: RESTORE SANDBOX3                                │ │
│     └─────────────────────────────────────────────────────────┘ │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 4.3 CONTINUATION.md Template

```markdown
# 🔄 CONTINUATION PROMPT

**SANDBOX{N}** | `{session_id}`  
**Session Name:** {session_name}  
**Backup Date:** {date}  
**GitHub:** {github_url}  
**Notion:** {notion_url}

---

## 📋 QUICK RESTORE

RESTORE SANDBOX{N}

---

## 🎯 TASK OBJECTIVE

{AI-generated summary of what this task aimed to accomplish}

---

## ✅ COMPLETED WORK

1. {Completed item 1}
2. {Completed item 2}
3. {Completed item 3}

---

## 🔲 TODO

### High Priority
- [ ] {High priority item 1}
- [ ] {High priority item 2}

### Medium Priority
- [ ] {Medium priority item 1}

### Low Priority
- [ ] {Low priority item 1}

---

## 📁 FILES

| File | Description |
|------|-------------|
| `file1.py` | Main application code |
| `config.json` | Configuration settings |

---

## 🔧 ENVIRONMENT

- **Python Packages:** {count}
- **Node Packages:** {count}
- **System Packages:** {list}

---

**🚀 To restore: `RESTORE SANDBOX{N}`**
```

---

## 5. Restore Workflow

### 5.1 Trigger Commands

```
RESTORE SANDBOX2      # Restore specific backup
RESTORE LATEST        # Restore most recent backup
```

### 5.2 Full Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ RESTORE SANDBOX{N} WORKFLOW                                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. PARSE COMMAND                                                │
│     ├─ Extract N from "RESTORE SANDBOX{N}"                      │
│     └─ If "RESTORE LATEST" → get highest N from registry        │
│                                                                  │
│  2. CLONE/PULL REPOSITORY                                        │
│     └─ gh repo clone omarzsalah1/manus-task-backups             │
│        OR cd ~/manus-task-backups && git pull                   │
│                                                                  │
│  3. LOOKUP SESSION                                               │
│     ├─ Read registry.json                                       │
│     ├─ Find session where shorthand_id == "SANDBOX{N}"          │
│     └─ Get backup_folder path                                   │
│                                                                  │
│  4. RESTORE FILES                                                │
│     └─ cp -r backups/{folder}/sandbox/* /home/ubuntu/           │
│                                                                  │
│  5. RESTORE ENVIRONMENT                                          │
│     ├─ pip3 install -r requirements.txt                         │
│     ├─ npm install (if package.json exists)                     │
│     └─ sudo apt-get install (if apt-packages.txt exists)        │
│                                                                  │
│  6. DISPLAY CONTINUATION CONTEXT                                 │
│     ├─ Read CONTINUATION.md                                     │
│     ├─ Show task objective                                      │
│     ├─ Show completed work                                      │
│     ├─ Show TODO items                                          │
│     └─ Show file inventory                                      │
│                                                                  │
│  7. READY TO CONTINUE                                            │
│     ┌─────────────────────────────────────────────────────────┐ │
│     │ ✅ SANDBOX3 restored successfully!                       │ │
│     │ Session: "API Integration Project"                       │ │
│     │ Files: 25 restored | Environment: 45 pip packages        │ │
│     │                                                          │ │
│     │ 📋 TODO Remaining:                                       │ │
│     │ - [ ] Complete API endpoint testing                      │ │
│     │ - [ ] Add error handling                                 │ │
│     │                                                          │ │
│     │ Ready to continue. What would you like to work on?       │ │
│     └─────────────────────────────────────────────────────────┘ │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. List Workflow

### 6.1 Trigger Command

```
LIST SANDBOXES
```

### 6.2 Output Format

```
┌──────────┬─────────────────────────┬────────────┬──────────┐
│ ID       │ Name                    │ Date       │ Status   │
├──────────┼─────────────────────────┼────────────┼──────────┤
│ SANDBOX1 │ Backup Skill Setup      │ 2025-12-31 │ ✅       │
│ SANDBOX2 │ System v2 Enhancement   │ 2025-12-31 │ ✅       │
│ SANDBOX3 │ API Integration Project │ 2026-01-01 │ 🔄       │
└──────────┴─────────────────────────┴────────────┴──────────┘

Restore any with: RESTORE SANDBOX{N}
```

---

## 7. File Structure

```
manus-task-backups/
├── README.md                          # Main documentation
├── SANDBOX-COMMANDS.md                # Quick reference for all commands
├── FULL-IMPLEMENTATION-PLAN.md        # This document
├── sessions/
│   └── registry.json                  # Master registry with counter
├── config/
│   └── notion-integration.json        # Notion sync settings
├── scripts/
│   ├── capture-env.sh                 # Environment capture script
│   ├── restore-env.sh                 # Environment restore script
│   └── backup-inventory.sh            # File manifest generator
├── templates/
│   └── continuation-template-v2.md    # CONTINUATION.md template
└── backups/
    ├── 2025-12-31_continuation-skill-setup/
    │   ├── CONTINUATION.md            # SANDBOX1 restore prompt
    │   ├── manifest.json
    │   └── sandbox/                   # Backed up files
    └── 2025-12-31_backup-system-v2-enhancement/
        ├── CONTINUATION.md            # SANDBOX2 restore prompt
        ├── manifest.json
        ├── environment.json
        ├── restore-env.sh
        └── sandbox/                   # Backed up files
```

---

## 8. Notion Database Schema

**Database:** Backup Sessions Registry  
**URL:** https://www.notion.so/1337a26936fd4f4a9e82a30eea20c78d

| Field | Type | Description |
|-------|------|-------------|
| Session ID | Title | SANDBOX{N} shorthand |
| Session Name | Text | AI-generated descriptive name |
| Backup Date | Date | When backup was created |
| Backup Type | Select | Manual / Auto-Hourly / Error-Recovery / Checkpoint |
| Status | Select | Active / Complete / Error / Archived |
| GitHub URL | URL | Link to backup folder |
| Tags | Multi-select | system, infrastructure, website, api, etc. |
| Total Files | Number | Count of backed up files |
| Sandbox Size | Text | Approximate size |
| Python Packages | Number | pip package count |
| Node Packages | Number | npm package count |
| System Packages | Number | apt package count |
| TODO High | Number | High priority items remaining |
| TODO Medium | Number | Medium priority items |
| TODO Low | Number | Low priority items |
| Completion Pct | Percent | Task completion percentage |
| Task Objective | Text | What the task aimed to accomplish |
| Restore Command | Text | RESTORE SANDBOX{N} |
| Notes | Text | Additional context |

---

## 9. Command Reference

| Command | Description | Example |
|---------|-------------|---------|
| `BACKUP & CONTINUE` | Full backup with auto-generated SANDBOX ID | Creates SANDBOX3 |
| `RESTORE SANDBOX{N}` | Restore specific backup | `RESTORE SANDBOX2` |
| `RESTORE LATEST` | Restore most recent backup | Auto-detects highest N |
| `LIST SANDBOXES` | Show all available backups | Displays table |
| `CHECKPOINT` | Quick save without full documentation | Fast mid-task save |
| `ERROR BACKUP` | Recovery backup on failure | Detailed error context |

---

## 10. iOS/macOS Shortcuts

### 10.1 Full Backup Command (iOS Shortcut)

Copy this entire block into your iOS Shortcut:

```
BACKUP & CONTINUE: Create a comprehensive continuation package with auto-generated SANDBOX ID. Back up ALL sandbox files to GitHub (omarzsalah1/manus-task-backups), generate a detailed CONTINUATION.md with:
1. SANDBOX{N} shorthand ID for easy restoration
2. Explicit details of everything completed
3. What remains to be done (TODO: High/Medium/Low priority)
4. Full file inventory with paths
5. GitHub pull instructions: RESTORE SANDBOX{N}
6. Environment/dependency capture (pip, npm, apt packages)
7. Notion database sync with full metadata
8. Any suggestions for seamless continuation

Push everything to a dated folder in backups/ directory. Report completion as:
✅ SANDBOX{N} backup complete
Session: "[AI-generated name]"
Files: X | Size: XKB | TODO: X items
Restore: RESTORE SANDBOX{N}
```

### 10.2 Text Replacement Setup (Fastest Method)

Go to **Settings > General > Keyboard > Text Replacement** and add:

| Shortcut | Phrase |
|----------|--------|
| `rsb` | `RESTORE SANDBOX` |
| `rsl` | `RESTORE LATEST` |
| `lsb` | `LIST SANDBOXES` |
| `bkc` | `BACKUP & CONTINUE` |

**Usage:** Type `rsb2` → expands to `RESTORE SANDBOX2`

### 10.3 Shortcuts App Setup

1. Open **Shortcuts** app
2. Create new shortcut for each command
3. Add action: **Text** → paste command
4. Add action: **Copy to Clipboard**
5. Add to Home Screen or Menu Bar

### 10.4 All Commands for Shortcuts

**Backup (Full):**
```
BACKUP & CONTINUE
```

**Restore Specific:**
```
RESTORE SANDBOX
```
(Then add the number)

**Restore Latest:**
```
RESTORE LATEST
```

**List All:**
```
LIST SANDBOXES
```

**Quick Checkpoint:**
```
CHECKPOINT
```

**Error Recovery:**
```
ERROR BACKUP
```

---

## 11. Quick Reference Card

```
╔═══════════════════════════════════════════════════════════════╗
║           MANUS BACKUP & RESTORE - QUICK REFERENCE            ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  💾 BACKUP                                                    ║
║  ─────────────────────────────────────────────────────────── ║
║  BACKUP & CONTINUE     Full backup → creates SANDBOX{N}      ║
║  CHECKPOINT            Quick save, minimal docs               ║
║  ERROR BACKUP          Recovery backup on failure             ║
║                                                               ║
║  🔄 RESTORE                                                   ║
║  ─────────────────────────────────────────────────────────── ║
║  RESTORE SANDBOX2      Restore backup #2                      ║
║  RESTORE LATEST        Restore most recent                    ║
║                                                               ║
║  📋 LIST                                                      ║
║  ─────────────────────────────────────────────────────────── ║
║  LIST SANDBOXES        Show all available backups             ║
║                                                               ║
║  ⌨️ TEXT REPLACEMENTS                                         ║
║  ─────────────────────────────────────────────────────────── ║
║  rsb  →  RESTORE SANDBOX                                      ║
║  rsl  →  RESTORE LATEST                                       ║
║  lsb  →  LIST SANDBOXES                                       ║
║  bkc  →  BACKUP & CONTINUE                                    ║
║                                                               ║
║  🔗 RESOURCES                                                 ║
║  ─────────────────────────────────────────────────────────── ║
║  GitHub:  github.com/omarzsalah1/manus-task-backups          ║
║  Notion:  notion.so/1337a26936fd4f4a9e82a30eea20c78d         ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## Current Sandboxes

| ID | Name | Date | Status | Restore |
|----|------|------|--------|---------|
| SANDBOX1 | Backup & Continue Skill Setup | 2025-12-31 | ✅ Complete | `RESTORE SANDBOX1` |
| SANDBOX2 | System v2.0 Enhancement | 2025-12-31 | ✅ Complete | `RESTORE SANDBOX2` |

**Next backup will be:** SANDBOX3

---

## Resources

- **GitHub Repository:** https://github.com/omarzsalah1/manus-task-backups
- **Notion Database:** https://www.notion.so/1337a26936fd4f4a9e82a30eea20c78d
- **Notion Parent Page:** https://www.notion.so/2dbff518007781239528f3298aaecd79

---

*Manus Task Backup System v3.0 - SANDBOX Edition*  
*Last Updated: 2025-12-31*
