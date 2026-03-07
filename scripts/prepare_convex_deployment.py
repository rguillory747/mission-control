#!/usr/bin/env python3
"""
Convex Deployment Preparation Script
Helps prepare for non-interactive Convex deployment
"""

import os
import sys
import json
from datetime import datetime

def check_current_environment():
    """Check current Convex environment configuration"""
    print("🔍 Checking current Convex environment...")
    
    env_file = ".env.local"
    config = {}
    
    if os.path.exists(env_file):
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    config[key] = value
    
    print(f"✅ Found {len(config)} environment variables in {env_file}")
    
    # Check for Convex-related variables
    convex_vars = {k: v for k, v in config.items() if "CONVEX" in k}
    
    if convex_vars:
        print("\n📋 Current Convex configuration:")
        for key, value in convex_vars.items():
            print(f"   {key}: {value[:50]}{'...' if len(value) > 50 else ''}")
    else:
        print("❌ No Convex environment variables found")
    
    return config

def analyze_key_type(key_value):
    """Analyze what type of Convex key we have"""
    print(f"\n🔑 Analyzing key type...")
    
    if not key_value:
        return "missing", "No key provided"
    
    # Check for JWT format (starts with eyJ)
    if key_value.startswith("eyJ"):
        return "jwt_api_key", "Looks like a JWT API key (starts with 'eyJ')"
    
    # Check for deploy key format (contains |)
    elif "|" in key_value:
        parts = key_value.split("|")
        if len(parts) == 2:
            return "deploy_key", f"Looks like a deploy key (instance: {parts[0]})"
        else:
            return "unknown_format", "Has '|' but not in expected deploy key format"
    
    # Check for hex/random string
    elif len(key_value) == 64 and all(c in "0123456789abcdefABCDEF" for c in key_value):
        return "hex_key", "Looks like a hex-encoded key (64 chars)"
    
    else:
        return "unknown", f"Unknown key format ({len(key_value)} chars)"

def generate_deployment_plan(config):
    """Generate a deployment plan based on current configuration"""
    print("\n📋 Generating deployment plan...")
    
    plan = {
        "timestamp": datetime.now().isoformat(),
        "current_status": "requires_deploy_key",
        "steps": [],
        "missing_items": [],
        "next_actions": []
    }
    
    # Check what we have
    has_convex_url = "NEXT_PUBLIC_CONVEX_URL" in config
    has_convex_deployment = "CONVEX_DEPLOYMENT" in config
    has_convex_api_key = "CONVEX_API_KEY" in config
    has_convex_deploy_key = "CONVEX_DEPLOY_KEY" in config
    
    # Analyze the key if we have one
    key_type = None
    if has_convex_api_key:
        key_type, key_desc = analyze_key_type(config.get("CONVEX_API_KEY"))
        print(f"   API Key: {key_desc}")
    
    if has_convex_deploy_key:
        key_type, key_desc = analyze_key_type(config.get("CONVEX_DEPLOY_KEY"))
        print(f"   Deploy Key: {key_desc}")
    
    # Determine current status
    if has_convex_deploy_key and key_type == "deploy_key":
        plan["current_status"] = "ready_for_deployment"
        plan["steps"].append("✅ Has valid deploy key")
    elif has_convex_api_key and key_type == "jwt_api_key":
        plan["current_status"] = "has_api_key_need_deploy_key"
        plan["steps"].append("⚠️  Has API key but needs deploy key for deployment")
    else:
        plan["current_status"] = "missing_credentials"
        plan["steps"].append("❌ Missing deploy key")
    
    # Check deployment URL
    if has_convex_url:
        url = config.get("NEXT_PUBLIC_CONVEX_URL", "")
        if url and "convex.cloud" in url:
            plan["steps"].append(f"✅ Has Convex URL: {url}")
        else:
            plan["steps"].append(f"⚠️  Convex URL may not be valid: {url}")
    else:
        plan["missing_items"].append("NEXT_PUBLIC_CONVEX_URL")
    
    # Check deployment environment
    if has_convex_deployment:
        deployment = config.get("CONVEX_DEPLOYMENT", "")
        if deployment.startswith("prod:") or deployment.startswith("dev:"):
            plan["steps"].append(f"✅ Has deployment target: {deployment}")
        else:
            plan["steps"].append(f"⚠️  Deployment target may need adjustment: {deployment}")
    else:
        plan["missing_items"].append("CONVEX_DEPLOYMENT")
    
    # Generate next actions based on status
    if plan["current_status"] == "ready_for_deployment":
        plan["next_actions"].append("Run: CONVEX_DEPLOY_KEY=your-key npx convex deploy")
        plan["next_actions"].append("Run: CONVEX_DEPLOY_KEY=your-key npx convex run seed:seed --prod")
        plan["next_actions"].append("Deploy frontend to Vercel: npx vercel --prod")
    
    elif plan["current_status"] == "has_api_key_need_deploy_key":
        plan["next_actions"].append("1. Get deploy key from Convex dashboard:")
        plan["next_actions"].append("   - Go to https://dashboard.convex.dev")
        plan["next_actions"].append("   - Navigate to your project")
        plan["next_actions"].append("   - Go to Settings → Deploy key")
        plan["next_actions"].append("   - Copy the deploy key (format: instance-name|key)")
        plan["next_actions"].append("2. Update .env.local with CONVEX_DEPLOY_KEY")
        plan["next_actions"].append("3. Run deployment commands")
    
    else:  # missing_credentials
        plan["next_actions"].append("1. Get Convex deploy key:")
        plan["next_actions"].append("   - Login to Convex dashboard")
        plan["next_actions"].append("   - Create or select your project")
        plan["next_actions"].append("   - Get deploy key from Settings")
        plan["next_actions"].append("2. Set up environment variables:")
        plan["next_actions"].append("   - CONVEX_DEPLOY_KEY")
        plan["next_actions"].append("   - CONVEX_DEPLOYMENT")
        plan["next_actions"].append("   - NEXT_PUBLIC_CONVEX_URL")
    
    return plan

