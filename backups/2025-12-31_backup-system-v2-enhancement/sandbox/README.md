# Manus Task Backups v2.0

**Comprehensive backup and continuation system for Manus AI tasks.**

This repository stores sandbox snapshots, environment configurations, and continuation prompts for seamless task resumption across sessions.

## 🆕 What's New in v2.0

- **Named Sessions:** Each backup has a descriptive session ID for easy identification
- **One-Command Restoration:** Full environment rebuild including all packages
- **Notion Integration:** Automatic documentation and TODO task creation
- **Roadmap/TODO Tracking:** Structured tracking of completed and remaining work
- **Auto-Triggers:** Automatic checkpoints and error recovery backups
- **Environment Capture:** Full pip, npm, and apt package snapshots

## 🎯 Purpose

When working on complex tasks with Manus, you can trigger a full backup of all sandbox files and generate a detailed continuation prompt. This allows you to:

- **Resume any task** from exactly where you left off
- **Access all files** (code, assets, documents) created during a session
- **Restore the full environment** with all dependencies
- **Track TODO items** across sessions
- **Get explicit instructions** on what was done and what remains
- **Seamlessly continue** in a new Manus session

## 📁 Repository Structure

```
manus-task-backups/
├── backups/                          # Task backup folders
│   └── YYYY-MM-DD_session-name/      # Individual task backup
│       ├── sandbox/                  # Full sandbox file snapshot
│       ├── CONTINUATION.md           # Detailed continuation prompt
│       ├── manifest.json             # File inventory and metadata
│       ├── requirements.txt          # Python packages
│       ├── npm-global-packages.txt   # Node.js packages
│       ├── apt-packages.txt          # System packages
│       └── restore-env.sh            # Environment restoration script
├── sessions/                         # Session management
│   └── registry.json                 # All sessions registry
├── config/                           # Configuration files
│   └── notion-integration.json       # Notion sync settings
├── templates/                        # Reusable templates
│   ├── continuation-template.md      # Basic template
│   └── continuation-template-v2.md   # Enhanced template with TODOs
├── scripts/                          # Utility scripts
│   ├── backup-inventory.sh           # File manifest generator
│   ├── capture-env.sh                # Environment capture
│   └── restore-env.sh                # Environment restoration
├── README.md                         # This file
├── TRIGGER-PHRASE.md                 # Original trigger phrases
└── TRIGGER-PHRASE-v2.md              # Enhanced trigger phrases
```

## 🚀 Trigger Commands

### Full Backup & Continue
```
BACKUP & CONTINUE [session-name]: Full backup with TODO tracking and Notion sync.
```

### Quick Checkpoint
```
CHECKPOINT [session-name]: Save current progress snapshot.
```

### Error Recovery
```
ERROR BACKUP [session-name]: Backup on failure for debugging.
```

### Restore Session
```
RESTORE SESSION [session-id]: Pull and restore full environment.
```

### List Sessions
```
LIST SESSIONS: Show all available backup sessions.
```

## 📥 How to Resume a Task

### Option 1: One-Command Restore
```bash
gh repo clone omarzsalah1/manus-task-backups ~/manus-task-backups 2>/dev/null || (cd ~/manus-task-backups && git pull)
cp -r ~/manus-task-backups/backups/[backup-folder]/sandbox/* ~/
cd ~/manus-task-backups/backups/[backup-folder] && bash restore-env.sh
```

### Option 2: Paste Continuation Prompt
1. Start a new Manus session
2. Paste the contents of `backups/[session]/CONTINUATION.md`
3. Manus will restore your working state automatically

## 📋 What Gets Backed Up

| Category | Items |
|----------|-------|
| **Files** | All files in `/home/ubuntu/` (excluding system directories) |
| **Code** | Scripts, source files, configurations |
| **Assets** | Images, PDFs, documents, data files |
| **Environment** | pip packages, npm packages, apt packages |
| **Context** | Task objective, completed work, TODO items |

## 🔗 Integrations

- **GitHub:** https://github.com/omarzsalah1/manus-task-backups
- **Notion:** https://www.notion.so/2dbff518007781239528f3298aaecd79

---

*Manus Task Backup System v2.0 - Created for seamless AI task continuity*
