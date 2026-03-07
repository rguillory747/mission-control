#!/usr/bin/env python3
"""
Test Mission Control Agent Integration
Simulates Jarvis agent connecting to Mission Control
"""

import os
import sys
import time
import json
from mission_control_client import MissionControlAgent, MissionControlConfig

def test_basic_integration():
    """Test basic agent integration with Mission Control"""
    print("🧪 Testing Mission Control Agent Integration")
    print("=" * 60)
    
    # Configure for your deployment
    config = MissionControlConfig(
        base_url="https://mission-control-aiorg-bvbdrgk6i-reginald-guillorys-projects.vercel.app",
        heartbeat_interval=15,  # Faster for testing
        timeout=10
    )
    
    # Create Jarvis agent
    jarvis = MissionControlAgent("Jarvis", config)
    
    print(f"🤖 Agent: {jarvis.name}")
    print(f"🌐 Base URL: {config.base_url}")
    print()
    
    # Test 1: Initial heartbeat
    print("1. Sending initial heartbeat...")
    try:
        result = jarvis.heartbeat("active", "Testing Mission Control integration")
        print(f"   ✅ Success: {result.get('message', 'No message')}")
        print(f"   Status: {result.get('status', 'N/A')}")
        print(f"   Timestamp: {result.get('timestamp', 'N/A')}")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False
    
    # Test 2: Log activities
    print("\n2. Logging activities...")
    activities = [
        ("Booted", "Jarvis connected to Mission Control"),
        ("Initialized", "Starting agent monitoring"),
        ("Health check", "All systems operational"),
    ]
    
    for action, detail in activities:
        try:
            result = jarvis.log_activity(action, detail)
            print(f"   ✅ {action}: {detail}")
            time.sleep(0.5)
        except Exception as e:
            print(f"   ❌ Activity failed: {e}")
            return False
    
    # Test 3: Create tasks
    print("\n3. Creating sample tasks...")
    tasks = [
        {
            "title": "Monitor agent health",
            "description": "Check all agent heartbeats and status",
            "status": "in_progress",
            "assignee": "Jarvis",
            "priority": "P0"
        },
        {
            "title": "Deploy updates",
            "description": "Deploy latest Mission Control updates",
            "status": "inbox",
            "assignee": "Forge",
            "priority": "P1"
        },
        {
            "title": "Research AI trends",
            "description": "Gather latest AI development news",
            "status": "inbox",
            "assignee": "Scout",
            "priority": "P2"
        }
    ]
    
    for task in tasks:
        try:
            result = jarvis.create_task(**task)
            print(f"   ✅ Created: {task['title']} ({task['priority']}) -> {task['assignee']}")
            time.sleep(0.5)
        except Exception as e:
            print(f"   ❌ Task creation failed: {e}")
            # Continue with other tests
    
    # Test 4: Update task status
    print("\n4. Updating task status...")
    try:
        result = jarvis.update_task("Monitor agent health", "done")
        print(f"   ✅ Updated: Monitor agent health -> done")
    except Exception as e:
        print(f"   ❌ Task update failed: {e}")
    
    # Test 5: Report metrics
    print("\n5. Reporting metrics...")
    metrics = [
        ("agents_online", 1, None),
        ("tasks_created", None, 3),
        ("heartbeats_received", None, 1),
    ]
    
    for key, value, increment in metrics:
        try:
            if value is not None:
                result = jarvis.report_metric(key, value=value)
                print(f"   ✅ Metric set: {key} = {value}")
            else:
                result = jarvis.report_metric(key, increment=increment)
                print(f"   ✅ Metric incremented: {key} += {increment}")
            time.sleep(0.5)
        except Exception as e:
            print(f"   ❌ Metric failed: {e}")
    
    # Test 6: Automatic heartbeat loop
    print("\n6. Testing automatic heartbeat loop...")
    print("   Starting heartbeat loop (15s interval)...")
    
    try:
        jarvis.start_heartbeat_loop("active", "Running integration tests")
        
        # Let it run for a bit
        for i in range(3):
            print(f"   Waiting... ({i+1}/3)")
            time.sleep(5)
            
            # Log some activities during heartbeats
            jarvis.log_activity("Working", f"Test iteration {i+1}")
        
        jarvis.stop_heartbeat_loop()
        print("   ✅ Heartbeat loop test completed")
    except Exception as e:
        print(f"   ❌ Heartbeat loop failed: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 Mission Control Integration Test Complete!")
    print()
    print("📋 Next steps for Jarvis:")
    print("1. Copy mission_control_client.py to Jarvis's codebase")
    print("2. Set environment variable: MISSION_CONTROL_URL")
    print("3. Initialize: jarvis = MissionControlAgent('Jarvis')")
    print("4. Start heartbeats: jarvis.start_heartbeat_loop()")
    print("5. Log activities as Jarvis works")
    print()
    print("🔗 Dashboard should now show:")
    print("   • Jarvis agent with 'active' status")
    print("   • Activities in the feed")
    print("   • Tasks in the Kanban board")
    print("   • Updated metrics")
    
    return True

def quick_test():
    """Quick test without all the output"""
    print("🚀 Quick Mission Control Test")
    
    try:
        agent = MissionControlAgent("QuickTest")
        result = agent.heartbeat("active", "Quick test")
        print(f"✅ Connected: {result.get('message', 'Success')}")
        print(f"   URL: {agent.config.base_url}")
        return True
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

if __name__ == "__main__":
    # Add the scripts directory to Python path
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    if len(sys.argv) > 1 and sys.argv[1] == "quick":
        success = quick_test()
    else:
        success = test_basic_integration()
    
    sys.exit(0 if success else 1)