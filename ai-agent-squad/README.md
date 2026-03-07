# AI Agent Squad Templates

The exact system running 5 autonomous AI agents 24/7 on Steven's Shoaf Systems.

## What's Included

### Agent SOULs (Identity Files)
- **closer/SOUL.md** — Outreach specialist, handles lead generation
- **ghost/SOUL.md** — Content & SEO writer, creates pages and copy
- **forge/SOUL.md** — Builder, ships code every night at 2am
- **scout/SOUL.md** — Researcher, finds opportunities and intel
- **hype/SOUL.md** — Social media, manages Twitter presence
- **reviewer/SOUL.md** — PR reviewer, checks code quality

### Coordination Files
- **AGENTS.md** — Master rules all agents follow
- **HEARTBEAT.md** — Proactive task list for heartbeat checks

## How It Works

1. Each agent has a SOUL.md defining their personality, skills, and rules
2. Agents run on cron schedules (e.g., Forge at 2am, others throughout day)
3. All agents report to Mission Control dashboard via API
4. HEARTBEAT.md defines what to check during idle moments

## Setup

1. Install OpenClaw (https://openclaw.ai)
2. Create agents/ folder in your workspace
3. Copy these SOULs and customize for your needs
4. Set up crons to run agents on schedule
5. Build your own Mission Control or use the template

## Mission Control API

Agents report status via HTTP:
```bash
curl -X POST 'https://your-api/heartbeat' \
  -d '{"name":"AgentName","status":"active","currentTask":"..."}'
```

Built by Steven Shoaf — shoaf.dev
