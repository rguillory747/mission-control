#!/usr/bin/env python3
"""
Agent Squad Seeding Script for Mission Control
Creates the default agent squad exactly as documented in SKILL.md and README.md
"""

import json
import os
import sys
from datetime import datetime
import time

def create_agent_squad():
    """Create the default agent squad exactly as documented"""
    
    # From SKILL.md: Default squad
    # - Forge 🔨 - Code Builder
    # - Scout 🔍 - Research & Discovery  
    # - Ghost 👻 - Outreach & Growth
    # - Closer 🤝 - Sales & Deals
    # - Hype 📣 - Social & Content
    
    agents = [
        {
            "name": "Forge",
            "role": "Code Builder",
            "emoji": "🔨",
            "color": "blue",
            "status": "active",  # From SKILL.md: active, idle, sleeping, error
            "currentTask": "Building mission control dashboard",
            "lastSeen": int(time.time() * 1000),
            "lastHeartbeat": int(time.time() * 1000)
        },
        {
            "name": "Scout",
            "role": "Research & Discovery",
            "emoji": "🔍",
            "color": "green",
            "status": "active",
            "currentTask": "Researching AI agent patterns",
            "lastSeen": int(time.time() * 1000),
            "lastHeartbeat": int(time.time() * 1000)
        },
        {
            "name": "Ghost",
            "role": "Outreach & Growth",
            "emoji": "👻",
            "color": "purple",
            "status": "idle",
            "currentTask": "Preparing outreach campaign",
            "lastSeen": int(time.time() * 1000),
            "lastHeartbeat": int(time.time() * 1000)
        },
        {
            "name": "Closer",
            "role": "Sales & Deals",
            "emoji": "🤝",
            "color": "orange",
            "status": "sleeping",
            "currentTask": "Following up with leads",
            "lastSeen": int(time.time() * 1000),
            "lastHeartbeat": int(time.time() * 1000)
        },
        {
            "name": "Hype",
            "role": "Social & Content",
            "emoji": "📣",
            "color": "red",
            "status": "active",
            "currentTask": "Creating social content",
            "lastSeen": int(time.time() * 1000),
            "lastHeartbeat": int(time.time() * 1000)
        }
    ]
    
    return agents

def create_sample_tasks():
    """Create sample tasks with documented status values"""
    
    # From SKILL.md: Status options: inbox, in_progress, review, done, blocked
    # Note: in_progress with underscore, NOT in-progress
    
    tasks = [
        {
            "title": "Deploy Mission Control to Vercel",
            "description": "Deploy the Mission Control dashboard to Vercel with custom domain mission-control.aiorg.app",
            "status": "in_progress",  # Note: underscore
            "assignee": "Forge",
            "priority": "P0",  # From SKILL.md: P0 (urgent), P1 (high), P2 (normal)
            "createdAt": int(time.time() * 1000),
            "updatedAt": int(time.time() * 1000)
        },
        {
            "title": "Research AI agent monitoring patterns",
            "description": "Research best practices for monitoring AI agent performance and real-time dashboards",
            "status": "inbox",
            "assignee": "Scout",
            "priority": "P1",
            "createdAt": int(time.time() * 1000),
            "updatedAt": int(time.time() * 1000)
        },
        {
            "title": "Create outreach campaign for AiOrg",
            "description": "Design and launch outreach campaign for AiOrg AI development services",
            "status": "inbox",
            "assignee": "Ghost",
            "priority": "P1",
            "createdAt": int(time.time() * 1000),
            "updatedAt": int(time.time() * 1000)
        },
        {
            "title": "Follow up with potential clients",
            "description": "Follow up with 5 potential clients from last week's outreach",
            "status": "review",
            "assignee": "Closer",
            "priority": "P0",
            "createdAt": int(time.time() * 1000),
            "updatedAt": int(time.time() * 1000)
        },
        {
            "title": "Create social media content calendar",
            "description": "Plan and schedule social media content for March 2026",
            "status": "done",
            "assignee": "Hype",
            "priority": "P2",
            "createdAt": int(time.time() * 1000),
            "updatedAt": int(time.time() * 1000)
        },
        {
            "title": "Fix API authentication issue",
            "description": "Resolve authentication problem with Convex backend",
            "status": "blocked",
            "assignee": "Forge",
            "priority": "P0",
            "createdAt": int(time.time() * 1000),
            "updatedAt": int(time.time() * 1000)
        }
    ]
    
    return tasks

def create_sample_activities():
    """Create sample activities for the activity feed"""
    
    activities = []
    now = int(time.time() * 1000)
    
    # Activities from the last 24 hours
    for i in range(10):
        agents = ["Forge", "Scout", "Ghost", "Closer", "Hype"]
        actions = [
            "Sent heartbeat",
            "Logged activity",
            "Updated task status",
            "Completed research",
            "Deployed code",
            "Sent outreach emails",
            "Closed deal",
            "Published content",
            "Fixed bug",
            "Optimized performance"
        ]
        
        activity = {
            "agent": agents[i % len(agents)],
            "action": actions[i % len(actions)],
            "detail": f"Sample activity #{i+1} for testing dashboard",
            "timestamp": now - (i * 3600000)  # Each hour back
        }
        activities.append(activity)
    
    return activities

def create_sample_metrics():
    """Create sample metrics for tracking"""
    
    metrics = [
        {
            "key": "agents_active",
            "value": 3,  # Forge, Scout, Hype are active
            "updatedAt": int(time.time() * 1000)
        },
        {
            "key": "tasks_completed_today",
            "value": 12,
            "updatedAt": int(time.time() * 1000)
        },
        {
            "key": "heartbeats_received",
            "value": 47,
            "updatedAt": int(time.time() * 1000)
        },
        {
            "key": "api_requests",
            "value": 156,
            "updatedAt": int(time.time() * 1000)
        }
    ]
    
    return metrics

