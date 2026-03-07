#!/usr/bin/env python3
"""
Local API Testing Script for Mission Control
Tests Next.js API routes that work without Convex backend
"""

import json
import requests
import sys
from datetime import datetime

class LocalAPITester:
    def __init__(self, base_url="http://localhost:3000"):
        self.base_url = base_url
        self.results = {}
        
    def test_ops_health(self):
        """Test GET /api/ops/health"""
        print("\n🧪 Testing GET /api/ops/health")
        
        url = f"{self.base_url}/api/ops/health"
        
        try:
            response = requests.get(url, timeout=10)
            
            result = {
                "status_code": response.status_code,
                "success": response.status_code == 200,
                "response": response.json() if response.status_code == 200 else response.text
            }
            
            if result["success"]:
                print(f"✅ Health check successful")
                print(f"   Response: {json.dumps(result['response'], indent=2)}")
            else:
                print(f"❌ Health check failed: HTTP {result['status_code']}")
                print(f"   Response: {result['response'][:200]}")
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Health check request failed: {e}")
            return {"success": False, "error": str(e)}
    
    def test_ops_heartbeat_get(self):
        """Test GET /api/ops/heartbeat"""
        print("\n🧪 Testing GET /api/ops/heartbeat")
        
        url = f"{self.base_url}/api/ops/heartbeat"
        
        try:
            response = requests.get(url, timeout=10)
            
            result = {
                "status_code": response.status_code,
                "success": response.status_code == 200,
                "response": response.json() if response.status_code == 200 else response.text
            }
            
            if result["success"]:
                print(f"✅ Heartbeat GET successful")
                print(f"   Response: {json.dumps(result['response'], indent=2)}")
            else:
                print(f"❌ Heartbeat GET failed: HTTP {result['status_code']}")
                print(f"   Response: {result['response'][:200]}")
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Heartbeat GET request failed: {e}")
            return {"success": False, "error": str(e)}
    
    def test_ops_heartbeat_post(self):
        """Test POST /api/ops/heartbeat"""
        print("\n🧪 Testing POST /api/ops/heartbeat")
        
        url = f"{self.base_url}/api/ops/heartbeat"
        test_data = {
            "agent": "TestAgent",
            "status": "active"
        }
        
        try:
            response = requests.post(url, json=test_data, timeout=10)
            
            result = {
                "status_code": response.status_code,
                "success": response.status_code == 200,
                "response": response.json() if response.status_code == 200 else response.text
            }
            
            if result["success"]:
                print(f"✅ Heartbeat POST successful")
                print(f"   Response: {json.dumps(result['response'], indent=2)}")
            else:
                print(f"❌ Heartbeat POST failed: HTTP {result['status_code']}")
                print(f"   Response: {result['response'][:200]}")
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Heartbeat POST request failed: {e}")
            return {"success": False, "error": str(e)}
    
    def test_build_queue(self):
        """Test GET /api/build-queue"""
        print("\n🧪 Testing GET /api/build-queue")
        
        url = f"{self.base_url}/api/build-queue"
        
        try:
            response = requests.get(url, timeout=10)
            
            result = {
                "status_code": response.status_code,
                "success": response.status_code == 200,
                "response": response.json() if response.status_code == 200 else response.text
            }
            
            if result["success"]:
                print(f"✅ Build queue check successful")
                print(f"   Response: {json.dumps(result['response'], indent=2)}")
            else:
                print(f"❌ Build queue check failed: HTTP {result['status_code']}")
                print(f"   Response: {result['response'][:200]}")
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Build queue request failed: {e}")
            return {"success": False, "error": str(e)}
    
    def test_frontend_pages(self):
        """Test basic frontend pages"""
        print("\n🧪 Testing frontend pages")
        
        pages_to_test = [
            "/",          # Main dashboard
            "/ops",       # Operations page
            "/tasks",     # Tasks page
            "/activity",  # Activity feed
            "/settings"   # Settings page
        ]
        
        results = {}
        
        for page in pages_to_test:
            url = f"{self.base_url}{page}"
            
            try:
                response = requests.get(url, timeout=10)
                
                result = {
                    "status_code": response.status_code,
                    "success": response.status_code == 200,
                    "content_type": response.headers.get("content-type", ""),
                    "content_length": len(response.text)
                }
                
                if result["success"]:
                    print(f"✅ {page}: HTTP 200 ({result['content_length']} bytes)")
                else:
                    print(f"❌ {page}: HTTP {result['status_code']}")
                
                results[page] = result
                
            except requests.exceptions.RequestException as e:
                print(f"❌ {page}: Request failed - {e}")
                results[page] = {"success": False, "error": str(e)}
        
        return results
    
    def test_all_local_endpoints(self):
        """Test all local endpoints that don't require Convex"""
        print("=" * 60)
        print("Mission Control - Local API Testing")
        print("=" * 60)
        print("Testing endpoints that work without Convex backend")
        
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "base_url": self.base_url,
            "endpoints": {},
            "frontend_pages": {}
        }
        
        # Test API endpoints
        self.results["endpoints"]["ops_health"] = self.test_ops_health()
        self.results["endpoints"]["ops_heartbeat_get"] = self.test_ops_heartbeat_get()
        self.results["endpoints"]["ops_heartbeat_post"] = self.test_ops_heartbeat_post()
        self.results["endpoints"]["build_queue"] = self.test_build_queue()
        
        # Test frontend pages
        self.results["frontend_pages"] = self.test_frontend_pages()
        
        # Calculate statistics
        api_successful = sum(1 for endpoint in self.results["endpoints"].values() if endpoint.get("success", False))
        api_total = len(self.results["endpoints"])
        
        page_successful = sum(1 for page in self.results["frontend_pages"].values() if page.get("success", False))
        page_total = len(self.results["frontend_pages"])
        
        self.results["summary"] = {
            "api_endpoints_tested": api_total,
            "api_endpoints_successful": api_successful,
            "api_success_rate": api_successful / api_total if api_total > 0 else 0,
            "frontend_pages_tested": page_total,
            "frontend_pages_successful": page_successful,
            "frontend_success_rate": page_successful / page_total if page_total > 0 else 0
        }
        
        return self.results
    
    def generate_report(self):
        """Generate a comprehensive testing report"""
        print("\n📊 Generating local testing report...")
        
        report = {
            "timestamp": self.results["timestamp"],
            "base_url": self.results["base_url"],
            "summary": self.results["summary"],
            "api_endpoints": self.results["endpoints"],
            "frontend_pages": self.results["frontend_pages"],
            "convex_dependent_endpoints": {
                "note": "These endpoints require Convex backend to be deployed and running",
                "endpoints": [
                    "POST /api/heartbeat",
                    "POST /api/activity", 
                    "POST /api/task-create",
                    "POST /api/task-update",
                    "POST /api/metric",
                    "POST /api/leads",
                    "POST /api/actions",
                    "POST /api/content-drop"
                ]
            },
            "recommendations": [],
            "status": "unknown"
        }
        
        # Determine overall status
        api_rate = report["summary"]["api_success_rate"]
        frontend_rate = report["summary"]["frontend_success_rate"]
        
        if api_rate == 1.0 and frontend_rate == 1.0:
            report["status"] = "fully_operational_local"
        elif api_rate >= 0.5 and frontend_rate >= 0.5:
            report["status"] = "partially_operational_local"
        elif api_rate > 0 or frontend_rate > 0:
            report["status"] = "minimally_operational_local"
        else:
            report["status"] = "not_operational"
        
        # Generate recommendations
        if report["status"] == "fully_operational_local":
            report["recommendations"].append("✅ Local Next.js server is fully operational")
            report["recommendations"].append("Frontend pages and local API endpoints are working")
            report["recommendations"].append("Next: Deploy Convex backend to enable full functionality")
        
        elif report["status"] == "partially_operational_local":
            report["recommendations"].append("⚠️ Local server is partially operational")
            
            # List failing endpoints
            failing_api = []
            for endpoint_name, result in report["api_endpoints"].items():
                if not result.get("success", False):
                    failing_api.append(endpoint_name)
            
            failing_pages = []
            for page_name, result in report["frontend_pages"].items():
                if not result.get("success", False):
                    failing_pages.append(page_name)
            
            if failing_api:
                report["recommendations"].append(f"Failing API endpoints: {', '.join(failing_api)}")
            
            if failing_pages:
                report["recommendations"].append(f"Failing frontend pages: {', '.join(failing_pages)}")
            
            report["recommendations"].append("Check server logs for errors")
            report["recommendations"].append("Verify Next.js build completed successfully")
        
        elif report["status"] == "minimally_operational_local":
            report["recommendations"].append("❌ Local server has minimal functionality")
            report["recommendations"].append("Check if server is running correctly")
            report["recommendations"].append("Verify port 3000 is accessible")
            report["recommendations"].append("Check for build errors")
        
        else:
            report["recommendations"].append("❌ Local server is not operational")
            report["recommendations"].append("Server may not be running")
            report["recommendations"].append("Check if Next.js dev server started")
            report["recommendations"].append("Verify no port conflicts")
        
        # Add Convex-specific recommendations
        report["recommendations"].append("\n🔧 For full functionality, deploy Convex backend:")
        report["recommendations"].append("  1. Run: npx convex login")
        report["recommendations"].append("  2. Run: npx convex dev")
        report["recommendations"].append("  3. Run: npx convex deploy")
        report["recommendations"].append("  4. Update NEXT_PUBLIC_CONVEX_URL in environment")
        
        # Save report to file
        report_file = "local_testing_report.json"
        with open(report_file, "w") as f:
            json.dump(report, f, indent=2)
        
        print(f"✅ Report saved to {report_file}")
        
        # Print summary
        print("\n" + "=" * 60)
        print("Local Testing Report Summary")
        print("=" * 60)
        print(f"Status: {report['status'].replace('_', ' ').title()}")
        print(f"\nAPI Endpoints: {report['summary']['api_success_rate']:.0%} "
              f"({report['summary']['api_endpoints_successful']}/{report['summary']['api_endpoints_tested']})")
        print(f"Frontend Pages: {report['summary']['frontend_success_rate']:.0%} "
              f"({report['summary']['frontend_pages_successful']}/{report['summary']['frontend_pages_tested']})")
        
        print("\nConvex-Dependent Endpoints (not tested):")
        for endpoint in report["convex_dependent_endpoints"]["endpoints"][:3]:
            print(f"  • {endpoint}")
        print(f"  • ... and {len(report['convex_dependent_endpoints']['endpoints']) - 3} more")
        
        if report["recommendations"]:
            print("\nRecommendations:")
            for i, rec in enumerate(report["recommendations"], 1):
                if rec.startswith("🔧"):
                    print(f"\n{rec}")
                else:
                    print(f"  {i}. {rec}")
        
        print("=" * 60)
        
        return report

def main():
    """Main testing function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Test Mission Control local endpoints")
    parser.add_argument("--url", default="http://localhost:3000", 
                       help="Base URL of Mission Control (default: http://localhost:3000)")
    
    args = parser.parse_args()
    
    print("🚀 Starting local API tests...")
    print(f"📡 Testing against: {args.url}")
    
    tester = LocalAPITester(args.url)
    results = tester.test_all_local_endpoints()
    report = tester.generate_report()
    
    # Determine exit code
    if report["status"] == "fully_operational_local":
        print("\n🎉 Local tests passed! Ready for Convex deployment.")
        return 0
    else:
        print(f"\n⚠️  Local tests completed with issues. Status: {report['status']}")
        return 1

if __name__ == "__main__":
    sys.exit(main())