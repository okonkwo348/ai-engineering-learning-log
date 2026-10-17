import pytest
from study_companion.main import QuizQuestion, StudySession, save_sessions, load_sessions 


def test_storage(tmp_path):
    q1 = QuizQuestion("python", "what is variable", "act as a container of values")
    q2 = QuizQuestion("python", "What is self?", "The instance")

    sessions = [StudySession("python", "python is a highlevel interpreted programming", [q1, q2]), StudySession("programming", "programmingis a step by step instruction of rules", [q1, q2])]
    path = tmp_path / "storage.json"
    save_sessions(sessions, str(path))
    loaded = load_sessions(str(path)) 

    assert loaded == sessions
