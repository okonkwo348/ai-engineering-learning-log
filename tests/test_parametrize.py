import pytest
from study_companion.main import validate_session_payload

VALID_PAYLOAD = {
    "title": "Python Basics",
    "summary": "Introduction to syntax and data types",
    "questions": [
        {
            "title": "Variables",
            "question": "What is a variable?",
            "answer": "A container for strong data values."
        }
    ]
}

@pytest.mark.parametrize(
    "payload", "expected_error",
    [
        # --- Invalid Top-Level Data Types ---
        (
            {**VALID_PAYLOAD, "title": 5, "summary": "s", "questions":[]}, ValueError
        ),
        (
            {**VALID_PAYLOAD, "title": "t", "summary": 5, "questions": []}, ValueError
        ),
        (
            {**VALID_PAYLOAD, "title": "t", "summary": "s", "questions":5}, ValueError
        ),


        ]
)

def test_validate_session_payload_negative_case(payload, expected_error):
    with pytest.raises(expected_error):
        validate_session_payload(payload)