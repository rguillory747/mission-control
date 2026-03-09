import { NextResponse } from 'next/server';

export async function GET() {
  const tasks = [
    {
      id: 'task-1',
      title: 'Test Mission Control Integration',
      status: 'done',
    },
    {
      id: 'task-2',
      title: 'Build pricing page',
      status: 'inbox',
    },
    {
      id: 'task-3',
      title: 'Research competitor pricing',
      status: 'inbox',
    },
  ];

  const res = NextResponse.json({
    ok: true,
    tasks,
    count: tasks.length,
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
