"""
Concept: Functions + Control Flow (if / elif / else)

Real-world context:
APIs return status codes (200, 404, 500, etc). Backend and AI systems constantly
need to translate these raw codes into meaningful, human-readable outcomes.
This function demonstrates that pattern using an elif chain, where only ONE
branch executes for a given input (unlike separate independent `if` statements,
which would each be checked regardless of earlier matches).
"""


def describe_status(status_code: int) -> str:
    """
    Convert an HTTP-style status code into a human-readable description.

    Args:
        status_code: The status code to evaluate (e.g. 200, 404, 500).

    Returns:
        A short string describing the outcome.
    """
    if status_code == 200:
        return "Success"
    elif status_code == 400 or status_code == 404:
        return "Client Error"
    elif status_code == 500:
        return "Server Error"
    else:
        return "Unknown Status"


if __name__ == "__main__":
    # Example calls — mirrors how status codes actually arrive from a real API response.
    print(describe_status(200))  # Success
    print(describe_status(404))  # Client Error
    print(describe_status(500))  # Server Error
    print(describe_status(999))  # Unknown Status
