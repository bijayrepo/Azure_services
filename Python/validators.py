import re
from typing import Tuple

class UserValidator:
    """Validator for User input - Single Responsibility: Validate user data"""
    
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, str]:
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True, ""
        return False, "Invalid email format"
    
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        """Validate name is not empty and reasonable length"""
        name = name.strip()
        if not name:
            return False, "Name cannot be empty"
        if len(name) < 2:
            return False, "Name must be at least 2 characters"
        if len(name) > 100:
            return False, "Name must not exceed 100 characters"
        return True, ""
    
    @staticmethod
    def validate_phone(phone: str) -> Tuple[bool, str]:
        """Validate phone number format"""
        pattern = r'^\+?1?\d{9,15}$'
        phone_cleaned = phone.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
        if re.match(pattern, phone_cleaned):
            return True, ""
        return False, "Invalid phone number format"
    
    @staticmethod
    def validate_user_data(name: str, email: str, phone: str) -> Tuple[bool, str]:
        """Validate all user data"""
        is_valid, msg = UserValidator.validate_name(name)
        if not is_valid:
            return False, msg
        
        is_valid, msg = UserValidator.validate_email(email)
        if not is_valid:
            return False, msg
        
        if phone:
            is_valid, msg = UserValidator.validate_phone(phone)
            if not is_valid:
                return False, msg
        
        return True, ""
