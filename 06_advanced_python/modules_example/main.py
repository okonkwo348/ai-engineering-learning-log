"""
Concept: Imports - reusing a function defined in another file.

Real-world context:
Real projects are split across many files. Importing lets you reuse
logic (like string_utils.shout) without copy-pasting it, and without
that file's own demo/test code firing unexpectedly on import (see the
__name__ guard in string_utils.py).

Run this directly to see the difference vs running string_utils.py
directly:
    python string_utils.py   -> prints "TEST!" (its own __main__ block runs)
    python main.py            -> prints only "HELLO!" (string_utils's
                                   __main__ block is skipped on import)
"""

from string_utils import shout

print(shout("hello"))
