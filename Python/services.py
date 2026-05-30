from typing import Optional
from models import User
from interfaces import IUserRepository, IUserService
from validators import UserValidator

class UserService(IUserService):
    """User Service for business logic - Single Responsibility: Business logic
    Dependency Inversion: Depends on IUserRepository interface"""
    
    def __init__(self, repository: IUserRepository):
        self._repository = repository
        self._validator = UserValidator()
    
    def create_user(self, name: str, email: str, phone: str = "") -> User:
        """Create a new user following SOLID principles"""
        # Validate input (SRP: Validation is delegated to UserValidator)
        is_valid, error_msg = self._validator.validate_user_data(name, email, phone)
        if not is_valid:
            raise ValueError(error_msg)
        
        # Check if user already exists
        existing_user = self._repository.get_by_email(email)
        if existing_user:
            raise ValueError(f"User with email {email} already exists")
        
        # Create new user
        user = User(name=name, email=email, phone=phone)
        
        # Save to repository (SRP: Data access is delegated to repository)
        return self._repository.add(user)
    
    def get_user(self, user_id: str) -> Optional[User]:
        """Retrieve a user by ID"""
        return self._repository.get_by_id(user_id)
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Retrieve a user by email"""
        return self._repository.get_by_email(email)
    
    def update_user(self, user_id: str, name: str = None, phone: str = None) -> User:
        """Update user information"""
        user = self._repository.get_by_id(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")
        
        if name:
            is_valid, error_msg = self._validator.validate_name(name)
            if not is_valid:
                raise ValueError(error_msg)
            user.name = name
        
        if phone:
            is_valid, error_msg = self._validator.validate_phone(phone)
            if not is_valid:
                raise ValueError(error_msg)
            user.phone = phone
        
        return self._repository.update(user)
    
    def delete_user(self, user_id: str) -> bool:
        """Delete a user"""
        return self._repository.delete(user_id)
