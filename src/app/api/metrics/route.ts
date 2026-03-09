// src/app/api/metrics/route.ts
import { corsOptionsResponse, corsJsonResponse } from '@/lib/cors';

export async function GET() {
  const mockMetrics = [
    { id: 'apiAvailability', value: 40 },
    { id: 'taskAccuracy', value: 33 },
    { id: 'agentCoordination', value: 0 },
    { id: 'modelAccess', value: 100 },
    { id: 'overallHealth', value: 43 },
  ];

  return corsJsonResponse({
    ok: true,
    metrics: mockMetrics,
    count: mockMetrics.length,
    source: 'mock',
    timestamp: new Date().toISOString(),
  });
}

export async function OPTIONS() {
  return corsOptionsResponse();
}
