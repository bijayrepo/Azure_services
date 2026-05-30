from abc import ABC, abstractmethod
from typing import Optional
from models import User

class IUserRepository(ABC):
    """Interface for User Repository - Dependency Inversion Principle"""
    
    @abstractmethod
    def add(self, user: User) -> User:
        """Add a new user"""
        pass
    
    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[User]:
        """Get user by ID"""
        pass
    
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        pass
    
    @abstractmethod
    def update(self, user: User) -> User:
        """Update existing user"""
        pass
    
    @abstractmethod
    def delete(self, user_id: str) -> bool:
        """Delete user"""
        pass


class IUserService(ABC):
    """Interface for User Service - Dependency Inversion Principle"""
    
    @abstractmethod
    def create_user(self, name: str, email: str, phone: str) -> User:
        """Create a new user"""
        pass
    
    @abstractmethod
    def get_user(self, user_id: str) -> Optional[User]:
        """Get user by ID"""
        pass
