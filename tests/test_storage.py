import pytest
import json
from study_companion.main import QuizQuestion, StudySession, save_sessions, load_sessions, validate_session_payload


def test_save_then_load_round_trip(tmp_path):
    q1 = QuizQuestion("python", "what is variable", "act as a container of values")
    q2 = QuizQuestion("python", "What is self?", "The instance")
    q3 = QuizQuestion("variable", "write a variable in camelcase?", "myVariable")
    q4 = QuizQuestion("variable", "write a variable in snakecase", "my_variable")

    sessions = [
        StudySession("python", "python is a highlevel interpreted programming", [q1, q2]),
        StudySession("programming", "programmingis a step by step instruction of rules", [q3, q4])
        ]
    original_dicts = [s.to_dict() for s in sessions]

    path = tmp_path / "storage.json"
    save_sessions(sessions, str(path))
    loaded = load_sessions(str(path)) 
    loaded_dicts = [s.to_dict() for s in loaded]

    assert loaded_dicts == original_dicts

def test_load_sessions_missing_file(tmp_path):
    path = tmp_path / "nonexistent_storage.json"
    loaded = load_sessions(str(path))
    assert loaded == []  # Expecting an empty list when the file does not exist


def test_load_sessions_raises_value_error_naming_bad_session (tmp_path):
    malformed_data = [
        {
            "title": "python",
            "summary": "python is a highlevel interpreted programming",
            "questions": [{"title": "python", "question": "what is variable", "answer": "act as a container"}]
        },
        {
            # Missing "title" key intentionally!
            "summary": "programming is a step by step instruction of rules",
            "questions": [{"title": "variable", "question": "camelcase?", "answer": "myVariable"}]
        },
        {
            "title": "variable",
            "summary": "programming is a step by step instruction of rules",
            "questions": [{"title": "variable", "question": "snakecase?", "answer": "a"}] 
        }
    ]
    path = tmp_path / "storage.json"
    
    path.write_text(json.dumps(malformed_data))
    

    with pytest.raises(ValueError,match=r"index 1"):
        load_sessions(str(path))  # Expecting a ValueError due to the malformed data

   