#!/usr/bin/env python3
"""
Comprehensive test for admin candidate management functionality
"""
import sys
import requests
import json
import time
import subprocess
import os
from threading import Thread
import signal

# Configuration
BACKEND_DIR = '/Users/gauravsali/Gaurav/Work/My-Work/e-voting/backend'
API_BASE_URL = 'http://localhost:5000/api'

def start_backend():
    """Start the Flask backend server"""
    print("Starting backend server...")
    os.chdir(BACKEND_DIR)
    
    # Use the virtual environment python
    venv_python = './venv/bin/python'
    
    # Start the server
    process = subprocess.Popen([venv_python, 'app.py'], 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE)
    
    # Wait a moment for server to start
    time.sleep(3)
    
    return process

def test_admin_workflow():
    """Test the complete admin workflow"""
    print("\n=== Testing Admin E-Voting Workflow ===")
    
    # Test 1: Admin Login
    print("\n1. Testing Admin Login...")
    login_data = {
        "email": "admin@evoting.com",
        "password": "admin123"
    }
    
    try:
        response = requests.post(f"{API_BASE_URL}/login", 
                               json=login_data, 
                               headers={'Content-Type': 'application/json'},
                               timeout=10)
        
        if response.status_code == 200:
            login_result = response.json()
            token = login_result.get('access_token')
            user = login_result.get('user')
            
            print(f"✅ Admin login successful!")
            print(f"   - User: {user.get('email')}")
            print(f"   - Is Admin: {user.get('is_admin')}")
            print(f"   - Token: {token[:30]}...")
            
            if not user.get('is_admin'):
                print("❌ User is not marked as admin!")
                return False
                
        else:
            print(f"❌ Login failed: {response.status_code} - {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Login request failed: {e}")
        return False
    
    # Test 2: Get Admin Candidates
    print("\n2. Testing Admin Candidate Access...")
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    
    try:
        response = requests.get(f"{API_BASE_URL}/admin/candidates", 
                              headers=headers,
                              timeout=10)
        
        if response.status_code == 200:
            candidates_result = response.json()
            candidates = candidates_result.get('candidates', [])
            
            print(f"✅ Admin candidate access successful!")
            print(f"   - Found {len(candidates)} candidates:")
            for candidate in candidates:
                print(f"     • {candidate.get('name')} ({candidate.get('party')}) - Votes: {candidate.get('vote_count')}")
                
        else:
            print(f"❌ Candidate access failed: {response.status_code} - {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Candidate request failed: {e}")
        return False
    
    # Test 3: Add New Candidate
    print("\n3. Testing Add New Candidate...")
    new_candidate = {
        "name": "Test Candidate",
        "party": "Test Party",
        "description": "A test candidate for validation",
        "image_url": "https://via.placeholder.com/150"
    }
    
    try:
        response = requests.post(f"{API_BASE_URL}/admin/candidates",
                               json=new_candidate,
                               headers=headers,
                               timeout=10)
        
        if response.status_code == 201:
            print("✅ Successfully added new candidate!")
        else:
            print(f"❌ Failed to add candidate: {response.status_code} - {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Add candidate request failed: {e}")
        return False
    
    # Test 4: Verify candidate was added
    print("\n4. Verifying candidate was added...")
    try:
        response = requests.get(f"{API_BASE_URL}/admin/candidates", 
                              headers=headers,
                              timeout=10)
        
        if response.status_code == 200:
            candidates_result = response.json()
            candidates = candidates_result.get('candidates', [])
            
            test_candidate_found = any(c.get('name') == 'Test Candidate' for c in candidates)
            
            if test_candidate_found:
                print("✅ New candidate successfully verified in database!")
                print(f"   - Total candidates now: {len(candidates)}")
            else:
                print("❌ New candidate not found in database!")
                return False
                
        else:
            print(f"❌ Verification failed: {response.status_code} - {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Verification request failed: {e}")
        return False
    
    print("\n🎉 All admin functionality tests passed!")
    return True

def main():
    # Start backend server
    backend_process = None
    try:
        backend_process = start_backend()
        
        # Run tests
        success = test_admin_workflow()
        
        if success:
            print("\n✅ CONCLUSION: Admin candidate management is working correctly!")
            print("   - Admin user can login successfully")
            print("   - Admin can view all candidates") 
            print("   - Admin can add new candidates")
            print("   - Changes are persisted in database")
        else:
            print("\n❌ CONCLUSION: There are issues with admin candidate management")
            
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    except Exception as e:
        print(f"\nTest failed with error: {e}")
    finally:
        # Clean up backend process
        if backend_process:
            backend_process.terminate()
            backend_process.wait()
            print("\nBackend server stopped")

if __name__ == "__main__":
    main()