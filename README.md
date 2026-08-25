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
```

## Topics Covered So Far

- **Python Foundations** — variables, types, f-strings, functions, control flow (`if`/`elif`/`else`)
- **Data Structures** — lists, dictionaries (including nested), safe access (`.get()` vs `[]`)
- **Loops** — `for`, `while`, `break`, `continue`, and the infinite-loop trap when a loop
  variable isn't updated on every path
- **APIs & Networking** — `requests`, JSON parsing, HTTP status codes, error handling with
  `try`/`except`, building a reusable, failure-safe API-calling function
- **Python conventions** — `if __name__ == "__main__":`, docstrings, type hints, snake_case

## Why This Matters

Every concept here is deliberately connected to real AI-engineering work: parsing API responses
(JSON ≈ dicts/lists), handling unreliable network calls (the same pattern used for OpenAI/Anthropic
API calls), and writing reusable, production-style functions rather than one-off scripts.

## What's Next

- Environment variables & secrets management
- Calling LLM APIs (Anthropic/OpenAI)
- Structured outputs & tool/function calling
- Retrieval-augmented generation (RAG)
- AI agents
