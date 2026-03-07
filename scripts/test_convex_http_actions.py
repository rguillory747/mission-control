#!/usr/bin/env python3
"""
Test Convex HTTP Actions with current JWT API key
Based on convex/http.ts in the project
"""

import requests
import json
import sys

# Configuration
CONVEX_URL = "https://fancy-ape-615.convex.cloud"
CONVEX_API_KEY = "eyJ2MiI6IjVmNWU1MmJlMTVlYTQ2NGE4OWFhYWRkMGFkNmFlY2VjIn0="

def test_http_action(endpoint, data):
    """Test a Convex HTTP action endpoint"""
    url = f"{CONVEX_URL}{endpoint}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CONVEX_API_KEY}"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        return {
            "success": response.status_code == 200,
            "status": response.status_code,
            "response": response.json() if response.status_code == 200 else response.text
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

def main():
    print("=" * 60)
    print("Testing Convex HTTP Actions")
    print("=" * 60)
    print(f"URL: {CONVEX_URL}")
    print(f"API Key: {CONVEX_API_KEY[:30]}...")
    
    # Test endpoints from convex/http.ts
    tests = [
        {
            "name": "POST /api/heartbeat",
            "endpoint": "/api/heartbeat",
            "data": {"name": "TestAgent", "status": "active", "currentTask": "Testing"}
        },
        {
            "name": "POST /api/activity", 
            "endpoint": "/api/activity",
            "data": {"agent": "TestAgent", "action": "Tested HTTP API", "detail": "Testing connectivity"}
        },
        {
            "name": "POST /api/task-create",
            "endpoint": "/api/task-create",
            "data": {
                "title": "Test Task via HTTP",
                "description": "Created via HTTP API test",
                "status": "in_progress",
                "assignee": "Forge",
                "priority": "P1"
            }
        }
    ]
    
    results = []
    
    for test in tests:
        print(f"\n🧪 Testing {test['name']}...")
        result = test_http_action(test["endpoint"], test["data"])
        
        if result.get("success"):
            print(f"   ✅ Success! Status: {result['status']}")
            print(f"   Response: {json.dumps(result['response'], indent=2)[:150]}...")
        elif "error" in result:
            print(f"   ❌ Error: {result['error']}")
        else:
            print(f"   ❌ Failed: Status {result['status']}")
            print(f"   Response: {result['response'][:150]}")
        
        results.append({
            "test": test["name"],
            "success": result.get("success", False),
            "status": result.get("status"),
            "response": result.get("response", result.get("error", "Unknown"))
        })
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    successful = sum(1 for r in results if r["success"])
    total = len(results)
    
    print(f"Successful: {successful}/{total} ({successful/total*100:.0f}%)")
    
    for result in results:
        status = "✅" if result["success"] else "❌"
        print(f"{status} {result['test']}: HTTP {result.get('status', 'N/A')}")
    
    print("\n🎯 Analysis:")
    if successful == total:
        print("✅ HTTP API is fully functional with current JWT key")
        print("   You can use HTTP API for agent integration")
        print("   But still need deploy key for CLI deployment")
    elif successful > 0:
        print("⚠️  HTTP API is partially functional")
        print("   Some endpoints work, others don't")
        print("   Check CORS and authentication settings")
    else:
        print("❌ HTTP API is not accessible")
        print("   Possible issues:")
        print("   1. Deployment not running")
        print("   2. API key invalid or expired")
        print("   3. CORS configuration issues")
        print("   4. Wrong deployment URL")
    
    print("\n📚 Next Steps:")
    print("1. Get deploy key from Convex dashboard for CLI deployment")
    print("2. Or configure agents to use HTTP API if it works")
    print("3. Check Convex dashboard for deployment status")
    
    # Save results
    with open("http_api_test_results.json", "w") as f:
        json.dump({
            "timestamp": "2026-03-07T06:45:00Z",
            "convex_url": CONVEX_URL,
            "api_key_type": "JWT",
            "results": results,
            "summary": {
                "total_tests": total,
                "successful_tests": successful,
                "success_rate": successful/total if total > 0 else 0
            }
        }, f, indent=2)
    
    print(f"\n✅ Results saved to: http_api_test_results.json")
    
    return 0 if successful > 0 else 1

if __name__ == "__main__":
    sys.exit(main())