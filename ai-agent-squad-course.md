# AI Agent Squad: Build Your Autonomous Team

## Course Description (for Whop)
The exact system running 5 AI agents 24/7. Mission Control dashboard, agent SOULs, heartbeat coordination, and cron automation. Stop doing everything yourself — build a squad that works while you sleep.

---

## Chapter 1: The Agent Architecture

### Lesson 1: Why Agent Squads Work
Most people try to make one AI do everything. That fails. Here's why specialized agents with clear roles outperform generalists:

- **Single responsibility** — Each agent masters one domain
- **Parallel execution** — Multiple agents work simultaneously  
- **Clear handoffs** — Agents know when to pass work to others
- **Fault isolation** — One agent failing doesn't break everything

The squad: Closer (outreach), Ghost (content), Forge (code), Scout (research), Hype (social).

### Lesson 2: The SOUL.md Pattern
Every agent needs an identity file. This is their personality, skills, and rules. Here's the structure:

```markdown
# SOUL.md — [Agent Name]

## Identity
- Name, role, emoji
- Personality traits
- Communication style

## Skills
- What they're good at
- Tools they use
- Domains they own

## Rules
- What they must always do
- What they must never do
- How they handle edge cases

## Mission Control (MANDATORY)
- Status update commands
- Activity logging
- Task tracking
```

The SOUL.md is loaded at the start of every session. It's how the agent knows who they are.

### Lesson 3: AGENTS.md — The Master Rules
AGENTS.md contains rules ALL agents follow. This is your constitution:

- Memory management (how to persist context)
- Safety rules (what never to do)
- External vs internal actions
- Group chat behavior
- Tool usage patterns

Every agent reads AGENTS.md + their own SOUL.md on startup.

---

## Chapter 2: Mission Control

### Lesson 4: The Dashboard
Mission Control is your real-time view of what all agents are doing:

- Agent status (active/sleeping)
- Current task descriptions
- Activity log (what they did)
- Task board (inbox/in-progress/done)

Built with Next.js + Convex for real-time updates.

### Lesson 5: The Heartbeat API
Agents report status via simple HTTP calls:

```bash
# Agent starts work
curl -X POST 'https://your-api/heartbeat' \
  -d '{"name":"Forge","status":"active","currentTask":"Building feature X"}'

# Agent logs activity
curl -X POST 'https://your-api/activity' \
  -d '{"agent":"Forge","action":"Created PR #42"}'

# Agent finishes
curl -X POST 'https://your-api/heartbeat' \
  -d '{"name":"Forge","status":"sleeping"}'
```

Every agent cron includes these calls. Steven watches the dashboard 24/7.

### Lesson 6: Task Coordination
Tasks flow through the system:

1. Steven adds task to inbox
2. Relevant agent picks it up (based on assignee/skills)
3. Agent moves to in_progress, updates currentTask
4. Agent completes work, logs activity
5. Agent moves task to done or review
6. Next agent picks up if needed

No manual coordination. Agents self-organize based on their SOULs.

---

## Chapter 3: Cron Automation

### Lesson 7: Scheduling Agent Runs
Agents run on cron schedules. Example setup:

- **2:00am** — Forge nightly builder (ships code)
- **7:00am** — Daily email report
- **7:30am** — Squad standup
- **8:00am** — Morning briefing
- **9:15am, 5:15pm** — Closer outreach cycles
- **9:25am, 5:25pm** — Ghost content cycles
- **9:35am, 5:35pm** — Scout research cycles

Each cron triggers an isolated agent session that runs, reports, and sleeps.

### Lesson 8: The Heartbeat Pattern
Between cron runs, agents can be proactive via heartbeats:

1. Main session receives periodic heartbeat poll
2. Agent checks HEARTBEAT.md for tasks
3. If nothing needs attention: `HEARTBEAT_OK`
4. If something's urgent: take action, report

This lets agents stay responsive without running 24/7.

### Lesson 9: Error Handling & Recovery
When things go wrong:

- Rate limits → Stagger cron times, use different model tiers
- Agent stuck "active" → Audit cron cleans up stale statuses
- Task blocked → Agent marks blocked, notifies in next standup
- API failures → Retry logic, fallback models

Build resilience into the system from day one.

---

## Chapter 4: Your Squad

### Lesson 10: Choosing Your Agents
Start with agents that match YOUR needs:

- **Revenue focus** → Closer (outreach) + Ghost (content/SEO)
- **Product focus** → Forge (code) + Scout (research)
- **Growth focus** → Hype (social) + Ghost (content)

You don't need all 5. Start with 2-3 and add as needed.

### Lesson 11: Customizing SOULs
Take the templates and make them yours:

1. Change the personality to match your brand voice
2. Add your specific tools and workflows
3. Define YOUR rules and boundaries
4. Add domain knowledge they need

The SOUL is a living document. Update it as you learn what works.

### Lesson 12: Scaling Up
Once your squad is working:

- Add more specialized agents
- Build agent-to-agent handoffs
- Create shared memory (Supabase pgvector)
- Add feedback loops (track predictions vs outcomes)

The goal: a self-improving system that gets smarter over time.

---

## Downloads

- **ai-agent-squad.zip** — All SOUL templates, AGENTS.md, HEARTBEAT.md
- **Mission Control repo** — Dashboard code (Next.js + Convex)

---

Built by Steven Shoaf
https://shoaf.dev
