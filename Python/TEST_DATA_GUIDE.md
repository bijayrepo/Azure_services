# User API - SOLID Principles HTTP Trigger Functions
# Testing Guide and Sample Data Documentation

## Project Structure

### Core Implementation Files (SOLID Architecture)

1. **models.py** - Data Layer
   - User dataclass that represents user data
   - Single Responsibility: Data representation only

2. **validators.py** - Validation Layer
   - UserValidator class with static methods
   - Single Responsibility: Input validation
   - Validates: email, name, phone patterns

3. **interfaces.py** - Abstraction Layer
   - IUserRepository (Dependency Inversion Principle)
   - IUserService (Dependency Inversion Principle)
   - Abstract base classes for loose coupling

4. **repositories.py** - Data Access Layer
   - InMemoryUserRepository implementation
   - Single Responsibility: Data persistence
   - Can be replaced with database implementation

5. **services.py** - Business Logic Layer
   - UserService implementation
   - Single Responsibility: Business logic orchestration
   - Depends on IUserRepository (Dependency Inversion)

6. **function_app.py** - HTTP Trigger Layer
   - add_user: POST endpoint to create users
   - get_user: GET endpoint to retrieve users
   - Existing http_trigger: Original example endpoint

### Testing Files

7. **sample_data.py** - Sample Data for Testing
   - SAMPLE_USERS: 8 pre-configured test users
   - TEST_CASES: Organized test scenarios
   - Valid and invalid test data

8. **demo_test.py** - Manual Testing Script
   - 7 comprehensive test functions
   - Tests all CRUD operations
   - Demonstrates sample data usage
   - Run: python demo_test.py

9. **test_functions.py** - Automated Unit Tests
   - PyTest framework compatible
   - 40+ test cases
   - Tests all layers: Validator, Service, Repository
   - Integration tests with sample data
   - Run: pytest test_functions.py -v

10. **TESTING_GUIDE.md** - HTTP Testing Documentation
    - cURL command examples
    - Test scenarios for all endpoints
    - Expected request/response formats
    - HTTP status codes reference

## Sample Data Included

### 8 Pre-configured Users:
1. John Doe - john.doe@example.com - +14155552671
2. Jane Smith - jane.smith@example.com - +14155552672
3. Michael Johnson - michael.johnson@example.com - +14155552673
4. Sarah Williams - sarah.williams@example.com - +14155552674
5. Robert Brown - robert.brown@example.com - +14155552675
6. Emily Davis - emily.davis@example.com - +14155552676
7. David Miller - david.miller@example.com - +14155552677
8. Lisa Anderson - lisa.anderson@example.com - +14155552678

### Test Case Categories in sample_data.py:
- Valid test cases (passing scenarios)
- Invalid email test cases
- Invalid name test cases
- Invalid phone test cases
- Missing required fields test cases

## How to Run Tests

### Manual Testing (Demo Script):
\\\
cd f:\Live Projects\Vendor\Azure Services\Azure_services\Python
python demo_test.py
\\\

Expected Output:
- TEST 1: Creating users from sample data (5 users)
- TEST 2: Retrieving users by ID
- TEST 3: Retrieving users by email
- TEST 4: Duplicate email rejection
- TEST 5: Validation error handling
- TEST 6: User deletion
- TEST 7: JSON serialization

### Automated Unit Tests:
\\\
pytest test_functions.py -v
\\\

Test Classes:
- TestUserValidator (8 tests)
- TestUserService (9 tests)
- TestInMemoryUserRepository (4 tests)
- TestIntegration (2 tests)

### HTTP API Testing (When Running Function):
\\\
func host start
\\\

Then use cURL commands from TESTING_GUIDE.md:
\\\
curl.exe -X POST http://localhost:7071/api/add_user -H \"Content-Type: application/json\" -d '{\"name\":\"John Doe\",\"email\":\"john.doe@example.com\",\"phone\":\"+14155552671\"}'
\\\

## SOLID Principles Applied

? **Single Responsibility Principle**
  - Each class has one reason to change
  - Services handle business logic only
  - Validators handle validation only
  - Repositories handle data access only

? **Open/Closed Principle**
  - Extensible through interfaces
  - New repositories can be added without modifying existing code

? **Liskov Substitution Principle**
  - Implementations are interchangeable
  - InMemoryUserRepository can be replaced with DatabaseRepository

? **Interface Segregation Principle**
  - Clients depend on specific interfaces
  - IUserRepository, IUserService clearly defined

? **Dependency Inversion Principle**
  - Services depend on IUserRepository, not concrete implementation
  - Dependency injection used for loose coupling

## Features

? User Model (CRUD): Create, Read, Update, Delete
? Input Validation: Email, Name, Phone patterns
? Duplicate Prevention: Prevents duplicate email addresses
? Error Handling: Comprehensive exception handling
? JSON Serialization: User to JSON conversion for API responses
? In-Memory Storage: Ready for database integration
? Comprehensive Testing: Unit and integration tests included

## Next Steps

1. Replace InMemoryUserRepository with DatabaseRepository
2. Add authentication/authorization
3. Implement additional endpoints (list all users, update user)
4. Add logging and monitoring
5. Deploy to Azure Functions
