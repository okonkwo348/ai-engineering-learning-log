"""
Concept: Strings, string methods, and slicing

Real-world context:
Cleaning and validating user/API input (whitespace, casing) and masking
sensitive data in logs (e.g. showing only part of an API key) are both
constant tasks in backend and AI engineering work.

Key lesson (slicing trap): slicing walks LEFT TO RIGHT through a string by
position. If `start`'s position comes after `stop`'s position - regardless
of whether either was written as a negative index - the result is an empty
string. It has nothing to do with index 0 being special; it's about the
relative order of start vs stop.
"""


def clean_email(raw_input: str) -> str:
    """Strip whitespace and lowercase an email string for comparison."""
    return raw_input.strip().lower()


def is_gmail(raw_input: str) -> bool:
    """Check whether a (possibly messy) email string is a gmail address."""
    return clean_email(raw_input).endswith("gmail.com")


def mask_key(key: str) -> str:
    """Return a masked preview of a secret, e.g. 'sk-ant...z789'."""
    first_six = key[0:6]
    last_four = key[-4:]
    return f"{first_six}...{last_four}"


if __name__ == "__main__":
    raw_input = "  Emmanuel@GMAIL.com  "
    if is_gmail(raw_input):
        print("Valid Gmail address")
    else:
        print("Not a Gmail address")

    api_key_display = "sk-ant-abc123xyz789"
    print(f"Key preview: {mask_key(api_key_display)}")

    # Proof of the slicing trap: start position after stop position -> empty.
    print(repr(api_key_display[-4:0]))   # '' (empty string)
    print(repr(api_key_display[-4:]))    # 'z789'
    print(repr(api_key_display[-4:20]))  # 'z789' - same as [-4:] since 20 is past the last index
