# 🔄 CONTINUATION PROMPT v3.0

**Session ID:** {{SESSION_ID}}  
**Session Name:** {{SESSION_NAME}}  
**Backup Date:** {{BACKUP_DATE}}  
**Backup Type:** {{BACKUP_TYPE}} *(manual | auto-hourly | error-recovery)*  
**GitHub Location:** https://github.com/omarzsalah1/manus-task-backups/tree/main/backups/{{BACKUP_FOLDER}}  
**Notion Page:** {{NOTION_URL}}

---

## 📋 QUICK RESTORE

```bash
RESTORE {{SESSION_ID}}
```

### Manual Full Restoration
```bash
gh repo clone omarzsalah1/manus-task-backups ~/manus-task-backups 2>/dev/null || (cd ~/manus-task-backups && git pull)
cp -r ~/manus-task-backups/backups/{{BACKUP_FOLDER}}/sandbox/* ~/
cd ~/manus-task-backups/backups/{{BACKUP_FOLDER}} && bash restore-env.sh 2>/dev/null || echo "Env restored"
echo "✅ Session '{{SESSION_ID}}' restored successfully!"
```

---

## 🎯 TASK OBJECTIVE

{{TASK_OBJECTIVE}}

---

## ✅ COMPLETED WORK

{{WORK_COMPLETED}}

---

## 🔲 DETAILED ROADMAP / TODO LIST

### 🔴 High Priority
| Task | Est. Time | Dependencies | Acceptance Criteria | Risk |
|------|-----------|--------------|---------------------|------|
{{TODO_HIGH_PRIORITY_TABLE}}

### 🟡 Medium Priority
| Task | Est. Time | Dependencies | Acceptance Criteria | Risk |
|------|-----------|--------------|---------------------|------|
{{TODO_MEDIUM_PRIORITY_TABLE}}

### 🟢 Low Priority / Nice to Have
| Task | Est. Time | Dependencies | Acceptance Criteria | Risk |
|------|-----------|--------------|---------------------|------|
{{TODO_LOW_PRIORITY_TABLE}}

### ⏸️ Blocked / Waiting
| Task | Blocked By | Expected Resolution |
|------|------------|---------------------|
{{TODO_BLOCKED_TABLE}}

---

## 🚨 MISTAKES & LESSONS LEARNED

### What Went Wrong
| Mistake | What Happened | Lesson Learned | Time Lost |
|---------|---------------|----------------|-----------|
{{MISTAKES_TABLE}}

### Failed Approaches
| Approach Tried | Why It Failed | Better Approach |
|----------------|---------------|-----------------|
{{FAILED_APPROACHES_TABLE}}

### Time Sinks to Avoid
{{TIME_SINKS}}

---

## 📝 USER INSTRUCTIONS & PREFERENCES

### Explicit Instructions Given
{{USER_INSTRUCTIONS}}

### Discovered Preferences
| Preference | How Discovered | Application |
|------------|----------------|-------------|
{{USER_PREFERENCES_TABLE}}

### Key Decision Points
| Decision | User Choice | Rationale | Date |
|----------|-------------|-----------|------|
{{DECISION_POINTS_TABLE}}

---

## 💡 INSIGHTS & DISCOVERIES

### Technical Insights
| Insight | Context | Future Application |
|---------|---------|-------------------|
{{TECHNICAL_INSIGHTS_TABLE}}

### Domain Knowledge Acquired
{{DOMAIN_KNOWLEDGE}}

### Best Practices Learned
| Practice | When to Apply | Why It Works |
|----------|---------------|--------------|
{{BEST_PRACTICES_TABLE}}

### Patterns Identified
{{PATTERNS}}

---

## 📋 DECISION LOG

| Date | Decision | Options Considered | Rationale | User Approved |
|------|----------|-------------------|-----------|---------------|
{{DECISION_LOG_TABLE}}

---

## ⚠️ BLOCKERS & WARNINGS

### Known Issues (Unresolved)
| Issue | Impact | Workaround | Priority |
|-------|--------|------------|----------|
{{KNOWN_ISSUES_TABLE}}

