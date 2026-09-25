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

# import logging
# import os
# import datetime as dt
# from pydantic import BaseModel, Field

# from dotenv import load_dotenv
# from google import genai
# from google.genai import types  # <--- Add this import!
# from google.genai import errors

# # --- One-time setup (loaded once, reused across every function call) ---

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")

# if api_key is None:
#     raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

# class DataModel(BaseModel):
#     name: str
#     age: int    
#     birthday: dt.date
#     gender: str = Field(..., description='Either M for male or F for female')


# client = genai.Client(api_key=api_key)

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


# def ask_gemini(prompt: str) -> str | None:
#     """
#     Send a prompt to Gemini and return the response text.

#     Returns None on failure instead of raising, so callers must check
#     `if result is None:` before using the result (same pattern as
#     fetch_json() in 03_apis_and_requests/reusable_fetch_function.py).
#     """
#     try:
#         logger.info("Sending prompt to Gemini")
#         response = client.models.generate_content(
#             model="gemini-3.6-flash",  # <--- Updated model name
#             contents=prompt,
#             config=types.GenerateContentConfig(
#                 response_mime_type="application/json",
#                 response_schema=DataModel,
#                 # Disable automatic function calling to prevent 503 spikes
#                 automatic_function_calling=types.AutomaticFunctionCallingConfig(
#                     disable=True
#                 ),
#             ),
#         )
#         return response.text
#     except errors.APIError as e:
#         logger.error(f"Gemini request failed: {e}")
#         return None


# if __name__ == "__main__":
#     result = ask_gemini(f"Mike was born April 4th 1990. Today is {dt.date.today()}. Fill the data model based on this information")
#     print(result)
#     if result is None:
#         logger.warning("No data received")
#     else:
#         logger.info(result)





import logging
import os
import json

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai import errors

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
    `if result is None:` before using the result.
    """
    try:
        logger.info("Sending prompt to Gemini")
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )
        try:
            result = json.loads(response.text)
            return result
        except json.JSONDecodeError as e:
            logger.warning(e)
            return None
    except errors.ClientError as e:
        logger.error(f"Gemini request failed: {e}")
        return None


def generate_study_session(text):
    prompt = f"""
Based on the following text, generate a JSON object with this exact structure:
{{
  "title": "a short title for this topic",
  "summary": "a concise summary of the text",
  "questions": [
    {{"title": "same as the main title", "question": "a quiz question", "answer": "the correct answer"}}
  ]
}}
Generate exactly 3 questions. Text: {text}
"""
    return ask_gemini(prompt)



if __name__ == "__main__":
    
    result = generate_study_session("a paragraph about Python functions")
    print(result)
    if result is None:
        logger.warning("No data received")
    else:
        logger.info(result)


