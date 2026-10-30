"""RPS-001 game rules. See SPEC.md."""


def determine_winner(player: str, computer: str) -> str:
    """Return 'win', 'lose', or 'tie' from the player's perspective.

    Results are from the player's perspective.
    """
    moves = {"rock", "paper", "scissors"}
    if player not in moves or computer not in moves:
        raise ValueError("Moves must be rock, paper, or scissors")
    if player == computer:
        return "tie"

    winning_matchups = {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    }
    return "win" if (player, computer) in winning_matchups else "lose"
