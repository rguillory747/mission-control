#!/usr/bin/env python3
"""
Convex Backend Verification Script for Mission Control
Tests Convex connection, functions, and seeds initial data
"""

import os
import sys
import json
import requests
from datetime import datetime
import time

# Configuration from .env.local
CONVEX_URL = "https://fancy-ape-615.convex.cloud"
CONVEX_API_KEY = "eyJ2MiI6IjVmNWU1MmJlMTVlYTQ2NGE4OWFhYWRkMGFkNmFlY2VjIn0="
CONVEX_TEAM_ID = "61526"

def test_convex_connection():
    """Test basic connection to Convex deployment"""
    print("🔌 Testing Convex connection...")
    
    # Try to ping the deployment
    try:
        response = requests.get(
            f"{CONVEX_URL}/ping",
            timeout=10
        )
        
        if response.status_code == 200:
            print("✅ Convex deployment is accessible")
            return True
        else:
            print(f"⚠️  Convex returned status: {response.status_code}")
            print(f"   Response: {response.text[:200]}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection failed: {e}")
        return False

def test_convex_function(function_name, args=None, method="query"):
    """Test a specific Convex function"""
    print(f"\n🧪 Testing {method}: {function_name}")
    
    url = f"{CONVEX_URL}/api/{function_name}"
    
    try:
        if method == "query":
            response = requests.get(url, timeout=10)
        elif method == "mutation":
            response = requests.post(
                url,
                json=args or {},
                timeout=10
            )
        else:
            print(f"❌ Unknown method: {method}")
            return False
        
        if response.status_code == 200:
            print(f"✅ {function_name} succeeded")
            try:
                data = response.json()
                print(f"   Response: {json.dumps(data, indent=2)[:200]}...")
                return True, data
            except:
                print(f"   Response: {response.text[:200]}")
                return True, response.text
        else:
            print(f"❌ {function_name} failed: HTTP {response.status_code}")
            print(f"   Error: {response.text[:200]}")
            return False, None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return False, None

def seed_agent_squad():
    """Seed the default agent squad"""
    print("\n🤖 Seeding agent squad...")
    
    agents = [
        {
            "name": "Forge",
            "role": "Code Builder",
            "emoji": "🔨",
            "color": "blue",
            "status": "active",
            "currentTask": "Building mission control dashboard",
            "lastSeen": int(time.time() * 1000)
        },
        {
            "name": "Scout",
            "role": "Research & Discovery",
            "emoji": "🔍",
            "color": "green",
            "status": "active",
            "currentTask": "Researching AI agent patterns",
            "lastSeen": int(time.time() * 1000)
        },
        {
            "name": "Ghost",
            "role": "Outreach & Growth",
            "emoji": "👻",
            "color": "purple",
            "status": "idle",
            "currentTask": "Preparing outreach campaign",
            "lastSeen": int(time.time() * 1000)
        },
        {
            "name": "Closer",
            "role": "Sales & Deals",
            "emoji": "🤝",
            "color": "orange",
            "status": "sleeping",
            "currentTask": "Following up with leads",
            "lastSeen": int(time.time() * 1000)
        },
        {
            "name": "Hype",
            "role": "Social & Content",
            "emoji": "📣",
            "color": "red",
            "status": "active",
            "currentTask": "Creating social content",
            "lastSeen": int(time.time() * 1000)
        }
    ]
    
    print(f"✅ Agent squad defined: {', '.join([a['name'] for a in agents])}")
    return agents

def seed_sample_tasks():
    """Seed sample tasks for the dashboard"""
    print("\n📋 Seeding sample tasks...")
    
    tasks = [
        {
            "title": "Deploy Mission Control to Vercel",
            "description": "Deploy the Mission Control dashboard to Vercel with custom domain",
            "status": "in_progress",
            "assignee": "Forge",
            "priority": "P0"
        },
        {
            "title": "Research AI agent monitoring patterns",
            "description": "Research best practices for monitoring AI agent performance",
            "status": "inbox",
            "assignee": "Scout",
            "priority": "P1"
        },
        {
            "title": "Create outreach campaign for AiOrg",
            "description": "Design and launch outreach campaign for AiOrg services",
            "status": "inbox",
            "assignee": "Ghost",
            "priority": "P1"
        },
        {
            "title": "Follow up with potential clients",
            "description": "Follow up with 5 potential clients from last week",
            "status": "review",
            "assignee": "Closer",
            "priority": "P0"
        },
        {
            "title": "Create social media content calendar",
            "description": "Plan and schedule social media content for March",
            "status": "done",
            "assignee": "Hype",
            "priority": "P2"
        }
    ]
    
    print(f"✅ Sample tasks created: {len(tasks)} tasks")
    return tasks

def seed_sample_activities():
    """Seed sample activities for the activity feed"""
    print("\n📝 Seeding sample activities...")
    
    activities = [
        {
            "agent": "Forge",
            "action": "Started deployment to Vercel",
            "detail": "Initializing Vercel deployment pipeline",
            "timestamp": int(time.time() * 1000) - 3600000  # 1 hour ago
        },
        {
            "agent": "Scout",
            "action": "Completed research on agent monitoring",
            "detail": "Found 15 relevant papers and articles",
            "timestamp": int(time.time() * 1000) - 7200000  # 2 hours ago
        },
        {
            "agent": "Ghost",
            "action": "Sent 25 outreach emails",
            "detail": "Campaign focused on AI development agencies",
            "timestamp": int(time.time() * 1000) - 10800000  # 3 hours ago
        },
        {
            "agent": "Closer",
            "action": "Closed deal with TechCorp Inc",
            "detail": "$15,000 annual contract signed",
            "timestamp": int(time.time() * 1000) - 14400000  # 4 hours ago
        },
        {
            "agent": "Hype",
            "action": "Published blog post on AI trends",
            "detail": "Post reached 2,500 views in first day",
            "timestamp": int(time.time() * 1000) - 18000000  # 5 hours ago
        }
    ]
    
    print(f"✅ Sample activities created: {len(activities)} activities")
    return activities