### Things to Avoid (Anti-Patterns)
{{ANTI_PATTERNS}}

### Edge Cases Discovered
| Edge Case | How to Handle | Notes |
|-----------|---------------|-------|
{{EDGE_CASES_TABLE}}

### Potential Future Problems
{{FUTURE_PROBLEMS}}

---

## 💬 COMMUNICATION SUMMARY

### Key Questions from User
| Question | Answer/Resolution | Date |
|----------|-------------------|------|
{{USER_QUESTIONS_TABLE}}

### Scope Changes
| Original Scope | Changed To | Reason | Date |
|----------------|------------|--------|------|
{{SCOPE_CHANGES_TABLE}}

### Important Clarifications
{{CLARIFICATIONS}}

### User Feedback Received
{{USER_FEEDBACK}}

---

## 📁 FILE INVENTORY

### Project Files
{{FILE_INVENTORY_PROJECT}}

### Configuration Files
{{FILE_INVENTORY_CONFIG}}

### Assets (Images, Data, etc.)
{{FILE_INVENTORY_ASSETS}}

### Key Files to Reference
| File | Purpose | When to Use |
|------|---------|-------------|
{{KEY_FILES_TABLE}}

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

### Working Directory
```
{{WORKING_DIRECTORY}}
```

---

## 🔗 EXTERNAL RESOURCES

### APIs & Services Used
| Service | Purpose | Auth Method | Notes |
|---------|---------|-------------|-------|
{{APIS_SERVICES_TABLE}}

### Documentation Links
{{DOC_LINKS}}

### Related Previous Sessions
| Session ID | Relationship | Key Learnings |
|------------|--------------|---------------|
{{RELATED_SESSIONS_TABLE}}

---

## 💡 CONTINUATION SUGGESTIONS

### Recommended First Steps
1. {{FIRST_STEP_1}}
2. {{FIRST_STEP_2}}
3. {{FIRST_STEP_3}}

### What to Review First
{{REVIEW_FIRST}}

### Potential Pitfalls
{{PITFALLS}}

### Alternative Approaches to Consider
{{ALTERNATIVES}}

---

## 📊 SESSION METADATA

| Field | Value |
|-------|-------|
| Session ID | `{{SESSION_ID}}` |
| Category | {{CATEGORY}} |
| Created | {{CREATED_DATE}} |
| Last Backup | {{BACKUP_DATE}} |
| Backup Count | {{BACKUP_COUNT}} |
| Total Files | {{TOTAL_FILES}} |
| Sandbox Size | {{SANDBOX_SIZE}} |
| Completion % | {{COMPLETION_PCT}} |
| TODO Items | {{TODO_COUNT}} ({{TODO_HIGH}} high, {{TODO_MEDIUM}} medium, {{TODO_LOW}} low) |

---

## 🔍 CONTEXT FOR AI CONTINUATION

### What This Task Is About
{{TASK_CONTEXT}}

### What Was Accomplished
{{ACCOMPLISHMENTS}}

### What the User Needs Next
{{USER_NEEDS_NEXT}}

### Key Success Factors
{{SUCCESS_FACTORS}}

### Potential Issues to Watch
{{ISSUES_TO_WATCH}}

---

## 📝 QUICK REFERENCE

**Context ID**: {{SESSION_ID}}  
**Session**: {{SESSION_NAME}}  
**Status**: {{STATUS}}  
**Main Deliverable**: {{MAIN_DELIVERABLE}}  
**Verification**: {{VERIFICATION_STATUS}}  
**TODO**: {{TODO_COUNT}} items ({{TODO_HIGH}} high, {{TODO_MEDIUM}} medium, {{TODO_LOW}} low)

**Restore Command**: `RESTORE {{SESSION_ID}}`

---

**Backup Created**: {{BACKUP_TIMESTAMP}}  
**Backup ID**: {{SESSION_ID}}  
**GitHub Path**: omarzsalah1/manus-task-backups/backups/{{BACKUP_FOLDER}}

---

*This continuation package contains everything needed to seamlessly resume work, including institutional knowledge, lessons learned, and detailed roadmaps.*
