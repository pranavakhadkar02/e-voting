#!/bin/bash
# Render Deployment Diagnostic Script
# Run this to diagnose your Render deployment issues

echo "🔍 E-Voting System - Render Deployment Diagnostics"
echo "=================================================="

# Get service URL from user
read -p "Enter your Render service URL (e.g., https://your-service.onrender.com): " SERVICE_URL

if [[ -z "$SERVICE_URL" ]]; then
    echo "❌ Service URL is required"
    exit 1
fi

echo ""
echo "🏥 Testing Service Health..."
echo "GET $SERVICE_URL/api/health"
echo ""

# Test health endpoint
HEALTH_RESPONSE=$(curl -s -w "HTTP_STATUS:%{http_code}" "$SERVICE_URL/api/health")
HTTP_STATUS=$(echo "$HEALTH_RESPONSE" | grep -o "HTTP_STATUS:[0-9]*" | cut -d: -f2)
RESPONSE_BODY=$(echo "$HEALTH_RESPONSE" | sed 's/HTTP_STATUS:[0-9]*$//')

if [[ "$HTTP_STATUS" == "200" ]]; then
    echo "✅ Service is healthy!"
    echo "Response: $RESPONSE_BODY"
    
    # Check mail configuration in response
    if echo "$RESPONSE_BODY" | grep -q '"mail":"configured"'; then
        echo "✅ Mail is configured"
    elif echo "$RESPONSE_BODY" | grep -q '"mail":"not configured"'; then
        echo "❌ Mail is NOT configured"
        echo "   → Check MAIL_USERNAME, MAIL_PASSWORD, MAIL_DEFAULT_SENDER env vars"
    fi
else
    echo "❌ Service health check failed (HTTP $HTTP_STATUS)"
    echo "Response: $RESPONSE_BODY"
    
    if [[ "$HTTP_STATUS" == "502" ]]; then
        echo ""
        echo "🚨 502 Bad Gateway - Common causes:"
        echo "   → Missing environment variables"
        echo "   → SMTP timeout (mail server issues)"
        echo "   → Service startup failure"
        echo "   → Check Render logs for details"
    fi
fi

echo ""
echo "📧 Testing Mail Functionality..."
echo "POST $SERVICE_URL/api/register"

# Test registration (which sends email)
REG_RESPONSE=$(curl -s -w "HTTP_STATUS:%{http_code}" -X POST "$SERVICE_URL/api/register" \
    -H "Content-Type: application/json" \
    -d '{"email":"test2@example.com","password":"test123"}')

REG_HTTP_STATUS=$(echo "$REG_RESPONSE" | grep -o "HTTP_STATUS:[0-9]*" | cut -d: -f2)
REG_RESPONSE_BODY=$(echo "$REG_RESPONSE" | sed 's/HTTP_STATUS:[0-9]*$//')

echo "HTTP Status: $REG_HTTP_STATUS"
echo "Response: $REG_RESPONSE_BODY"

if [[ "$REG_HTTP_STATUS" == "201" ]]; then
    echo "✅ Registration successful - OTP email should be sent"
elif [[ "$REG_HTTP_STATUS" == "500" ]] && echo "$REG_RESPONSE_BODY" | grep -q "Failed to send OTP email"; then
    echo "❌ Registration failed - Email sending issue"
    echo "   → Check Gmail App Password"
    echo "   → Verify MAIL_DEFAULT_SENDER is set"
    echo "   → Check Render logs for SMTP errors"
elif [[ "$REG_HTTP_STATUS" == "400" ]] && echo "$REG_RESPONSE_BODY" | grep -q "Email already registered"; then
    echo "ℹ️  Email already registered (expected)"
    echo "✅ Service is working - try with different email"
fi

echo ""
echo "📋 Troubleshooting Checklist:"
echo "[ ] MAIL_USERNAME set in Render environment"
echo "[ ] MAIL_PASSWORD set (Gmail App Password, not regular password)"
echo "[ ] MAIL_DEFAULT_SENDER set in Render environment"
echo "[ ] MAIL_SERVER=smtp.gmail.com"
echo "[ ] MAIL_PORT=587"
echo "[ ] Gmail 2FA enabled and App Password generated"
echo "[ ] Check Render service logs for errors"
echo ""
echo "🔗 Useful Links:"
echo "   Render Dashboard: https://dashboard.render.com/"
echo "   Gmail App Passwords: https://myaccount.google.com/apppasswords"
echo "   Service Health: $SERVICE_URL/api/health"
echo ""
echo "📞 Need help? Check the MAIL_TROUBLESHOOTING.md file"