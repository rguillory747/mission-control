"use client";

import { useQuery } from "convex/react";
import { api } from "../../../convex/_generated/api";
import { ConvexClientProvider } from "../ConvexClientProvider";
import { useState, useEffect } from "react";

function DebugContent() {
  const tasks = useQuery(api.tasks.list);
  const agents = useQuery(api.agents.list);
  const activities = useQuery(api.activities.list, { limit: 10 });
  
  const [connectionStatus, setConnectionStatus] = useState<string>("Checking...");
  const [convexUrl, setConvexUrl] = useState<string>("");

  useEffect(() => {
    // Check if Convex URL is available
    const url = process.env.NEXT_PUBLIC_CONVEX_URL;
    setConvexUrl(url || "NOT SET");
    
    // Test connection
    if (url) {
      fetch(url + "/api", { method: "OPTIONS" })
        .then(response => {
          if (response.status === 200) {
            setConnectionStatus("✅ Connected to Convex");
          } else {
            setConnectionStatus(`❌ Convex returned ${response.status}`);
          }
        })
        .catch(error => {
          setConnectionStatus(`❌ Error: ${error.message}`);
        });
    } else {
      setConnectionStatus("❌ NEXT_PUBLIC_CONVEX_URL not set");
    }
  }, []);

  return (
    <div className="p-8 bg-[#0a0a0a] text-white min-h-screen">
      <h1 className="text-3xl font-bold mb-6 text-emerald-500">Mission Control Debug</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        <div className="bg-[#1a1a1a] p-4 rounded-lg border border-[#2a2a2a]">
          <h2 className="text-xl font-semibold mb-2">Connection Status</h2>
          <p className="mb-2">Convex URL: <code className="bg-[#2a2a2a] px-2 py-1 rounded">{convexUrl}</code></p>
          <p className={`font-mono ${connectionStatus.includes("✅") ? "text-emerald-400" : "text-red-400"}`}>
            {connectionStatus}
          </p>
        </div>
        
        <div className="bg-[#1a1a1a] p-4 rounded-lg border border-[#2a2a2a]">
          <h2 className="text-xl font-semibold mb-2">Data Status</h2>
          <p>Tasks: {tasks ? tasks.length : "Loading..."} items</p>
          <p>Agents: {agents ? agents.length : "Loading..."} items</p>
          <p>Activities: {activities ? activities.length : "Loading..."} items</p>
        </div>
      </div>
      
      <div className="bg-[#1a1a1a] p-4 rounded-lg border border-[#2a2a2a] mb-8">
        <h2 className="text-xl font-semibold mb-4">Raw Data</h2>
        
        <div className="mb-6">
          <h3 className="text-lg font-medium mb-2">Tasks ({tasks ? tasks.length : 0})</h3>
          <pre className="bg-[#0c0c0c] p-4 rounded overflow-auto max-h-64 text-sm">
            {JSON.stringify(tasks, null, 2)}
          </pre>
        </div>
        
        <div className="mb-6">
          <h3 className="text-lg font-medium mb-2">Agents ({agents ? agents.length : 0})</h3>
          <pre className="bg-[#0c0c0c] p-4 rounded overflow-auto max-h-64 text-sm">
            {JSON.stringify(agents, null, 2)}
          </pre>
        </div>
        
        <div>
          <h3 className="text-lg font-medium mb-2">Recent Activities ({activities ? activities.length : 0})</h3>
          <pre className="bg-[#0c0c0c] p-4 rounded overflow-auto max-h-64 text-sm">
            {JSON.stringify(activities, null, 2)}
          </pre>
        </div>
      </div>
      
      <div className="bg-[#1a1a1a] p-4 rounded-lg border border-[#2a2a2a]">
        <h2 className="text-xl font-semibold mb-4">Test API Endpoints</h2>
        <div className="space-y-4">
          <div>
            <button 
              onClick={async () => {
                const response = await fetch("/api/ops/health");
                const data = await response.json();
                alert(`Health: ${JSON.stringify(data, null, 2)}`);
              }}
              className="px-4 py-2 bg-emerald-500/20 text-emerald-500 border border-emerald-500/30 rounded hover:bg-emerald-500/30 transition-colors"
            >
              Test Health Endpoint
            </button>
          </div>
          
          <div>
            <button 
              onClick={async () => {
                const response = await fetch("/api/heartbeat", {
                  method: "POST",
                  headers: { "Content-Type": "application/json" },
                  body: JSON.stringify({
                    name: "debug-test",
                    status: "active",
                    currentTask: "Testing debug page"
                  })
                });
                const data = await response.json();
                alert(`Heartbeat: ${JSON.stringify(data, null, 2)}`);
              }}
              className="px-4 py-2 bg-blue-500/20 text-blue-500 border border-blue-500/30 rounded hover:bg-blue-500/30 transition-colors"
            >
              Test Heartbeat API
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default function DebugPage() {
  return (
    <ConvexClientProvider>
      <DebugContent />
    </ConvexClientProvider>
  );
}