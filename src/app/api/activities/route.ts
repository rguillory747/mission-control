// src/app/api/activities/route.ts
import { NextRequest } from 'next/server';
import { corsOptionsResponse, corsJsonResponse, corsErrorResponse } from '@/lib/cors';

export async function GET() {
  // Simple health / debug response so GET isn’t 404
  return corsJsonResponse({
    ok: true,
    message: 'Activities endpoint is live (use POST to log activities)',
    timestamp: new Date().toISOString(),
  });
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { agent, action, detail } = body;

    if (!agent || !action) {
      return corsErrorResponse('agent and action are required', 400);
    }

    console.log(
      `[Mission Control] Activity from ${agent}: ${action} - ${detail || 'No details'}`
    );

    return corsJsonResponse({
      ok: true,
      message: `Activity logged from ${agent}`,
      timestamp: new Date().toISOString(),
    });
  } catch (error) {
    console.error('[Mission Control] Activity error:', error);
    return corsErrorResponse('Invalid request body', 400);
  }
}

export async function OPTIONS() {
  return corsOptionsResponse();
}
