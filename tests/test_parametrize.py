import pytest
from study_companion.main import validate_session_payload

VALID_PAYLOAD = {
    "title": "Python Basics",
    "summary": "Introduction to syntax and data types",
    "questions": [
        {
            "title": "Variables",
            "question": "What is a variable?",
            "answer": "A container for strong data values."
        }
    ]
}

@pytest.mark.parametrize(
    "payload_data, expected_error, error_message",
    [
        # --- payload not a dict ---
        (
            "aaa", ValueError, "must be a dictionary"
        ),
        # --- Invalid Top-Level Data Types ---
        (
            {**VALID_PAYLOAD, "title": 5, "summary": "s", "questions":[{"title": "s", "question": "q", "answer": "a"}]}, ValueError, "^title must be"
        ),
        (
            {**VALID_PAYLOAD, "title": "t", "summary": 5, "questions": [{"title": "s", "question": "q", "answer": "a"}]}, ValueError, "summary must be string and not empty"
        ),
        (
            {**VALID_PAYLOAD, "questions": [{**VALID_PAYLOAD["questions"][0], "question": 5}]}, ValueError, "question must be string and not empty"
        ),

        # Empty top-level "title"
        (
            {**VALID_PAYLOAD, "title": "", "summary": "s", "questions":[{"title": "s", "question": "q", "answer": "a"}]}, ValueError, "^title must be"
        ),

        # --missing Top-Level key field ---
        (
           { "summary": VALID_PAYLOAD["summary"], "questions": [{"title": "t", "question": "q", "answer": "A"}, {"title": "t2", "question": "q", "answer": "a"}]}, ValueError, "title key not available" 
        ),
        (
            {"title": VALID_PAYLOAD["title"], "questions": [{"title": "t", "question": "q", "answer": "A"}, {"title": "t2", "question": "q", "answer": "a"}]}, ValueError, "summary key not available"
        ),
        (
            # missing "questions" key
            {"title": VALID_PAYLOAD["title"], "summary": VALID_PAYLOAD["summary"]}, ValueError, 'questions key not available'
        ),
        (
            # "questions" is a string, not a list
            {"title": VALID_PAYLOAD["title"], "summary": VALID_PAYLOAD["summary"], "questions": "abc"}, ValueError, "must be a list"
        ),
        (
            # when the "questions" is an empty list
            {"title": VALID_PAYLOAD["title"], "summary": VALID_PAYLOAD["summary"], "questions": []}, ValueError, "list is empty"
        ),
        (
            # "question" is whitespace-only (bad item at index 0)
           {"title": "T", "summary": "S", "questions": [{"title": "Q", "question": "   ", "answer": "A"}]}, ValueError, "question must be string and not empty"
        ),
        (
            # when the "questions" list contains a dictionary with an empty "question" string
            {"title": "T", "summary": "S", "questions": [{"title": "t", "question": "q", "answer": "A"}, {"title": "t2", "question": "    ", "answer": "A2"}]}, ValueError, "question must be string and not empty"
        ),
            # Empty item-level for "question" at index 0
            (
                {"title": VALID_PAYLOAD["title"], "summary": VALID_PAYLOAD["summary"], "questions": [{"title": "t", "question": "", "answer": "A"}, {"title": "t2", "question": "q", "answer": "a"}]}, ValueError, "question 0: question must be string and not empty"
            ),
        (
            #non-string answer with index
            {"title": VALID_PAYLOAD["title"], "summary": VALID_PAYLOAD["summary"], "questions": [{"title": "t", "question": "q", "answer": "A"}, {"title": "t2", "question": "q", "answer": 3}]}, ValueError, "answer 1: answer must be string and not empty"
        ),
        (
            # Empty item-level for "answwer" at index 0
            {"title": VALID_PAYLOAD["title"], "summary": VALID_PAYLOAD["summary"], "questions": [{"title": "t", "question": "q", "answer": ""}, {"title": "t2", "question": "q", "answer": "a"}]}, ValueError, "answer 0: answer must be string and not empty"
        ),

            # the top-level title is valid and the bad item is at index 1:
        (
           {"title": VALID_PAYLOAD["title"], "summary": VALID_PAYLOAD["summary"], "questions": [{"title": "t", "question": "q", "answer": "A"}, {"title": " ", "question": "q", "answer": "a"}]}, ValueError, f"title 1: title must be string and not empty"
        ),
        (
           # Missing "title" at Item_level 
           {"title": VALID_PAYLOAD["title"], "summary": VALID_PAYLOAD["summary"], "questions": [{"title": "t", "question": "q", "answer": "A"}, {"question": "q", "answer": "a"}]}, ValueError, "title 1 not available"
        ),
        (
            # Missing "question" at Item_level
            {"title": VALID_PAYLOAD["title"], "summary": VALID_PAYLOAD["summary"], "questions": [{"title": "t", "question": "q", "answer": "A"}, {"title": "t", "answer": "a"}]}, ValueError, "question 1 not available"
        )




        ]
)

def test_validate_session_payload_negative_case(payload_data, expected_error, error_message):
    with pytest.raises(expected_error, match = error_message):
        validate_session_payload(payload_data)