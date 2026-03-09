import { NextRequest, NextResponse } from 'next/server';
import { corsOptionsResponse, corsJsonResponse, corsErrorResponse } from '@/lib/cors';

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
