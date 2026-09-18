# CLI Todo App

A command-line todo list with JSON file persistence, built as a synthesis
project after completing the core Python fundamentals curriculum -
combining dict-based data, file I/O, exception handling, and logging
into one working tool, debugged through several real iterations.

## Run

```bash
python3 main.py
```

## Commands

- `add` - add a new task
- `list` - show all tasks and their done/not-done status
- `done` - mark a task as done, by its index number (0-based)
- `exit` - quit the app

Tasks are saved to `file.json` in the same folder, and reloaded
automatically the next time the app starts.

## What this project demonstrates

- Loading persisted state once at startup rather than on every loop
  iteration (a real bug found while building this - see comments in
  `main.py`)
- The exception hierarchy in practice: `ValueError` and `IndexError` for
  bad "done" input, `AttributeError` for a `None`-vs-`[]` bug hit while
  building the file-loading logic, `json.JSONDecodeError` for a corrupted
  save file
- Correct ordering of mutate-then-save (mark a task done in memory
  *before* writing it to disk, not after)
- `logging` for internal error reporting vs. `print()` for user-facing
  menu output
