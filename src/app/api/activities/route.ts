import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { agent, action, detail } = body;

    if (!agent || !action) {
      const res = NextResponse.json(
        { error: 'agent and action are required' },
        { status: 400 }
      );
      res.headers.set('Access-Control-Allow-Origin', '*');
      return res;
    }

    console.log(
      `[Mission Control] Activity from ${agent}: ${action} - ${detail || 'No details'}`
    );

    const res = NextResponse.json({
      ok: true,
      message: `Activity logged from ${agent}`,
      timestamp: new Date().toISOString(),
    });
    res.headers.set('Access-Control-Allow-Origin', '*');
    return res;
  } catch (error) {
    console.error('[Mission Control] Activity error:', error);
    const res = NextResponse.json(
      { error: 'Invalid request body' },
      { status: 400 }
    );
    res.headers.set('Access-Control-Allow-Origin', '*');
    return res;
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
