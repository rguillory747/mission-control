#!/usr/bin/env python3
"""
API Endpoint Testing Script for Mission Control
Tests all documented API endpoints from SKILL.md
"""

import json
import requests
import sys
from datetime import datetime

class MissionControlAPITester:
    def __init__(self, base_url="http://localhost:3000"):
        self.base_url = base_url
        self.results = {}
        
    def test_heartbeat(self):
        """Test POST /api/heartbeat endpoint"""
        print("\n🧪 Testing POST /api/heartbeat")
        
        url = f"{self.base_url}/api/heartbeat"
        test_data = {
            "name": "TestAgent",
            "status": "active",
            "currentTask": "Testing API endpoints"
        }
        
        try:
            response = requests.post(url, json=test_data, timeout=10)
            
            result = {
                "status_code": response.status_code,
                "success": response.status_code == 200,
                "response": response.json() if response.status_code == 200 else response.text
            }
            
            if result["success"]:
                print(f"✅ Heartbeat successful: {result['response']}")
            else:
                print(f"❌ Heartbeat failed: HTTP {result['status_code']}")
                print(f"   Response: {result['response'][:200]}")
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Heartbeat request failed: {e}")
            return {"success": False, "error": str(e)}
    
    def test_activity(self):
        """Test POST /api/activity endpoint"""
        print("\n🧪 Testing POST /api/activity")
        
        url = f"{self.base_url}/api/activity"
        test_data = {
            "agent": "TestAgent",
            "action": "Tested API endpoints",
            "detail": "Ran comprehensive API tests for Mission Control"
        }
        
        try:
            response = requests.post(url, json=test_data, timeout=10)
            
            result = {
                "status_code": response.status_code,
                "success": response.status_code == 200,
                "response": response.json() if response.status_code == 200 else response.text
            }
            
            if result["success"]:
                print(f"✅ Activity logged: {result['response']}")
            else:
                print(f"❌ Activity logging failed: HTTP {result['status_code']}")
                print(f"   Response: {result['response'][:200]}")
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Activity request failed: {e}")
            return {"success": False, "error": str(e)}
    
    def test_task_create(self):
        """Test POST /api/task-create endpoint"""
        print("\n🧪 Testing POST /api/task-create")
        
        url = f"{self.base_url}/api/task-create"
        test_data = {
            "title": "Test API Endpoints",
            "description": "Create comprehensive API test suite for Mission Control",
            "status": "in_progress",  # Note: underscore, not hyphen
            "assignee": "Forge",
            "priority": "P1"
        }
        
        try:
            response = requests.post(url, json=test_data, timeout=10)
            
            result = {
                "status_code": response.status_code,
                "success": response.status_code == 200,
                "response": response.json() if response.status_code == 200 else response.text
            }
            
            if result["success"]:
                print(f"✅ Task created: {result['response']}")
            else:
                print(f"❌ Task creation failed: HTTP {result['status_code']}")
                print(f"   Response: {result['response'][:200]}")
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Task creation request failed: {e}")
            return {"success": False, "error": str(e)}
    
    def test_task_update(self):
        """Test POST /api/task-update endpoint"""
        print("\n🧪 Testing POST /api/task-update")
        
        url = f"{self.base_url}/api/task-update"
        test_data = {
            "title": "Test API Endpoints",
            "status": "done",  # From SKILL.md: inbox, in_progress, review, done, blocked
            "assignee": "Forge"
        }
        
        try:
            response = requests.post(url, json=test_data, timeout=10)
            
            result = {
                "status_code": response.status_code,
                "success": response.status_code == 200,
                "response": response.json() if response.status_code == 200 else response.text
            }
            
            if result["success"]:
                print(f"✅ Task updated: {result['response']}")
            else:
                print(f"❌ Task update failed: HTTP {result['status_code']}")
                print(f"   Response: {result['response'][:200]}")
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Task update request failed: {e}")
            return {"success": False, "error": str(e)}
    
    def test_metric(self):
        """Test POST /api/metric endpoint"""
        print("\n🧪 Testing POST /api/metric")
        
        url = f"{self.base_url}/api/metric"
        test_data = {
            "name": "api_tests_run",
            "value": 1,
            "agent": "TestAgent"
        }
        
        try:
            response = requests.post(url, json=test_data, timeout=10)
            
            result = {
                "status_code": response.status_code,
                "success": response.status_code == 200,
                "response": response.json() if response.status_code == 200 else response.text
            }
            
            if result["success"]:
                print(f"✅ Metric recorded: {result['response']}")
            else:
                print(f"❌ Metric recording failed: HTTP {result['status_code']}")
                print(f"   Response: {result['response'][:200]}")
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Metric request failed: {e}")
            return {"success": False, "error": str(e)}
    
    def test_health(self):
        """Test GET /api/ops/health endpoint"""
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
                print(f"✅ Health check: {result['response']}")
            else:
                print(f"❌ Health check failed: HTTP {result['status_code']}")
                print(f"   Response: {result['response'][:200]}")
            
            return result
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Health check request failed: {e}")
            return {"success": False, "error": str(e)}
    
    def test_all_endpoints(self):
        """Test all documented API endpoints"""
        print("=" * 60)
        print("Mission Control - API Endpoint Testing")
        print("=" * 60)
        
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "base_url": self.base_url,
            "endpoints": {}
        }
        
        # Test each endpoint
        self.results["endpoints"]["heartbeat"] = self.test_heartbeat()
        self.results["endpoints"]["activity"] = self.test_activity()
        self.results["endpoints"]["task_create"] = self.test_task_create()
        self.results["endpoints"]["task_update"] = self.test_task_update()
        self.results["endpoints"]["metric"] = self.test_metric()
        self.results["endpoints"]["health"] = self.test_health()
        
        # Calculate statistics
        successful = sum(1 for endpoint in self.results["endpoints"].values() if endpoint.get("success", False))
        total = len(self.results["endpoints"])
        
        self.results["summary"] = {
            "total_endpoints_tested": total,
            "successful_endpoints": successful,
            "success_rate": successful / total if total > 0 else 0
        }
        
        return self.results
    
    def generate_report(self):
        """Generate a comprehensive testing report"""
        print("\n📊 Generating API testing report...")
        
        report = {
            "timestamp": self.results["timestamp"],
            "base_url": self.results["base_url"],
            "summary": self.results["summary"],
            "detailed_results": self.results["endpoints"],
            "recommendations": [],
            "status": "unknown"
        }
        
        # Determine overall status
        success_rate = report["summary"]["success_rate"]
        if success_rate == 1.0:
            report["status"] = "all_endpoints_working"
        elif success_rate >= 0.5:
            report["status"] = "partially_working"
        elif success_rate > 0:
            report["status"] = "minimally_working"
        else:
            report["status"] = "no_endpoints_working"
        
        # Generate recommendations
        if report["status"] == "all_endpoints_working":
            report["recommendations"].append("✅ All API endpoints are working correctly")
            report["recommendations"].append("Proceed with OpenClaw integration")
            report["recommendations"].append("Test with real agent data")
        
        elif report["status"] == "partially_working":
            report["recommendations"].append("⚠️ Some API endpoints need attention")
            
            # List failing endpoints
            failing = []
            for endpoint_name, result in report["detailed_results"].items():
                if not result.get("success", False):
                    failing.append(endpoint_name)
            
            if failing:
                report["recommendations"].append(f"Failing endpoints: {', '.join(failing)}")
            
            report["recommendations"].append("Check server logs for errors")
            report["recommendations"].append("Verify Convex backend is running")
        
        elif report["status"] == "minimally_working":
            report["recommendations"].append("❌ Most API endpoints are failing")
            report["recommendations"].append("Check if server is running")
            report["recommendations"].append("Verify network connectivity")
            report["recommendations"].append("Check CORS configuration")
        
        else:
            report["recommendations"].append("❌ No API endpoints are working")
            report["recommendations"].append("Server may not be running")
            report["recommendations"].append("Check if port 3000 is accessible")
            report["recommendations"].append("Verify Next.js build completed successfully")
        
        # Save report to file
        report_file = "api_testing_report.json"
        with open(report_file, "w") as f:
            json.dump(report, f, indent=2)
        
        print(f"✅ Report saved to {report_file}")
        
        # Print summary
        print("\n" + "=" * 60)
        print("API Testing Report Summary")
        print("=" * 60)
        print(f"Status: {report['status'].replace('_', ' ').title()}")
        print(f"Success Rate: {report['summary']['success_rate']:.0%} "
              f"({report['summary']['successful_endpoints']}/{report['summary']['total_endpoints_tested']})")
        
        print("\nEndpoint Results:")
        for endpoint_name, result in report["detailed_results"].items():
            status = "✅" if result.get("success", False) else "❌"
            print(f"  {status} {endpoint_name}: HTTP {result.get('status_code', 'N/A')}")
        
        if report["recommendations"]:
            print("\nRecommendations:")
            for i, rec in enumerate(report["recommendations"], 1):
                print(f"  {i}. {rec}")
        
        print("=" * 60)
        
        return report

def main():
    """Main testing function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Test Mission Control API endpoints")
    parser.add_argument("--url", default="http://localhost:3000", 
                       help="Base URL of Mission Control (default: http://localhost:3000)")
    parser.add_argument("--report-only", action="store_true",
                       help="Only generate report from existing results")
    
    args = parser.parse_args()
    
    tester = MissionControlAPITester(args.url)
    
    if args.report_only:
        # Load existing results and generate report
        try:
            with open("api_testing_report.json", "r") as f:
                results = json.load(f)
            tester.results = results
            tester.generate_report()
        except FileNotFoundError:
            print("❌ No existing test results found. Run tests first.")
            return 1
    else:
        # Run tests and generate report
        results = tester.test_all_endpoints()
        report = tester.generate_report()
        
        # Determine exit code
        if report["status"] == "all_endpoints_working":
            print("\n🎉 All API tests passed! Ready for OpenClaw integration.")
            return 0
        else:
            print(f"\n⚠️  API tests completed with issues. Status: {report['status']}")
            return 1

if __name__ == "__main__":
    sys.exit(main())