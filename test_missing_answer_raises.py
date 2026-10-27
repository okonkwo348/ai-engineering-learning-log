import pytest
from study_companion.main import validate_session_payload

def test_validate_payload():
    data = {
    "title": "t",
    "summary": "s",
    "questions": [{"title": "t", "question": "Q1?"}],
}
    with pytest.raises(ValueError, match="answer 0 not avaible"):
        validate_session_payload(data)
    
def test_valid_payload_does_not_raise():
    data ={
        "title":"t",
        "summary":"s",
        "questions": [{"title": "t", "question": "Q1?", "answer": "A1"}]
    }
    validate_session_payload(data)