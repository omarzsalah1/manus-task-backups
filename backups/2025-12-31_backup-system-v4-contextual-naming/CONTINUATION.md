# 🔄 CONTINUATION PROMPT

**SANDBOX3** | `backup-system-v4-contextual-naming`  
**Session Name:** Manus Backup & Continue System v4.0 - Contextual Naming  
**Backup Date:** 2025-12-31  
**GitHub:** https://github.com/omarzsalah1/manus-task-backups/tree/master/backups/2025-12-31_backup-system-v4-contextual-naming  
**Notion:** https://www.notion.so/1337a26936fd4f4a9e82a30eea20c78d

---

## 📋 QUICK RESTORE

```
RESTORE SANDBOX3
```

---

## 🎯 TASK OBJECTIVE

Develop a comprehensive "Backup & Continue" skill for Manus that enables seamless task continuation across sessions. The system should:
1. Back up all sandbox files to GitHub
2. Generate detailed continuation prompts
3. Use AI-generated contextual shorthand IDs (VACATION1, WEBSITE2, etc.) instead of generic numbering
4. Sync with Notion for structured documentation
5. Support one-command restoration

---

## ✅ COMPLETED WORK

### Phase 1: Initial System Setup (SANDBOX1)
1. Created `manus-task-backups` GitHub repository
2. Built basic backup workflow
3. Created initial CONTINUATION.md template
4. Set up trigger phrase system

### Phase 2: Enhanced Features (SANDBOX2)
1. Added named sandbox sessions with descriptive IDs
2. Implemented environment capture (pip, npm, apt packages)
3. Created one-command restoration script
4. Integrated Notion for backup documentation
5. Added TODO/Roadmap tracking with priority levels

### Phase 3: SANDBOX Shorthand System
1. Implemented SANDBOX{N} shorthand IDs
2. Created collision-proof counter in registry
3. Added RESTORE SANDBOX{N} command
4. Added RESTORE LATEST command
5. Added LIST SANDBOXES command
6. Updated iOS/macOS Shortcuts documentation

### Phase 4: Contextual Naming System (v4.0) ✅
1. Replaced generic "SANDBOX" prefix with AI-generated contextual categories
2. Implemented multi-category counter system:
   - SANDBOX (system/infrastructure)
   - VACATION (travel/trips)
   - WEBSITE (web development)
   - API (integrations)
   - DATA (analysis)
   - REPORT (documents)
   - And 14 more categories
3. Updated registry.json with category-specific counters
4. Updated FULL-IMPLEMENTATION-PLAN.md with complete v4.0 documentation
5. Created BACKUP-COMMANDS.md quick reference
6. Updated iOS Shortcut with contextual naming instructions

---

## 🔲 TODO

### High Priority
- [ ] Test RESTORE command in a new task to verify full restoration
- [ ] Add automatic hourly checkpoint triggers for long tasks
- [ ] Implement error-recovery backup trigger

### Medium Priority
- [ ] Add Google Drive as secondary backup destination
- [ ] Create visual dashboard in Notion for backup overview
- [ ] Add diff view to show changes between backups

### Low Priority
- [ ] Add Slack/email notification on backup completion
- [ ] Create browser extension for quick backup trigger
- [ ] Add backup compression for large sandboxes

---

## 📁 FILES

| File | Description |
|------|-------------|
| `README.md` | Main repository documentation |
| `BACKUP-COMMANDS.md` | Quick reference for all commands |
| `FULL-IMPLEMENTATION-PLAN.md` | Complete v4.0 system documentation |
| `TRIGGER-PHRASE.md` | Original trigger phrase (v1) |
| `TRIGGER-PHRASE-v2.md` | Enhanced trigger phrase (v2) |
| `sessions/registry.json` | Master registry with multi-category counters |
| `config/notion-integration.json` | Notion sync configuration |
| `scripts/capture-env.sh` | Environment capture script |
| `scripts/restore-env.sh` | Environment restoration script |
| `scripts/backup-inventory.sh` | File manifest generator |
| `templates/continuation-template-v2.md` | CONTINUATION.md template |
| `docs/CLAUDE-BACKUP-COMMANDS.md` | Claude-specific backup commands |

---

## 🔧 ENVIRONMENT

- **Python Packages:** 45+ (see requirements.txt)
- **System Packages:** Standard Ubuntu 22.04
- **Node.js:** v22.13.0
- **GitHub CLI:** Configured and authenticated
- **Notion MCP:** Connected

---

## 🏷️ CATEGORY REFERENCE

| Category | Use For |
|----------|---------|
| `SANDBOX` | System tools, Manus configuration |
| `VACATION` | Travel planning, trips |
| `WEBSITE` | Web development |
| `API` | Backend integrations |
| `DATA` | Data analysis |
| `REPORT` | Documents, presentations |
| `PROJECT` | Project management |
| `RESEARCH` | Investigations |
| `CODE` | General coding |
| `DESIGN` | Creative work |
| `FINANCE` | Financial tasks |
| `LEARNING` | Education |
| `AUTOMATION` | Workflows |

---

## 💡 SUGGESTIONS FOR CONTINUATION

1. **Test the System:** Start a new task and run `RESTORE SANDBOX3` to verify the full restoration workflow works correctly.

2. **Try Different Categories:** Start a task about travel planning and run `BACKUP & CONTINUE` to see it generate `VACATION1`.

3. **Enhance Notion Integration:** The Notion database could display a visual timeline of backups with status indicators.

4. **Add Scheduled Backups:** Implement the `schedule` tool to create automatic hourly checkpoints during long tasks.

---

## 🔗 RESOURCES

- **GitHub Repository:** https://github.com/omarzsalah1/manus-task-backups
- **Notion Database:** https://www.notion.so/1337a26936fd4f4a9e82a30eea20c78d
- **Notion Parent Page:** https://www.notion.so/2dbff518007781239528f3298aaecd79

---

## 📱 iOS SHORTCUT

Copy this to your Shortcuts app:

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

**🚀 To restore this session: `RESTORE SANDBOX3`**

---

*Manus Task Backup System v4.0 - Contextual Naming Edition*  
*Backup created: 2025-12-31*
