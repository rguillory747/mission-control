import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { title, status, assignee } = body;

    if (!title || !status) {
      return NextResponse.json(
        { error: 'title and status are required' },
        { status: 400 }
      );
    }

    // For now, log the task update
    console.log(`[Mission Control] Task update: "${title}" -> ${status}${assignee ? ` (Assignee: ${assignee})` : ''}`);

    // TODO: Integrate with Convex backend
    // This should call Convex mutation to update task status
    
    return NextResponse.json({
      ok: true,
      message: `Task "${title}" updated to ${status}`,
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    console.error('[Mission Control] Task update error:', error);
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