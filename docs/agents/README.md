# Agent Playbooks

Mission Control ships with five default specialist agents and one orchestrator/traffic manager. Each agent is a pre-configured profile optimized for a specific type of work. Use them as-is, customize them, or build your own following the same patterns.

## Default Agents

- **[Forge](forge.md)** — Code builder. Picks up engineering tasks, writes code, runs tests, opens PRs.
- **[Scout](scout.md)** — Research specialist. Validates assumptions, finds competitive intel, feeds actionable data to other agents.
- **[Ghost](ghost.md)** — Outreach operator. Runs email campaigns, prospecting, partnerships, and demand generation.
- **[Closer](closer.md)** — Sales execution. Qualifies leads, runs discovery, sends proposals, moves deals to closed-won.
- **[Hype](hype.md)** — Content engine. Turns product updates into social posts, threads, launch announcements.
- **[Orchestrator](orchestrator.md)** — Traffic manager. Routes work to specialists, monitors health, keeps task states current.

## How They Work Together

```
Orchestrator  →  Routes tasks to specialists
                 ↓
Scout         →  Research findings  →  Forge (build), Ghost (outreach), Hype (content)
Forge         →  Ships code         →  Hype (launch content)
Ghost         →  Qualified leads    →  Closer (close deals)
Closer        →  Customer feedback  →  Scout (research), Forge (feature requests)
Hype          →  Published content  →  Ghost (distribution)
```

**Example workflow:**
1. Orchestrator assigns "Research competitor pricing" to Scout
2. Scout delivers findings → creates task "Build pricing page" for Forge
3. Forge ships pricing page → creates task "Launch announcement" for Hype
4. Hype publishes launch thread → Ghost uses it for outreach campaign
5. Ghost qualifies leads → Closer closes deals

## When to Use Each Agent

| Task Type | Agent | Why |
|-----------|-------|-----|
| Build feature, fix bug, refactor code | **Forge** | Engineering work |
| Validate product idea, competitive analysis | **Scout** | Research and evidence |
| Cold email, partnerships, community outreach | **Ghost** | Top-of-funnel motion |
| Sales calls, proposals, deal negotiation | **Closer** | Bottom-of-funnel conversion |
| Social posts, launch content, changelogs | **Hype** | Audience-facing narratives |
| Triage backlog, route work, monitor health | **Orchestrator** | Meta-level coordination |

## Quick Start

### 1. Pick an Agent
Start with **one** specialist based on your immediate need:
- Building product? Start with **Forge**
- Need market validation? Start with **Scout**
- Growing audience? Start with **Hype**

### 2. Set Up Cron Job
Copy the example cron job from the agent's doc and customize the schedule/message.

### 3. Watch Mission Control
Your agent will:
- Send heartbeat (shows as "active" in dashboard)
- Log activities (audit trail)
- Update task statuses (move through pipeline)

### 4. Add More Agents
Once one agent works smoothly, add complementary specialists and use the **Orchestrator** to route between them.

## Customization

### Rename Agents
Edit `config/agents.json` or use the `/settings` UI in your dashboard. Keep API calls consistent with new names.

### Adjust Run Frequency
Change the cron schedule:
- `*/30 * * * *` = every 30 minutes
- `0 9 * * 1-5` = 9am weekdays only
- `0 */4 * * *` = every 4 hours

### Filter Task Assignment
Add filters to cron messages:
```
"Pick one P0 task tagged 'backend' assigned to Forge..."
```

### Add Approval Gates
For sensitive operations (social posts, email blasts), add human review:
```
"Draft content and mark task 'review' for approval before posting"
```

## Safety & Guardrails

Every agent doc includes a **Guardrails** section with:
- Rate limits (avoid API spam)
- Approval requirements (what needs human review)
- Privacy rules (no sharing sensitive data)
- Platform compliance (ToS, GDPR, CAN-SPAM)

**Default stance:** Agents draft, humans approve. Once trust is built, enable auto-execution for low-risk tasks.

## Common Patterns

### Two-Phase Workflow (Draft → Approve)
1. Agent drafts work, marks task `review`
2. Human approves in dashboard
3. Agent executes on next run

### Handoff Between Agents
1. Scout completes research → creates task for Forge
2. Forge ships feature → creates task for Hype
3. Hype publishes content → Ghost uses it for outreach

### Orchestrator-Managed Squad
1. Orchestrator triages backlog every 20 min
2. Routes tasks to specialists by type
3. Monitors for blockers and escalates to humans

## Examples

See each agent's doc for:
- **Purpose** — What it's optimized for
- **Responsibilities** — Concrete actions it takes
- **Inputs/Outputs** — What it consumes and produces
- **Example Cron Job** — Copy/paste schedule
- **Guardrails** — Safety and rate limits
- **Customization** — How to adapt it to your workflow

## Next Steps

1. **Read [SKILL.md](../../SKILL.md)** for API reference
2. **Pick one agent** and set up a cron job
3. **Watch it run** in Mission Control dashboard
4. **Add more agents** as needs grow
5. **Use Orchestrator** to coordinate multi-agent workflows

Questions? Open an issue or check [QUICKSTART.md](../../QUICKSTART.md).
