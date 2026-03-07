# AiOrg Mission Control

## Overview
**AiOrg Mission Control** is a real-time dashboard for monitoring and managing AI agents across the AiOrg ecosystem. Built with Next.js 15, Convex, and Tailwind CSS, it provides a centralized command center for all your AI operations.

## Features

### 🎯 Real-time Monitoring
- Live agent status and heartbeat tracking
- Performance metrics (CPU, memory, tasks completed)
- Uptime monitoring with automatic timeout detection

### 🤖 Agent Management
- Register and configure AI agents
- Assign tasks and track progress
- View agent activity history

### 📊 Dashboard
- Interactive charts and visualizations
- Kanban-style task management
- Activity feed with real-time updates

### 🔌 Integration
- REST API for external agent integration
- Webhook support for notifications
- OpenClaw compatibility out of the box

## Quick Start

### Prerequisites
- Node.js 18+ and npm
- Convex account (free tier available)
- Vercel account (free tier available)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/aiorg-app/mission-control.git
   cd mission-control
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env.local
   # Edit .env.local with your configuration
   ```

4. **Set up Convex:**
   ```bash
   npx convex login
   npx convex dev
   ```

5. **Run development server:**
   ```bash
   npm run dev
   ```

6. **Open your browser:**
   Navigate to [http://localhost:3000](http://localhost:3000)

## Deployment

### Deploy to Vercel

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Import to Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Click "Add New" → "Project"
   - Import your GitHub repository
   - Configure environment variables
   - Click "Deploy"

3. **Set up custom domain:**
   - In Vercel project settings, go to "Domains"
   - Add `mission-control.aiorg.app`
   - Configure DNS as instructed

### Deploy Convex Backend

1. **Deploy to production:**
   ```bash
   npx convex deploy --prod
   ```

2. **Update environment variables:**
   - Copy the production Convex URL
   - Update `NEXT_PUBLIC_CONVEX_URL` in Vercel

## Integration with OpenClaw

### For OpenClaw Agents

1. **Copy the SKILL.md file:**
   ```bash
   cp SKILL.md ~/.openclaw/skills/mission-control/
   ```

2. **Configure OpenClaw:**
   Add to your `openclaw.json`:
   ```json
   {
     "missionControl": {
       "enabled": true,
       "apiUrl": "https://mission-control.aiorg.app",
       "heartbeatInterval": 30
     }
   }
   ```

3. **Test integration:**
   ```bash
   # Send test heartbeat
   curl -X POST https://mission-control.aiorg.app/api/heartbeat \
     -H "Content-Type: application/json" \
     -d '{"agentId":"test","agentName":"Test Agent","status":"active"}'
   ```

## Configuration

### Agent Configuration
Edit `config/agents.json` to define your agents:
```json
[
  {
    "id": "reggie",
    "name": "Reggie",
    "description": "AiOrg's Personal & Executive Assistant",
    "status": "active",
    "lastHeartbeat": "2026-03-07T00:00:00Z",
    "tasksCompleted": 127
  }
]
```

### Environment Variables
See `.env.example` for all available configuration options.

## API Documentation

### Endpoints

#### POST /api/heartbeat
Send agent heartbeat.

**Request:**
```json
{
  "agentId": "string",
  "agentName": "string",
  "status": "active|idle|error|offline",
  "currentTask": "string",
  "metrics": {
    "cpu": "number",
    "memory": "number",
    "tasksCompleted": "number",
    "uptime": "string"
  }
}
```

#### GET /api/agents
Get all registered agents.

#### POST /api/tasks
Create a new task.

## Support

### Documentation
- [Integration Guide](./INTEGRATION_GUIDE.md)
- [Deployment Summary](./DEPLOYMENT_SUMMARY.md)
- [API Testing](./AGENT_API_TESTING.md)

### Contact
- **Website:** [aiorg.app](https://aiorg.app)
- **Email:** support@aiorg.app
- **GitHub:** [aiorg-app/mission-control](https://github.com/aiorg-app/mission-control)

## License
This project is proprietary software owned by R & L Guillory Enterprises LLC (DBA: AiOrg).

---

*Deployed: March 07, 2026*
*Version: 1.0.0*
