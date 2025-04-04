"""File to define Bear class."""


class Bear:

    hunger_score: int
    age: int

    def __init__(self):
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        return None

    def eat(self, num_fish: int):
        self.hunger_score = +num_fish
        return None
