"""
Sample data for testing the User API
"""

SAMPLE_USERS = [
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+14155552671"
    },
    {
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "phone": "+14155552672"
    },
    {
        "name": "Michael Johnson",
        "email": "michael.johnson@example.com",
        "phone": "+14155552673"
    },
    {
        "name": "Sarah Williams",
        "email": "sarah.williams@example.com",
        "phone": "+14155552674"
    },
    {
        "name": "Robert Brown",
        "email": "robert.brown@example.com",
        "phone": "+14155552675"
    },
    {
        "name": "Emily Davis",
        "email": "emily.davis@example.com",
        "phone": "+14155552676"
    },
    {
        "name": "David Miller",
        "email": "david.miller@example.com",
        "phone": "+14155552677"
    },
    {
        "name": "Lisa Anderson",
        "email": "lisa.anderson@example.com",
        "phone": "+14155552678"
    }
]

# Test cases for validation
TEST_CASES = {
    "valid": [
        {"name": "Valid User", "email": "valid@example.com", "phone": "+14155552671"},
        {"name": "Another Valid", "email": "another@test.com", "phone": "5551234567"},
    ],
    "invalid_email": [
        {"name": "Bad Email", "email": "invalid-email", "phone": "+14155552671"},
        {"name": "Bad Email 2", "email": "no-domain@", "phone": "+14155552671"},
        {"name": "Bad Email 3", "email": "@nodomain.com", "phone": "+14155552671"},
    ],
    "invalid_name": [
        {"name": "", "email": "test@example.com", "phone": "+14155552671"},
        {"name": "A", "email": "test@example.com", "phone": "+14155552671"},
        {"name": "A" * 101, "email": "test@example.com", "phone": "+14155552671"},
    ],
    "invalid_phone": [
        {"name": "Bad Phone", "email": "test@example.com", "phone": "123"},
        {"name": "Bad Phone 2", "email": "test@example.com", "phone": "abc-def-ghij"},
    ],
    "missing_required_fields": [
        {"name": "No Email", "phone": "+14155552671"},
        {"email": "test@example.com", "phone": "+14155552671"},
    ]
}
