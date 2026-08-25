"""
Concept: Loops - for, while, break, continue

Real-world context:
`for` loops are used constantly to iterate over API results (a list of users,
messages, search results). `while` loops show up in polling patterns
("keep checking until the job status is 'done'").

Key lesson (the important bug I actually hit while learning this):
if you use `continue` inside a `while` loop, make sure the loop's counter is
updated BEFORE the `continue` runs on every path. Otherwise the counter never
changes, the loop condition never becomes False, and you get an infinite loop.
"""


def print_odd_numbers_until_nine(limit: int = 11) -> None:
    """
    Print numbers from 1 up to (but not including) `limit`, skipping even
    numbers, and stopping entirely once the number reaches 9.

    Demonstrates the correct placement of `continue` relative to the
    loop's increment, to avoid an infinite loop.
    """
    x = 1
    while limit > x:
        if x % 2 == 0:
            # Increment BEFORE continue - otherwise x never changes and
            # the loop runs forever once it hits the first even number.
            x += 1
            continue

        if x == 9:
            break

        print(x)
        x += 1


if __name__ == "__main__":
    print_odd_numbers_until_nine()  # prints: 1, 3, 5, 7

    # A simple `for` loop over a list, for comparison.
    tags = ["premium", "verified", "active"]
    for tag in tags:
        print(tag)
