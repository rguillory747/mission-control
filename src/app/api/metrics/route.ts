import { NextRequest, NextResponse } from 'next/server';
import { ConvexHttpClient } from 'convex/browser';
import { api } from '@/convex/_generated/api';

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

    // Create Convex HTTP client and query metrics
    const convex = new ConvexHttpClient(convexUrl);
    const metrics = await convex.query(api.metrics.list);

    console.log(`[Mission Control] Fetched ${metrics?.length || 0} metrics`);

    return NextResponse.json({
      ok: true,
      metrics: metrics || [],
      count: metrics?.length || 0,
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    console.error('[Mission Control] Metrics fetch error:', error);
    return NextResponse.json(
      { 
        ok: false, 
        error: 'Failed to fetch metrics',
        details: String(error),
        metrics: [] // Return empty array as fallback
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