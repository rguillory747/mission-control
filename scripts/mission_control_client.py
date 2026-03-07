#!/usr/bin/env python3
"""
Mission Control Python Client Library
For AI agents to integrate with Mission Control dashboard
"""

import os
import requests
import time
from typing import Optional, Dict, Any
from dataclasses import dataclass
import json

@dataclass
class MissionControlConfig:
    """Configuration for Mission Control client"""
    base_url: str = "https://mission-control-aiorg-bvbdrgk6i-reginald-guillorys-projects.vercel.app"
    heartbeat_interval: int = 30  # seconds
    timeout: int = 10  # seconds
    
    @classmethod
    def from_env(cls):
        """Load configuration from environment variables"""
        base_url = os.getenv("MISSION_CONTROL_URL", cls.base_url)
        heartbeat_interval = int(os.getenv("MISSION_CONTROL_HEARTBEAT_INTERVAL", cls.heartbeat_interval))
        timeout = int(os.getenv("MISSION_CONTROL_TIMEOUT", cls.timeout))
        return cls(base_url=base_url, heartbeat_interval=heartbeat_interval, timeout=timeout)

class MissionControlError(Exception):
    """Mission Control API error"""
    pass

class MissionControlAgent:
    """
    Python client for AI agents to integrate with Mission Control
    
    Usage:
        >>> agent = MissionControlAgent("Jarvis")
        >>> agent.heartbeat("active", "Managing agents")
        >>> agent.log_activity("Booted", "Connected to Mission Control")
    """
    
    def __init__(self, name: str, config: Optional[MissionControlConfig] = None):
        self.name = name
        self.config = config or MissionControlConfig.from_env()
        self._heartbeat_thread = None
        self._running = False
        
    def _make_request(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Make HTTP request to Mission Control API"""
        url = f"{self.config.base_url}{endpoint}"
        
        try:
            response = requests.post(
                url,
                json=data,
                timeout=self.config.timeout,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise MissionControlError(f"API request failed: {e}")
    
    def heartbeat(self, status: str = "active", current_task: str = "") -> Dict[str, Any]:
        """
        Send heartbeat to Mission Control
        
        Args:
            status: Agent status ("active", "idle", "sleeping", "error")
            current_task: What the agent is currently working on
            
        Returns:
            API response as dictionary
        """
        data = {
            "name": self.name,
            "status": status,
            "currentTask": current_task
        }
        
        return self._make_request("/api/heartbeat", data)
    
    def log_activity(self, action: str, detail: str = "") -> Dict[str, Any]:
        """
        Log activity to Mission Control
        
        Args:
            action: What the agent did
            detail: Additional details
            
        Returns:
            API response as dictionary
        """
        data = {
            "agent": self.name,
            "action": action,
            "detail": detail
        }
        
        return self._make_request("/api/activity", data)
    
    def create_task(self, title: str, description: str = "", 
                   status: str = "inbox", assignee: str = "", 
                   priority: str = "P1") -> Dict[str, Any]:
        """
        Create a new task in Mission Control
        
        Args:
            title: Task title
            description: Task description
            status: Task status ("inbox", "in_progress", "review", "done", "blocked")
            assignee: Who the task is assigned to
            priority: Task priority ("P0", "P1", "P2")
            
        Returns:
            API response as dictionary
        """
        if not assignee:
            assignee = self.name
            
        data = {
            "title": title,
            "description": description,
            "status": status,
            "assignee": assignee,
            "priority": priority
        }
        
        return self._make_request("/api/task-create", data)
    
    def update_task(self, title: str, status: str, assignee: Optional[str] = None) -> Dict[str, Any]:
        """
        Update task status in Mission Control
        
        Args:
            title: Task title
            status: New status ("inbox", "in_progress", "review", "done", "blocked")
            assignee: Optional new assignee
            
        Returns:
            API response as dictionary
        """
        data = {
            "title": title,
            "status": status
        }
        
        if assignee:
            data["assignee"] = assignee
            
        return self._make_request("/api/task-update", data)
    
    def report_metric(self, key: str, value: Optional[float] = None, 
                     increment: Optional[float] = None) -> Dict[str, Any]:
        """
        Report metric to Mission Control
        
        Args:
            key: Metric name
            value: Set metric to this value
            increment: Increment metric by this amount
            
        Returns:
            API response as dictionary
        """
        if value is None and increment is None:
            raise ValueError("Either value or increment must be provided")
            
        data = {"key": key}
        if value is not None:
            data["value"] = value
        if increment is not None:
            data["increment"] = increment
            
        return self._make_request("/api/metric", data)
    
    def start_heartbeat_loop(self, status: str = "active", current_task: str = ""):
        """
        Start automatic heartbeat loop (runs in background)
        
        Args:
            status: Default status for heartbeats
            current_task: Default current task
        """
        self._running = True
        
        def heartbeat_loop():
            while self._running:
                try:
                    self.heartbeat(status, current_task)
                except MissionControlError as e:
                    print(f"Heartbeat failed: {e}")
                time.sleep(self.config.heartbeat_interval)
        
        import threading
        self._heartbeat_thread = threading.Thread(target=heartbeat_loop, daemon=True)
        self._heartbeat_thread.start()
        print(f"Heartbeat loop started for {self.name} (interval: {self.config.heartbeat_interval}s)")
    
    def stop_heartbeat_loop(self):
        """Stop automatic heartbeat loop"""
        self._running = False
        if self._heartbeat_thread:
            self._heartbeat_thread.join(timeout=5)
        print(f"Heartbeat loop stopped for {self.name}")
    
    def __enter__(self):
        """Context manager entry"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - stop heartbeat loop"""
        self.stop_heartbeat_loop()

# Example usage
if __name__ == "__main__":
    # Example 1: Simple usage
    print("=== Example 1: Simple Agent ===")
    agent = MissionControlAgent("Jarvis")
    
    # Send heartbeat
    result = agent.heartbeat("active", "Testing Mission Control integration")
    print(f"Heartbeat result: {json.dumps(result, indent=2)}")
    
    # Log activity
    result = agent.log_activity("Booted", "Connected to Mission Control API")
    print(f"Activity result: {json.dumps(result, indent=2)}")
    
    # Create task
    result = agent.create_task(
        title="Test Task",
        description="Created via Python client",
        status="inbox",
        assignee="Jarvis",
        priority="P1"
    )
    print(f"Task create result: {json.dumps(result, indent=2)}")
    
    # Example 2: With automatic heartbeats
    print("\n=== Example 2: With Automatic Heartbeats ===")
    
    # Using context manager for automatic cleanup
    with MissionControlAgent("AutoAgent") as auto_agent:
        auto_agent.start_heartbeat_loop("active", "Running automated tasks")
        
        # Do some work
        auto_agent.log_activity("Started work", "Processing data")
        time.sleep(2)
        auto_agent.log_activity("Completed work", "Processed 100 records")
        
        # Heartbeats continue automatically in background
        time.sleep(10)  # Would send multiple heartbeats during this time
    
    print("\n=== Mission Control Client Ready ===")
    print("To use in your agent:")
    print("1. Set environment variable: export MISSION_CONTROL_URL='https://your-deployment.vercel.app'")
    print("2. Import: from mission_control_client import MissionControlAgent")
    print("3. Create agent: agent = MissionControlAgent('YourAgentName')")
    print("4. Start heartbeats: agent.start_heartbeat_loop()")