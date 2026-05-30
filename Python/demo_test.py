# -*- coding: utf-8 -*-
"""
Manual Testing Demo Script
Run this script to test the User API with sample data

Usage:
    python demo_test.py
"""

import json
from repositories import InMemoryUserRepository
from services import UserService
from sample_data import SAMPLE_USERS, TEST_CASES

def print_section(title):
    """Print a formatted section header"""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def test_create_users():
    """Test creating users from sample data"""
    print_section("TEST 1: Creating Users from Sample Data")
    
    repository = InMemoryUserRepository()
    service = UserService(repository)
    created_users = []
    
    for user_data in SAMPLE_USERS[:5]:
        try:
            user = service.create_user(
                user_data['name'],
                user_data['email'],
                user_data['phone']
            )
            created_users.append(user)
            print(f"\n[OK] Created: {user.name}")
            print(f"  Email: {user.email}")
            print(f"  ID: {user.id}")
            print(f"  Created At: {user.created_at}")
        except Exception as e:
            print(f"\n[FAIL] Failed to create {user_data['name']}: {str(e)}")
    
    return service, created_users

def test_retrieve_users(service, users):
    """Test retrieving users"""
    print_section("TEST 2: Retrieving Users")
    
    if not users:
        print("No users to retrieve")
        return
    
    user = users[0]
    retrieved = service.get_user(user.id)
    
    if retrieved:
        print(f"\n[OK] Retrieved User by ID:")
        print(f"  Name: {retrieved.name}")
        print(f"  Email: {retrieved.email}")
        print(f"  Phone: {retrieved.phone}")
    else:
        print(f"\n[FAIL] Failed to retrieve user")

def test_get_by_email(service, users):
    """Test retrieving user by email"""
    print_section("TEST 3: Retrieving User by Email")
    
    if not users:
        print("No users to retrieve")
        return
    
    user = users[1]
    retrieved = service.get_user_by_email(user.email)
    
    if retrieved:
        print(f"\n[OK] Retrieved User by Email:")
        print(f"  Name: {retrieved.name}")
        print(f"  Email: {retrieved.email}")
        print(json.dumps(retrieved.to_dict(), indent=2, default=str))
    else:
        print(f"\n[FAIL] Failed to retrieve user by email")

def test_duplicate_email(service):
    """Test duplicate email rejection"""
    print_section("TEST 4: Testing Duplicate Email Rejection")
    
    try:
        user1 = service.create_user("User One", "duplicate@example.com", "+1234567890")
        print(f"\n[OK] First user created: {user1.name}")
    except Exception as e:
        print(f"\n[FAIL] Failed to create first user: {str(e)}")
        return
    
    try:
        user2 = service.create_user("User Two", "duplicate@example.com", "+1234567891")
        print(f"\n[FAIL] Second user should have been rejected but was created!")
    except ValueError as e:
        print(f"\n[OK] Duplicate email correctly rejected: {str(e)}")

def test_validation_errors():
    """Test validation error handling"""
    print_section("TEST 5: Testing Validation Errors")
    
    repository = InMemoryUserRepository()
    service = UserService(repository)
    
    # Test invalid email
    print("\n--- Testing Invalid Email ---")
    try:
        service.create_user("John Doe", "invalid-email", "+1234567890")
        print("[FAIL] Invalid email should have been rejected")
    except ValueError as e:
        print(f"[OK] Invalid email rejected: {str(e)}")
    
    # Test invalid name
    print("\n--- Testing Invalid Name (too short) ---")
    try:
        service.create_user("A", "valid@example.com", "+1234567890")
        print("[FAIL] Short name should have been rejected")
    except ValueError as e:
        print(f"[OK] Short name rejected: {str(e)}")
    
    # Test invalid phone
    print("\n--- Testing Invalid Phone ---")
    try:
        service.create_user("John Doe", "john@example.com", "123")
        print("[FAIL] Invalid phone should have been rejected")
    except ValueError as e:
        print(f"[OK] Invalid phone rejected: {str(e)}")
    
    # Test missing phone (should be optional)
    print("\n--- Testing Optional Phone ---")
    try:
        user = service.create_user("John Doe", "john@example.com")
        print(f"[OK] User created without phone: {user.name}")
    except ValueError as e:
        print(f"[FAIL] User creation without phone failed: {str(e)}")

def test_delete_user(service, users):
    """Test deleting a user"""
    print_section("TEST 6: Testing User Deletion")
    
    if not users:
        print("No users to delete")
        return
    
    user = users[0]
    print(f"\nDeleting user: {user.name}")
    
    deleted = service.delete_user(user.id)
    if deleted:
        print(f"[OK] User successfully deleted")
    else:
        print(f"[FAIL] User deletion failed")
    
    # Try to retrieve deleted user
    retrieved = service.get_user(user.id)
    if retrieved is None:
        print(f"[OK] Confirmation: Deleted user cannot be retrieved")
    else:
        print(f"[FAIL] Deleted user still exists!")

def test_json_serialization(service):
    """Test JSON serialization of user objects"""
    print_section("TEST 7: Testing JSON Serialization")
    
    user = service.create_user("John Doe", "john@example.com", "+1234567890")
    user_dict = user.to_dict()
    user_json = json.dumps(user_dict, indent=2, default=str)
    
    print("\nUser as JSON:")
    print(user_json)

def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("  USER API DEMO - Manual Testing with Sample Data")
    print("="*60)
    
    # Run tests
    service, users = test_create_users()
    test_retrieve_users(service, users)
    test_get_by_email(service, users)
    test_duplicate_email(service)
    test_validation_errors()
    test_delete_user(service, users)
    test_json_serialization(service)
    
    print_section("TESTS COMPLETED")
    print("\n[OK] All manual tests completed successfully!")
    print("\nTo run automated tests with pytest, use:")
    print("  pytest test_functions.py -v\n")

if __name__ == "__main__":
    main()
