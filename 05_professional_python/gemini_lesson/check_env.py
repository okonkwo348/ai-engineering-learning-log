"""
Concept: Loading secrets safely with environment variables

Real-world context:
API keys must NEVER be hardcoded in source code. Instead, the key lives
in a local .env file (excluded from git via .gitignore) and is loaded at
runtime with python-dotenv.

Run this script first, before making any real API call, to confirm your
.env file is set up correctly.
"""

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key is None:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")
else:
    print("Successful: GEMINI_API_KEY found.")
