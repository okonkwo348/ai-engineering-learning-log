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
├── .gitignore
├── README.md
├── instruction.md
├── requirements.txt
├── requirements-dev.txt
├── main.py
├── practice.py
├── tryExcept.py
├── test.txt
├── test2.txt
├── test_quiz_question.py
├── test_storage.py
├── test_study_session.py
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
├── gemini_lesson/
├── resource_inventory/
│   └── main.py
├── study_companion/
│   └── main.py
```


## Curriculum Progress

### Fully covered
- Phase 1-2: variables, types, f-strings, functions, control flow,
  lists, dicts, loops, strings/slicing, tuples, sets, comprehensions,
  exceptions in depth, file handling, iterators/generators, modules
- Classes: `__init__`, `self`, attributes, methods, composition,
  serialization (`to_dict`/`from_dict` with `@classmethod`),
  `__str__`/`__repr__`
- APIs: `requests`, JSON, HTTP status codes, try/except for server and
  connection failures, failure-safe functions (`fetch_json`,
  `ask_gemini`)
- Professional practices: virtual environments, `.env` +
  `python-dotenv`, `logging` vs `print()`, `.gitignore`, type hints
  (applied project-wide, forward references, "honest hint" principle)
- AI engineering (partial): Gemini API (`google-genai`), structured
  outputs via `response_mime_type="application/json"`, prompt
  engineering for title quality (verified across 7 topics)
- Debugging habits built from live bugs: `if __name__` guard,
  `None`-safety at API boundaries, exception hierarchy
  (`errors.APIError`), `TypeError` vs `AttributeError` vs `KeyError`,
  list comprehension vs generator expression, `list.append()` returns
  `None`, `if`/`elif` chain mechanics, `for` loop variable persists,
  `input()` never returns `None`, exact-match vs substring search,
  dead code causing `NameError`, relative-path resolution against the
  working directory

### Testing with pytest (DONE for now, completed this period)
- Why tests exist; `assert actual == expected`; `AssertionError` is the
  exception a failed `assert` raises; `test_` naming convention
- **A test you have never seen fail is not trusted.** Break the code on
  purpose, watch it fail for the right reason, restore, confirm pass
- Reading failure output: `>` marks the failing line, `E` lines give
  detail, `-vv` shows the full diff (`-vv` is a flag, not a concept)
- Different failures look different: `AssertionError` = code ran but
  values differed; `FileNotFoundError` etc. = code crashed before the
  `assert`; `IndentationError` at collection = the file never loaded so
  no test ran at all
- **dict `==` ignores key order; list `==` compares by position**
  (verified in a shell). Dicts hold insertion order since 3.7, but
  equality ignores it
- `expected` is typed by hand so a test can't compare a function with
  itself
- Python's default `==` on objects is identity, not value.
  `StudySession` defines no `__eq__`, so tests compare `to_dict()`
  output instead. Chosen deliberately: don't change production code
  just to make a test convenient
- `tmp_path` fixture: each test gets its own empty throwaway folder, so
  tests never touch real `storage.json` and results don't depend on the
  machine. Pass `str(path)` because the functions are hinted `filename: str`
- Test data must contain differences the bug would erase. Sharing the
  same questions across two sessions hid a "wrong questions loaded"
  bug; distinct `q3`/`q4` fixed it
- Tests written and break-tested:
  - `test_quiz_question.py::test_to_dict` (swapped question/answer)
  - `test_study_session.py::test_to_dict` (`reversed(...)` question list)
  - `test_storage.py::test_save_then_load_round_trip` (load returned
    `[]`; hardcoded one-question list; distinct `q3`/`q4` data)
  - `test_storage.py::test_load_sessions_missing_file`
    (removed `FileNotFoundError` handler)
  - Currently 4 tests, all passing
- Indentation: Python compares raw indent characters; tabs vs spaces
  can look identical in an editor but count differently. Configure the
  editor to insert spaces and don't mix
- `requirements-dev.txt` created: `-r requirements.txt` then
  `pytest==9.1.1`. Runtime vs dev dependency split understood

### Git skills practiced this period
- `git rm --cached` stops tracking but keeps the file; `.gitignore`
  only affects untracked files; `git check-ignore -v <path>` is the
  proof a rule works
- `git diff`, `git diff --staged`, `git show HEAD:<path>`,
  `git log --oneline -- <path>`, `git ls-files`
- A clean `git status` only proves disk equals `HEAD`; it doesn't prove
  the push happened. `git pull` saying "already up to date" does not
  prove your own edits are committed
- Fresh clone only contains what was pushed: `venv/`, `.env`, and
  `storage.json` are missing and must be rebuilt by hand

### Deferred on purpose
- **Inheritance & polymorphism**: until the Study Companion needs a
  second question type (the `APIError` bug was a first taste)
- Encapsulation's access-control side (underscore-prefix conventions)

### Not yet started
- Phase 3 remainder: debugging tools, packaging
- Phase 4 remainder: data validation (Pydantic, likely replaces
  hand-written `to_dict`/`from_dict`), NumPy/Pandas basics
- Phase 5: FastAPI, databases (SQL, SQLite, ORM)
- Phase 6 remainder: multi-turn chat, tool/function calling,
  streaming, cost optimization, evaluation
- Phase 7: embeddings, vector databases, RAG, chunking, search, ranking
- Phase 8: agent architecture, planning, memory, tools, multi-agent,
  evaluation, observability
- Phase 9: Docker, deployment, CI/CD, monitoring, scaling, security,
  performance, production debugging

---

## Projects

### Completed: CLI Todo App
- `ai-engineering-learning-log/07_cli_todo_app/`. An older copy at the
  repo root (`CLI_Todo_App/`) is unaudited and likely stale

### In progress: Study Companion (portfolio project)
- Location: `ai-engineering-learning-log/study_companion/`; main code
  in `study_companion/main.py` (`QuizQuestion`, `StudySession`,
  `load_sessions`, `save_sessions`, menu loop); `ask_gemini` in
  `gemini_lesson/ask_gemini.py`
- Works end to end: new/list/view/exit menu, persistence, `503`
  handled with `continue`, title-quality prompt fix, type hints
- **`storage.json` is now untracked and in `.gitignore`** (commit
  `3619676` stopped tracking it; `4c1656c` added the ignore rules).
  It is throwaway developer data. A fresh clone starts with no file and
  `load_sessions` returns `[]`, now covered by a test
- **`.env` is ignored** (`git check-ignore -v .env` matched line 5, and
  `HEAD:.gitignore` contains it). Not tracked anywhere (checked at repo
  root; the all-folders check `git ls-files | Select-String "\.env"`
  was never pasted)
- Current `.gitignore`: `venv/`, `__pycache__/`, `*.pyc`,
  `storage.json`, `.env`
- Layout note: the working venv lives at `gemini_lesson\venv` and tests
  sit at the repo root. A cleanup question for later, before Docker
- Latest known commit: `6943501` "Add requirements-dev.txt with
  pytest", pushed and verified (`origin/main` on the same hash)
- **Known gap, parked:** no validation of Gemini's output shape. A
  missing key raises `KeyError` in `from_dict()`. Next topic

### Learn2Earn "resources inventory" project
- Built during the October break (list/borrow/return/search/report,
  while-loop menu). Commits `5aeebc2`, `ae7cf48`, `79baf9e`
- **Deferred by learner.** Review later, predict-first, when they
  bring the code. Don't raise it again until they do

---

## Roadmap Status

- A Sept 22 - Dec 2026 roadmap was drafted (Mon-Fri, 8hrs/day) and is
  **paused**, pending whether Learn2Earn has a fixed start date for
  JavaScript/HTML/CSS or is competency-based. Once confirmed, finalize
  or adjust

## Other open items

1. **`requirements.txt` existence is UNVERIFIED.** Run
   `git ls-files | Select-String "requirements"`. If it's missing,
   `requirements-dev.txt` fails on a fresh clone with "Could not open
   requirements file". If creating it: use
   `pip freeze | Set-Content -Encoding ascii requirements.txt`, then
   trim it to runtime packages only (`google-genai`, `python-dotenv`,
   `requests`), not `pytest`
2. Run `git ls-files | Select-String "\.env"` once to confirm `.env`
   is tracked nowhere
3. Gemini output validation (the `KeyError` gap): next lesson
4. Two earlier "vibe-coded" projects on the learner's GitHub are a
   portfolio risk until audited and refactored by hand
5. Reflection answers have drifted toward "nothing unclear / move on".
   Next session, test that claim with a task done with no template
6. Windows vs Linux drift: on Linux, `git pull` will delete the local
   `storage.json` (it's now untracked). That's expected
7. Mentor can `git clone` the repo in its sandbox to verify state but
   can't fetch GitHub URLs directly

## Next session

1. `git pull`, paste this tracker, paste `git status`
2. Verify `requirements.txt` (open item 1)
3. Gemini output validation: predict first how `from_dict` should
   behave when a key is missing (retry vs placeholder vs raise)
4. Write the validation test yourself, then break-test it
