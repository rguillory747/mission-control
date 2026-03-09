import { NextResponse } from 'next/server';

export async function GET() {
  const mockMetrics = [
    { id: 'apiAvailability', value: 40 },
    { id: 'taskAccuracy', value: 33 },
    { id: 'agentCoordination', value: 0 },
    { id: 'modelAccess', value: 100 },
    { id: 'overallHealth', value: 43 },
  ];

  return NextResponse.json({
    ok: true,
    metrics: mockMetrics,
    count: mockMetrics.length,
    source: 'mock',
    timestamp: new Date().toISOString(),
  });
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

