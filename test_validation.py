import pytest
from study_companion.main import validate_session_data

def test_validate_missing_answer():
    # A raw dictionary payload simulating Gemini's response missing the "answer" key
    bad_payload = {
        "title": "Python",
        "summary": "A brief summary",
        "questions": [
            {
                "title": "Q1",
                "question": "What is a variable?",
                # "answer" is missing completely!
            }
        ]
    }

    # Assert that calling the validator raises a ValueError
    with pytest.raises(ValueError):
        validate_session_data(bad_payload)