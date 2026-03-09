import { NextRequest, NextResponse } from 'next/server';
import { withCors, corsOptionsResponse, corsJsonResponse, corsErrorResponse } from '@/lib/cors';

const CONVEX_SITE_URL = process.env.CONVEX_SITE_URL || 'https://good-corgi-153.convex.site';

export async function GET(request: NextRequest) {
  try {
    // Try to fetch from Convex HTTP actions
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 5000);
    
    const response = await fetch(`${CONVEX_SITE_URL}/api/activities`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      signal: controller.signal,
    });
    
    clearTimeout(timeoutId);

    if (response.ok) {
      const data = await response.json();
      console.log(`[Mission Control] Fetched ${data.activities?.length || 0} activities from Convex`);
      
      return corsJsonResponse({
        ok: true,
        activities: data.activities || [],
        count: data.activities?.length || 0,
        source: 'convex',
        timestamp: new Date().toISOString()
      });
    } else {
      console.error(`[Mission Control] Convex API returned status ${response.status}`);
      return corsJsonResponse({
        ok: false,
        activities: [],
        count: 0,
        error: `Convex API returned status ${response.status}`,
        timestamp: new Date().toISOString()
      }, 200);
    }
    
  } catch (error) {
    console.error('[Mission Control] Error fetching activities:', error);
    
    // Fallback to empty array if Convex is unavailable
    return corsJsonResponse({
      ok: false,
      activities: [],
      count: 0,
      error: error instanceof Error ? error.message : 'Unknown error',
      timestamp: new Date().toISOString()
    }, 200);
  }
}

export async function OPTIONS() {
  return corsOptionsResponse();
}