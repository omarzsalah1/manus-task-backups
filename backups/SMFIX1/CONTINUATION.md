# SMFIX1 - Supermemory Recall Fix

## Session ID
SMFIX1

## Category
BUGFIX

## Priority
HIGH - Blocking T5 test completion

## Problem Statement
Supermemory `memory` (save) works, but `recall` returns empty content despite showing match percentages.

## Symptoms
1. Save works: `memory` action returned ID: syDbKeQqZpkfQkmxpWh4Yi
2. Recall broken: Query returns "Memory 1 (77% match)" but content is BLANK
3. Profile summary populates correctly
4. Individual memory contents don't display

## Test Evidence

### Save (WORKED)
```json
{
  "action": "save",
  "content": "XRR Protocol Test Results 2026-01-03: All core tests passed..."
}
// Result: Saved memory (id: syDbKeQqZpkfQkmxpWh4Yi) in sm_project_default project
```

### Recall (BROKEN)
```json
{
  "query": "XRR protocol test results"
}
// Result: 
// ### Memory 1 (77% match)
// [EMPTY - no content displayed]
// ### Memory 2 (70% match)
// [EMPTY - no content displayed]
```

## Available Tools
- `mcp-supermemory-ai:memory` - save/forget
- `mcp-supermemory-ai:recall` - search
- `mcp-supermemory-ai:whoAmI` - user info
- `api-supermemory-ai:addMemory` - alternative save
- `api-supermemory-ai:search` - alternative search

## TODO

| Priority | Task |
|----------|------|
| HIGH | Test alternative API tools (api-supermemory-ai:search) |
| HIGH | Check if whoAmI returns valid user/project |
| HIGH | Try saving and immediately recalling same content |
| MEDIUM | Check if containerTag parameter helps |
| MEDIUM | Compare mcp-supermemory-ai vs api-supermemory-ai behavior |

## Hypothesis
Possible causes:
1. Indexing delay - memories saved but not yet searchable
2. Project scoping issue - saved to wrong project
3. API response parsing - content field not being extracted
4. Tool version mismatch between save/recall endpoints

## Success Criteria
- Save a memory with known content
- Recall that memory and see the ACTUAL CONTENT displayed
- Document which tool combination works

## Restore Command
```
pickup SMFIX1
```
