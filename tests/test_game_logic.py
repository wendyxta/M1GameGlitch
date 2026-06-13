from logic_utils import check_guess

def test_winning_guess():
    assert check_guess(50, 50)[0] == "Win"


def test_guess_too_high():
    assert check_guess(60, 50)[0] == "Too High"


def test_guess_too_low():
    assert check_guess(40, 50)[0] == "Too Low"


# Test cases to test bug: backwards hints — when guess is too high the hint should say LOWER,
# and when guess is too low the hint should say HIGHER.

def test_too_high_hint_says_lower():
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_hint_says_higher():
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
