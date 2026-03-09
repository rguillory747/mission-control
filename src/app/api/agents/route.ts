import { NextRequest, NextResponse } from 'next/server';
import { withCors, corsOptionsResponse, corsJsonResponse, corsErrorResponse } from '@/lib/cors';

const CONVEX_SITE_URL = process.env.CONVEX_SITE_URL || 'https://good-corgi-153.convex.site';

export async function GET(request: NextRequest) {
  try {
    // Try to fetch from Convex HTTP actions
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 5000);
    
    const response = await fetch(`${CONVEX_SITE_URL}/api/agents`, {
      headers: {
        'Content-Type': 'application/json',
      },
      signal: controller.signal,
    });
    
    clearTimeout(timeoutId);

    if (!response.ok) {
      throw new Error(`Convex API returned ${response.status}: ${response.statusText}`);
    }

    const data = await response.json();
    
    console.log(`[Mission Control] Fetched ${data.agents?.length || 0} agents from Convex`);

    return corsJsonResponse({
      ok: true,
      agents: data.agents || [],
      count: data.agents?.length || 0,
      source: 'convex',
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    console.error('[Mission Control] Agents fetch error:', error);
    
    // Fallback to mock data if Convex is unavailable
    const mockAgents = [
      {
        _id: "mock-1",
        name: "Jarvis",
        role: "Squad Lead",
        emoji: "🎯",
        color: "#10b981",
        status: "active",
        currentTask: "Coordinating agent squad operations",
        lastSeen: Date.now()
      },
      {
        _id: "mock-2",
        name: "Forge",
        role: "Code Builder",
        emoji: "🔨",
        color: "#f59e0b",
        status: "active",
        currentTask: "Building pricing page",
        lastSeen: Date.now()
      },
      {
        _id: "mock-3",
        name: "Scout",
        role: "Research Specialist",
        emoji: "🔍",
        color: "#3b82f6",
        status: "active",
        currentTask: "Researching competitor pricing",
        lastSeen: Date.now()
      }
    ];

    return corsJsonResponse({
      ok: true,
      agents: mockAgents,
      count: mockAgents.length,
      source: 'mock-fallback',
      error: error instanceof Error ? error.message : 'Unknown error',
      timestamp: new Date().toISOString()
    });
  }
}

export async function OPTIONS() {
  return corsOptionsResponse();
}
