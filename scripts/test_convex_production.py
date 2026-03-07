#!/usr/bin/env python3
"""
Test Convex Production Deployment
"""

import requests
import json
import sys

# Updated configuration
CONVEX_URL = "https://good-corgi-153.convex.cloud"
CONVEX_API_KEY = "YOUR_CONVEX_API_KEY_HERE"

def test_endpoint(endpoint, method="GET", data=None):
    """Test a Convex endpoint"""
    url = f"{CONVEX_URL}{endpoint}"
    headers = {"Content-Type": "application/json"}
    
    if CONVEX_API_KEY:
        headers["Authorization"] = f"Bearer {CONVEX_API_KEY}"
    
    try:
        if method == "POST":
            response = requests.post(url, headers=headers, json=data, timeout=10)
        else:
            response = requests.get(url, headers=headers, timeout=10)
        
        return {
            "success": response.status_code == 200,
            "status": response.status_code,
            "response": response.json() if response.status_code == 200 else response.text
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

def main():
    print("=" * 60)
    print("Testing Convex Production Deployment")
    print("=" * 60)
    print(f"URL: {CONVEX_URL}")
    
    # Test 1: Basic ping
    print("\n1. Testing ping...")
    result = test_endpoint("/api/ping")
    if result["success"]:
        print(f"   ✅ Ping successful: {result['response']}")
    else:
        print(f"   ❌ Ping failed: {result.get('status', 'N/A')}")
        print(f"   Error: {result.get('response', result.get('error', 'Unknown'))}")
    
    # Test 2: HTTP actions from convex/http.ts
    print("\n2. Testing HTTP actions...")
    
    actions = [
        ("/api/heartbeat", {"name": "TestAgent", "status": "active"}),
        ("/api/activity", {"agent": "TestAgent", "action": "Testing"}),
    ]
    
    for endpoint, data in actions:
        print(f"\n   Testing {endpoint}...")
        result = test_endpoint(endpoint, "POST", data)
        if result["success"]:
            print(f"      ✅ Success: {result['response']}")
        else:
            print(f"      ❌ Failed: HTTP {result.get('status', 'N/A')}")
            print(f"      Error: {result.get('response', result.get('error', 'Unknown'))[:100]}")
    
    # Test 3: Check if we can query data
    print("\n3. Testing data query...")
    print("   Note: May need proper authentication setup")
    
    # Test 4: Check CORS
    print("\n4. Testing CORS headers...")
    try:
        response = requests.options(CONVEX_URL + "/api/heartbeat", timeout=5)
        cors_headers = {k: v for k, v in response.headers.items() if "access-control" in k.lower()}
        if cors_headers:
            print(f"   ✅ CORS headers present: {list(cors_headers.keys())}")
        else:
            print("   ⚠️  No CORS headers detected")
    except Exception as e:
        print(f"   ❌ CORS test failed: {e}")
    
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    
    # Check if deployment is accessible
    try:
        response = requests.get(CONVEX_URL, timeout=5)
        if response.status_code != 404:
            print(f"✅ Deployment is accessible (HTTP {response.status_code})")
        else:
            print("❌ Deployment returns 404 - may not be configured for HTTP")
    except Exception as e:
        print(f"❌ Cannot reach deployment: {e}")
    
    print("\n🎯 Next Steps:")
    print("1. Check Convex dashboard for HTTP configuration")
    print("2. Verify CORS settings in convex/http.ts")
    print("3. Test with proper authentication")
    print("4. Deploy frontend to Vercel")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())