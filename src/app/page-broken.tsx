"use client";

import { AgentCards } from "@/components/AgentCards";
import { ActivityFeed } from "@/components/ActivityFeed";
import { TaskBoard } from "@/components/TaskBoard";
import { MetricsBar } from "@/components/MetricsBar";
import { Header } from "@/components/Header";
import { Onboarding } from "@/components/Onboarding";
import { RevenueTrackerV2 } from "@/components/RevenueTrackerV2";
import { BuildQueue } from "@/components/BuildQueue";
import { TaskCreator } from "@/components/TaskCreator";
import { LeadTracker } from "@/components/LeadTracker";
import { ActionLog } from "@/components/ActionLog";
import { useState, useEffect } from "react";

type TabType = "dashboard" | "leads" | "actions";

function TabButton({
  label,
  isActive,
  onClick,
}: {
  label: string;
  isActive: boolean;
  onClick: () => void;
}) {
  return (
    <button
      onClick={onClick}
      className={`px-4 py-2 font-mono text-xs uppercase tracking-wider rounded transition-colors ${
        isActive
          ? "bg-emerald-500/20 text-emerald-500 border border-emerald-500/30"
          : "text-[#737373] hover:text-white hover:bg-[#1e1e1e] border border-transparent"
      }`}
    >
      {label}
    </button>
  );
}

export default function DashboardFixed() {
  const [activeTab, setActiveTab] = useState<TabType>("dashboard");
  const [agents, setAgents] = useState<any[]>([]);
  const [tasks, setTasks] = useState<any[]>([]);
  const [activities, setActivities] = useState<any[]>([]);
  const [metrics, setMetrics] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchData() {
      setIsLoading(true);
      setError(null);
      
      try {
        // Fetch all data in parallel
        const [agentsRes, tasksRes, activitiesRes, metricsRes] = await Promise.all([
          fetch('/api/agents').then(res => res.json()),
          fetch('/api/tasks').then(res => res.json()),
          fetch('/api/activities').then(res => res.json()),
          fetch('/api/metrics').then(res => res.json())
        ]);

        if (agentsRes.ok) setAgents(agentsRes.agents || []);
        if (tasksRes.ok) setTasks(tasksRes.tasks || []);
        if (activitiesRes.ok) setActivities(activitiesRes.activities || []);
        if (metricsRes.ok) setMetrics(metricsRes.metrics || []);

        // If any request failed, set error
        if (!agentsRes.ok || !tasksRes.ok || !activitiesRes.ok || !metricsRes.ok) {
          setError('Some data failed to load. Showing available data.');
        }
      } catch (err) {
        console.error('Error fetching data:', err);
        setError('Failed to load dashboard data');
      } finally {
        setIsLoading(false);
      }
    }

    fetchData();
    
    // Refresh data every 30 seconds
    const interval = setInterval(fetchData, 30000);
    return () => clearInterval(interval);
  }, []);

  const isEmpty = agents.length === 0 && tasks.length === 0 && activities.length === 0;

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="text-emerald-500 font-mono text-lg mb-2">LOADING DASHBOARD...</div>
          <div className="w-48 h-1 bg-[#1e1e1e] rounded overflow-hidden">
            <div className="h-full bg-emerald-500 rounded animate-pulse" style={{ width: "60%" }} />
          </div>
          <div className="mt-4 text-sm text-[#737373]">
            Fetching data from Mission Control API...
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="text-red-500 font-mono text-lg mb-2">⚠️ PARTIAL DATA LOAD</div>
          <div className="text-white mb-4">{error}</div>
          <div className="text-sm text-[#737373]">
            Agents: {agents.length} | Tasks: {tasks.length} | Activities: {activities.length}
          </div>
        </div>
      </div>
    );
  }

  if (isEmpty) {
    return <Onboarding />;
  }

  const renderTabContent = () => {
    switch (activeTab) {
      case "leads":
        return (
          <div className="flex-1 px-4 pb-3 overflow-auto">
            <LeadTracker />
          </div>
        );
      
      case "actions":
        return (
          <div className="flex-1 px-4 pb-3 overflow-auto">
            <ActionLog />
          </div>
        );

      default: // dashboard
        return (
          <div className="flex-1 overflow-auto">
            {/* Agent Status Cards */}
            <div className="px-4 py-3">
              <AgentCards agents={agents} />
            </div>

            {/* Main Content: Activity Feed + Task Board */}
            <div className="flex-1 flex gap-4 px-4 pb-3 min-h-0">
              {/* Activity Feed - 60% */}
              <div className="w-[60%] flex flex-col min-h-0">
                <ActivityFeed activities={activities} agents={agents} />
              </div>

              {/* Task Board - 40% */}
              <div className="w-[40%] flex flex-col min-h-0">
                <TaskBoard tasks={tasks} agents={agents} />
              </div>
            </div>

            {/* Bottom Row: Metrics + Build Queue */}
            <div className="flex gap-4 px-4 pb-3">
              {/* Metrics - 70% */}
              <div className="w-[70%]">
                <MetricsBar metrics={metrics} />
              </div>

              {/* Build Queue - 30% */}
              <div className="w-[30%]">
                <BuildQueue />
              </div>
            </div>

            {/* Revenue Tracker */}
            <div className="px-4 pb-3">
              <RevenueTrackerV2 />
            </div>
          </div>
        );
    }
  };

  return (
    <div className="min-h-screen bg-[#0a0a0a] text-white flex flex-col">
      {/* Header */}
      <Header />

      {/* Tab Navigation */}
      <div className="flex gap-2 px-4 pt-3">
        <TabButton
          label="Dashboard"
          isActive={activeTab === "dashboard"}
          onClick={() => setActiveTab("dashboard")}
        />
        <TabButton
          label="Leads"
          isActive={activeTab === "leads"}
          onClick={() => setActiveTab("leads")}
        />
        <TabButton
          label="Actions"
          isActive={activeTab === "actions"}
          onClick={() => setActiveTab("actions")}
        />
      </div>

      {/* Task Creator */}
      <div className="px-4 py-3">
        <TaskCreator />
      </div>

      {/* Main Content */}
      {renderTabContent()}

      {/* Data Status Footer */}
      <div className="px-4 py-2 text-xs text-[#737373] border-t border-[#1e1e1e]">
        Data: {agents.length} agents, {tasks.length} tasks, {activities.length} activities • 
        Last updated: {new Date().toLocaleTimeString()} • 
        <button 
          onClick={() => window.location.reload()}
          className="ml-2 text-emerald-500 hover:text-emerald-400"
        >
          Refresh
        </button>
      </div>
    </div>
  );
}