#!/usr/bin/env python3
"""
E-Voting System Management Script
Use this script to manage candidates, users, and database operations
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, User, Candidate, Vote
from werkzeug.security import generate_password_hash

def add_candidate():
    """Add a new candidate to the system"""
    print("\n=== Add New Candidate ===")
    name = input("Candidate Name: ").strip()
    if not name:
        print("Error: Name is required")
        return
    
    party = input("Party Name: ").strip()
    if not party:
        print("Error: Party name is required") 
        return
    
    description = input("Description (optional): ").strip()
    image_url = input("Image URL (optional, press Enter for default): ").strip()
    
    if not image_url:
        image_url = "https://via.placeholder.com/150"
    
    with app.app_context():
        candidate = Candidate(
            name=name,
            party=party,
            description=description,
            image_url=image_url
        )
        
        db.session.add(candidate)
        db.session.commit()
        
        print(f"✅ Successfully added candidate: {name} ({party})")

def list_candidates():
    """List all candidates"""
    print("\n=== Current Candidates ===")
    with app.app_context():
        candidates = Candidate.query.all()
        if not candidates:
            print("No candidates found")
            return
        
        print(f"{'ID':<3} {'Name':<20} {'Party':<20} {'Votes':<6}")
        print("-" * 50)
        for candidate in candidates:
            print(f"{candidate.id:<3} {candidate.name:<20} {candidate.party:<20} {candidate.vote_count:<6}")

def delete_candidate():
    """Delete a candidate"""
    list_candidates()
    print("\n=== Delete Candidate ===")
    try:
        candidate_id = int(input("Enter candidate ID to delete: "))
        with app.app_context():
            candidate = Candidate.query.get(candidate_id)
            if not candidate:
                print("Error: Candidate not found")
                return
            
            confirm = input(f"Are you sure you want to delete {candidate.name}? (yes/no): ")
            if confirm.lower() == 'yes':
                db.session.delete(candidate)
                db.session.commit()
                print(f"✅ Successfully deleted candidate: {candidate.name}")
            else:
                print("Cancelled")
    except ValueError:
        print("Error: Please enter a valid number")

def create_admin():
    """Create a new admin user"""
    print("\n=== Create Admin User ===")
    email = input("Admin Email: ").strip().lower()
    if not email:
        print("Error: Email is required")
        return
    
    password = input("Admin Password: ").strip()
    if not password:
        print("Error: Password is required")
        return
    
    with app.app_context():
        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            print("Error: User with this email already exists")
            return
        
        user = User(
            email=email,
            password_hash=generate_password_hash(password),
            is_verified=True,
            is_admin=True
        )
        
        db.session.add(user)
        db.session.commit()
        
        print(f"✅ Successfully created admin user: {email}")

def reset_votes():
    """Reset all votes (use with caution!)"""
    print("\n=== Reset All Votes ===")
    print("⚠️  WARNING: This will delete all votes and reset vote counts!")
    confirm = input("Are you sure? Type 'RESET' to confirm: ")
    
    if confirm == 'RESET':
        with app.app_context():
            # Delete all votes
            Vote.query.delete()
            
            # Reset vote counts
            candidates = Candidate.query.all()
            for candidate in candidates:
                candidate.vote_count = 0
            
            # Reset user vote status
            users = User.query.all()
            for user in users:
                user.has_voted = False
            
            db.session.commit()
            print("✅ All votes have been reset")
    else:
        print("Cancelled")

def show_stats():
    """Show system statistics"""
    print("\n=== System Statistics ===")
    with app.app_context():
        total_users = User.query.count()
        verified_users = User.query.filter_by(is_verified=True).count()
        admin_users = User.query.filter_by(is_admin=True).count()
        total_votes = Vote.query.count()
        total_candidates = Candidate.query.count()
        
        print(f"Total Users: {total_users}")
        print(f"Verified Users: {verified_users}")
        print(f"Admin Users: {admin_users}")
        print(f"Total Votes Cast: {total_votes}")
        print(f"Total Candidates: {total_candidates}")
        
        if total_votes > 0:
            print(f"Voter Turnout: {(total_votes/verified_users*100):.1f}%" if verified_users > 0 else "N/A")

def main():
    """Main menu"""
    while True:
        print("\n" + "="*50)
        print("E-VOTING SYSTEM MANAGEMENT")
        print("="*50)
        print("1. Add Candidate")
        print("2. List Candidates")
        print("3. Delete Candidate")
        print("4. Create Admin User")
        print("5. Show Statistics")
        print("6. Reset All Votes")
        print("0. Exit")
        print("-"*50)
        
        choice = input("Enter your choice (0-6): ").strip()
        
        try:
            if choice == '1':
                add_candidate()
            elif choice == '2':
                list_candidates()
            elif choice == '3':
                delete_candidate()
            elif choice == '4':
                create_admin()
            elif choice == '5':
                show_stats()
            elif choice == '6':
                reset_votes()
            elif choice == '0':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()