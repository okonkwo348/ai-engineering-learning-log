import pytest
from study_companion.main import validate_session_payload


def test_non_dict_question_raises():
    data = {
        "title": "t", 
        "summary": "s", 
        "questions": ["oops"]
        }
    with pytest.raises(ValueError, match =  "question 0 : is not a dictionary"):
        validate_session_payload(data)

def test_non_dict_question_does_not_raises():
    data = {
        "title": "t", 
        "summary": "s", 
        "questions": ["oops"]
        }
    validate_session_payload(data)

