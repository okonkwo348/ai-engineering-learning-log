import pytest
from study_companion.main import QuizQuestion, StudySession, save_sessions, load_sessions 


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
