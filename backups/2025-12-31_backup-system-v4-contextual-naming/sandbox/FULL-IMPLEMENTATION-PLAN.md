# 📋 Full Implementation Plan: Manus Backup & Restore System v4.0

## Table of Contents
1. [System Overview](#1-system-overview)
2. [Architecture](#2-architecture)
3. [AI-Generated Contextual Naming System](#3-ai-generated-contextual-naming-system)
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

- **AI-generated contextual shorthand IDs** (VACATION1, WEBSITE2, API3, etc.)
- **Full sandbox file backup** to GitHub
- **Environment capture & restoration** (pip, npm, apt packages)
- **Notion integration** for structured documentation
- **TODO/Roadmap tracking** for incomplete work
- **Simple restore commands** for Mac/iOS Shortcuts

### Key Innovation: Contextual Naming

Unlike generic numbering, the system **analyzes your task context** and generates a meaningful category prefix:

| Task About | Shorthand ID |
|------------|--------------|
| Backup system infrastructure | `SANDBOX1` |
| Booking flight tickets | `VACATION1` |
| Building a landing page | `WEBSITE1` |
| Integrating Stripe API | `API1` |
| Analyzing sales data | `DATA1` |
| Writing quarterly report | `REPORT1` |

### Key Benefits

| Feature | Benefit |
|---------|---------|
| Contextual IDs | Instantly know what each backup contains |
| Category Counters | Each category tracks its own sequence |
| Dual ID System | Quick access (VACATION1) + descriptive name |
| Environment Capture | Full restoration including all packages |
| Notion Sync | Searchable, filterable backup database |
| TODO Tracking | Never lose track of incomplete work |

---

## 2. Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER INTERFACE                               │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────────────┐ │
│  │ BACKUP &    │  │ RESTORE      │  │ LIST BACKUPS            │ │
│  │ CONTINUE    │  │ VACATION1    │  │                         │ │
│  └──────┬──────┘  └──────┬───────┘  └────────────┬────────────┘ │
└─────────┼────────────────┼──────────────────────┼───────────────┘
          │                │                      │
          ▼                ▼                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                     MANUS AI PROCESSING                          │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ 1. Parse command (BACKUP/RESTORE/LIST)                      ││
│  │ 2. Analyze task context → Select category                   ││
│  │ 3. Read registry.json for category counter                  ││
│  │ 4. Execute appropriate workflow                             ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
          │                │                      │
          ▼                ▼                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                     STORAGE LAYER                                │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │ GitHub Repo     │  │ Notion Database │  │ Local Registry  │  │
│  │ manus-task-     │  │ Backup Sessions │  │ registry.json   │  │
│  │ backups         │  │ Registry        │  │ (multi-counter) │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. AI-Generated Contextual Naming System

### 3.1 Available Categories

| Category | Use For | Example Tasks |
|----------|---------|---------------|
| `SANDBOX` | System tools, backup infrastructure | Manus configuration, this backup system |
| `VACATION` | Travel planning, trips | Flight tickets, hotel bookings, itineraries |
| `WEBSITE` | Web development | Site redesign, landing pages, portfolios |
| `API` | Backend development | API integrations, webhooks, endpoints |
| `DATA` | Data work | Analysis, spreadsheets, visualizations |
| `REPORT` | Documents | Reports, presentations, summaries |
| `EMAIL` | Communication | Email campaigns, newsletters, templates |
| `MEETING` | Meetings | Prep, agendas, notes, follow-ups |
| `PROJECT` | Project management | Planning, coordination, tracking |
| `RESEARCH` | Research | Investigations, competitive analysis |
| `DESIGN` | Creative work | UI/UX, graphics, branding |
| `CODE` | General coding | Scripts, development tasks |
| `DOCS` | Documentation | Guides, manuals, knowledge bases |
| `FINANCE` | Financial | Budgets, invoices, expenses |
| `HEALTH` | Health/Wellness | Medical, fitness, tracking |
| `TRAVEL` | Transportation | Logistics, maps, directions |
| `SHOPPING` | Purchases | Shopping lists, product research |
| `LEARNING` | Education | Courses, tutorials, skill development |
| `AUTOMATION` | Workflows | Automation scripts, integrations |
| `MISC` | Everything else | Anything that doesn't fit above |

### 3.2 ID Generation Process

When `BACKUP & CONTINUE` is triggered:

```
Step 1: Analyze Task Context
        → What is this task about?
        → Keywords: "flight", "booking", "trip" → VACATION
        → Keywords: "website", "landing page" → WEBSITE
        → Keywords: "API", "endpoint", "integration" → API

Step 2: Read Category Counter from registry.json
        → counters.VACATION = 0

Step 3: Generate Shorthand ID
        → Increment counter: 0 + 1 = 1
        → shorthand_id = "VACATION" + "1" = "VACATION1"

Step 4: AI Generates Descriptive Session Name
        → "Hawaii Trip Planning - Flight & Hotel"

Step 5: Save to Registry
        → counters.VACATION = 1
        → Add session entry with dual IDs

Step 6: Report to User
        → "✅ VACATION1 backup complete"
```

### 3.3 Multi-Category Counter Registry

```json
{
  "schema_version": "4.0",
  "counters": {
    "SANDBOX": 3,
    "VACATION": 1,
    "WEBSITE": 2,
    "API": 1,
    "DATA": 0,
    "REPORT": 0,
    ...
  },
  "sessions": [
    {
      "shorthand_id": "SANDBOX1",
      "category": "SANDBOX",
      "session_name": "Backup & Continue Skill Setup",
      ...
    },
    {
      "shorthand_id": "VACATION1",
      "category": "VACATION",
      "session_name": "Hawaii Trip Planning - Flight & Hotel",
      ...
    },
    {
      "shorthand_id": "WEBSITE1",
      "category": "WEBSITE",
      "session_name": "Portfolio Site Redesign",
      ...
    }
  ]
}
```

### 3.4 Collision Prevention

Each category has its own counter:
- **Independent tracking** - VACATION1, VACATION2 don't affect WEBSITE1, WEBSITE2
- **Never decreases** - counters only increment
- **Persists across sessions** - stored in GitHub
- **Pulled before each backup** - ensures latest counter

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
│  1. ANALYZE TASK CONTEXT                                         │
│     ├─ Review conversation history                              │
│     ├─ Identify key topics and keywords                         │
│     └─ Select appropriate category (VACATION, WEBSITE, etc.)    │
│                                                                  │
│  2. GENERATE IDs                                                 │
│     ├─ Read category counter from registry.json                 │
│     ├─ Increment counter: VACATION 0 → 1                        │
│     ├─ Create shorthand: VACATION1                              │
│     └─ AI generates descriptive session_name                    │
│                                                                  │
│  3. CREATE BACKUP FOLDER                                         │
│     └─ backups/{DATE}_{session_id}/                             │
│         ├─ sandbox/           (all user files)                  │
│         ├─ CONTINUATION.md    (restore prompt)                  │
│         ├─ manifest.json      (file inventory)                  │
│         ├─ environment.json   (packages list)                   │
│         └─ restore-env.sh     (restoration script)              │
│                                                                  │
│  4. CAPTURE ENVIRONMENT                                          │
│     ├─ pip3 freeze > requirements.txt                           │
│     ├─ npm list --json > package-list.json                      │
│     └─ dpkg --get-selections > apt-packages.txt                 │
│                                                                  │
│  5. COPY SANDBOX FILES                                           │
│     └─ cp -r /home/ubuntu/* → backup/sandbox/                   │
│         (excluding .git, .nvm, .cache, node_modules)            │
│                                                                  │
│  6. GENERATE CONTINUATION.md                                     │
│     ├─ Shorthand ID (VACATION1)                                 │
│     ├─ Task objective                                           │
│     ├─ Completed work summary                                   │
│     ├─ TODO/Roadmap (High/Medium/Low priority)                  │
│     ├─ File inventory table                                     │
│     ├─ Environment snapshot                                     │
│     └─ Restore command: RESTORE VACATION1                       │
│                                                                  │
│  7. UPDATE REGISTRY                                              │
│     ├─ Increment category counter                               │
│     └─ Add new session entry to sessions[]                      │
│                                                                  │
│  8. SYNC TO NOTION                                               │
│     └─ Create database entry with all metadata                  │
│                                                                  │
│  9. PUSH TO GITHUB                                               │
│     └─ git add -A && git commit && git push                     │
│                                                                  │
│ 10. REPORT COMPLETION                                            │
│     ┌─────────────────────────────────────────────────────────┐ │
│     │ ✅ VACATION1 backup complete                             │ │
│     │ Session: "Hawaii Trip Planning - Flight & Hotel"         │ │
│     │ Files: 12 | Size: 85KB | TODO: 3 items                   │ │
│     │ Restore: RESTORE VACATION1                               │ │
│     └─────────────────────────────────────────────────────────┘ │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 4.3 CONTINUATION.md Template

```markdown
# 🔄 CONTINUATION PROMPT

**VACATION1** | `hawaii-trip-planning`  
**Session Name:** Hawaii Trip Planning - Flight & Hotel  
**Backup Date:** 2026-01-15  
**GitHub:** {github_url}  
**Notion:** {notion_url}

---

## 📋 QUICK RESTORE

RESTORE VACATION1

---

## 🎯 TASK OBJECTIVE

Planning a 7-day trip to Hawaii including flight bookings, hotel reservations, 
and activity planning for the family vacation in March 2026.

---

## ✅ COMPLETED WORK

1. Researched flight options from LAX to Honolulu
2. Compared hotel prices in Waikiki area
3. Created initial itinerary draft

---

## 🔲 TODO

### High Priority
- [ ] Book flights (United vs Hawaiian Airlines)
- [ ] Reserve hotel (Hilton vs Marriott)

### Medium Priority
- [ ] Plan daily activities
- [ ] Research restaurant reservations

### Low Priority
- [ ] Create packing list
- [ ] Arrange airport transportation

---

## 📁 FILES

| File | Description |
|------|-------------|
| `flight-comparison.xlsx` | Price comparison spreadsheet |
| `itinerary-draft.md` | Day-by-day plan |
| `hotel-options.json` | Hotel data from search |

---

**🚀 To restore: `RESTORE VACATION1`**
```

---

## 5. Restore Workflow

### 5.1 Trigger Commands

```
RESTORE VACATION1     # Restore specific backup
RESTORE WEBSITE2      # Restore different category
RESTORE LATEST        # Restore most recent backup (any category)
```

### 5.2 Full Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ RESTORE {CATEGORY}{N} WORKFLOW                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. PARSE COMMAND                                                │
│     ├─ Extract category and number: "VACATION" + "1"            │
│     └─ If "RESTORE LATEST" → find most recent session           │
│                                                                  │
│  2. CLONE/PULL REPOSITORY                                        │
│     └─ gh repo clone omarzsalah1/manus-task-backups             │
│        OR cd ~/manus-task-backups && git pull                   │
│                                                                  │
│  3. LOOKUP SESSION                                               │
│     ├─ Read registry.json                                       │
│     ├─ Find session where shorthand_id == "VACATION1"           │
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
│     │ ✅ VACATION1 restored successfully!                      │ │
│     │ Session: "Hawaii Trip Planning - Flight & Hotel"         │ │
│     │ Files: 12 restored | Environment: ready                  │ │
│     │                                                          │ │
│     │ 📋 TODO Remaining:                                       │ │
│     │ - [ ] Book flights (United vs Hawaiian Airlines)         │ │
│     │ - [ ] Reserve hotel (Hilton vs Marriott)                 │ │
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
LIST BACKUPS
```

### 6.2 Output Format

```
┌────────────┬─────────────────────────────────┬────────────┬──────────┐
│ ID         │ Name                            │ Date       │ Status   │
├────────────┼─────────────────────────────────┼────────────┼──────────┤
│ SANDBOX1   │ Backup Skill Setup              │ 2025-12-31 │ ✅       │
│ SANDBOX2   │ System v2 Enhancement           │ 2025-12-31 │ ✅       │
│ VACATION1  │ Hawaii Trip Planning            │ 2026-01-15 │ 🔄       │
│ WEBSITE1   │ Portfolio Site Redesign         │ 2026-01-10 │ ✅       │
│ API1       │ Stripe Integration              │ 2026-01-12 │ 🔄       │
└────────────┴─────────────────────────────────┴────────────┴──────────┘

Restore any with: RESTORE {ID}  (e.g., RESTORE VACATION1)
```

---

## 7. File Structure

```
manus-task-backups/
├── README.md                          # Main documentation
├── BACKUP-COMMANDS.md                 # Quick reference for all commands
├── FULL-IMPLEMENTATION-PLAN.md        # This document
├── sessions/
│   └── registry.json                  # Master registry with multi-category counters
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
    │   └── sandbox/
    ├── 2025-12-31_backup-system-v2-enhancement/
    │   ├── CONTINUATION.md            # SANDBOX2 restore prompt
    │   └── sandbox/
    ├── 2026-01-15_hawaii-trip-planning/
    │   ├── CONTINUATION.md            # VACATION1 restore prompt
    │   └── sandbox/
    └── 2026-01-10_portfolio-site-redesign/
        ├── CONTINUATION.md            # WEBSITE1 restore prompt
        └── sandbox/
```

---

## 8. Notion Database Schema

**Database:** Backup Sessions Registry  
**URL:** https://www.notion.so/1337a26936fd4f4a9e82a30eea20c78d

| Field | Type | Description |
|-------|------|-------------|
| Session ID | Title | Contextual shorthand (VACATION1, WEBSITE2) |
| Category | Select | SANDBOX, VACATION, WEBSITE, API, etc. |
| Session Name | Text | AI-generated descriptive name |
| Backup Date | Date | When backup was created |
| Backup Type | Select | Manual / Auto-Hourly / Error-Recovery / Checkpoint |
| Status | Select | Active / Complete / Error / Archived |
| GitHub URL | URL | Link to backup folder |
| Tags | Multi-select | Additional tags for filtering |
| Total Files | Number | Count of backed up files |
| Sandbox Size | Text | Approximate size |
| Python Packages | Number | pip package count |
| Node Packages | Number | npm package count |
| TODO High | Number | High priority items remaining |
| TODO Medium | Number | Medium priority items |
| TODO Low | Number | Low priority items |
| Completion Pct | Percent | Task completion percentage |
| Task Objective | Text | What the task aimed to accomplish |
| Restore Command | Text | RESTORE VACATION1 |
| Notes | Text | Additional context |

---

## 9. Command Reference

| Command | Description | Example |
|---------|-------------|---------|
| `BACKUP & CONTINUE` | Full backup with AI-generated contextual ID | Creates VACATION1, WEBSITE2, etc. |
| `RESTORE {ID}` | Restore specific backup | `RESTORE VACATION1` |
| `RESTORE LATEST` | Restore most recent backup | Auto-detects latest |
| `LIST BACKUPS` | Show all available backups | Displays table |
| `CHECKPOINT` | Quick save without full documentation | Fast mid-task save |
| `ERROR BACKUP` | Recovery backup on failure | Detailed error context |

---

## 10. iOS/macOS Shortcuts

### 10.1 Full Backup Command (iOS Shortcut)

Copy this entire block into your iOS Shortcut:

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

### 10.2 Text Replacement Setup (Fastest Method)

Go to **Settings > General > Keyboard > Text Replacement** and add:

| Shortcut | Phrase |
|----------|--------|
| `rr` | `RESTORE ` |
| `rsl` | `RESTORE LATEST` |
| `lsb` | `LIST BACKUPS` |
| `bkc` | `BACKUP & CONTINUE` |

**Usage:** 
- Type `rr` → expands to `RESTORE ` → then type `VACATION1`
- Type `bkc` → expands to `BACKUP & CONTINUE`

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
RESTORE VACATION1
RESTORE WEBSITE2
RESTORE API1
```

**Restore Latest:**
```
RESTORE LATEST
```

**List All:**
```
LIST BACKUPS
```

---

## 11. Quick Reference Card

```
╔═══════════════════════════════════════════════════════════════╗
║      MANUS BACKUP & RESTORE v4.0 - CONTEXTUAL NAMING          ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  💾 BACKUP                                                    ║
║  ─────────────────────────────────────────────────────────── ║
║  BACKUP & CONTINUE     AI picks category → VACATION1, etc.   ║
║  CHECKPOINT            Quick save, minimal docs               ║
║  ERROR BACKUP          Recovery backup on failure             ║
║                                                               ║
║  🔄 RESTORE                                                   ║
║  ─────────────────────────────────────────────────────────── ║
║  RESTORE VACATION1     Restore travel task backup             ║
║  RESTORE WEBSITE2      Restore web dev backup                 ║
║  RESTORE API1          Restore API integration backup         ║
║  RESTORE LATEST        Restore most recent (any category)     ║
║                                                               ║
║  📋 LIST                                                      ║
║  ─────────────────────────────────────────────────────────── ║
║  LIST BACKUPS          Show all available backups             ║
║                                                               ║
║  🏷️ CATEGORIES                                                ║
║  ─────────────────────────────────────────────────────────── ║
║  SANDBOX   System/infrastructure    VACATION  Travel/trips    ║
║  WEBSITE   Web development          API       Integrations    ║
║  DATA      Analysis/spreadsheets    REPORT    Documents       ║
║  PROJECT   Project management       RESEARCH  Investigations  ║
║  CODE      General coding           DESIGN    Creative work   ║
║  FINANCE   Financial tasks          HEALTH    Wellness        ║
║  LEARNING  Education/courses        AUTOMATION Workflows      ║
║                                                               ║
║  ⌨️ TEXT REPLACEMENTS                                         ║
║  ─────────────────────────────────────────────────────────── ║
║  rr   →  RESTORE                                              ║
║  rsl  →  RESTORE LATEST                                       ║
║  lsb  →  LIST BACKUPS                                         ║
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

## Current Backups

| ID | Category | Name | Date | Restore |
|----|----------|------|------|---------|
| SANDBOX1 | SANDBOX | Backup & Continue Skill Setup | 2025-12-31 | `RESTORE SANDBOX1` |
| SANDBOX2 | SANDBOX | System v2.0 Enhancement | 2025-12-31 | `RESTORE SANDBOX2` |

**Next backup IDs available:** SANDBOX3, VACATION1, WEBSITE1, API1, DATA1, etc.

---

## Resources

- **GitHub Repository:** https://github.com/omarzsalah1/manus-task-backups
- **Notion Database:** https://www.notion.so/1337a26936fd4f4a9e82a30eea20c78d
- **Notion Parent Page:** https://www.notion.so/2dbff518007781239528f3298aaecd79

---

*Manus Task Backup System v4.0 - Contextual Naming Edition*  
*Last Updated: 2025-12-31*
