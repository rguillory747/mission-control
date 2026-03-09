import { NextResponse } from 'next/server';

export async function GET() {
  const res = NextResponse.json({
    ok: true,
    metrics: {
      apiAvailability: 40,
      taskAccuracy: 33,
      agentCoordination: 0,
      modelAccess: 100,
      overallHealth: 43,
    },
    timestamp: new Date().toISOString(),
  });
  res.headers.set('Access-Control-Allow-Origin', '*');
  return res;
}

export async function OPTIONS() {
  return new NextResponse(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    },
  });
}
