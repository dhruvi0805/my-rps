"""RPS-001 unit and integration tests."""

import pytest

import app as web
from game import determine_winner


@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
@pytest.mark.unit
def test_determine_winner_returns_expected_result(player, computer, expected):
    """Each literal matchup returns the player's expected result."""
    assert determine_winner(player, computer) == expected


@pytest.fixture(name="client")
def fixture_client():
    """Create a test client for real Flask requests."""
    web.app.config.update(TESTING=True)
    return web.app.test_client()


@pytest.mark.integration
def test_submitted_round_uses_real_rules_and_displays_result(client, monkeypatch):
    """A submitted round uses the real rule function and response mapping."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")

    response = client.post("/", data={"move": "rock"})

    page = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "Rock" in page and "Paper" in page
    assert "Computer wins" in page
    assert 'data-outcome="lose"' in page
