import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { key, value, increment } = body;

    if (!key) {
      return NextResponse.json(
        { error: 'key is required' },
        { status: 400 }
      );
    }

    // For now, log the metric
    if (value !== undefined) {
      console.log(`[Mission Control] Metric set: ${key} = ${value}`);
    } else if (increment !== undefined) {
      console.log(`[Mission Control] Metric increment: ${key} += ${increment}`);
    } else {
      return NextResponse.json(
        { error: 'value or increment is required' },
        { status: 400 }
      );
    }

    // TODO: Integrate with Convex backend
    // This should call Convex mutation to update metrics
    
    return NextResponse.json({
      ok: true,
      message: `Metric ${key} updated`,
      timestamp: new Date().toISOString()
    });
  } catch (error) {
    console.error('[Mission Control] Metric error:', error);
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