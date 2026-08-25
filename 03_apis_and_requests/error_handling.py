"""
Concept: Handling API failures with try / except

Real-world context:
Networks fail. Servers go down. Endpoints get typo'd. Rate limits get hit.
Production code can never assume an API call will succeed - if it does and
you don't handle the failure, one bad request crashes your entire program.

Key lesson: there are two distinct failure points to know about.
  1. The server responds, but with an error status (e.g. 404) -
     `response.raise_for_status()` is what raises the exception here.
  2. The request never reaches a server at all (e.g. the domain doesn't
     exist / DNS lookup fails) - `requests.get(...)` itself raises the
     exception, before raise_for_status() ever runs.

Both are subclasses of `requests.exceptions.RequestException`, so catching
that one base class handles both cases with a single except block.
"""

import requests

# Case 1: server responds, but with a 404 (bad endpoint on a real domain).
try:
    response = requests.get("https://api.github.com/this-does-not-exist")
    response.raise_for_status()  # raises HTTPError because status is 404
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")


if __name__ == "__main__":
    # Case 2: the domain itself doesn't exist - fails at requests.get()
    # itself, before raise_for_status() is ever reached.
    try:
        response = requests.get("https://this-domain-does-not-exist-xyz123.com")
        response.raise_for_status()
        data = response.json()
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
