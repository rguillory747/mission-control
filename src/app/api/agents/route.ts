import { NextRequest, NextResponse } from 'next/server';

export async function GET(request: NextRequest) {
  try {
    // Mock data for now
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

    const res = NextResponse.json({
      ok: true,
      agents: mockAgents,
      count: mockAgents.length,
      source: 'mock',
      timestamp: new Date().toISOString()
    });
    res.headers.set('Access-Control-Allow-Origin', '*');
    return res;
  } catch (error) {
    console.error('[Mission Control] Agents fetch error:', error);

    const res = NextResponse.json(
      {
        ok: false,
        error: 'Failed to fetch agents',
        agents: [],
        count: 0,
        source: 'error',
        timestamp: new Date().toISOString()
      },
      { status: 500 }
    );
    res.headers.set('Access-Control-Allow-Origin', '*');
    return res;
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
