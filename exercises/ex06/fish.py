"""File to define Fish class."""
__author__= """730859678"""

class Fish:
    """A class representing a fish in the river simulation."""


    def __init__(self) -> None:
        """Initialize a new fish with age 0."""
        self.age = 0


    def one_day(self) -> None:
        """Simulate one day passing for the fish."""
        self.age += 1