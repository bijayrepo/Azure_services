"""
Unit tests for User API functions
Run: pytest test_functions.py -v
"""

import pytest
import json
from models import User
from validators import UserValidator
from repositories import InMemoryUserRepository
from services import UserService
from sample_data import SAMPLE_USERS, TEST_CASES

# Test Fixtures
@pytest.fixture
def repository():
    """Create a fresh repository for each test"""
    return InMemoryUserRepository()

@pytest.fixture
def service(repository):
    """Create a service with fresh repository"""
    return UserService(repository)

@pytest.fixture
def validator():
    """Create a validator instance"""
    return UserValidator()


# Tests for UserValidator
class TestUserValidator:
    """Test validation logic"""
    
    def test_validate_valid_email(self, validator):
        """Test valid email validation"""
        is_valid, msg = validator.validate_email("john@example.com")
        assert is_valid is True
        assert msg == ""
    
    def test_validate_invalid_email(self, validator):
        """Test invalid email validation"""
        is_valid, msg = validator.validate_email("invalid-email")
        assert is_valid is False
        assert len(msg) > 0
    
    def test_validate_valid_name(self, validator):
        """Test valid name validation"""
        is_valid, msg = validator.validate_name("John Doe")
        assert is_valid is True
        assert msg == ""
    
    def test_validate_short_name(self, validator):
        """Test name too short"""
        is_valid, msg = validator.validate_name("A")
        assert is_valid is False
        assert "at least 2 characters" in msg
    
    def test_validate_long_name(self, validator):
        """Test name too long"""
        is_valid, msg = validator.validate_name("A" * 101)
        assert is_valid is False
        assert "not exceed 100 characters" in msg
    
    def test_validate_valid_phone(self, validator):
        """Test valid phone validation"""
        is_valid, msg = validator.validate_phone("+1-555-0101")
        assert is_valid is True
        assert msg == ""
    
    def test_validate_invalid_phone(self, validator):
        """Test invalid phone validation"""
        is_valid, msg = validator.validate_phone("123")
        assert is_valid is False
        assert len(msg) > 0


# Tests for UserService
class TestUserService:
    """Test business logic"""
    
    def test_create_user_success(self, service):
        """Test successful user creation"""
        user = service.create_user("John Doe", "john@example.com", "+1234567890")
        assert user.name == "John Doe"
        assert user.email == "john@example.com"
        assert user.id is not None
        assert user.created_at is not None
    
    def test_create_user_duplicate_email(self, service):
        """Test duplicate email rejection"""
        service.create_user("John Doe", "john@example.com", "+1234567890")
        
        with pytest.raises(ValueError, match="already exists"):
            service.create_user("Jane Doe", "john@example.com", "+1234567891")
    
    def test_create_user_invalid_email(self, service):
        """Test invalid email rejection"""
        with pytest.raises(ValueError, match="Invalid email"):
            service.create_user("John Doe", "invalid-email", "+1234567890")
    
    def test_create_user_invalid_name(self, service):
        """Test invalid name rejection"""
        with pytest.raises(ValueError, match="Name"):
            service.create_user("", "john@example.com", "+1234567890")
    
    def test_create_user_invalid_phone(self, service):
        """Test invalid phone rejection"""
        with pytest.raises(ValueError, match="Invalid phone"):
            service.create_user("John Doe", "john@example.com", "123")
    
    def test_get_user_success(self, service):
        """Test retrieving existing user"""
        created_user = service.create_user("John Doe", "john@example.com", "+1234567890")
        retrieved_user = service.get_user(created_user.id)
        
        assert retrieved_user is not None
        assert retrieved_user.id == created_user.id
        assert retrieved_user.name == "John Doe"
    
    def test_get_user_not_found(self, service):
        """Test retrieving non-existent user"""
        user = service.get_user("non-existent-id")
        assert user is None
    
    def test_get_user_by_email_success(self, service):
        """Test retrieving user by email"""
        created_user = service.create_user("John Doe", "john@example.com", "+1234567890")
        retrieved_user = service.get_user_by_email("john@example.com")
        
        assert retrieved_user is not None
        assert retrieved_user.id == created_user.id
    
    def test_delete_user_success(self, service):
        """Test successful user deletion"""
        created_user = service.create_user("John Doe", "john@example.com", "+1234567890")
        deleted = service.delete_user(created_user.id)
        
        assert deleted is True
        assert service.get_user(created_user.id) is None
    
    def test_delete_user_not_found(self, service):
        """Test deleting non-existent user"""
        deleted = service.delete_user("non-existent-id")
        assert deleted is False


# Tests for InMemoryUserRepository
class TestInMemoryUserRepository:
    """Test repository operations"""
    
    def test_add_user_success(self, repository):
        """Test adding user to repository"""
        user = User(name="John Doe", email="john@example.com", phone="+1234567890")
        result = repository.add(user)
        
        assert result.id is not None
        assert result.created_at is not None
    
    def test_add_user_duplicate_email(self, repository):
        """Test duplicate email rejection in repository"""
        user1 = User(name="John Doe", email="john@example.com")
        user2 = User(name="Jane Doe", email="john@example.com")
        
        repository.add(user1)
        with pytest.raises(ValueError, match="already exists"):
            repository.add(user2)
    
    def test_get_by_id(self, repository):
        """Test retrieving user by ID"""
        user = User(name="John Doe", email="john@example.com")
        added_user = repository.add(user)
        
        retrieved = repository.get_by_id(added_user.id)
        assert retrieved is not None
        assert retrieved.id == added_user.id
    
    def test_get_by_email(self, repository):
        """Test retrieving user by email"""
        user = User(name="John Doe", email="john@example.com")
        repository.add(user)
        
        retrieved = repository.get_by_email("john@example.com")
        assert retrieved is not None
        assert retrieved.email == "john@example.com"


# Integration Tests
class TestIntegration:
    """Test end-to-end workflows"""
    
    def test_create_multiple_users_from_sample_data(self, service):
        """Test creating multiple users from sample data"""
        created_users = []
        
        for user_data in SAMPLE_USERS[:3]:  # Test first 3 users
            user = service.create_user(
                user_data['name'],
                user_data['email'],
                user_data['phone']
            )
            created_users.append(user)
        
        assert len(created_users) == 3
        for i, user in enumerate(created_users):
            assert user.id is not None
            assert user.name == SAMPLE_USERS[i]['name']
            assert user.email == SAMPLE_USERS[i]['email']
    
    def test_user_to_dict_serialization(self, service):
        """Test user serialization to dict for JSON response"""
        user = service.create_user("John Doe", "john@example.com", "+1234567890")
        user_dict = user.to_dict()
        
        assert user_dict['name'] == "John Doe"
        assert user_dict['email'] == "john@example.com"
        assert user_dict['id'] is not None
        assert user_dict['created_at'] is not None
        # Ensure it can be serialized to JSON
        json_str = json.dumps(user_dict)
        assert len(json_str) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
