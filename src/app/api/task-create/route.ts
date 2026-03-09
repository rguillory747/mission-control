import { NextRequest, NextResponse } from 'next/server';
import { withCors, corsOptionsResponse, corsJsonResponse, corsErrorResponse } from '@/lib/cors';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { title, description, status, assignee, priority } = body;

    if (!title || !status || !assignee || !priority) {
      return corsErrorResponse('title, status, assignee, and priority are required', 400);
    }

    // For now, log the task creation
    console.log(`[Mission Control] Task created: "${title}" (${priority}) -> ${status} - Assignee: ${assignee}`);
    if (description) {
      console.log(`  Description: ${description}`);
    }

    // TODO: Integrate with Convex backend
    // This should call Convex mutation to create task
    
    return corsJsonResponse({
      ok: true,
      message: `Task "${title}" created`,
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    console.error('[Mission Control] Task create error:', error);
    return corsErrorResponse('Invalid request body', 400);
  }
}

export async function OPTIONS() {
  return corsOptionsResponse();
}