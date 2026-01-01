# 🔄 CONTINUATION PROMPT v2.0

**Session ID:** {{SESSION_ID}}  
**Session Name:** {{SESSION_NAME}}  
**Backup Date:** {{BACKUP_DATE}}  
**Backup Type:** {{BACKUP_TYPE}} *(manual | auto-hourly | error-recovery)*  
**GitHub Location:** https://github.com/omarzsalah1/manus-task-backups/tree/main/backups/{{BACKUP_FOLDER}}  
**Notion Page:** {{NOTION_URL}}

---

## 📋 RESTORATION INSTRUCTIONS

**IMPORTANT:** This is a continuation of session `{{SESSION_ID}}`. Execute the restoration command below:

### One-Command Full Restoration
```bash
# Full restoration with environment rebuild
gh repo clone omarzsalah1/manus-task-backups ~/manus-task-backups 2>/dev/null || (cd ~/manus-task-backups && git pull)
cp -r ~/manus-task-backups/backups/{{BACKUP_FOLDER}}/sandbox/* ~/
cd ~/manus-task-backups/backups/{{BACKUP_FOLDER}} && bash restore-env.sh
echo "✅ Session '{{SESSION_ID}}' restored successfully!"
```

---

## 🎯 TASK OBJECTIVE

{{TASK_OBJECTIVE}}

---

## ✅ COMPLETED WORK

{{WORK_COMPLETED}}

---

## 🔲 ROADMAP / TODO LIST

### High Priority
{{TODO_HIGH_PRIORITY}}

### Medium Priority
{{TODO_MEDIUM_PRIORITY}}

### Low Priority / Nice to Have
{{TODO_LOW_PRIORITY}}

### Blocked / Waiting
{{TODO_BLOCKED}}

---

## 📁 FILE INVENTORY

### Project Files
{{FILE_INVENTORY_PROJECT}}

### Configuration Files
{{FILE_INVENTORY_CONFIG}}

### Assets (Images, Data, etc.)
{{FILE_INVENTORY_ASSETS}}

### Key Files to Note
{{KEY_FILES}}

---

## 🔧 ENVIRONMENT SNAPSHOT

### Python Packages
```
{{PYTHON_PACKAGES}}
```

### Node.js Packages
```
{{NODE_PACKAGES}}
```

### System Packages Installed
```
{{SYSTEM_PACKAGES}}
```

### Environment Variables
```
{{ENV_VARIABLES}}
```

---

## ⚠️ IMPORTANT CONTEXT & DECISIONS

{{IMPORTANT_CONTEXT}}

### Decisions Made
{{DECISIONS_MADE}}

### Known Issues / Bugs
{{KNOWN_ISSUES}}

---

## 🔗 EXTERNAL RESOURCES

### APIs & Services Used
{{APIS_SERVICES}}

### Documentation Links
{{DOC_LINKS}}

### Related Previous Sessions
{{RELATED_SESSIONS}}

---

## 💡 SUGGESTIONS FOR NEXT SESSION

{{SUGGESTIONS}}

---

## 📊 SESSION METADATA

| Field | Value |
|-------|-------|
| Session ID | `{{SESSION_ID}}` |
| Created | {{CREATED_DATE}} |
| Last Backup | {{BACKUP_DATE}} |
| Backup Count | {{BACKUP_COUNT}} |
| Total Files | {{TOTAL_FILES}} |
| Sandbox Size | {{SANDBOX_SIZE}} |

---

**🚀 Ready to continue? Paste this prompt into a new Manus session!**
