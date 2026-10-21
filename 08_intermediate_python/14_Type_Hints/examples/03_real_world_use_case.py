"""
03_real_world_use_case.py
Real-world scenario: Type-Safe REST API Request & Response Framework.
Demonstrates:
- TypedDict for structured JSON payloads (required and optional keys)
- Literal for HTTP method validation
- Type safety without runtime class instantiation overhead
"""

from typing import TypedDict, Literal, Optional

# Define HTTP Method type constraint
HttpMethod = Literal["GET", "POST", "PUT", "DELETE", "PATCH"]

# Define User DTO structure
class UserDTO(TypedDict):
    id: int
    username: str
    email: str
    is_active: bool

# Define API Response structure with generic metadata
class ApiResponse(TypedDict):
    status_code: int
    data: Optional[UserDTO]
    error: Optional[str]
    method: HttpMethod

def dispatch_user_request(method: HttpMethod, user_id: int) -> ApiResponse:
    """Dispatches simulated REST request with strictly typed contracts."""
    if method == "GET":
        mock_user: UserDTO = {
            "id": user_id,
            "username": "sarah_connor",
            "email": "sarah@resistance.net",
            "is_active": True
        }
        return {
            "status_code": 200,
            "data": mock_user,
            "error": None,
            "method": method
        }
    elif method == "DELETE":
        return {
            "status_code": 204,
            "data": None,
            "error": None,
            "method": method
        }
    else:
        return {
            "status_code": 405,
            "data": None,
            "error": f"Method {method} not supported for user endpoint",
            "method": method
        }


def main():
    print("--- Type-Safe API Request / Response ---")
    response_get = dispatch_user_request("GET", 101)
    print(f"GET Response [Status {response_get['status_code']}]:")
    print(f"  User: {response_get['data']}")

    response_delete = dispatch_user_request("DELETE", 101)
    print(f"\nDELETE Response [Status {response_delete['status_code']}]: Data = {response_delete['data']}")

if __name__ == "__main__":
    main()