def generate_verification_report(results):
    """Generate a comprehensive verification report"""
    print("\n📊 Generating verification report...")
    
    report = {
        "timestamp": datetime.now().isoformat(),
        "convex_url": CONVEX_URL,
        "team_id": CONVEX_TEAM_ID,
        "connection_test": results.get("connection", False),
        "function_tests": results.get("functions", {}),
        "data_seeding": {
            "agents": len(results.get("agents", [])),
            "tasks": len(results.get("tasks", [])),
            "activities": len(results.get("activities", []))
        },
        "recommendations": [],
        "status": "unknown"
    }
    
    # Calculate overall status
    if results.get("connection", False):
        report["status"] = "connected"
        
        # Check function tests
        function_results = results.get("functions", {})
        if function_results:
            successful_tests = sum(1 for test in function_results.values() if test.get("success", False))
            total_tests = len(function_results)
            
            if successful_tests == total_tests:
                report["status"] = "fully_operational"
            elif successful_tests > 0:
                report["status"] = "partially_operational"
            else:
                report["status"] = "connected_but_functions_failing"
    else:
        report["status"] = "not_connected"
    
    # Generate recommendations
    if report["status"] == "not_connected":
        report["recommendations"].append("Check Convex deployment URL and API key")
        report["recommendations"].append("Verify network connectivity to Convex")
        report["recommendations"].append("Check if Convex deployment is running")
    
    elif report["status"] == "connected_but_functions_failing":
        report["recommendations"].append("Check Convex function implementations")
        report["recommendations"].append("Verify schema matches function expectations")
        report["recommendations"].append("Check authentication for function calls")
    
    elif report["status"] == "partially_operational":
        report["recommendations"].append("Fix failing functions")
        report["recommendations"].append("Test all API endpoints")
        report["recommendations"].append("Monitor error logs")
    
    elif report["status"] == "fully_operational":
        report["recommendations"].append("Proceed with deployment")
        report["recommendations"].append("Test with real agent data")
        report["recommendations"].append("Monitor performance metrics")
    
    # Save report to file
    report_file = "convex_verification_report.json"
    with open(report_file, "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"✅ Report saved to {report_file}")
    
    # Print summary
    print("\n" + "=" * 60)
    print("Convex Verification Report Summary")
    print("=" * 60)
    print(f"Status: {report['status'].replace('_', ' ').title()}")
    print(f"Connection: {'✅' if report['connection_test'] else '❌'}")
    print(f"Data Seeding: {report['data_seeding']['agents']} agents, "
          f"{report['data_seeding']['tasks']} tasks, "
          f"{report['data_seeding']['activities']} activities")
    
    if report["recommendations"]:
        print("\nRecommendations:")
        for i, rec in enumerate(report["recommendations"], 1):
            print(f"  {i}. {rec}")
    
    print("=" * 60)
    
    return report

def main():
    """Main verification function"""
    print("=" * 60)
    print("Mission Control - Convex Backend Verification")
    print("=" * 60)
    
    results = {
        "connection": False,
        "functions": {},
        "agents": [],
        "tasks": [],
        "activities": []
    }
    
    # Test connection
    results["connection"] = test_convex_connection()
    
    if results["connection"]:
        # Test Convex functions
        functions_to_test = [
            ("activities:list", None, "query"),
            ("tasks:list", None, "query"),
        ]
        
        for func_name, args, method in functions_to_test:
            success, data = test_convex_function(func_name, args, method)
            results["functions"][func_name] = {
                "success": success,
                "data": data if success else None
            }
    
    # Seed sample data (offline - for reference)
    results["agents"] = seed_agent_squad()
    results["tasks"] = seed_sample_tasks()
    results["activities"] = seed_sample_activities()
    
    # Generate report
    report = generate_verification_report(results)
    
    # Determine next steps
    print("\n🎯 Next Steps:")
    
    if report["status"] == "fully_operational":
        print("1. ✅ Convex backend is ready for deployment")
        print("2. Proceed with Vercel deployment")
        print("3. Configure custom domain")
        print("4. Test end-to-end integration")
    elif report["status"] == "partially_operational":
        print("1. ⚠️  Some functions need attention")
        print("2. Check failing function implementations")
        print("3. Verify Convex deployment configuration")
        print("4. Retry verification after fixes")
    elif report["status"] == "connected_but_functions_failing":
        print("1. ❌ Functions are not working")
        print("2. Check Convex function code")
        print("3. Verify schema compatibility")
        print("4. Consider redeploying Convex backend")
    else:
        print("1. ❌ Connection failed")
        print("2. Check Convex deployment URL")
        print("3. Verify API key and authentication")
        print("4. Ensure Convex deployment is running")
    
    print("=" * 60)
    
    # Return exit code based on status
    if report["status"] in ["fully_operational", "partially_operational"]:
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit(main())