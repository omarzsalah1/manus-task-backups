# Manus Task Backups

**Comprehensive backup and continuation system for Manus AI tasks.**

This repository stores sandbox snapshots and continuation prompts for seamless task resumption across sessions.

## 🎯 Purpose

When working on complex tasks with Manus, you can trigger a full backup of all sandbox files and generate a detailed continuation prompt. This allows you to:

- **Resume any task** from exactly where you left off
- **Access all files** (code, assets, documents) created during a session
- **Get explicit instructions** on what was done and what remains
- **Seamlessly continue** in a new Manus session

## 📁 Repository Structure

```
manus-task-backups/
├── backups/                    # Task backup folders (dated)
│   └── YYYY-MM-DD_task-name/   # Individual task backup
│       ├── sandbox/            # Full sandbox file snapshot
│       ├── CONTINUATION.md     # Detailed continuation prompt
│       └── manifest.json       # File inventory and metadata
├── templates/                  # Reusable templates
│   └── continuation-template.md
├── scripts/                    # Utility scripts
│   └── backup-inventory.sh
└── README.md
```

## 🚀 Trigger Command

Use this phrase in any Manus task to trigger a full backup and continuation prompt:

> **"BACKUP & CONTINUE: Create a comprehensive continuation package - back up all sandbox files to GitHub (manus-task-backups), generate a detailed continuation prompt with explicit context of everything done, what remains, file paths, and pull instructions for seamless resumption."**

### Shortened Version (for iOS/macOS Shortcuts):

> **"BACKUP & CONTINUE: Full sandbox backup to GitHub with continuation prompt."**

## 📥 How to Resume a Task

1. Start a new Manus session
2. Paste the continuation prompt from `backups/[task-folder]/CONTINUATION.md`
3. Manus will clone the backup and restore your working state

## 📋 What Gets Backed Up

- All files in `/home/ubuntu/` (excluding system directories)
- Code, scripts, documents, images, PDFs, and all assets
- Project configurations and dependencies
- Full directory structure preserved

---

*Created for seamless AI task continuity*
