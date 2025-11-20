#!/bin/bash

# E-Voting Deployment Helper Script

echo "🚀 E-Voting System Deployment Helper"
echo "====================================="

# Check if we're in the right directory
if [ ! -f "DEPLOYMENT.md" ]; then
    echo "❌ Please run this script from the project root directory"
    exit 1
fi

echo "📋 Pre-deployment Checklist:"
echo ""

# Check if git repo is clean
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  You have uncommitted changes. Consider committing them first."
    git status --short
    echo ""
fi

# Generate secure keys
echo "🔐 Generating secure keys for deployment:"
echo ""

SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_urlsafe(32))")
JWT_SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_urlsafe(32))")

echo "SECRET_KEY=$SECRET_KEY"
echo "JWT_SECRET_KEY=$JWT_SECRET_KEY"
echo ""
echo "⚠️  IMPORTANT: Save these keys securely and use them in your deployment platform!"
echo ""

# Check backend dependencies
echo "📦 Checking backend dependencies..."
cd backend
if python3 -c "import flask, flask_sqlalchemy, flask_jwt_extended, flask_mail, flask_cors, gunicorn, psycopg2" 2>/dev/null; then
    echo "✅ All backend dependencies are available"
else
    echo "❌ Some backend dependencies are missing. Run: pip install -r requirements.txt"
fi
cd ..

# Check frontend dependencies
echo "📦 Checking frontend dependencies..."
cd frontend
if [ -d "node_modules" ]; then
    echo "✅ Frontend dependencies installed"
else
    echo "⚠️  Frontend dependencies not installed. Run: npm install"
fi
cd ..

echo ""
echo "🌐 Deployment Options:"
echo "1. Render (Full Stack) - Currently Deployed"
echo ""
echo "📖 For detailed instructions, see DEPLOYMENT.md"
echo ""

# Check for .env files
if [ -f "backend/.env" ]; then
    echo "⚠️  Found backend/.env file - make sure not to commit it!"
fi

if [ -f "frontend/.env" ]; then
    echo "⚠️  Found frontend/.env file - make sure not to commit it!"
fi

echo ""
echo "🎯 Next Steps:"
echo "1. Copy the generated keys above"
echo "2. Choose a deployment platform (Render recommended)"
echo "3. Follow the detailed guide in DEPLOYMENT.md"
echo "4. Set up environment variables on your chosen platform"
echo "5. Configure Gmail app password for email functionality"
echo ""
echo "🎓 Perfect for college demo projects! Good luck with your deployment!"