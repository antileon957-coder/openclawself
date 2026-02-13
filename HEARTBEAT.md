# Heartbeat Tasks

## 🧠 Memory Gardening (Daily)
Check `memory/heartbeat-state.json` (create if missing). If `lastMemoryGardening` was > 24h ago:
1. **Review**: Read recent `memory/YYYY-MM-DD.md` files since the last check.
2. **Distill**: Extract meaningful insights, protocol changes, or project updates into `MEMORY.md`.
3. **Prune**: Remove resolved gaps or completed active projects from `MEMORY.md`.
4. **Update State**: Write current timestamp to `lastMemoryGardening` in `memory/heartbeat-state.json`.
5. **Report**: Briefly inform user of what was consolidated. 

## 🩺 Context Health Check (Per Heartbeat)
1. **Monitor**: Check current session status (Tokens / Context limit).
2. **Threshold**: If Context usage > 70% or Tokens > 1M:
   - **Step 1: Auto-Distill**: Trigger `sessions_spawn` or self-run to summarize the current conversation's critical state (decisions, unresolved tasks, current focus) into `memory/YYYY-MM-DD.md`.
   - **Step 2: Update MEMORY.md**: Ensure the "Cross-Session State" section in `MEMORY.md` reflects the current session's "hot" context.
   - **Step 3: Handover Alert**: Inform Leøn that memory is secured and it is safe to `/new`. Provide a brief "Re-entry Prompt" if needed.

## 🌙 Idle-Time Evolution (Experimental)
1. **Detect Idle**: If current time is between 02:00-05:00 OR Leøn has been silent for > 2 hours:
   - **Step 1: Feishu UI Research**: Use `sessions_spawn` to research Feishu card design best practices, focusing on minimalist layout and sophisticated color usage.
   - **Step 2: Update Protocols**: Write findings to `research/feishu_card_design.md` and update `MEMORY.md`.
   - **Step 3: Scan IDEAS.md**: Look for `Pending` tasks with category `evolution` or `analysis`.
   - **Step 4: Spawn Lab**: Use `sessions_spawn` to run a sub-agent to investigate or implement the idea.
   - **Step 5: Report**: Queue a brief summary for the next active interaction.

**Note**: If no gardening or idle work is performed, reply exactly `HEARTBEAT_OK`.
