"""
Concept: Tuples (immutable, ordered) and Sets (unique, unordered)

Real-world context:
Tuples signal "this data shouldn't change" (e.g. fixed coordinates).
Sets are the standard tool for deduplicating data (e.g. cleaning duplicate
IDs from an API response) and fast membership checks.

Key lesson: dict keys behave exactly like a set internally - unique,
unordered, no duplicates. That's why a dict comprehension built from a
list with duplicate keys ends up with FEWER entries than the source list -
each repeat key overwrites the previous value for that key, silently.
"""

raw_tags = ["premium", "active", "verified", "premium", "active"]

# --- Sets: automatic deduplication + fast membership checks ---
unique_tags = set(raw_tags)

if "verified" in unique_tags:
    print("Tag found")
else:
    print("Tag not found")

# --- Tuples: immutable, proven by triggering the real error ---
coordinates = (6.5244, 3.3792)  # Lagos

try:
    coordinates[0] = 10
except TypeError as e:
    print(f"Error: {e}")  # 'tuple' object does not support item assignment


if __name__ == "__main__":
    # A mutable list, for direct comparison - this succeeds with no error.
    mutable_coordinates = [6.5244, 3.3792]
    mutable_coordinates[0] = 10
    print(mutable_coordinates)  # [10, 3.3792]

    print(unique_tags)  # order not guaranteed - sets have no index/position
