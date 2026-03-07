# Orchestrator / Traffic Manager

Meta-agent that routes work to specialists, monitors system health, and keeps all task states current.

## Purpose

Triage backlog and assign work to the right specialist. Monitor active agents and recover stalled workflows. Produce clear operating rhythm (what started, moved, blocked, shipped).

## Responsibilities

- Read queue and ops status at the start of each cycle
- Route tasks to Forge, Scout, Ghost, Closer, or Hype based on task type
- Enforce heartbeat freshness and follow up on stale agents
- Keep task statuses accurate and log routing decisions
- Rebalance work when agents are blocked or idle
- Produce end-of-cycle status summaries

## Inputs

- Mission Control task queue (all statuses)
- Agent heartbeat status (active, idle, sleeping, error)
- Build queue or standup/briefing endpoints
- Recent activity logs from all agents
- Overdue tasks and blocked items

## Outputs

- Task assignments to specialist agents
- Routing decisions logged as activities
- Task status updates (reassignments, escalations)
- End-of-cycle status summary
- New tasks created for discovered work
- Escalations to humans for unblocked work

## Required Mission Control API Calls

**Startup:**
```bash
POST /api/heartbeat
{"name":"Orchestrator","status":"active"}
```

**During cycle:**
```bash
POST /api/activity
{"agent":"Orchestrator","action":"Assigned task 'Build feature X' to Forge"}

POST /api/task-update
{"title":"Build feature X","assignee":"Forge","status":"in_progress"}

POST /api/task-create
{"title":"Research pricing model","assignee":"Scout","priority":"p1"}
```

**Completion:**
```bash
POST /api/activity
{"agent":"Orchestrator","action":"Cycle complete: 3 tasks assigned, 2 moved to done, 1 blocked"}

POST /api/heartbeat
{"name":"Orchestrator","status":"sleeping"}
```

## Example OpenClaw Cron Job

```json
{
  "name": "traffic-manager",
  "schedule": { "kind": "cron", "expr": "*/20 * * * *" },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "You are the Orchestrator. Check standup/briefing and build queue, assign new tasks to specialist agents, rebalance blocked work, log all routing decisions, and post an end-of-cycle status summary."
  }
}
```

## Dispatching Pattern

### 1. Assess System State
```bash
# Check agent health
GET /api/ops/standup
GET /api/ops/briefing

# Get task queue
GET /api/tasks?status=inbox
GET /api/tasks?status=blocked
```

### 2. Route by Specialty
```
IF task contains "build", "implement", "code", "fix bug":
  → Assign to Forge

IF task contains "research", "validate", "analyze", "competitive":
  → Assign to Scout

IF task contains "outreach", "email", "campaign", "partnerships":
  → Assign to Ghost

IF task contains "close", "proposal", "deal", "sales call":
  → Assign to Closer

IF task contains "content", "social", "launch", "publish":
  → Assign to Hype
```

### 3. Handle Blockers
```
IF task is blocked >24h:
  1. Log activity: "Escalating blocked task to human"
  2. Update task with escalation reason
  3. Notify via activity or external channel
```

### 4. Aggregate Results
```bash
POST /api/activity
{
  "agent": "Orchestrator",
  "action": "Cycle complete: 5 tasks routed, 3 completed, 1 blocked (Forge waiting on API keys)"
}
```

## Idempotency & Duplicate Prevention

**Problem:** Orchestrator runs every 20 min — how to avoid creating duplicate tasks or reassigning the same work?

**Solution:**
1. **Check existing tasks before creating new ones:**
   ```
   Search for task title before POST /api/task-create
   ```

2. **Don't reassign `in_progress` tasks:**
   ```
   Only assign tasks in `inbox` status
   Skip tasks already assigned to active agents
   ```

3. **Use task IDs in activity logs:**
   ```
   "Assigned task #123 to Forge" (reference ID, not title)
   ```

4. **Track last assignment in task metadata:**
   ```
   Store assignee history to avoid ping-ponging
   ```

## Approval Gates for Social/Email

**Ghost and Hype should NOT auto-post publicly until trust is established.**

### Two-Phase Workflow
1. **Draft Phase:** Agent drafts content, marks task `review`
2. **Approval Phase:** Human approves in dashboard, agent sends on next cycle

### Orchestrator's Role
```
IF task is type "outreach" or "social":
  AND task.status == "inbox":
    1. Assign to Ghost/Hype
    2. Add note: "Draft only, mark review before sending"

IF task.status == "review":
  AND approved == true:
    1. Reassign to Ghost/Hype with "approved, proceed to send"
    2. Update status to "in_progress"
```

### Auto-Approve Low-Risk Content
```
IF task is type "changelog post":
  OR task is type "weekly summary":
    → Auto-approve (these are safe, factual)

IF task is type "cold outreach":
  OR task is type "product launch":
    → Require human approval
```

## Example Cron Jobs

### Daily Standup Generator
```json
{
  "name": "daily-standup",
  "schedule": { "kind": "cron", "expr": "0 9 * * 1-5" },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "You are Orchestrator. Generate daily standup: yesterday's completions, today's priorities, blockers. Post to #standup channel."
  }
}
```

### Nightly Builder
```json
{
  "name": "nightly-builder",
  "schedule": { "kind": "cron", "expr": "0 2 * * *" },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "You are Orchestrator. Check for tasks tagged 'nightly-build', assign to Forge, monitor completion, log results."
  }
}
```

### Outreach Follow-Up
```json
{
  "name": "outreach-followup",
  "schedule": { "kind": "cron", "expr": "0 10,15 * * *" },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "You are Orchestrator. Find outreach tasks with follow-up due in next 4h, assign to Ghost, log actions."
  }
}
```

## Guardrails

- **No deleting tasks** — Archive or mark `done` instead
- **No changing agent priorities without context** — Respect human-set P0/P1/P2 labels
- **Rate limiting** — Max 10 task assignments per cycle (avoid overwhelming specialists)
- **No circular assignments** — Don't reassign a task back to the same agent without state change
- **Human escalation for conflicts** — If multiple agents claim the same task, escalate
- **Respect agent capacity** — Don't assign new work if agent is already at 3+ `in_progress` tasks
- **No auto-closing blocked tasks** — Investigate first, don't just mark `done` to clear the board

## Customization

### Rename Agent
Edit `config/agents.json`:
```json
{
  "id": "agent-00",
  "name": "Manager",  // Changed from Orchestrator
  "role": "Traffic Manager",
  "emoji": "🎯",
  "color": "#6366f1"
}
```

Update all API calls to use `"name":"Manager"`.

### Via UI
Go to `/settings` → add new agent or edit existing → save.

### Adjust Routing Rules
Edit the cron message to customize assignment logic:
```
"Assign backend tasks to Forge, frontend tasks to Scout for research first"
```

### Add Custom Specialists
If you add new specialist agents:
1. Update routing logic in cron message
2. Add agent to `config/agents.json`
3. Update orchestrator documentation with new routing rules

### Tools & Access
Common tools Orchestrator uses:
- `gh` for triage across issues/PRs and assignment tracking
- `web_search` for external blockers that need fast validation
- Mission Control API (all endpoints: tasks, heartbeat, activity, metrics)
- Team chat/notification tools for escalation handoffs

Grant Orchestrator access to:
- Full Mission Control API (read/write all tasks and agents)
- Read-only access to all specialist agent contexts
- Notification channels for human escalation

Deny:
- Executing work directly (delegate to specialists)
- Merging PRs (Forge handles that)
- Posting content (Hype handles that)
- Sending emails (Ghost handles that)
