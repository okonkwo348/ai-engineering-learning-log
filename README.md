# AI Engineering Learning Log

This repository is my structured learning log and project workspace as I transition from software engineering into AI engineering.

My path is:

- Software Engineer
- AI Engineer
- Robotics Engineer

The goal is not to rush through tutorials, but to build solid understanding through practical, real-world AI engineering work: API integrations, backend thinking, LLM usage, and agent-style problem solving.

## Repository purpose

This repo captures:

- Python foundations and core programming concepts
- Data structures and problem-solving patterns
- APIs, HTTP requests, and error handling
- Classes and reusable application design
- Professional Python habits such as virtual environments, `.env` management, and logging
- LLM integration with Gemini
- Small portfolio-style project work built from the learning

## Current structure

```text
ai-engineering-learning-log/
├── README.md
├── instruction.md
├── requirements.txt
├── requirements-dev.txt
├── main.py
├── practice.py
├── tryExcept.py
├── test_quiz_question.py
├── test_storage.py
├── test_study_session.py
├── 01_python_foundations/
├── 02_data_structures/
├── 03_apis_and_requests/
├── 04_classes/
├── 05_professional_python/
├── 06_advanced_python/
├── 07_cli_todo_app/
├── gemini_lesson/
├── study_companion/
├── resource_inventory/
└── CLI_Todo_App/
```

## Learning phases covered

The repo currently includes work across several phases, including:

- Python fundamentals: variables, functions, control flow, loops, strings, slicing, exceptions, modules, file handling
- Data structures: lists, dicts, tuples, sets, comprehensions
- API work: `requests`, JSON handling, HTTP status codes, and safe retry/error patterns
- Classes: object-oriented design, `__init__`, methods, serialization, and debugging common class issues
- Professional Python: virtual environments, `.env` files, logging, type hints, and clean code habits
- AI engineering basics: Gemini API integration, prompt design, and structured outputs
- Testing: `pytest`, failure-driven debugging, and writing tests that catch real regressions

## Key projects

### 1. CLI Todo App
Located in `07_cli_todo_app/`.

This project demonstrates:

- JSON persistence
- Structured menu-driven CLI design
- Safe input validation
- Exception handling for invalid actions and corrupted data
- Logging instead of noisy debug output

### 2. Study Companion
Located in `study_companion/`.

This is the main portfolio-style project in the repo. It includes:

- study session tracking
- quiz question storage and loading
- persistence to a JSON file
- menu-driven user interaction
- test coverage for core behavior

### 3. Gemini lesson
Located in `gemini_lesson/`.

This folder demonstrates how to:

- manage API keys with `.env`
- create a virtual environment
- call Gemini safely
- avoid crashing on API failures
- structure code for real AI application usage

## Getting started

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

If you are working on dev tooling and tests:

```bash
pip install -r requirements-dev.txt
```

Run a project example:

```bash
python3 07_cli_todo_app/main.py
```

Or for the Gemini example:

```bash
cd gemini_lesson
python3 check_env.py
python3 ask_gemini.py
```

## Current focus

The repo is currently centered around:

- solidifying Python fundamentals
- building reliable API-integration patterns
- learning how to debug real failures instead of guessing
- creating reusable, testable AI project code
- preparing portfolio work that demonstrates practical engineering skill

## Notes

- `.env` and generated local data files are intentionally ignored for safety and cleanliness.
- The repo emphasizes learning by doing, with real examples and testing rather than isolated toy exercises.
- This is a personal learning repository, but the code is structured to be readable, useful, and portfolio-ready.

## Roadmap direction

Planned next steps include:

- deeper AI engineering topics such as RAG, embeddings, and orchestration
- broader backend and application design patterns
- more production-minded debugging and validation practices
- stronger portfolio projects with cleaner documentation and architecture

---

This repository reflects a practical, disciplined approach to learning: understand the concept, test the behavior, debug the failure, and then keep moving with confidence.
