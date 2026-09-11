"""
Concept: List and dict comprehensions

Real-world context:
Comprehensions are the idiomatic, concise way to transform or filter
collections in Python - extremely common when reshaping API response data
or cleaning a dataset in one readable line instead of a multi-line loop.

Key lesson: a dict comprehension can silently LOSE data if the source has
duplicate keys - each repeated key just overwrites the previous value,
since dict keys must be unique (same uniqueness rule as a set).
"""

raw_tags = ["premium", "active", "verified", "premium", "active"]

# Transform every item (duplicates preserved - comprehensions don't dedupe).
upper_tags = [tag.upper() for tag in raw_tags]

# Filter with a condition - strictly more than 6 characters.
long_tags = [tag for tag in raw_tags if len(tag) > 6]

# Dict comprehension - duplicate keys overwrite, so this has fewer entries
# than len(raw_tags) even though every item is visited.
tag_lengths = {tag: len(tag) for tag in raw_tags}


if __name__ == "__main__":
    print(upper_tags)      # ['PREMIUM', 'ACTIVE', 'VERIFIED', 'PREMIUM', 'ACTIVE']
    print(long_tags)       # ['premium', 'verified', 'premium'] - "active" (6 chars) excluded
    print(tag_lengths)     # {'premium': 7, 'active': 6, 'verified': 8} - only 3 entries, not 5
