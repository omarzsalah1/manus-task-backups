# 🎯 BACKUP & CONTINUE v2.0 - Trigger Phrases

## 📱 iOS/macOS Shortcuts Commands

Copy these phrases to your Shortcuts app for quick access.

---

## 1️⃣ FULL BACKUP & CONTINUE (Primary Command)

```
BACKUP & CONTINUE: Create a comprehensive continuation package for session "[SESSION_NAME]":
1. Back up ALL sandbox files to GitHub (omarzsalah1/manus-task-backups)
2. Capture environment (pip packages, npm packages, system packages)
3. Generate detailed CONTINUATION.md with:
   - Explicit details of everything completed
   - ROADMAP/TODO list (High/Medium/Low priority + Blocked items)
   - Full file inventory with paths
   - One-command restoration instructions
   - Environment/dependency notes
   - Suggestions for seamless continuation
4. Update Notion backup page with session documentation
5. Create Notion tasks for any incomplete TODO items
6. Push everything to a dated folder in backups/
```

**Short Version:**
```
BACKUP & CONTINUE [SESSION_NAME]: Full backup with TODO tracking and Notion sync.
```

---

## 2️⃣ CHECKPOINT (Mid-Task Save)

```
CHECKPOINT [SESSION_NAME]: Save current progress snapshot:
- Quick backup of current sandbox state
- Update session registry
- Note current progress point
- No full documentation (faster)
```

---

## 3️⃣ ERROR BACKUP (On Failure)

```
ERROR BACKUP [SESSION_NAME]: Something went wrong - create error recovery package:
- Full sandbox backup for debugging
- Capture error logs and stack traces
- Document what was attempted
- Note the failure point
- Suggestions for debugging
```

---

## 4️⃣ RESTORE SESSION (Resume Work)

```
RESTORE SESSION [SESSION_ID]: Pull from GitHub and restore full environment:
- Clone/pull manus-task-backups repo
- Copy sandbox files to home directory
- Reinstall all packages (pip, npm, apt)
- Load environment variables
- Verify restoration
- Display session context
```

**Example:**
```
RESTORE SESSION continuation-skill-v2: Pull and restore full environment.
```

---

## 5️⃣ LIST SESSIONS (View All Backups)

```
LIST SESSIONS: Show all available backup sessions from registry with:
- Session ID and name
- Backup date
- Status (complete/active/error)
- Quick restore command
```

---

## 📋 Session Naming Convention

When using these commands, replace `[SESSION_NAME]` with a descriptive identifier:

| Format | Example |
|--------|---------|
| `project-feature` | `website-redesign` |
| `client-task` | `acme-api-integration` |
| `type-description` | `data-analysis-q4` |

**Rules:**
- Use lowercase with hyphens
- Keep under 30 characters
- Be descriptive but concise

---

## 🔄 Auto-Triggers (Automatic)

These happen automatically when enabled:

| Trigger | When | Action |
|---------|------|--------|
| **Hourly Checkpoint** | Every 2 hours during long tasks | Quick snapshot backup |
| **Error Recovery** | On task failure | Full backup with error context |

---

## 📍 Quick Reference Card

| Action | Short Command |
|--------|---------------|
| Full Backup | `BACKUP & CONTINUE [name]` |
| Quick Save | `CHECKPOINT [name]` |
| Error Save | `ERROR BACKUP [name]` |
| Restore | `RESTORE SESSION [id]` |
| List All | `LIST SESSIONS` |

---

## 🔗 Resources

- **GitHub:** https://github.com/omarzsalah1/manus-task-backups
- **Notion:** https://www.notion.so/2dbff518007781239528f3298aaecd79

---

*Enhanced Backup & Continue System v2.0 - Manus AI*
