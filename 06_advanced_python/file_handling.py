"""
Concept: File handling - reading, writing, and the `with` statement

Real-world context:
Persisting data to disk (logs, config, datasets) is a constant backend
need. `with open(...) as f:` is essentially an automatic try/finally for
files - it guarantees the file gets closed even if an error happens while
working with it, the same guarantee `finally` gives explicitly.

Key lesson: `for line in f:` iterates line-by-line (the file object is
itself iterable). `for line in f.read():` does NOT do this - f.read()
collapses everything into a single string first, so looping over THAT
goes character by character instead.
"""

LOG_FILE = "api_log.txt"


def write_sample_log() -> None:
    with open(LOG_FILE, "w") as f:
        f.write("Request 1: Success\nRequest 2: Failed\nRequest 3: Success")


def read_and_flag_failures() -> None:
    with open(LOG_FILE, "r") as f:
        for line in f:
            if "Failed" in line:
                print("\u26a0\ufe0f " + line.strip())
            else:
                print(line.strip())


if __name__ == "__main__":
    write_sample_log()
    read_and_flag_failures()

    # Proving FileNotFoundError firsthand, with guaranteed cleanup messaging.
    try:
        open("does_not_exist.txt", "r")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    finally:
        print("File operation attempt finished")
