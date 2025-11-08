"""File to define Fish class."""
__author__= """730859678"""

class Fish:
    """Fish class representing Fish in River Simulation"""

    def __init__(self) -> None:
        """Initialize a new fish with age 0"""
        self.age = 0

    def one_day(self) -> None:
        """Simulate one day passing for the fish."""
        self.age += 1
