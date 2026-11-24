import re

from study_companion import main


def test_menu_loop_prints_error_when_save_sessions_raises_runtime_error(monkeypatch, capsys):
    inputs = iter(["new", "pytest basics", "exit"])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(inputs))
    monkeypatch.setattr(
        main,
        "generate_study_session",
        lambda _topic: {
            "title": "Pytest Basics",
            "summary": "Core testing concepts",
            "questions": [
                {
                    "title": "Fixtures",
                    "question": "What does monkeypatch do?",
                    "answer": "Temporarily modifies attributes or items during a test.",
                }
            ],
        },
    )
    monkeypatch.setattr(main, "load_sessions", lambda _filename: [])

    def failing_save(_sessions, _filename):
        raise RuntimeError("FAKE_SAVE_FAILURE: simulated disk failure")

    monkeypatch.setattr(main, "save_sessions", failing_save)

    main.main()

    captured = capsys.readouterr()
    assert re.search(r"^Could not save sessions:", captured.out, flags=re.MULTILINE)
    assert "A new session created successfully" not in captured.out

import re
import pytest

from study_companion import main


@pytest.mark.parametrize(
    "command_inputs",
    [
        ["new", "pytest basics", "exit"],
        ["list", "exit"],
        # "1" is a placeholder title: load_sessions raises ValueError before lookup uses it.
        ["view", "1", "exit"],
    ],
    ids=["new", "list", "view"],
)
def test_menu_loop_prints_error_when_load_sessions_raises_value_error(
    monkeypatch, capsys, command_inputs
):
    inputs = iter(command_inputs)
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(inputs))
    monkeypatch.setattr(
        main,
        "generate_study_session",
        lambda _topic: {
            "title": "Pytest Basics",
            "summary": "Core testing concepts",
            "questions": [
                {
                    "title": "Fixtures",
                    "question": "What does monkeypatch do?",
                    "answer": "Temporarily modifies attributes or items during a test.",
                }
            ],
        },
    )

    def failing_load(_filename):
        raise ValueError("FAKE_LOAD_FAILURE: corrupt session data")

    save_calls = []

    def spy_save(sessions, filename):
        save_calls.append((sessions, filename))

    monkeypatch.setattr(main, "load_sessions", failing_load)
    monkeypatch.setattr(main, "save_sessions", spy_save)

    main.main()

    captured = capsys.readouterr()
    assert re.search(r"^Could not load sessions:", captured.out, flags=re.MULTILINE)
    assert len(save_calls) == 0