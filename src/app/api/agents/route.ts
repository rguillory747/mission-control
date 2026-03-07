import { NextRequest, NextResponse } from 'next/server';

export async function GET(request: NextRequest) {
  try {
    // Try to get from Convex first
    const convexUrl = process.env.NEXT_PUBLIC_CONVEX_URL;
    if (convexUrl) {
      try {
        const { ConvexHttpClient } = await import('convex/browser');
        const { api } = await import('../../../convex/_generated/api');
        
        const convex = new ConvexHttpClient(convexUrl);
        const agents = await convex.query(api.agents.list);

        console.log(`[Mission Control] Fetched ${agents?.length || 0} agents from Convex`);

        return NextResponse.json({
          ok: true,
          agents: agents || [],
          count: agents?.length || 0,
          source: 'convex',
          timestamp: new Date().toISOString()
        });
      } catch (convexError) {
        console.warn('[Mission Control] Convex fetch failed, using mock data:', convexError);
        // Fall through to mock data
      }
    }

    // Mock data as fallback
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

    console.log(`[Mission Control] Using ${mockAgents.length} mock agents`);

    return NextResponse.json({
      ok: true,
      agents: mockAgents,
      count: mockAgents.length,
      source: 'mock',
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    console.error('[Mission Control] Agents fetch error:', error);
    
    // Even on error, return something
    return NextResponse.json({
      ok: false,
      error: 'Failed to fetch agents',
      agents: [],
      count: 0,
      source: 'error',
      timestamp: new Date().toISOString()
    });
  }
}

export async function OPTIONS() {
  return new NextResponse(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    },
  });
}