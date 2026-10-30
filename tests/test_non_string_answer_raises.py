import pytest
from study_companion.main import validate_session_payload

def test_non_string_answer_raises():
    data = {
        "title": "t",
        "summary": "s",
        "questions":[{"title": "t", "question": "q", "answer": 5}]
    }
    with pytest.raises(ValueError, match ="answer must be string and not empty"):
        validate_session_payload(data)

def test_valid_answer_does_not_raise():
    data = {
        "title": "t",
        "summary": "s",
        "questions":[{"title": "t", "question": "q", "answer": "a"}]
    }
    validate_session_payload(data)
