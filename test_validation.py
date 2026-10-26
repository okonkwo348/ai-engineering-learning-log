import pytest
from study_companion.main import validate_session_payload

def test_validate_payload():
    data = {
    "title": "t",
    "summary": "s",
    "questions": [{"title": "t", "question": "Q1?"}],
}
    with pytest.raises(ValueError):
        validate_session_payload(data)
    
