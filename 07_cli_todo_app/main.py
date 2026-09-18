"""
Project: CLI Todo App with JSON file persistence

Real-world context:
A synthesis project combining everything from Lessons 1-17: dict-based
records, file I/O (json.dump/json.load), the exception hierarchy
(ValueError, IndexError, AttributeError, json.JSONDecodeError all showed
up as real bugs while building this), logging vs print, and a stateful
command loop.

Design notes (each one was a real bug found and fixed while building this):

- Tasks are loaded ONCE at startup (`tasks = load_task()`), not on every
  loop iteration. Loading inside the loop caused two problems: it wasted
  disk I/O on every single command, and combined with save-then-mark
  ordering bugs, could silently overwrite in-memory changes with stale
  disk data. One load at startup = one source of truth for the session.

- load_task() returning [] when the file doesn't exist (rather than the
  function returning None, or crashing) was essential - the very first
  bug found while building this was `AttributeError: 'NoneType' object
  has no attribute 'append'`, caused by tasks briefly being None when no
  save file existed yet, and add_tasks() calling `tasks.append(...)` on
  that None.

- mark_task() must run BEFORE save_task() in the "done" branch - saving
  first would persist the task's old (not-done) state, since the actual
  mutation hadn't happened in memory yet.

- The "done" command wraps int(index_list) in try/except (ValueError,
  IndexError) - ValueError catches non-numeric input like "abc", while
  IndexError catches a numeric but out-of-range index like 99.
"""

import json
import logging
from pathlib import Path


def load_task() -> list:
    """Load tasks from file.json, or return an empty list if it doesn't
    exist yet / is corrupted."""
    file_path = Path("file.json")

    if file_path.is_file():
        try:
            with open("file.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


tasks = load_task()


def add_tasks(new_task: str) -> None:
    tasks.append({"title": new_task, "done": False})


def list_all_task():
    if len(tasks) == 0:
        return "Empty: add one task, eg resting, cleaning"
    return tasks


def mark_task(index_list: int) -> None:
    tasks[index_list]["done"] = True


def save_task() -> None:
    with open("file.json", "w") as file:
        json.dump(tasks, file, indent=2)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    select = True
    while select:
        print("Welcome to Todo App!")
        select = input(
            ": Enter: 'add' to add tasks, 'list' to list all tasks, "
            "'done' to mark a tasks done, 'exit' to quit > "
        )
        select = select.lower().strip()

        if select == "add":
            new_task = input(" Enter task e.g 'sweep', 'cook'....> ")
            add_tasks(new_task)
            save_task()

        elif select == "list":
            print(list_all_task())

        elif select == "done":
            index_list = input("Enter the task number: ")
            try:
                mark_task(int(index_list))
            except (ValueError, IndexError) as e:
                logger.error(f"Invalid task number: {e}")
                continue  # skip save_task() - nothing changed
            save_task()

        elif select == "exit":
            select = False


if __name__ == "__main__":
    main()
