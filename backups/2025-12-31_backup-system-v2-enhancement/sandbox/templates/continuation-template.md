# 🔄 CONTINUATION PROMPT

**Task:** {{TASK_NAME}}  
**Backup Date:** {{BACKUP_DATE}}  
**Backup ID:** {{BACKUP_ID}}  
**GitHub Backup Location:** https://github.com/omarzsalah1/manus-task-backups/tree/main/backups/{{BACKUP_FOLDER}}

---

## 📋 INSTRUCTIONS FOR MANUS

**IMPORTANT:** This is a continuation of a previous task. Please follow these steps:

### Step 1: Clone and Restore Backup
```bash
gh repo clone omarzsalah1/manus-task-backups ~/manus-task-backups
cp -r ~/manus-task-backups/backups/{{BACKUP_FOLDER}}/sandbox/* ~/
```

### Step 2: Review Context Below and Resume Work

---

## 🎯 ORIGINAL TASK OBJECTIVE

{{TASK_OBJECTIVE}}

---

## ✅ WORK COMPLETED

{{WORK_COMPLETED}}

---

## 🔲 REMAINING WORK

{{REMAINING_WORK}}

---

## 📁 FILE INVENTORY

### Files Created/Modified During This Task:

{{FILE_INVENTORY}}

### Key Files to Note:

{{KEY_FILES}}

---

## 🔧 ENVIRONMENT & DEPENDENCIES

{{ENVIRONMENT_NOTES}}

---

## ⚠️ IMPORTANT CONTEXT & NOTES

{{IMPORTANT_NOTES}}

---

## 🔗 EXTERNAL RESOURCES & LINKS

{{EXTERNAL_RESOURCES}}

---

## 💡 SUGGESTIONS FOR CONTINUATION

{{SUGGESTIONS}}

---

## 📥 QUICK RESTORE COMMAND

Copy and paste this entire block to restore the workspace:

```bash
# Clone backup repository
gh repo clone omarzsalah1/manus-task-backups ~/manus-task-backups 2>/dev/null || (cd ~/manus-task-backups && git pull)

# Restore sandbox files
cp -r ~/manus-task-backups/backups/{{BACKUP_FOLDER}}/sandbox/* ~/

# Verify restoration
echo "✅ Workspace restored from backup: {{BACKUP_FOLDER}}"
ls -la ~/
```

---

**Ready to continue? Just paste this entire prompt into a new Manus session!**
