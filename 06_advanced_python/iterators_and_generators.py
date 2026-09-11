"""
Concept: Iterators and generators

Real-world context:
This is the mechanism behind streaming LLM responses (Claude/ChatGPT
"typing" word by word) and behind processing huge datasets without
loading everything into memory at once. A generator produces one value
at a time, on demand, instead of computing and storing an entire
sequence up front.

Key lesson: calling a generator function does NOT run any of its code -
not even the first line. It just returns a generator object, paused and
ready. Code only actually executes as each value is requested via
next() (which is what a `for` loop does automatically under the hood).
Generators are also single-use: once exhausted, calling next() again
raises StopIteration.
"""


def even_numbers_up_to(n: int):
    """Yield even numbers from 2 up to and including n."""
    x = 2
    while x <= n:
        yield x
        x += 2


if __name__ == "__main__":
    # Consumed automatically by a for loop (calls next() under the hood
    # until StopIteration, then stops cleanly).
    for num in even_numbers_up_to(10):
        print(num)

    # Manual iteration, to see next() mechanics directly. Uses a FRESH
    # call - the generator above was already fully consumed by the loop.
    manual = iter(even_numbers_up_to(6))
    print(next(manual))  # 2
    print(next(manual))  # 4
    print(next(manual))  # 6
    # print(next(manual))  # would raise StopIteration - nothing left

    # Calling the generator function itself, without looping or next(),
    # does NOT run its code - it just returns a generator object.
    print(even_numbers_up_to(3))  # <generator object ... at 0x...>
