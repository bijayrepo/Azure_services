# HTTP API Testing Guide with cURL
# 
# This file contains curl commands to test the User API endpoints
# 
# Prerequisites:
#   - Azure Functions Runtime started: func host start
#   - API runs on http://localhost:7071
#   - Have curl installed

# ============================================================
# TEST 1: ADD USER ENDPOINT - Valid User
# ============================================================
curl.exe -X POST http://localhost:7071/api/add_user -H "Content-Type: application/json" -d '{"name":"John Doe","email":"john.doe@example.com","phone":"+1-555-0101"}' -w "\nStatus: %{http_code}\n"

# Expected Response (201 Created):
# {
#   "success": true,
#   "message": "User created successfully",
#   "user": {
#     "id": "550e8400-e29b-41d4-a716-446655440000",
#     "name": "John Doe",
#     "email": "john.doe@example.com",
#     "phone": "+1-555-0101",
#     "created_at": "2026-05-30T10:30:45.123456"
#   }
# }


# ============================================================
# TEST 2: ADD USER - Multiple Users (Sample Data)
# ============================================================

# User 2:
curl.exe -X POST http://localhost:7071/api/add_user -H "Content-Type: application/json" -d '{"name":"Jane Smith","email":"jane.smith@example.com","phone":"+1-555-0102"}'

# User 3:
curl.exe -X POST http://localhost:7071/api/add_user -H "Content-Type: application/json" -d '{"name":"Michael Johnson","email":"michael.johnson@example.com","phone":"+1-555-0103"}'


# ============================================================
# TEST 3: ADD USER - Invalid Email
# ============================================================
curl.exe -X POST http://localhost:7071/api/add_user -H "Content-Type: application/json" -d '{"name":"Bad Email User","email":"invalid-email-format","phone":"+1-555-0105"}' -w "\nStatus: %{http_code}\n"

# Expected Response (400 Bad Request):
# {"error": "Invalid email format"}


# ============================================================
# TEST 4: GET USER - Retrieve by ID
# ============================================================
curl.exe -X GET "http://localhost:7071/api/get_user?id=550e8400-e29b-41d4-a716-446655440000" -w "\nStatus: %{http_code}\n"

# Expected Response (200 OK):
# {"success": true, "user": {...}}


# ============================================================
# TEST 5: GET USER - User Not Found
# ============================================================
curl.exe -X GET "http://localhost:7071/api/get_user?id=non-existent-id" -w "\nStatus: %{http_code}\n"

# Expected Response (404 Not Found):
# {"error": "User not found"}

