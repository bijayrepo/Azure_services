import uuid
from typing import Optional, Dict
from datetime import datetime
from models import User
from interfaces import IUserRepository

class InMemoryUserRepository(IUserRepository):
    """In-memory implementation of User Repository - Single Responsibility: Data access"""
    
    def __init__(self):
        self._users: Dict[str, User] = {}
    
    def add(self, user: User) -> User:
        """Add a new user to repository"""
        if not user.id:
            user.id = str(uuid.uuid4())
        if not user.created_at:
            user.created_at = datetime.utcnow()
        
        # Check if email already exists
        if any(u.email == user.email for u in self._users.values()):
            raise ValueError(f"User with email {user.email} already exists")
        
        self._users[user.id] = user
        return user
    
    def get_by_id(self, user_id: str) -> Optional[User]:
        """Get user by ID"""
        return self._users.get(user_id)
    
    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        for user in self._users.values():
            if user.email == email:
                return user
        return None
    
    def update(self, user: User) -> User:
        """Update existing user"""
        if user.id not in self._users:
            raise ValueError(f"User with ID {user.id} not found")
        self._users[user.id] = user
        return user
    
    def delete(self, user_id: str) -> bool:
        """Delete user"""
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False
