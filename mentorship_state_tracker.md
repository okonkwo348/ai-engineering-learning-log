# Mentorship State Tracker (lean)
Paste this at the start of every session. Last updated: Thu 2026-11-05.
Full history lives in the old tracker file (keep it in the repo, do NOT paste it).

## Standing agreements
- Predict before running or coding; no full solutions handed over
- One concept at a time; one question at a time; short sentences
- Test first: a test you have never seen fail is not trusted. Break on purpose, watch it fail for the right reason, restore, confirm
- Do the red run BEFORE the fix. Twice on Nov 4 the code change landed before the red run. Order: write test, see red, then change code
- Claims are not proof. Paste raw output (git status, git log --oneline, git diff, pytest). Output beats memory. Mentor must not assume repo state either
- Do not re-paste old output. Read each command before Enter
- Real reflection answers; "nothing" needs a reason
- git is truth: pull before work, add/commit/push after, verify push with status + log (origin/main on same hash as HEAD)
- A commit never needs the network; only push/pull/fetch do. A failed push loses nothing: commits stay local, retry the push
- One purpose per commit; message must say what actually changed (imperative: "Add...", "Fix...")
- PowerShell: never use `>` (UTF-16). Use Set-Content/Add-Content -Encoding ascii
- Windows is primary (cmd prompt); Linux (zsh, python3 -m pytest) is the second machine
- Keep chats short: see "Saving chat space"

## Saving chat space (free tier)
- `pytest -q --tb=short` for routine runs; `-vv` only to read one failure
- Paste only failing lines, or `... | tail -20`
- Use `git --no-pager diff` and `git --no-pager log --oneline -5`
- Paste a snippet or `git diff`, not whole files
- One task per chat; end at a milestone and update this file
- Do not paste the old long tracker

## Current state (verified unless marked)
- Study Companion in `study_companion/main.py`: QuizQuestion, StudySession, load/save_sessions, `validate_session_payload`, menu loop
- Latest pushed commit: `6df1a38` "Add test for empty item title with index" (HEAD = origin/main = origin/HEAD, tree clean)
- Last run: 22 passed (Linux)
- Tests in `tests/`; validator cases live in `tests/test_parametrize.py` (one parametrized function, params are `(payload_data, expected_error, error_message)`)
- `pytest.ini` at repo root (`pythonpath = .`)
- storage.json and .env ignored
- requirements.txt line 3 (requests pin) UNVERIFIED

## Validator: what is in the function now
Checks in order: payload is dict; title key / type+non-empty; summary key / type+non-empty; questions key; questions is list; questions not empty; then per item: item is dict, title key, title type/non-empty, question key, question type/non-empty, answer key, answer type/non-empty
- Item-level messages carry the index: "title {i}: ...", "question {i}: ...", "answer {i}: ..."
- Top-level title/summary messages carry no index (they do not need one)

## Validator test coverage
Tested (red first, break-tested): missing questions key, questions is string, questions empty list, whitespace-only question (index 0 and index 1), non-string answer at index 1, whitespace-only item title at index 1
Earlier: item not a dict, missing "answer", answer wrong type, summary empty, wrong-type title/summary/question
NOT tested yet: payload not a dict, missing top-level title or summary, missing item "title"/"question" keys, empty top-level title, empty question/answer at index 0 as separate cases
Known weaknesses:
- The "avaible" typo in messages (changing a message means changing its `match`)
- Item-level missing-key messages ("title {i} not avaible") use a different format from type messages ("title {i}: title must be...")
- Test IDs are unreadable (`payload_data5-...`): add `ids=` to parametrize
- Comment above the whitespace-question case (index 0) still says "non-dictionary item". Wrong. Fix in its own test-only commit. NOT done as of Nov 5 (diff output showed it unchanged)
- Commit `6df1a38` message hides that it also rewrote one comment; the new case is whitespace-only, not empty

## Concepts done recently
pytest.raises + match (re.search: pattern is found ANYWHERE in the message), a loose match can pass on two different messages so it cannot tell which line fired; make the match contain something unique to one line (e.g. "title 1:"); test data must make the bug visible (bad item at index 1, not 0, so a hardcoded 0 fails); `.strip()` catches whitespace-only strings that plain truthiness misses; empty list passes isinstance(list) and the for loop runs zero times; KeyError is not caught by `except ValueError`; `git status` "ahead of origin/main" = committed, not pushed; green = staged, red = unstaged/untracked

## Open items
1. Fix wrong comment on whitespace case (own commit)
2. Add `ids=` to the parametrize
3. Finish "NOT tested yet" list above
4. save_sessions has no OSError handling; load_sessions does not catch KeyError; `view` only catches ValueError (index out of range)
5. Retry on bad Gemini payload: deferred
6. Reflection answers drift to "nothing unclear" (happened again Nov 5). Test the claim: next session gives a task with NO template (see Next session, step 2)
7. Two older vibe-coded GitHub projects need an audit
8. Verify requirements.txt line 3 and Linux pyproject.toml warning (low priority)

## Deferred
- Inheritance/polymorphism (until a second question type exists)
- Learn2Earn "resources inventory" project: learner deferred; review only when they bring it
- Roadmap (Sept-Dec) paused pending Learn2Earn schedule

## Next session
1. `git pull`, `git status`, `pytest -q --tb=short`
2. No-template task: write ONE new validator test from a blank line, for a case from the NOT tested list, red first, no copying an existing tuple. Predict the exception and message first
3. Fix the comment, add `ids=`, commit each separately
4. Then Pydantic (replaces hand-written validation)
