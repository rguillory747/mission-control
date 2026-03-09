import { NextRequest, NextResponse } from 'next/server';

export async function GET(request: NextRequest) {
  const url = new URL(request.url);
  const limit = parseInt(url.searchParams.get('limit') || '50');

  const tasks = [
    {
      id: 'demo-1',
      title: 'Demo task',
      status: 'in_progress',
      owner: 'orchestrator',
      createdAt: new Date().toISOString(),
    },
  ].slice(0, limit);

  return NextResponse.json({
    ok: true,
    tasks,
    count: tasks.length,
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

