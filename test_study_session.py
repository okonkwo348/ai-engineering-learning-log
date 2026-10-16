import pytest
from study_companion.main import QuizQuestion, StudySession

def test_to_dict():
        
    q1 = QuizQuestion("python", "what is variable", "act as a container of values")
    q2 = QuizQuestion("python", "What is self?", "The instance")

    session = StudySession("python", "python is a highlevel interpreted programming", [q1, q2])
    expected = {
            "title" : "python",
            "summary": "python is a highlevel interpreted programming",
            "questions": [{"title": "python", "question": "what is variable", "answer":"act as a container of values"}, {"title": "python", "question":"What is self?", "answer": "The instance"}]
        }
    actual = session.to_dict()

    assert actual == expected