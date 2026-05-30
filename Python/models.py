from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class User:
    """User model - Single Responsibility: Represent user data"""
    id: Optional[str] = None
    name: str = ""
    email: str = ""
    phone: str = ""
    created_at: Optional[datetime] = None
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
