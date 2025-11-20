#!/usr/bin/env python3
"""
Debug JWT token issue
"""
import sys
import os
sys.path.append('/Users/gauravsali/Gaurav/Work/My-Work/e-voting/backend')

from app import app, db, User
from flask_jwt_extended import create_access_token, decode_token
import jwt
import json

def debug_jwt_issue():
    with app.app_context():
        print("=== JWT Debug Information ===")
        
        # Get admin user
        admin = User.query.filter_by(email='admin@evoting.com').first()
        print(f"Admin ID: {admin.id}")
        
        # Create token
        token = create_access_token(identity=str(admin.id))
        print(f"Generated token: {token[:50]}...")
        
        # Try to decode the token
        try:
            decoded = decode_token(token)
            print(f"Token decoded successfully:")
            print(f"  Subject (user_id): {decoded['sub']}")
            print(f"  Type: {decoded['type']}")
            print(f"  Fresh: {decoded['fresh']}")
        except Exception as e:
            print(f"Failed to decode token: {e}")
        
        # Check JWT configuration
        print(f"\nJWT Configuration:")
        print(f"  SECRET_KEY: {app.config.get('SECRET_KEY')[:20]}...")
        print(f"  JWT_SECRET_KEY: {app.config.get('JWT_SECRET_KEY')[:20]}...")
        
        # Try manual decode
        try:
            manual_decode = jwt.decode(token, 
                                     app.config['JWT_SECRET_KEY'], 
                                     algorithms=['HS256'])
            print(f"Manual decode successful: {manual_decode}")
        except Exception as e:
            print(f"Manual decode failed: {e}")

if __name__ == "__main__":
    debug_jwt_issue()