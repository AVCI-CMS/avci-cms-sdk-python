class AvciAPIError(Exception):
    """Base exception for all API errors."""
    def __init__(self, message: str, status_code: int = None, details: dict = None):
        super().__init__(message)
        self.status_code = status_code
        self.details = details or {}

class UnauthorizedError(AvciAPIError):
    """Raised when authentication fails (401/403)."""
    pass

class NotFoundError(AvciAPIError):
    """Raised when a resource is not found (404)."""
    pass

class ValidationError(AvciAPIError):
    """Raised when the server returns a 400 validation error."""
    pass

def handle_response_error(response):
    """Helper to raise the appropriate exception based on HTTP status."""
    if 200 <= response.status_code < 300:
        return

    try:
        data = response.json()
        message = data.get("message", "Unknown API Error")
        details = data.get("details", {})
    except Exception:
        message = response.text
        details = {}

    if response.status_code in (401, 403):
        raise UnauthorizedError(message, response.status_code, details)
    elif response.status_code == 404:
        raise NotFoundError(message, response.status_code, details)
    elif response.status_code == 400:
        raise ValidationError(message, response.status_code, details)
    
    raise AvciAPIError(message, response.status_code, details)
