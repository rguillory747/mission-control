# Mission Control Integration Guide for OpenClaw Agents

## Overview
This guide explains how to connect your OpenClaw agents to the Mission Control dashboard for real-time monitoring.

## API Endpoints

### 1. Heartbeat Endpoint
**URL:** `POST /api/heartbeat`
**Purpose:** Send regular heartbeat updates to show agent is alive

**Request Body:**
```json
{
  "agentId": "your-agent-id",
  "agentName": "Your Agent Name",
  "status": "active|idle|error|offline",
  "currentTask": "Description of current task",
  "metrics": {
    "cpu": 45.2,
    "memory": 68.7,
    "tasksCompleted": 127,
    "uptime": "12:34:56"
  }
}
```

**Example using Python:**
```python
import requests
import time
from datetime import datetime

def send_heartbeat():
    url = "https://mission-control.aiorg.app/api/heartbeat"
    payload = {
        "agentId": "reggie",
        "agentName": "Reggie",
        "status": "active",
        "lastHeartbeat": datetime.utcnow().isoformat() + "Z",
        "currentTask": "Processing user requests",
        "metrics": {
            "cpu": 45.2,
            "memory": 68.7,
            "tasksCompleted": 127,
            "uptime": "12:34:56"
        }
    }
    
    response = requests.post(url, json=payload)
    return response.status_code == 200

# Send heartbeat every 30 seconds
while True:
    send_heartbeat()
    time.sleep(30)
```

### 2. Activity Logging
**URL:** `POST /api/activities`
**Purpose:** Log significant agent activities

**Request Body:**
```json
{
  "agentId": "your-agent-id",
  "type": "task_completed|error|warning|info",
  "title": "Brief title of activity",
  "description": "Detailed description",
  "metadata": {
    "taskId": "optional-task-id",
    "duration": "00:05:23",
    "success": true
  }
}
```

### 3. Task Management
**URL:** `POST /api/tasks`
**Purpose:** Create and update tasks

## OpenClaw Integration

### Using the SKILL.md
Copy the provided `SKILL.md` to your OpenClaw skills directory to enable Mission Control integration.

### Environment Variables
Add to your OpenClaw configuration:
```yaml
missionControl:
  enabled: true
  apiUrl: "https://mission-control.aiorg.app"
  heartbeatInterval: 30  # seconds
```

## Testing Integration

1. **Test Connection:**
```bash
curl -X POST https://mission-control.aiorg.app/api/heartbeat \
  -H "Content-Type: application/json" \
  -d '{"agentId":"test","agentName":"Test Agent","status":"active"}'
```

2. **Verify in Dashboard:**
   - Navigate to https://mission-control.aiorg.app
   - Check if your agent appears in the agent list
   - Verify heartbeat timestamps are updating

## Troubleshooting

### Common Issues:
1. **Agent not appearing:** Check CORS settings and API endpoint
2. **Heartbeats not updating:** Verify network connectivity and API URL
3. **Dashboard not loading:** Check browser console for errors

## Support
For integration assistance, contact the AiOrg team at support@aiorg.app
