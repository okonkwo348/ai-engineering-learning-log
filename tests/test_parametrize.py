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
    "payload_data, expected_error, error_message",
    [
        # --- Invalid Top-Level Data Types ---
        (
            {**VALID_PAYLOAD, "title": 5, "summary": "s", "questions":[{"title": "s", "question": "q", "answer": "a"}]}, ValueError, "title must be string and not empty"
        ),
        (
            {**VALID_PAYLOAD, "title": "t", "summary": 5, "questions": [{"title": "s", "question": "q", "answer": "a"}]}, ValueError, "summary must be string and not empty"
        ),
        (
            {**VALID_PAYLOAD, "questions": [{**VALID_PAYLOAD["questions"][0], "question": 5}]}, ValueError, "question must be string and not empty"
        ),

        (
            {"title": VALID_PAYLOAD["title"], "summary": VALID_PAYLOAD["summary"]}, ValueError, 'questions key not avaible'
        ),


        ]
)

def test_validate_session_payload_negative_case(payload_data, expected_error, error_message):
    with pytest.raises(expected_error, match = error_message):
        validate_session_payload(payload_data)