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

    // Get limit from query params
    const url = new URL(request.url);
    const limit = parseInt(url.searchParams.get('limit') || '100');

    // Create Convex HTTP client and query activities
    const convex = new ConvexHttpClient(convexUrl);
    const activities = await convex.query(api.activities.list, { limit });

    console.log(`[Mission Control] Fetched ${activities?.length || 0} activities`);

    return NextResponse.json({
      ok: true,
      activities: activities || [],
      count: activities?.length || 0,
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    console.error('[Mission Control] Activities fetch error:', error);
    return NextResponse.json(
      { 
        ok: false, 
        error: 'Failed to fetch activities',
        details: String(error),
        activities: [] // Return empty array as fallback
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