import { NextResponse } from 'next/server';

export async function GET() {
  return NextResponse.json({
    ok: true,
    source: 'activities-test',
    timestamp: new Date().toISOString(),
  });
}
