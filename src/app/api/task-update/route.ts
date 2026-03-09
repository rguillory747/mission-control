import { NextRequest, NextResponse } from 'next/server';
import { withCors, corsOptionsResponse, corsJsonResponse, corsErrorResponse } from '@/lib/cors';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { title, status, assignee } = body;

    if (!title || !status) {
      return corsErrorResponse('title and status are required', 400);
    }

    // For now, log the task update
    console.log(`[Mission Control] Task update: "${title}" -> ${status}${assignee ? ` (Assignee: ${assignee})` : ''}`);

    // TODO: Integrate with Convex backend
    // This should call Convex mutation to update task status
    
    return corsJsonResponse({
      ok: true,
      message: `Task "${title}" updated to ${status}`,
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    console.error('[Mission Control] Task update error:', error);
    return corsErrorResponse('Invalid request body', 400);
  }
}

export async function OPTIONS() {
  return corsOptionsResponse();
}