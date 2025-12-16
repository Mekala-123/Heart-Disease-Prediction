class NotFoundError(Exception):
    """Raised when an item is not found."""
    pass

class ConflictError(Exception):
    """Raised when an item already exists (unique constraint)."""
    pass

class ValidationError(Exception):
    """Raised when input validation fails."""
    pass
