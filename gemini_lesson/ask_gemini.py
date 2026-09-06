"""
Concept: Calling a real LLM API safely - secrets + reusable function +
error handling + structured logging, all combined.

Real-world context:
This is the core loop of nearly every AI application: load config safely,
authenticate once, send a prompt, handle failure gracefully, extract the
result. Everything more advanced (RAG, tool calling, agents) builds on
this exact shape.

Notes on library choice:
- `google-generativeai` is deprecated; this uses the current `google-genai`
  package (`from google import genai`).
- `errors.ClientError` is the exception type this SDK raises for
  client-side failures (bad model name, bad request, etc). Found by
  reading the SDK's own `errors` module - see the note in the learning log
  README about how to discover the right exception type for a new library.
"""

import logging
import os

from dotenv import load_dotenv
from google import genai
from google.genai import errors

# --- One-time setup (loaded once, reused across every function call) ---

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key is None:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

client = genai.Client(api_key=api_key)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def ask_gemini(prompt: str) -> str | None:
    """
    Send a prompt to Gemini and return the response text.

    Returns None on failure instead of raising, so callers must check
    `if result is None:` before using the result (same pattern as
    fetch_json() in 03_apis_and_requests/reusable_fetch_function.py).
    """
    try:
        logger.info("Sending prompt to Gemini")
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )
        return response.text
    except errors.ClientError as e:
        logger.error(f"Gemini request failed: {e}")
        return None


if __name__ == "__main__":
    result = ask_gemini("Say hello in one short sentence.")

    if result is None:
        logger.warning("No data received")
    else:
        logger.info(result)
