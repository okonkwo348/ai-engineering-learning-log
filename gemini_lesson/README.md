# Gemini API Lesson

Demonstrates safe secrets handling, virtual environments, a reusable
failure-safe LLM-calling function, and structured logging - the core
building blocks behind every AI application.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in your real key (never commit `.env` itself):

```bash
cp .env.example .env
```

## Files

- `check_env.py` - confirms your `.env` file and key are loading correctly
  before spending any real API calls.
- `ask_gemini.py` - the actual reusable, error-handled, logged function
  that sends a prompt to Gemini and returns the response text (or `None`
  on failure).

## Run

```bash
python3 check_env.py
python3 ask_gemini.py
```

## Key lessons this demonstrates

- Never hardcode API keys - load them from `.env` via `python-dotenv`.
- Use a virtual environment per project to avoid system-wide package
  conflicts (`externally-managed-environment` errors on modern Ubuntu).
- Wrap external API calls in `try`/`except`, returning `None` on failure
  rather than crashing the whole program - callers must check for `None`.
- Prefer `logging` over `print()` in real code: severity levels, timestamps,
  and module names come for free, and libraries you didn't write (like
  `httpx` and `google_genai`) surface their own useful logs once logging
  is configured.
