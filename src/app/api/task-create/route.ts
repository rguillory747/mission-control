import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { title, description, status, assignee, priority } = body;

    if (!title || !status || !assignee || !priority) {
      return NextResponse.json(
        { error: 'title, status, assignee, and priority are required' },
        { status: 400 }
      );
    }

    // For now, log the task creation
    console.log(`[Mission Control] Task created: "${title}" (${priority}) -> ${status} - Assignee: ${assignee}`);
    if (description) {
      console.log(`  Description: ${description}`);
    }

    // TODO: Integrate with Convex backend
    // This should call Convex mutation to create task
    
    return NextResponse.json({
      ok: true,
      message: `Task "${title}" created`,
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    console.error('[Mission Control] Task create error:', error);
    return NextResponse.json(
      { error: 'Invalid request body' },
      { status: 400 }
    );
  }
}

export async function OPTIONS() {
  return new NextResponse(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    },
  });
}