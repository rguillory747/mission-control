import { NextResponse } from 'next/server';

/**
 * CORS helper utility for Mission Control API routes
 * Apply CORS headers to all API responses
 */
export function withCors(response: NextResponse): NextResponse {
  // Apply CORS headers
  response.headers.set('Access-Control-Allow-Origin', '*');
  response.headers.set('Access-Control-Allow-Methods', 'GET, POST, PUT, PATCH, DELETE, OPTIONS');
  response.headers.set('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  response.headers.set('Access-Control-Max-Age', '86400'); // 24 hours
  
  return response;
}

/**
 * Create a CORS-enabled OPTIONS response
 */
export function corsOptionsResponse(): NextResponse {
  return withCors(
    new NextResponse(null, { status: 204 })
  );
}

/**
 * Create a CORS-enabled JSON response
 */
export function corsJsonResponse(data: any, status: number = 200): NextResponse {
  const response = NextResponse.json(data, { status });
  return withCors(response);
}

/**
 * Create a CORS-enabled error response
 */
export function corsErrorResponse(message: string, status: number = 500): NextResponse {
  const response = NextResponse.json({ error: message }, { status });
  return withCors(response);
}