def create_deployment_scripts(plan):
    """Create deployment scripts based on the plan"""
    print("\n📝 Creating deployment scripts...")
    
    scripts_dir = "deployment_scripts"
    os.makedirs(scripts_dir, exist_ok=True)
    
    # Create deployment script
    deploy_script = f"""#!/bin/bash
# Mission Control Deployment Script
# Generated: {datetime.now().isoformat()}
# Status: {plan['current_status']}

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
"""
    
    deploy_script_path = os.path.join(scripts_dir, "deploy_convex.sh")
    with open(deploy_script_path, "w") as f:
        f.write(deploy_script)
    
    os.chmod(deploy_script_path, 0o755)
    print(f"✅ Created: {deploy_script_path}")
    
    # Create environment template
    env_template = f"""# Mission Control Environment Variables
# Generated: {datetime.now().isoformat()}
# Copy to .env.local and fill in values

# Convex Deployment Configuration
# Get from: https://dashboard.convex.dev → Settings → Deploy key
CONVEX_DEPLOY_KEY=instance-name|your-deploy-key-here

# Deployment target (prod:deployment-id or dev:deployment-id)
CONVEX_DEPLOYMENT=prod:your-deployment-id

# Client URL (from Convex dashboard)
NEXT_PUBLIC_CONVEX_URL=https://your-instance.convex.cloud

# Team ID (optional)
CONVEX_TEAM_ID=your-team-id

# Optional: AI features
OPENAI_API_KEY=sk-proj-your-key-here

# Optional: Revenue tracking
STRIPE_SECRET_KEY=sk_live_your_key_here

# Optional: Database
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
"""
    
    env_template_path = os.path.join(scripts_dir, "env.template")
    with open(env_template_path, "w") as f:
        f.write(env_template)
    
    print(f"✅ Created: {env_template_path}")
    
    # Create quick reference
    quick_ref = f"""# Mission Control Deployment Quick Reference
# Generated: {datetime.now().isoformat()}

## Current Status: {plan['current_status']}

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
"""
    
    quick_ref_path = os.path.join(scripts_dir, "QUICK_REFERENCE.md")
    with open(quick_ref_path, "w") as f:
        f.write(quick_ref)
    
    print(f"✅ Created: {quick_ref_path}")
    
    return scripts_dir

def main():
    """Main function"""
    print("=" * 60)
    print("Mission Control - Convex Deployment Preparation")
    print("=" * 60)
    
    # Check current environment
    config = check_current_environment()
    
    # Generate deployment plan
    plan = generate_deployment_plan(config)
    
    # Create deployment scripts
    scripts_dir = create_deployment_scripts(plan)
    
    # Print summary
    print("\n" + "=" * 60)
    print("Deployment Preparation Complete!")
    print("=" * 60)
    
    print(f"\n📊 Status: {plan['current_status'].replace('_', ' ').title()}")
    
    print("\n📋 Steps identified:")
    for step in plan["steps"]:
        print(f"  {step}")
    
    if plan["missing_items"]:
        print(f"\n❌ Missing items: {', '.join(plan['missing_items'])}")
    
    print(f"\n📁 Scripts created in: {scripts_dir}/")
    print("   • deploy_convex.sh - Deployment automation script")
    print("   • env.template - Environment variable template")
    print("   • QUICK_REFERENCE.md - Deployment guide")
    
    print("\n🎯 Next Actions:")
    for i, action in enumerate(plan["next_actions"], 1):
        print(f"  {i}. {action}")
    
    print("\n" + "=" * 60)
    
    # Save plan to file
    plan_file = "deployment_plan.json"
    with open(plan_file, "w") as f:
        json.dump(plan, f, indent=2)
    
    print(f"✅ Deployment plan saved to: {plan_file}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())