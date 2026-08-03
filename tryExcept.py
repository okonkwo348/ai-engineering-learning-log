import requests

try:
    response = requests.get("https://api.github.com/this-does-not-exist")
    # response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e} ")

# Code inside try: runs normally — if it succeeds, except is skipped entirely.
#If an error occurs anywhere inside try, Python immediately jumps to except instead of crashing the program.
#response.raise_for_status() is a requests-specific method: it manually raises an exception if the status code is 4xx or 5xx (by default, requests does not treat those as Python errors — only actual network failures raise automatically).
#requests.exceptions.RequestException is the base exception class for requests — it catches connection errors, timeouts, and bad status codes (when combined with raise_for_status()) all in one place

# Wrong/nonexistent endpoint on a real domain (like /this-does-not-exist on api.github.com) → the server does respond, just with a 404 → failure point is response.raise_for_status().
# Nonexistent domain entirely → DNS lookup fails, no server ever responds → failure point is requests.get(...) itself.
