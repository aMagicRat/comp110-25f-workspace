"""main river simulation file"""

from exercises.ex06.bear import Bear
from exercises.ex06.fish import Fish

__author__= "730859678"


class River:
    """A class representing the river that contains fish and bears."""


    def __init__(self, num_fish: int, num_bears: int) -> None:
        """Initialize a river with a given number of fish and bears."""
        self.day = 0
        self.fish = [Fish() for _ in range(num_fish)]
        self.bears = [Bear() for _ in range(num_bears)]


    def view_river(self) -> None:
        """Display the current number of fish and bears in the river."""
        print(f"Day {self.day}: {len(self.fish)} fish, {len(self.bears)} bears")


    def check_ages(self) -> None:
        """Remove old fish and bears that exceed their lifespan."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]


    def one_river_day(self) -> None:
        """Simulate one day in the river."""
        for fish in self.fish:
            fish.one_day()
        for bear in self.bears:
            bear.one_day()
        self.day += 1
        self.check_ages()


    def repopulate_fish(self) -> None:
        """Repopulate the river with new fish."""
        new_fish = (len(self.fish) // 2) * 4
        for _ in range(new_fish):
            self.fish.append(Fish())


    def repopulate_bears(self) -> None:
        """Repopulate the river with new bears."""
        new_bears = len(self.bears) // 2
        for _ in range(new_bears):
            self.bears.append(Bear())


    def one_river_week(self) -> None:
        """Simulate seven days in the river."""
        for _ in range(7):
            self.one_river_day()