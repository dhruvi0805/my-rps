# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

 Agreed plan: implement one independent round using the supplied interface and server. `determine_winner(player, computer)` will return `win`, `lose`, or `tie` for lowercase `rock`, `paper`, and `scissors`; the page will display both choices and the result, with no score or saved history. Test all nine literal matchups, including the valid loss `rock` versus `paper` and the valid win `paper` versus `rock`. Reject any player input other than `rock`, `paper`, or `scissors` (for example, `lizard` or an empty value) with the supplied HTTP 400 behavior. Add one real integration round and one real browser round with replay, fixing only the computer choice in tests.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: https://github.com/dhruvi0805/my-rps/issues/1
- Pull request / CI: add actual URLs when they exist.
- Implementation: [game.py](./game.py), [tests/test_game.py](./tests/test_game.py), and [tests/e2e/test_round.py](./tests/e2e/test_round.py) implement and verify RPS-001.
- Checks: Full `.venv/bin/python check.py` passed, including formatting, code analysis, non-browser tests, and Chromium browser checks. Browser observation: player chose Rock, computer chose Scissors, and the page displayed a win; this matches the rules because Rock beats Scissors.
