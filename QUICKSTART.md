# 🚀 Quick Start Guide

Get Mission Control running in **5 minutes**.

---

## Step 1: Install Dependencies

```bash
cd mission-control
npm install
```

## Step 2: Set Up Convex

```bash
npx convex login    # Login with GitHub
npx convex dev      # Start backend (keep this running!)
```

This auto-creates your `.env.local` with deployment credentials.

## Step 3: Start Frontend

**In a new terminal:**

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

## Step 4: Seed Data

Click **"DEPLOY AGENT SQUAD"** button on the page, or run:

```bash
npx convex run seed:seed
```

## Step 5: Test API

```bash
curl -X POST http://localhost:3000/api/heartbeat \
  -H "Content-Type: application/json" \
  -d '{"name":"MyAgent","status":"active","currentTask":"Testing"}'
```

---

## ✅ You're Ready!

Your dashboard is live. Now:

1. **Customize agents** in `convex/seed.ts`
2. **Add metrics** in `src/components/MetricsBar.tsx`
3. **Integrate your agents** via the [HTTP API](README.md#-http-api-endpoints)
4. **Deploy to production** with `npx convex deploy && vercel --prod`

---

## 📚 Next Steps

- **Full Setup Guide:** [docs/SETUP.md](docs/SETUP.md)
- **Configuration:** [docs/CONFIGURATION.md](docs/CONFIGURATION.md)
- **Deployment:** [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)
- **Customization:** [docs/CUSTOMIZATION.md](docs/CUSTOMIZATION.md)

## 🤖 What Are the Default Agents?

Mission Control ships with **five specialist agents** and **one orchestrator** — pre-configured profiles optimized for specific work types. Each agent connects to your Mission Control dashboard via the API to track status, log activities, and update tasks in real-time.

**Specialists:**
- **[Forge](docs/agents/forge.md)** — Code builder (picks up engineering tasks, writes code, opens PRs)
- **[Scout](docs/agents/scout.md)** — Research specialist (validates assumptions, competitive intel)
- **[Ghost](docs/agents/ghost.md)** — Outreach operator (email campaigns, partnerships)
- **[Closer](docs/agents/closer.md)** — Sales execution (qualifies leads, sends proposals)
- **[Hype](docs/agents/hype.md)** — Content engine (social posts, launch announcements)

**Coordinator:**
- **[Orchestrator](docs/agents/orchestrator.md)** — Traffic manager (routes work, monitors health, keeps tasks current)

**Start with one specialist** based on your immediate need, then add the Orchestrator to coordinate multi-agent workflows. Full playbooks and copy/paste cron jobs in [docs/agents/](docs/agents/).

---

## 🆘 Troubleshooting

**"Convex deployment not found"**
- Make sure `npx convex dev` is running

**Port 3000 in use**
```bash
PORT=3001 npm run dev
```

**Empty dashboard**
- Click "DEPLOY AGENT SQUAD" or run `npx convex run seed:seed`

---

**Happy building!** 🎯
