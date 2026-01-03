# SMFIX1 - Supermemory Recall Fix

## Session ID
SMFIX1

## Status
✅ DIAGNOSED - API BUG CONFIRMED

## Problem Statement
Supermemory `memory` (save) works, but `recall` returns empty content despite showing match percentages.

## DIAGNOSIS RESULTS

### Test Performed
1. Saved test memory with unique keywords: "purple elephant flying submarine"
2. Memory ID returned: CGdjRzFvmqtpEcQb2TyXj9
3. Immediate recall with same keywords: "No memories found"
4. Recall with includeProfile=true: REVEALED THE BUG

### What Works
- `mcp-supermemory-ai:memory` save → Returns ID ✅
- `mcp-supermemory-ai:recall` User Profile section → Returns summarized facts ✅
- `mcp-supermemory-ai:recall` Match percentages → Shows 84%, 83%, etc. ✅
- `api-supermemory-ai:search` → Returns profile summaries ✅

### What's Broken
- `mcp-supermemory-ai:recall` Memory Content → EMPTY despite match percentages ❌

### Evidence
Profile section correctly shows:
```
- The Supermemory recall diagnostic test is identified as SMFIX1 TEST.
- The Supermemory recall diagnostic test utilizes keywords "purple elephant flying submarine".
- SMFIX1 TEST is scheduled for 2026-01-03 12:15 UTC.
```

But Memory sections show:
```
### Memory 1 (84% match)
[EMPTY]
### Memory 2 (83% match)
[EMPTY]
```

## Root Cause
Supermemory API response format strips actual memory content from the "Relevant Memories" section while correctly:
1. Storing the memory
2. Indexing it for search
3. Calculating match scores
4. Extracting facts to User Profile

## Workaround
Use `includeProfile=true` and rely on the User Profile section for distilled facts from memories. Not ideal for verbatim recall but functional for context.

## Recommendation
1. Report bug to Supermemory team
2. For critical persistence, use GitHub handoffs (100% reliable)
3. Use Supermemory for contextual facts, not verbatim storage

## Pickup Command
```
pickup SMFIX1
```
