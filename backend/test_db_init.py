#!/usr/bin/env python3
"""
Test script to verify database initialization works correctly
"""

import os
import sys
import tempfile
from app import app, db, User, Candidate, Vote

def test_database_initialization():
    """Test that database tables can be created and admin user is set up"""
    
    # Use a temporary database for testing
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
        test_db_path = tmp.name
    
    # Configure app for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{test_db_path}'
    app.config['TESTING'] = True
    
    try:
        with app.app_context():
            # Drop all tables first (clean slate)
            db.drop_all()
            
            # Create all tables
            db.create_all()
            
            # Verify tables exist by trying to query them
            user_count = User.query.count()
            candidate_count = Candidate.query.count()
            vote_count = Vote.query.count()
            
            print(f"✅ Tables created successfully")
            print(f"   Users: {user_count}")
            print(f"   Candidates: {candidate_count}")
            print(f"   Votes: {vote_count}")
            
            # Test creating an admin user
            from werkzeug.security import generate_password_hash
            
            admin_user = User(
                email='test-admin@evoting.com',
                password_hash=generate_password_hash('testpass123'),
                is_verified=True,
                is_admin=True
            )
            db.session.add(admin_user)
            db.session.commit()
            
            # Verify admin user was created
            admin = User.query.filter_by(is_admin=True).first()
            if admin and admin.email == 'test-admin@evoting.com':
                print(f"✅ Admin user created successfully: {admin.email}")
            else:
                print("❌ Failed to create admin user")
                return False
            
            print("✅ Database initialization test passed!")
            return True
            
    except Exception as e:
        print(f"❌ Database initialization test failed: {e}")
        return False
    
    finally:
        # Clean up test database
        try:
            os.unlink(test_db_path)
        except:
            pass

if __name__ == '__main__':
    success = test_database_initialization()
    sys.exit(0 if success else 1)