def save_to_config_files():
    """Save agent squad to config files for reference"""
    
    # Create config directory if it doesn't exist
    config_dir = "config"
    os.makedirs(config_dir, exist_ok=True)
    
    # Save agents to config/agents.json
    agents = create_agent_squad()
    agents_config = []
    
    for agent in agents:
        agents_config.append({
            "id": agent["name"].lower(),
            "name": agent["name"],
            "description": agent["role"],
            "status": agent["status"],
            "lastHeartbeat": datetime.fromtimestamp(agent["lastHeartbeat"] / 1000).isoformat() + "Z",
            "tasksCompleted": 0  # Will be updated by actual activity
        })
    
    with open(os.path.join(config_dir, "agents.json"), "w") as f:
        json.dump(agents_config, f, indent=2)
    
    print(f"✅ Saved {len(agents_config)} agents to config/agents.json")
    
    # Save sample data to test_data.json
    sample_data = {
        "agents": agents,
        "tasks": create_sample_tasks(),
        "activities": create_sample_activities(),
        "metrics": create_sample_metrics(),
        "generated_at": datetime.now().isoformat(),
        "note": "This is sample data for testing. Real data will come from Convex backend."
    }
    
    with open("test_data.json", "w") as f:
        json.dump(sample_data, f, indent=2)
    
    print(f"✅ Saved sample data to test_data.json")
    
    return agents_config, sample_data

def generate_seeding_report():
    """Generate a report of what was seeded"""
    
    agents = create_agent_squad()
    tasks = create_sample_tasks()
    activities = create_sample_activities()
    metrics = create_sample_metrics()
    
    report = {
        "timestamp": datetime.now().isoformat(),
        "summary": {
            "agents": len(agents),
            "tasks": len(tasks),
            "activities": len(activities),
            "metrics": len(metrics)
        },
        "agent_status_distribution": {
            "active": sum(1 for a in agents if a["status"] == "active"),
            "idle": sum(1 for a in agents if a["status"] == "idle"),
            "sleeping": sum(1 for a in agents if a["status"] == "sleeping"),
            "error": sum(1 for a in agents if a["status"] == "error")
        },
        "task_status_distribution": {
            "inbox": sum(1 for t in tasks if t["status"] == "inbox"),
            "in_progress": sum(1 for t in tasks if t["status"] == "in_progress"),
            "review": sum(1 for t in tasks if t["status"] == "review"),
            "done": sum(1 for t in tasks if t["status"] == "done"),
            "blocked": sum(1 for t in tasks if t["status"] == "blocked")
        },
        "task_priority_distribution": {
            "P0": sum(1 for t in tasks if t["priority"] == "P0"),
            "P1": sum(1 for t in tasks if t["priority"] == "P1"),
            "P2": sum(1 for t in tasks if t["priority"] == "P2")
        },
        "agents": [a["name"] for a in agents],
        "next_steps": [
            "Deploy Convex backend with: npx convex deploy",
            "Seed data using Convex import or API calls",
            "Start development server: npm run dev",
            "Test API endpoints with sample data",
            "Verify dashboard displays seeded data"
        ]
    }
    
    # Save report
    with open("seeding_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"✅ Generated seeding report: seeding_report.json")
    
    return report

def main():
    """Main seeding function"""
    print("=" * 60)
    print("Mission Control - Agent Squad Seeding")
    print("=" * 60)
    
    print("\n📋 Creating default agent squad...")
    agents = create_agent_squad()
    print(f"✅ Created {len(agents)} agents:")
    for agent in agents:
        print(f"   • {agent['emoji']} {agent['name']} - {agent['role']} ({agent['status']})")
    
    print("\n📋 Creating sample tasks...")
    tasks = create_sample_tasks()
    print(f"✅ Created {len(tasks)} tasks with status distribution:")
    status_counts = {}
    for task in tasks:
        status_counts[task["status"]] = status_counts.get(task["status"], 0) + 1
    
    for status, count in status_counts.items():
        print(f"   • {status}: {count} tasks")
    
    print("\n📋 Creating sample activities...")
    activities = create_sample_activities()
    print(f"✅ Created {len(activities)} activities")
    
    print("\n📋 Creating sample metrics...")
    metrics = create_sample_metrics()
    print(f"✅ Created {len(metrics)} metrics")
    
    print("\n💾 Saving to config files...")
    agents_config, sample_data = save_to_config_files()
    
    print("\n📊 Generating seeding report...")
    report = generate_seeding_report()
    
    print("\n" + "=" * 60)
    print("Seeding Complete!")
    print("=" * 60)
    
    print(f"\n🎯 Agent Squad Ready:")
    for agent in agents:
        print(f"   {agent['emoji']} {agent['name']} - {agent['role']}")
    
    print(f"\n📊 Data Summary:")
    print(f"   • Agents: {report['summary']['agents']}")
    print(f"   • Tasks: {report['summary']['tasks']}")
    print(f"   • Activities: {report['summary']['activities']}")
    print(f"   • Metrics: {report['summary']['metrics']}")
    
    print(f"\n📁 Files Created:")
    print(f"   • config/agents.json - Agent configuration")
    print(f"   • test_data.json - Sample data for testing")
    print(f"   • seeding_report.json - Detailed seeding report")
    
    print(f"\n🚀 Next Steps:")
    for i, step in enumerate(report["next_steps"], 1):
        print(f"   {i}. {step}")
    
    print("\n" + "=" * 60)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())