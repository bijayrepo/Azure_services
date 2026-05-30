import azure.functions as func
import json
import logging
from repositories import InMemoryUserRepository
from services import UserService

# Initialize dependencies (Dependency Injection)
user_repository = InMemoryUserRepository()
user_service = UserService(user_repository)

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully. Ready to development")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )


@app.route(route="add_user", methods=["POST"])
def add_user(req: func.HttpRequest) -> func.HttpResponse:
    """HTTP trigger to add a new user - Following SOLID Principles

    SOLID Principles Applied:
    - Single Responsibility: Each class has one reason to change
    - Open/Closed: Extensible through interfaces
    - Interface Segregation: Clients depend on specific interfaces
    - Dependency Inversion: Depends on abstractions, not concrete classes
    - Liskov Substitution: Implementations are interchangeable

    Expected POST body:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+1234567890"
    }
    """
    logging.info('Add user function triggered')

    try:
        # Extract request body
        req_body = req.get_json()
        name = req_body.get('name')
        email = req_body.get('email')
        phone = req_body.get('phone', '')

        # Validate required fields
        if not name or not email:
            return func.HttpResponse(
                json.dumps({"error": "Name and email are required"}),
                status_code=400,
                mimetype="application/json"
            )

        # Create user using service (Business Logic Layer)
        user = user_service.create_user(name=name, email=email, phone=phone)

        # Return successful response
        return func.HttpResponse(
            json.dumps({
                "success": True,
                "message": "User created successfully",
                "user": user.to_dict()
            }),
            status_code=201,
            mimetype="application/json"
        )

    except ValueError as validation_error:
        """Handle validation errors"""
        logging.error(f"Validation error: {str(validation_error)}")
        return func.HttpResponse(
            json.dumps({"error": str(validation_error)}),
            status_code=400,
            mimetype="application/json"
        )

    except json.JSONDecodeError:
        """Handle invalid JSON"""
        logging.error("Invalid JSON in request body")
        return func.HttpResponse(
            json.dumps({"error": "Invalid JSON in request body"}),
            status_code=400,
            mimetype="application/json"
        )

    except Exception as ex:
        """Handle unexpected errors"""
        logging.error(f"Unexpected error: {str(ex)}")
        return func.HttpResponse(
            json.dumps({"error": "An unexpected error occurred"}),
            status_code=500,
            mimetype="application/json"
        )


@app.route(route="get_user", methods=["GET"])
def get_user(req: func.HttpRequest) -> func.HttpResponse:
    """HTTP trigger to retrieve a user by ID"""
    try:
        user_id = req.params.get('id')

        if not user_id:
            return func.HttpResponse(
                json.dumps({"error": "User ID is required"}),
                status_code=400,
                mimetype="application/json"
            )

        user = user_service.get_user(user_id)

        if not user:
            return func.HttpResponse(
                json.dumps({"error": "User not found"}),
                status_code=404,
                mimetype="application/json"
            )

        return func.HttpResponse(
            json.dumps({
                "success": True,
                "user": user.to_dict()
            }),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as ex:
        logging.error(f"Error retrieving user: {str(ex)}")
        return func.HttpResponse(
            json.dumps({"error": "An unexpected error occurred"}),
            status_code=500,
            mimetype="application/json"
        )
