from study_companion.main import QuizQuestion

def test_to_dict():

    q = QuizQuestion("Python", "What is self?", "The instance")

    actual = q.to_dict()

    expected = {
        "title": "Python",
        "question": "What is self?",
        "answer": "The instance",
    }

    assert actual == expected