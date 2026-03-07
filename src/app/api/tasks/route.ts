import { NextRequest, NextResponse } from 'next/server';
import { ConvexHttpClient } from 'convex/browser';
import { api } from '../../../convex/_generated/api';

export async function GET(request: NextRequest) {
  try {
    // Get Convex URL from environment
    const convexUrl = process.env.NEXT_PUBLIC_CONVEX_URL;
    if (!convexUrl) {
      console.error('[Mission Control] NEXT_PUBLIC_CONVEX_URL not set');
      return NextResponse.json(
        { error: 'Server configuration error' },
        { status: 500 }
      );
    }

    // Create Convex HTTP client and query tasks
    const convex = new ConvexHttpClient(convexUrl);
    const tasks = await convex.query(api.tasks.list);

    console.log(`[Mission Control] Fetched ${tasks?.length || 0} tasks`);

    return NextResponse.json({
      ok: true,
      tasks: tasks || [],
      count: tasks?.length || 0,
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    console.error('[Mission Control] Tasks fetch error:', error);
    return NextResponse.json(
      { 
        ok: false, 
        error: 'Failed to fetch tasks',
        details: String(error),
        tasks: [] // Return empty array as fallback
      },
      { status: 500 }
    );
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