# AI Engineering Learning Log

This repository is my structured learning log and project workspace as I transition from software engineering into AI engineering.

My path is:

- Software Engineer
- AI Engineer
- Robotics Engineer

The goal is to build strong fundamentals through hands-on work: API integrations, backend thinking, LLM usage, debugging, and practical AI application patterns.

## Repository purpose

This repo captures:

- Python foundations and core programming concepts
- Data structures and problem-solving patterns
- APIs, HTTP requests, and error handling
- Classes and reusable application design
- Professional Python habits such as virtual environments, `.env` management, and logging
- LLM integration with Gemini
- Small portfolio-style project work built from real learning exercises
- Testing and failure-driven debugging with `pytest`

## Current project structure

```text
ai-engineering-learning-log/
├── .gitignore
├── README.md
├── instruction.md
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
├── main.py
├── practice.py
├── tryExcept.py
├── test2.txt
├── AI_Concepts/
│   └── ai_engineering_foundations_reference_guide.md
├── 01_python_foundations/
│   ├── functions_control_flow.py
│   ├── loop.py
│   └── variables_types.py
├── 02_data_structures/
│   ├── dicts_lists.py
│   └── loops.py
├── 03_apis_and_requests/
│   ├── error_handling.py
│   ├── first_api_call.py
│   └── reusable_fetch_function.py
├── 04_classes/
│   └── api_response_class.py
├── 05_professional_python/
│   └── gemini_lesson/
│       ├── .env.example
│       ├── README.md
│       ├── ask_gemini.py
│       ├── check_env.py
│       └── requirements.txt
├── 06_advanced_python/
│   ├── comprehensions.py
│   ├── exceptions_in_depth.py
│   ├── file_handling.py
│   ├── iterators_and_generators.py
│   ├── modules_example/
│   │   ├── main.py
│   │   └── string_utils.py
│   ├── strings_and_slicing.py
│   └── tuples_and_sets.py
├── 07_cli_todo_app/
│   ├── README.md
│   └── main.py
├── CLI_Todo_App/
│   ├── file.json
│   └── main.py
├── gemini_lesson/
│   ├── .env.example
│   ├── .gitignore
│   ├── README.md
│   ├── ask_gemini.py
│   ├── check_env.py
│   └── requirements.txt
├── resource_inventory/
│   └── main.py
├── study_companion/
│   └── main.py
├── tests/
│   ├── test_missing_answer_raises.py
│   ├── test_non_dict_question_raises.py
│   ├── test_non_string_answer_raises.py
│   ├── test_quiz_question.py
│   ├── test_storage.py
│   └── test_study_session.py
└── README.md
```

## Learning phases covered

The repo currently includes work across several phases, including:

- Python fundamentals: variables, functions, control flow, loops, strings, slicing, exceptions, modules, and file handling
- Data structures: lists, dicts, tuples, sets, and comprehensions
- API work: `requests`, JSON handling, HTTP status codes, and safe error handling
- Classes: object-oriented design, `__init__`, methods, serialization, and debugging common class issues
- Professional Python: virtual environments, `.env` files, logging, type hints, and clean code habits
- AI engineering basics: Gemini API integration, prompt design, and structured outputs
- Testing: `pytest`, failure-driven debugging, and writing tests that catch real regressions

## Recent additions

New work has been added to strengthen the bridge between Python fundamentals and real AI application building:

- prompt design and interaction with Gemini through a safe `.env`-managed setup
- reusable API-wrapping patterns for handling failures without crashing the app
- study tracking workflows that combine persistence, validation, and test coverage
- small portfolio-style projects that demonstrate practical engineering habits rather than isolated toy examples
- a more structured approach to learning by building, testing, and debugging real behavior

## Key projects

### 1. CLI Todo App
Located in `07_cli_todo_app/`.

This project demonstrates:

- JSON persistence
- structured menu-driven CLI design
- safe input validation
- exception handling for invalid actions and corrupted data
- logging instead of noisy debugging output

### 2. Study Companion
Located in `study_companion/`.

This is the main portfolio-style project in the repo. It includes:

- study session tracking
- quiz question storage and loading
- persistence to a JSON file
- menu-driven user interaction
- tests for core behavior

### 3. Gemini lesson
Located in `gemini_lesson/` and `05_professional_python/gemini_lesson/`.

These folders demonstrate how to:

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
- expanding into more AI-focused workflow patterns such as prompt design, validation, and structured outputs

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
- practical experimentation with AI workflows, automation, and tool use in real project contexts

---

This repository reflects a practical, disciplined approach to learning: understand the concept, test the behavior, debug the failure, and then keep moving with confidence.
