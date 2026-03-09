import { NextRequest, NextResponse } from 'next/server';
import { ConvexHttpClient } from 'convex/browser';
import { api } from '../../../../convex/_generated/api';
import { withCors, corsOptionsResponse, corsJsonResponse, corsErrorResponse } from '@/lib/cors';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { name, status, currentTask } = body;

    if (!name || !status) {
      return corsErrorResponse('name and status are required', 400);
    }

    // Get Convex URL from environment
    const convexUrl = process.env.NEXT_PUBLIC_CONVEX_URL;
    if (!convexUrl) {
      console.error('[Mission Control] NEXT_PUBLIC_CONVEX_URL not set');
      return corsErrorResponse('Server configuration error', 500);
    }

    // Create Convex HTTP client and call mutation
    const convex = new ConvexHttpClient(convexUrl);
    await convex.mutation(api.agents.heartbeat, { 
      name, 
      status, 
      currentTask: currentTask || '' 
    });

    console.log(`[Mission Control] Heartbeat from ${name}: ${status} - ${currentTask || 'No task'}`);
    console.log(`[Convex] Updated agent ${name} with status ${status}`);

    return corsJsonResponse({
      ok: true,
      message: `Heartbeat received from ${name}`,
      agent: name,
      status: status,
      currentTask: currentTask || '',
      timestamp: new Date().toISOString(),
      convexUpdated: true
    });
  } catch (error) {
    console.error('[Mission Control] Heartbeat error:', error);
    return corsErrorResponse(`Failed to process heartbeat: ${error}`, 500);
  }
}

export async function OPTIONS() {
  return corsOptionsResponse();
}