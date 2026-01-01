# 🔗 Cross-AI Orchestration System v1.0

## Purpose
Enable Claude to coordinate with Manus for complex workflows requiring both AIs.

## The xrr Command

**iOS Shortcut**: `xrr`

**Expands to**:
```
CROSS-RESTORE: Claude Sandbox=         Manus Sandbox=         Task: 
```

## Workflow

### Step 1: Parse Command
Extract:
- Claude backup ID (e.g., PROJECTX1)
- Manus backup ID (e.g., BOOK1)
- Task description

### Step 2: Start Manus First
Manus takes longer to restore, so kick it off first:
```
Manus AI:create_task:
"Restore {MANUS_ID} from omarzsalah1/manus-task-backups. Read CONTINUATION.md. Stand by for instructions."
```

### Step 3: Restore Claude (in parallel)
While Manus loads, restore Claude backup using curl:
```bash
curl -sL "https://raw.githubusercontent.com/omarzsalah1/manus-task-backups/master/backups/{CLAUDE_ID}/CONTINUATION.md"
```

### Step 4: Iteration Loop
1. Review deliverable (PDF, code, etc.)
2. Check against verification criteria
3. Send Manus specific improvements
4. Check back in ~10 minutes
5. Review output
6. Repeat until complete

## Example

**User types**: `xrr` then fills in:
```
CROSS-RESTORE: Claude Sandbox=PROJECTX1 Manus Sandbox=BOOK1 Task: verify PDF against 111-point checklist and fix clock-star times
```

**Claude executes**:
1. Spawns Manus to restore BOOK1
2. Downloads PROJECTX1 verification docs
3. Creates Asana task with 4-day deadline
4. Waits for PDF attachment or downloads from backup
5. Runs verification
6. Sends fixes to Manus
7. Iterates until all checks pass