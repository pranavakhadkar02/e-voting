#!/usr/bin/env python3
"""
Test script to validate admin user authentication and candidate management
"""
import sys
import os
sys.path.append('/Users/gauravsali/Gaurav/Work/My-Work/e-voting/backend')

from app import app, db, User, Candidate
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

def test_admin_functionality():
    with app.app_context():
        print("=== Admin User Test ===")
        
        # Test 1: Check if admin user exists
        admin = User.query.filter_by(email='admin@evoting.com').first()
        if not admin:
            print("❌ Admin user not found!")
            return False
        
        print(f"✅ Admin user found: {admin.email}")
        print(f"   - Is Admin: {admin.is_admin}")
        print(f"   - Is Verified: {admin.is_verified}")
        print(f"   - Has Voted: {admin.has_voted}")
        
        # Test 2: Check password
        password_valid = check_password_hash(admin.password_hash, 'admin123')
        print(f"   - Password Valid: {password_valid}")
        
        if not password_valid:
            print("❌ Admin password is incorrect!")
            return False
        
        # Test 3: Generate JWT token
        try:
            token = create_access_token(identity=admin.id)
            print(f"✅ JWT token generated successfully")
            print(f"   - Token (first 50 chars): {token[:50]}...")
        except Exception as e:
            print(f"❌ Failed to generate JWT token: {e}")
            return False
        
        # Test 4: Check candidates exist
        candidates = Candidate.query.all()
        print(f"✅ Found {len(candidates)} candidates in database:")
        for candidate in candidates:
            print(f"   - {candidate.name} ({candidate.party}) - Votes: {candidate.vote_count}")
        
        print("\n=== Admin Authentication Simulation ===")
        
        # Simulate login flow
        if admin and password_valid and admin.is_admin and admin.is_verified:
            print("✅ Admin login would succeed")
            print("✅ Admin would have access to candidate management")
            return True
        else:
            print("❌ Admin login would fail")
            return False

if __name__ == "__main__":
    success = test_admin_functionality()
    sys.exit(0 if success else 1)