#!/bin/bash
# Mission Control Deployment Script
# Generated: 2026-03-07T06:45:43.135810
# Status: has_api_key_need_deploy_key

set -e  # Exit on error

echo "🚀 Mission Control Deployment"
echo "=============================="

# Check environment variables
echo "🔍 Checking environment..."
if [ -z "$CONVEX_DEPLOY_KEY" ]; then
    echo "❌ CONVEX_DEPLOY_KEY is not set"
    echo "   Get it from: https://dashboard.convex.dev → Settings → Deploy key"
    exit 1
fi

if [ -z "$CONVEX_DEPLOYMENT" ]; then
    echo "❌ CONVEX_DEPLOYMENT is not set"
    echo "   Format: prod:deployment-id or dev:deployment-id"
    exit 1
fi

if [ -z "$NEXT_PUBLIC_CONVEX_URL" ]; then
    echo "❌ NEXT_PUBLIC_CONVEX_URL is not set"
    echo "   Format: https://your-instance.convex.cloud"
    exit 1
fi

echo "✅ Environment variables check passed"

# Deploy Convex backend
echo "🚀 Deploying Convex backend..."
npx convex deploy --yes

if [ $? -eq 0 ]; then
    echo "✅ Convex backend deployed successfully"
else
    echo "❌ Convex deployment failed"
    exit 1
fi

# Seed data
echo "🌱 Seeding production data..."
npx convex run seed:seed --prod

if [ $? -eq 0 ]; then
    echo "✅ Data seeded successfully"
else
    echo "⚠️  Data seeding may have issues (check logs)"
fi

echo ""
echo "🎉 Convex deployment complete!"
echo "Next steps:"
echo "1. Deploy frontend to Vercel: npx vercel --prod"
echo "2. Configure custom domain: mission-control.aiorg.app"
echo "3. Test integration with OpenClaw agents"
