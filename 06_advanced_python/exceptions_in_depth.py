"""
Concept: Exceptions in depth - the built-in hierarchy, finally, and raise

Real-world context:
Production code needs to distinguish between different failure types
(ValueError vs TypeError vs KeyError, etc), guarantee cleanup code runs
regardless of success/failure (finally), and deliberately signal invalid
states before they cause confusing failures elsewhere (raise).

Key lesson (finally scoping): `finally` attaches to the SPECIFIC `try`
statement directly above it - not to "the whole script". If you have
multiple independent try/except blocks, each one needs its OWN finally;
a single finally at the bottom only binds to the nearest preceding try.

Built-in exception cheat sheet:
- ValueError         -> right type, wrong value      e.g. int("hello")
- TypeError           -> wrong type entirely           e.g. "5" + 5
- KeyError            -> dict key doesn't exist         e.g. {"a": 1}["b"]
- IndexError          -> list index out of range        e.g. [1, 2, 3][10]
- ZeroDivisionError   -> division by zero               e.g. 10 / 0
- FileNotFoundError   -> file doesn't exist on disk
"""


def safe_divide(a: float, b: float) -> float:
    """Divide a by b, raising a clear ValueError instead of letting a
    confusing ZeroDivisionError happen deeper in the call stack."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    # Each independent attempt gets its own complete try/except/finally -
    # a single finally at the bottom would only cover the last try block.
    try:
        print(safe_divide(10, 2))
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Division attempt complete")

    try:
        print(safe_divide(10, 0))
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Division attempt complete")
