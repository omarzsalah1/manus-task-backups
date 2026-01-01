# 🔄 Claude Backup & Restore System v5.0

## Overview
Unified backup system for Claude and Manus sandboxes.
- **Claude backups**: `{CATEGORY}X{N}` (e.g., PROJECTX1, BOOKX2)
- **Manus backups**: `{CATEGORY}{N}` (e.g., PROJECT1, BOOK2)
- **Repo**: `omarzsalah1/manus-task-backups`

---

## 📱 iOS Shortcuts

### Backup (cntN)
```
BACKUP & CONTINUE: Back up ALL sandbox files to GitHub manus-task-backups using {CATEGORY}X{N} naming. Include conversation transcript. Compress files >50MB. Use curl/GitHub MCP to push directly - no reading files first. Generate CONTINUATION.md. Return backup ID and restore command.
```

### Cross-Restore (xrr)
```
CROSS-RESTORE: Claude Sandbox=         Manus Sandbox=         Task: 
```

### Restore Claude (rsbx)
```
RESTORE SANDBOXX: 
```

### List Backups (lsb)
```
LIST BACKUPS
```

---

## 🔧 BACKUP Workflow

1. **Determine Category** - Based on task context
2. **Get Next ID** - Query registry, increment counter
3. **Stage Files** - Copy all files (NO READING)
4. **Compress Large Files** - gzip anything >50MB
5. **Create CONTINUATION.md** - Include conversation summary
6. **Push to GitHub** - Single push via MCP
7. **Update Registry** - Add session, increment counter
8. **Sync to Notion** - Database 1337a26936fd4f4a9e82a30eea20c78d
9. **Report** - Return backup ID and restore command

---

## 🔄 RESTORE Workflow

1. **Parse Backup ID** - Extract from command
2. **Lookup Folder** - Query registry for backup_folder
3. **Download Files** - Use curl (NOT web_fetch)
4. **Decompress** - gunzip any .gz files
5. **Read CONTINUATION.md** - Load context and continue

---

## 🔗 CROSS-RESTORE Workflow

**Input**: `CROSS-RESTORE: Claude Sandbox=PROJECTX1 Manus Sandbox=BOOK1 Task: verify PDF`

**Execution (PARALLEL)**:
1. Start Manus FIRST (takes longer) via Manus AI:create_task
2. Restore Claude backup while Manus loads
3. Create Asana task for tracking
4. Begin verification/iteration loop

---

## 📦 Large File Handling

- Compress >50MB with gzip
- If still >100MB → delegate to Manus for further compression
- Restore: decompress with gunzip

---

## 🎯 Command Recognition

| Pattern | Action |
|---------|--------|
| `BACKUP & CONTINUE` | Execute backup |
| `RESTORE {ID}` | Execute restore |
| `CROSS-RESTORE:` | Execute cross-restore |
| `LIST BACKUPS` | Query registry |