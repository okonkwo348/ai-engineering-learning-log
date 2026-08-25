"""
Concept: Lists and Dictionaries (including nested structures)

Real-world context:
JSON from real APIs is essentially just Python dicts and lists nested inside
each other. Being fluent in accessing, looping, and safely reading nested
data is a prerequisite for everything in AI engineering (parsing API
responses, reading LLM outputs, working with datasets).

Key lesson: use `["key"]` when a field is guaranteed to exist, and `.get()`
when a field might be missing or optional (safer — returns None instead of
crashing with a KeyError).
"""

api_response = {
    "status_code": 200,
    "user": {
        "name": "emmanuel",
        "email": "emmanuel3@gmail.com",
    },
    "tags": ["premium", "verified", "active"],
}

# Guaranteed field -> plain bracket access is fine.
print(api_response["user"]["name"])

# Potentially optional field -> use .get() for safety (returns None if missing).
print(api_response["user"].get("email"))

# Looping over a nested list.
for tag in api_response["tags"]:
    print(tag)


if __name__ == "__main__":
    # Demonstrates the crash vs. graceful-failure difference directly.
    try:
        print(api_response["user"]["phone"])  # KeyError: "phone" doesn't exist
    except KeyError as e:
        print(f"Direct access crashed as expected: missing key {e}")

    # .get() on the same missing key does NOT crash — returns None instead.
    print(api_response["user"].get("phone"))  # None
    print(api_response["user"].get("phone", "No phone provided"))  # fallback value
