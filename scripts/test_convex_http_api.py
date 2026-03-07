#!/usr/bin/env python3
"""
Test Convex HTTP API with current API key
Based on: https://docs.convex.dev/http-api/
"""

import requests
import json
import sys

# Current configuration from .env.local
CONVEX_URL = "https://fancy-ape-615.convex.cloud"
CONVEX_API_KEY = "eyJ2MiI6IjVmNWU1MmJlMTVlYTQ2NGE4OWFhYWRkMGFkNmFlY2VjIn0="

def test_http_api():
    """Test Convex HTTP API with current API key"""
    print("=" * 60)
    print("Testing Convex HTTP API")
    print("=" * 60)
    
    # Test 1: Simple ping
    print("\n1. Testing ping endpoint...")
    try:
        response = requests.get(f"{CONVEX_URL}/api/ping", timeout=10)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.text[:100]}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 2: Try to call a query (if API key works)
    print("\n2. Testing query with API key...")
    headers = {
        "Authorization": f"Bearer {CONVEX_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Try to list agents (a common query)
    try:
        # First check what functions are available
        response = requests.post(
            f"{CONVEX_URL}/api/query",
            headers=headers,
            json={"path": "agents:list"},
            timeout=10
        )
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            print(f"   ✅ Success! Response: {response.text[:200]}")
        else:
            print(f"   Response: {response.text[:200]}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 3: Check if this is a deployment API key
    print("\n3. Checking API key type...")
    print(f"   Key: {CONVEX_API_KEY[:50]}...")
    print(f"   Length: {len(CONVEX_API_KEY)} chars")
    
    # Analyze key format
    if CONVEX_API_KEY.startswith("eyJ"):
        print("   Format: JWT token (likely HTTP API key)")
        print("   Purpose: HTTP API authentication")
        print("   ❌ Not suitable for CLI deployment")
    elif "|" in CONVEX_API_KEY:
        print("   Format: Contains '|' (likely deploy key)")
        print("   Purpose: CLI deployment")
        print("   ✅ Suitable for npx convex deploy")
    else:
        print("   Format: Unknown")
    
    # Test 4: Try deployment API endpoint
    print("\n4. Testing deployment API...")
    try:
        # According to [2], deployment API might be different
        deployment_api_url = "https://api.convex.dev/api/deployment"
        response = requests.get(
            deployment_api_url,
            headers={"Authorization": f"Bearer {CONVEX_API_KEY}"},
            timeout=10
        )
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            print(f"   ✅ Deployment API accessible")
            data = response.json()
            print(f"   Data: {json.dumps(data, indent=2)[:200]}...")
        else:
            print(f"   Response: {response.text[:200]}")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n" + "=" * 60)
    print("Analysis Complete")
    print("=" * 60)
    
    # Recommendations
    print("\n🎯 Recommendations:")
    
    if CONVEX_API_KEY.startswith("eyJ"):
        print("1. Current key is a JWT HTTP API key")
        print("2. You need a deploy key for CLI deployment")
        print("3. Get deploy key from: https://dashboard.convex.dev")
        print("4. Format should be: instance-name|key")
        print("5. Set as CONVEX_DEPLOY_KEY environment variable")
    else:
        print("1. Key format unknown")
        print("2. Check Convex dashboard for correct key type")
    
    print("\n📚 Documentation references:")
    print("  • [1] Deploy keys: https://docs.convex.dev/cli/deploy-key-types")
    print("  • [2] Deployment API: https://docs.convex.dev/deployment-api/convex-deployment-api")
    print("  • [3] Deployment URLs: https://docs.convex.dev/client/react/deployment-urls")
    
    return 0

if __name__ == "__main__":
    sys.exit(test_http_api())