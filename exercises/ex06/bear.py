"""File to define Bear class."""

__author__= """730859678"""

class Bear:
    """Bear class representing Bear in River Simulation"""

    def __init__(self) -> None:
        """Initialize a bear with age and hunger score of 0"""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Simulate one day passing for the bear."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Increase hunger score by number of fish eaten."""
        self.hunger_score += num_fish