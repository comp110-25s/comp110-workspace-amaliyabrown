"""File to define River class."""

from fish import Fish
from bear import Bear


class River:

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        new_bear_list: list[Bear] = []
        new_fish_list: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish_list.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                new_bear_list.append(bear)

        self.bears = new_bear_list
        self.fish = new_fish_list

        return None

    def remove_fish(self, amount: int):
        if amount <= len(self.fish):
            idx: int = 0
            while idx < amount:
                self.fish.pop(0)
                idx += 1
        else:
            self.fish = []

        return None

    def bears_eating(self):
        if len(self.fish) >= 5:
            for bear in self.bears:
                bear.eat(3)
                self.remove_fish(3)

        return None

    def check_hunger(self):
        new_bear_list: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score > 0:
                new_bear_list.append(bear)

        self.bears = new_bear_list

        return None

    def repopulate_fish(self):
        idx: int = 0
        baby_fish: int = len(self.fish) // 2
        while idx < baby_fish:
            self.fish.append(Fish())
            idx += 1
        return None

    def repopulate_bears(self):
        idx: int = 0
        baby_bears: int = len(self.bears) // 2
        while idx < baby_bears:
            self.bears.append(Bear())
            idx += 1

        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.age += 1
            bear.hunger_score -= 1
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.age += 1
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        days = 0
        while days < 7:
            self.one_river_day()
            days += 1
