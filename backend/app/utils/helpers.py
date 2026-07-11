"""Utility functions for the application."""
import uuid
from typing import Any, Dict

def generate_uuid() -> str:
    """Generate a UUID string."""
    return str(uuid.uuid4())

def create_response(data: Any = None, message: str = None, success: bool = True) -> Dict:
    """Create a standard response format."""
    response = {
        "success": success,
        "data": data,
        "message": message,
    }
    return {k: v for k, v in response.items() if v is not None}
