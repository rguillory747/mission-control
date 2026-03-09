import { NextRequest, NextResponse } from 'next/server';
import { withCors, corsOptionsResponse, corsJsonResponse, corsErrorResponse } from '@/lib/cors';

const CONVEX_SITE_URL = process.env.CONVEX_SITE_URL || 'https://good-corgi-153.convex.site';

export async function GET(request: NextRequest) {
  try {
    // Try to fetch from Convex HTTP actions
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 5000);
    
    const response = await fetch(`${CONVEX_SITE_URL}/api/tasks`, {
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
    
    console.log(`[Mission Control] Fetched ${data.tasks?.length || 0} tasks from Convex`);

    return corsJsonResponse({
      ok: true,
      tasks: data.tasks || [],
      count: data.tasks?.length || 0,
      source: 'convex',
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    console.error('[Mission Control] Tasks fetch error:', error);
    
    // Fallback to mock data if Convex is unavailable
    const mockTasks = [
      {
        _id: "mock-1",
        title: "Test Mission Control Integration",
        description: "Verify that Jarvis can send heartbeats and log activities",
        status: "done",
        assignee: "Jarvis",
        priority: "P0",
        createdAt: Date.now() - 86400000, // 1 day ago
        updatedAt: Date.now() - 43200000 // 12 hours ago
      },
      {
        _id: "mock-2",
        title: "Build pricing page",
        description: "Create pricing page based on Scout's research",
        status: "in_progress",
        assignee: "Forge",
        priority: "P1",
        createdAt: Date.now() - 43200000, // 12 hours ago
        updatedAt: Date.now() - 21600000 // 6 hours ago
      },
      {
        _id: "mock-3",
        title: "Research competitor pricing",
        description: "Analyze 3 main competitors' pricing models",
        status: "inbox",
        assignee: "Scout",
        priority: "P2",
        createdAt: Date.now() - 21600000, // 6 hours ago
        updatedAt: Date.now() - 10800000 // 3 hours ago
      }
    ];

    return corsJsonResponse({
      ok: true,
      tasks: mockTasks,
      count: mockTasks.length,
      source: 'mock-fallback',
      error: error instanceof Error ? error.message : 'Unknown error',
      timestamp: new Date().toISOString()
    });
  }
}

export async function OPTIONS() {
  return corsOptionsResponse();
}