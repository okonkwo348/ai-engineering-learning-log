"""
Concept: Variables, Data Types, and f-strings

Real-world context:
Every API response carries typed data (status codes as int, messages as str,
success flags as bool). Before working with real APIs, you need to be fluent
in how Python represents and combines these basic types.

Key lesson: never hardcode a value that should be DERIVED from real data.
`is_success` below is computed from `status_code`, not hardcoded — this keeps
it correct even if `status_code` changes.
"""

api_name = "WeatherAPI"
status_code = 200

# Derive the boolean directly from a comparison instead of hardcoding it.
# `status_code == 200` already evaluates to True/False, so no if/else needed.
is_success = status_code == 200

print(f"{api_name} responded with status {status_code} (success: {is_success})")


if __name__ == "__main__":
    # A second example showing the same pattern with a failing status code,
    # to prove is_success is genuinely derived, not fixed.
    status_code = 404
    is_success = status_code == 200
    print(f"{api_name} responded with status {status_code} (success: {is_success})")
