"""RPS-001 real-browser round and replay tests."""

import pytest
from playwright.sync_api import Page, expect

import app as web

pytestmark = pytest.mark.e2e


def test_real_round_and_replay(page: Page, live_server, monkeypatch):
    """A player can see a result and play an independent second round."""
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    page.goto(live_server)

    page.get_by_role("button", name="Rock", exact=True).click()

    choices = page.get_by_label("This round’s choices")
    expect(choices).to_contain_text("Rock")
    expect(choices).to_contain_text("Paper")
    expect(
        page.get_by_role("heading", name="Computer wins", exact=True)
    ).to_be_visible()
    expect(page.locator('[data-outcome="lose"]')).to_have_count(1)

    monkeypatch.setattr(web.random, "choice", lambda _moves: "rock")
    page.get_by_role("button", name="Paper", exact=True).click()

    expect(choices).to_contain_text("Paper")
    expect(choices).to_contain_text("Rock")
    expect(page.get_by_role("heading", name="You win!", exact=True)).to_be_visible()
    expect(page.locator('[data-outcome="win"]')).to_have_count(1)
