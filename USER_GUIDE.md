# AiOrg Mission Control User Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Dashboard Overview](#dashboard-overview)
3. [Managing Agents](#managing-agents)
4. [Task Management](#task-management)
5. [Monitoring & Alerts](#monitoring--alerts)
6. [API Integration](#api-integration)
7. [Troubleshooting](#troubleshooting)

## 1. Getting Started

### Accessing Mission Control
1. Navigate to [https://mission-control.aiorg.app](https://mission-control.aiorg.app)
2. Login with your AiOrg credentials
3. You'll be directed to the main dashboard

### First-Time Setup
1. **Add Your First Agent:**
   - Click "Add Agent" in the sidebar
   - Enter agent details (ID, name, description)
   - Configure heartbeat interval (recommended: 30 seconds)

2. **Configure Integration:**
   - Follow the integration guide for your specific AI agent
   - Test the connection with the "Test Connection" button

## 2. Dashboard Overview

### Main Dashboard Components

**A. Agent Status Panel**
- Real-time status of all agents (Active, Idle, Error, Offline)
- Quick overview of agent count and health

**B. Performance Metrics**
- CPU and memory usage across agents
- Task completion rates
- Uptime statistics

**C. Activity Feed**
- Chronological log of all agent activities
- Filter by agent, activity type, or time range

**D. Task Kanban Board**
- Drag-and-drop task management
- Columns: Todo, In Progress, Review, Done
- Assign tasks to specific agents

## 3. Managing Agents

### Adding New Agents
1. Click "Agents" in the sidebar
2. Click "Add New Agent"
3. Fill in the form:
   - **Agent ID:** Unique identifier (e.g., "reggie")
   - **Name:** Display name (e.g., "Reggie")
   - **Description:** What this agent does
   - **Heartbeat URL:** Where the agent sends heartbeats
   - **Status:** Initial status

### Agent Configuration
Each agent can be configured with:
- **Heartbeat Interval:** How often to expect updates (15-300 seconds)
- **Timeout Threshold:** When to mark as offline (2-10 missed heartbeats)
- **Notification Rules:** When to send alerts
- **Performance Thresholds:** CPU/memory limits

### Viewing Agent Details
Click on any agent card to see:
- Detailed performance metrics
- Activity history
- Current task
- Configuration settings

## 4. Task Management

### Creating Tasks
1. Navigate to "Tasks" in the sidebar
2. Click "Create New Task"
3. Fill in task details:
   - **Title:** Brief description
   - **Description:** Detailed instructions
   - **Priority:** Low, Medium, High, Critical
   - **Assignee:** Which agent should handle it
   - **Due Date:** Optional deadline

### Task Workflow
Tasks move through four stages:
1. **Todo:** Newly created tasks
2. **In Progress:** Assigned and being worked on
3. **Review:** Completed, awaiting verification
4. **Done:** Successfully completed

### Assigning Tasks to Agents
1. Drag a task card to an agent's column
2. Or use the "Assign" button on the task detail view
3. Agents will receive the task via API

## 5. Monitoring & Alerts

### Real-time Monitoring
The dashboard updates in real-time showing:
- Agent status changes
- Task progress updates
- Performance metric fluctuations

### Setting Up Alerts
Configure alerts for:
- **Agent Offline:** When an agent misses heartbeats
- **High Resource Usage:** CPU > 80% or memory > 90%
- **Task Stuck:** Task in "In Progress" for too long
- **Error Rate:** Multiple errors in short period

### Notification Channels
Alerts can be sent to:
- Email (configured in settings)
- Slack/Discord webhooks
- SMS (requires Twilio integration)
- In-app notifications

## 6. API Integration

### For AI Agents
Your AI agents can integrate with Mission Control by:

1. **Sending Heartbeats:**
   ```python
   POST https://mission-control.aiorg.app/api/heartbeat
   ```

2. **Logging Activities:**
   ```python
   POST https://mission-control.aiorg.app/api/activities
   ```

3. **Updating Tasks:**
   ```python
   PUT https://mission-control.aiorg.app/api/tasks/{taskId}
   ```

### Webhook Integration
Mission Control can send webhooks for:
- Agent status changes
- Task completion
- Alert triggers

## 7. Troubleshooting

### Common Issues

**Agent Not Appearing**
1. Check if the agent is sending heartbeats
2. Verify the API endpoint is correct
3. Check CORS settings if accessing from different domain

**Heartbeats Not Updating**
1. Verify network connectivity
2. Check agent logs for errors
3. Ensure heartbeat interval is configured correctly

**Dashboard Loading Slowly**
1. Check browser console for errors
2. Verify Convex backend is running
3. Clear browser cache

### Getting Help
- Check the [Integration Guide](./INTEGRATION_GUIDE.md)
- Review [API Documentation](#api-integration)
- Contact support@aiorg.app

## Appendix

### Keyboard Shortcuts
- `Ctrl/Cmd + K`: Quick search
- `Ctrl/Cmd + N`: New task
- `Ctrl/Cmd + A`: Add agent
- `R`: Refresh dashboard

### Best Practices
1. Set appropriate heartbeat intervals (30-60 seconds)
2. Configure meaningful alert thresholds
3. Regularly review agent performance
4. Archive completed tasks monthly

---

*Last Updated: March 07, 2026*
*AiOrg Mission Control v1.0.0*
