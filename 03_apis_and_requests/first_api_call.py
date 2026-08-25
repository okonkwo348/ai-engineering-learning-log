"""
Concept: Making a real HTTP GET request with `requests`

Real-world context:
`requests` is the industry-standard Python library for calling web APIs.
Every AI-engineering task involving OpenAI, Anthropic, or any backend
service starts with this exact pattern: send a request, check the status
code, parse the JSON body.
"""

import requests

response = requests.get("https://api.github.com")

print(response.status_code)  # e.g. 200

data = response.json()  # parses the response body into a Python dict
print(data.get("current_user_url"))  # e.g. "https://api.github.com/user"


if __name__ == "__main__":
    # response.text gives the raw string body, for comparison with .json().
    print(type(response.text))  # <class 'str'>
    print(type(data))  # <class 'dict'>
