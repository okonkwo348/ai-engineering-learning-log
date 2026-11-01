import pytest

from study_companion.main import validate_session_payload


def test_valid_summary_passes_validation():
    data = {
        "title": "Python Basics",
        "summary": "Python is a high-level programming language used for scripting and automation.",
        "questions": [
            {
                "title": "Variables",
                "question": "What is a variable?",
                "answer": "A variable stores data in memory."
            }
        ]
    }

    validate_session_payload(data)


def test_invalid_summary_raises_value_error():
    data = {
        "title": "Python Basics",
        "summary": "",
        "questions": [
            {
                "title": "Variables",
                "question": "What is a variable?",
                "answer": "A variable stores data in memory."
            }
        ]
    }

    with pytest.raises(ValueError, match="summary must be string and not empty"):
        validate_session_payload(data)
