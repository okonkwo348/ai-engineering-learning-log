"""
Concept: Wrapping an API call in a reusable, failure-safe function

Real-world context:
Real applications call APIs repeatedly, from many places, with different
inputs. Copy-pasting the same try/except block everywhere is a maintenance
problem - if the error-handling logic needs to change, every copy has to be
updated. Wrapping the pattern in a function keeps the logic in one place.

This is the exact shape of a basic "API client" function you'd write in a
production backend or AI agent tool.

Key lesson: on failure, this function returns None rather than letting the
exception crash the caller. That means every CALLER is responsible for
checking `if result is None:` before using the result - forgetting this
check would raise a TypeError, since None doesn't support subscripting
(e.g. `None["key"]` fails with "'NoneType' object is not subscriptable").
"""

import requests


def fetch_json(url: str) -> dict | None:
    """
    Fetch a URL and return its parsed JSON body, or None on failure.

    Args:
        url: The endpoint to send a GET request to.

    Returns:
        The parsed JSON as a dict on success, or None if the request
        failed for any reason (bad status code or connection failure).
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


if __name__ == "__main__":
    valid = fetch_json("https://api.github.com")
    invalid = fetch_json("https://api.github.com/this-does-not-exist")

    # Callers must check for None before treating the result as real data.
    if valid is None:
        print("No data received")
    else:
        print(valid)

    if invalid is None:
        print("No data received")
    else:
        print(invalid)
