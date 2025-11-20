#!/usr/bin/env python3
"""
Database initialization script for production deployment
Run this script to create tables and initialize the database
"""

import os
import sys
from app import app, db, User
from werkzeug.security import generate_password_hash

def init_database():
    """Initialize database tables and create default admin user"""
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        
        # Create default admin user if none exists
        admin_email = os.getenv('ADMIN_EMAIL', 'admin@evoting.com')
        admin_password = os.getenv('ADMIN_PASSWORD', 'admin123')
        
        if not User.query.filter_by(is_admin=True).first():
            admin_user = User(
                email=admin_email,
                password_hash=generate_password_hash(admin_password),
                is_verified=True,
                is_admin=True
            )
            db.session.add(admin_user)
            db.session.commit()
            print(f"✅ Database initialized with default admin user: {admin_email}")
            print("⚠️  Please change the admin password after first login!")
        else:
            print("✅ Database tables created/verified")
            print("ℹ️  Admin user already exists")

if __name__ == '__main__':
    init_database()