# 🎯 SANDBOX Commands - Quick Reference

## Mac/iOS Shortcut Commands

Copy these to your Shortcuts app for instant access.

---

## 🔄 RESTORE Commands

### Restore Specific Backup
```
RESTORE SANDBOX2
```
Restores the backup with ID `SANDBOX2`. Replace the number with any valid SANDBOX ID.

### Restore Latest Backup
```
RESTORE LATEST
```
Automatically restores the most recent backup without needing to remember the number.

---

## 💾 BACKUP Commands

### Full Backup & Continue
```
BACKUP & CONTINUE
```
Creates a comprehensive backup with:
- Auto-generated SANDBOX ID (e.g., `SANDBOX3`)
- Full sandbox file snapshot
- Environment capture (pip, npm, apt packages)
- TODO/Roadmap tracking
- Notion database entry
- GitHub push

**Completion Message Format:**
```
✅ SANDBOX3 backup complete
Session: "Your Task Description"
Files: 15 | Size: 50KB | TODO: 4 items
Restore: RESTORE SANDBOX3
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

### List All Sandboxes
```
LIST SANDBOXES
```
Shows all available backups:
```
┌──────────┬─────────────────────────┬────────────┬──────────┐
│ ID       │ Name                    │ Date       │ Status   │
├──────────┼─────────────────────────┼────────────┼──────────┤
│ SANDBOX1 │ Backup Skill Setup      │ 2025-12-31 │ Complete │
│ SANDBOX2 │ System v2 Enhancement   │ 2025-12-31 │ Complete │
└──────────┴─────────────────────────┴────────────┴──────────┘
```

---

## 📱 iOS/macOS Shortcuts Setup

### Option 1: Text Replacement (Fastest)
1. Go to **Settings > General > Keyboard > Text Replacement**
2. Add these:
   - Phrase: `RESTORE SANDBOX` | Shortcut: `rsb`
   - Phrase: `RESTORE LATEST` | Shortcut: `rsl`
   - Phrase: `BACKUP & CONTINUE` | Shortcut: `bkc`
   - Phrase: `LIST SANDBOXES` | Shortcut: `lsb`

### Option 2: Shortcuts App
1. Open **Shortcuts** app
2. Create new shortcut for each command
3. Add action: **Text** → paste command
4. Add action: **Copy to Clipboard**
5. Add to Home Screen or Menu Bar

---

## 🗂️ Current Sandboxes

| ID | Name | Date | Restore Command |
|----|------|------|-----------------|
| SANDBOX1 | Backup & Continue Skill Setup | 2025-12-31 | `RESTORE SANDBOX1` |
| SANDBOX2 | System v2.0 Enhancement | 2025-12-31 | `RESTORE SANDBOX2` |

---

## 🔗 Resources

- **GitHub:** https://github.com/omarzsalah1/manus-task-backups
- **Notion Database:** https://www.notion.so/1337a26936fd4f4a9e82a30eea20c78d
- **Notion Parent Page:** https://www.notion.so/2dbff518007781239528f3298aaecd79

---

## How It Works

1. **BACKUP & CONTINUE** → Creates `SANDBOX{N}` with auto-increment
2. **Counter stored** in `sessions/registry.json` (never resets)
3. **Dual ID system**: `SANDBOX3` (quick) + `my-project-name` (descriptive)
4. **Notion synced** with all metadata fields
5. **GitHub pushed** automatically

---

*Manus Task Backup System v3.0 - SANDBOX Edition*
