"""
Concept: Classes - bundling data and behavior together

Real-world context:
Plain dicts work for simple data, but as soon as you have several functions
that all need to operate on the SAME piece of data, passing that dict into
every function separately gets messy and error-prone. A class bundles the
data (attributes) and the behavior that acts on it (methods) into one
object, so the behavior travels WITH the data instead of being threaded
through as a parameter every time.

This is the foundation of patterns you'll see constantly in AI engineering:
Pydantic models, FastAPI request/response models, agent state objects, etc.
"""


class APIResponse:
    """Represents a simplified API response with a status code and payload."""

    def __init__(self, status_code: int, data: dict | None):
        # __init__ runs automatically when a new APIResponse is created.
        # `self` refers to the specific object being created/operated on.
        self.status_code = status_code
        self.data = data

    def is_success(self) -> bool:
        """Return True if the status code indicates success."""
        return self.status_code == 200

    def summary(self) -> str:
        """Return a short human-readable summary of this response."""
        return f"Response: {self.status_code}, Success: {self.is_success()}"


if __name__ == "__main__":
    ok = APIResponse(200, {"key": "value"})
    print(ok.summary())  # Response: 200, Success: True

    not_ok = APIResponse(404, None)
    print(not_ok.summary())  # Response: 404, Success: False

    # Same method, different object plugged in as `self` -> different result.
    print(ok.is_success())      # True
    print(not_ok.is_success())  # False
