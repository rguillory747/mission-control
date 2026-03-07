# Mission Control Deployment Quick Reference
# Generated: 2026-03-07T06:45:43.135947

## Current Status: has_api_key_need_deploy_key

## Deployment Commands:

1. **Set environment variables:**
   export CONVEX_DEPLOY_KEY="your-key"
   export CONVEX_DEPLOYMENT="prod:deployment-id"
   export NEXT_PUBLIC_CONVEX_URL="https://instance.convex.cloud"

2. **Deploy Convex:**
   npx convex deploy --yes

3. **Seed data:**
   npx convex run seed:seed --prod

4. **Deploy to Vercel:**
   npx vercel --prod

5. **Add custom domain:**
   npx vercel domains add mission-control.aiorg.app

## Required Credentials:

1. **Convex Deploy Key:**
   - Format: instance-name|key
   - Source: Convex dashboard → Settings → Deploy key
   - Purpose: Non-interactive deployment authentication

2. **Convex Deployment ID:**
   - Format: prod:deployment-id or dev:deployment-id
   - Source: Convex dashboard after deployment
   - Purpose: Tells CLI which deployment to use

3. **Convex Client URL:**
   - Format: https://instance.convex.cloud
   - Source: Convex dashboard Settings
   - Purpose: Next.js client connection

## Troubleshooting:

- **"MissingAccessToken":** CONVEX_DEPLOY_KEY not set or invalid
- **"Deployment not found":** CONVEX_DEPLOYMENT value incorrect
- **"Connection failed":** NEXT_PUBLIC_CONVEX_URL incorrect or deployment not running
- **"Authentication required":** Need valid deploy key from dashboard

## Getting Help:
- Convex Docs: https://docs.convex.dev
- Vercel Docs: https://vercel.com/docs
- Mission Control Docs: ./docs/
