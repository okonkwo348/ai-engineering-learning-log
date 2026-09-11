"""
Concept: Modules - any .py file is automatically importable by other files.

This file's own `if __name__ == "__main__":` block only runs when THIS
file is executed directly (e.g. `python string_utils.py`). When another
file does `from string_utils import shout`, Python still runs this whole
file once (to define shout), but __name__ is set to "string_utils" here,
not "__main__" - so the block below is skipped.
"""


def shout(text: str) -> str:
    return text.upper() + "!"


if __name__ == "__main__":
    print(shout("test"))
