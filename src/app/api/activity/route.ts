import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { agent, action, detail } = body;

    if (!agent || !action) {
      return NextResponse.json(
        { error: 'agent and action are required' },
        { status: 400 }
      );
    }

    // For now, log the activity
    console.log(`[Mission Control] Activity from ${agent}: ${action} - ${detail || 'No details'}`);

    // TODO: Integrate with Convex backend
    // This should call Convex mutation to log activity
    
    return NextResponse.json({
      ok: true,
      message: `Activity logged from ${agent}`,
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    console.error('[Mission Control] Activity error:', error);
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