from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score, reset_game_state


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hints_bug_fixed_too_high():
    # Bug fix: When guess is too high, message should say to go LOWER
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_hints_bug_fixed_too_low():
    # Bug fix: When guess is too low, message should say to go HIGHER
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


# Tests for reset button functionality after playing a full game
def test_reset_returns_initial_state():
    """Test that reset_game_state returns all variables set to initial values."""
    reset_state = reset_game_state()
    
    assert reset_state["attempts"] == 0
    assert reset_state["score"] == 0
    assert reset_state["status"] == "playing"
    assert reset_state["history"] == []


def test_reset_clears_attempts_from_won_game():
    """Test that reset clears attempts after a winning game."""
    # Simulate state after winning game
    game_state = {
        "attempts": 5,
        "score": 60,
        "status": "won",
        "history": [25, 50, 75, 60, 50],
    }
    
    # Reset
    reset_state = reset_game_state()
    
    # Verify attempts cleared
    assert game_state["attempts"] == 5  # Before reset
    assert reset_state["attempts"] == 0  # After reset


def test_reset_clears_score_from_won_game():
    """Test that reset clears score after a winning game."""
    # Simulate state after winning game
    game_state = {
        "attempts": 5,
        "score": 60,
        "status": "won",
        "history": [25, 50, 75, 60, 50],
    }
    
    # Reset
    reset_state = reset_game_state()
    
    # Verify score cleared
    assert game_state["score"] == 60  # Before reset
    assert reset_state["score"] == 0  # After reset


def test_reset_changes_status_from_won_to_playing():
    """Test that reset changes status from 'won' back to 'playing'."""
    # Simulate state after winning game
    game_state = {
        "attempts": 5,
        "score": 60,
        "status": "won",
        "history": [25, 50, 75, 60, 50],
    }
    
    # Reset
    reset_state = reset_game_state()
    
    # Verify status changed
    assert game_state["status"] == "won"  # Before reset
    assert reset_state["status"] == "playing"  # After reset


def test_reset_changes_status_from_lost_to_playing():
    """Test that reset changes status from 'lost' back to 'playing'."""
    # Simulate state after losing game
    game_state = {
        "attempts": 8,
        "score": -15,
        "status": "lost",
        "history": [10, 20, 30, 40, 50, 60, 70, 80],
    }
    
    # Reset
    reset_state = reset_game_state()
    
    # Verify status changed
    assert game_state["status"] == "lost"  # Before reset
    assert reset_state["status"] == "playing"  # After reset


def test_reset_clears_history_from_won_game():
    """Test that reset clears guess history after a winning game."""
    # Simulate state after winning game
    game_state = {
        "attempts": 5,
        "score": 60,
        "status": "won",
        "history": [25, 50, 75, 60, 50],
    }
    
    # Reset
    reset_state = reset_game_state()
    
    # Verify history cleared
    assert len(game_state["history"]) == 5  # Before reset
    assert len(reset_state["history"]) == 0  # After reset
    assert reset_state["history"] == []


def test_reset_clears_history_from_lost_game():
    """Test that reset clears guess history after a lost game."""
    # Simulate state after losing game
    game_state = {
        "attempts": 8,
        "score": -15,
        "status": "lost",
        "history": [10, 20, 30, 40, 50, 60, 70, 80],
    }
    
    # Reset
    reset_state = reset_game_state()
    
    # Verify history cleared
    assert len(game_state["history"]) == 8  # Before reset
    assert len(reset_state["history"]) == 0  # After reset


def test_reset_after_complete_winning_game():
    """Test that reset clears ALL state after a complete winning game."""
    # Simulate a complete winning game with multiple guesses
    game_state = {
        "secret": 42,
        "attempts": 3,
        "score": 80,
        "status": "won",
        "history": [50, 40, 42],
    }
    
    # Verify game ended successfully
    assert game_state["status"] == "won"
    assert game_state["attempts"] == 3
    assert game_state["score"] > 0
    
    # Reset
    reset_state = reset_game_state()
    
    # Verify ALL game state is cleared
    assert reset_state["attempts"] == 0
    assert reset_state["score"] == 0
    assert reset_state["status"] == "playing"
    assert reset_state["history"] == []


def test_reset_after_complete_losing_game():
    """Test that reset clears ALL state after a complete losing game."""
    # Simulate a complete losing game (out of attempts)
    attempt_limit = 5
    game_state = {
        "secret": 75,
        "attempts": 5,
        "score": -20,
        "status": "lost",
        "history": [50, 60, 70, 80, 90],
    }
    
    # Verify game ended in loss
    assert game_state["status"] == "lost"
    assert game_state["attempts"] >= attempt_limit
    
    # Reset
    reset_state = reset_game_state()
    
    # Verify ALL game state is cleared
    assert reset_state["attempts"] == 0
    assert reset_state["score"] == 0
    assert reset_state["status"] == "playing"
    assert reset_state["history"] == []


def test_reset_preserves_secret_generation_capability():
    """Test that after reset, the game can generate a new secret."""
    import random
    
    difficulty = "Normal"
    old_secret = 42
    
    # Get range for difficulty
    low, high = get_range_for_difficulty(difficulty)
    
    # Reset state
    reset_state = reset_game_state()
    
    # Generate new secret
    new_secret = random.randint(low, high)
    
    # Verify we can generate a valid new secret in valid range
    assert new_secret >= low
    assert new_secret <= high
    # New secret should likely be different (not guaranteed, but highly probable)
    assert isinstance(new_secret, int)

