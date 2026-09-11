# AI Engineering Learning Log

This repository documents my structured transition from Software Engineering into AI Engineering,
as part of my long-term path: **Software Engineer → AI Engineer → Robotics Engineer**.

I'm following a mentor-guided curriculum (alongside the Learn2Earn AI Engineering programme)
that prioritizes deep understanding over speed — every concept here is tied to a real
AI-engineering use case (API integration, backend systems, LLM applications, agents)
rather than isolated toy examples.

## Structure

Each folder represents one phase of the curriculum. Files contain clean, working,
commented code demonstrating the core concept — not raw drafts.

```
ai-engineering-learning-log/
├── 01_python_foundations/
│   ├── variables_types.py
│   └── functions_control_flow.py
├── 02_data_structures/
│   ├── dicts_lists.py
│   └── loops.py
├── 03_apis_and_requests/
│   ├── first_api_call.py
│   ├── error_handling.py
│   └── reusable_fetch_function.py
├── 04_classes/
│   └── api_response_class.py
├── 05_professional_python/
│   └── gemini_lesson/
│       ├── README.md
│       ├── requirements.txt
│       ├── .env.example
│       ├── check_env.py
│       └── ask_gemini.py
├── 06_advanced_python/
│   ├── strings_and_slicing.py
│   ├── tuples_and_sets.py
│   ├── comprehensions.py
│   ├── exceptions_in_depth.py
│   ├── file_handling.py
│   └── iterators_and_generators.py
```

## Topics Covered So Far

- **Python Foundations** — variables, types, f-strings, functions, control flow (`if`/`elif`/`else`)
- **Data Structures** — lists, dictionaries (including nested), safe access (`.get()` vs `[]`)
- **Loops** — `for`, `while`, `break`, `continue`, and the infinite-loop trap when a loop
  variable isn't updated on every path
- **APIs & Networking** — `requests`, JSON parsing, HTTP status codes, error handling with
  `try`/`except`, building a reusable, failure-safe API-calling function
- **Classes** — bundling data (attributes) and behavior (methods) together, `__init__`, `self`
- **Professional Python practices** — virtual environments, `.env` secrets management with
  `python-dotenv`, and structured `logging` instead of `print()`
- **Real LLM API integration** — calling Google's Gemini API (`google-genai`) with proper
  authentication, a reusable failure-safe function, and logging
- **Strings & slicing** — string methods, cleaning input, masking secrets, the slicing
  start/stop position trap
- **Tuples & Sets** — immutability, deduplication, why dict keys behave like a set
- **Comprehensions** — list and dict comprehensions, the duplicate-key overwrite trap
- **Exceptions in depth** — the built-in exception hierarchy, `finally` scoping (it binds
  to a specific `try`, not the whole script), deliberately `raise`-ing errors
- **File handling** — `with open(...)`, read/write/append modes, line-by-line iteration,
  `FileNotFoundError`
- **Iterators & generators** — the iterator protocol (`iter()`/`next()`/`StopIteration`),
  `yield`, lazy evaluation, single-consumption behavior — the same mechanism behind
  streaming LLM responses
- **Python conventions** — `if __name__ == "__main__":`, docstrings, type hints, snake_case

## Why This Matters

Every concept here is deliberately connected to real AI-engineering work: parsing API responses
(JSON ≈ dicts/lists), handling unreliable network calls (the same pattern used for OpenAI/Anthropic
API calls), and writing reusable, production-style functions rather than one-off scripts.

## What's Next

- Modules & imports in depth (multi-file project structure)
- Prompt engineering & structured outputs
- Multi-turn chat / tool (function) calling
- Retrieval-augmented generation (RAG)
- AI agents

## Note on the `gemini_lesson` folder

This folder contains a real `.env`-based project with its own virtual
environment and dependencies. **Never commit a real `.env` file** — only
`.env.example` (a placeholder) is tracked in git. See `.gitignore` at the
repo root, and `05_professional_python/gemini_lesson/README.md` for setup
instructions.
