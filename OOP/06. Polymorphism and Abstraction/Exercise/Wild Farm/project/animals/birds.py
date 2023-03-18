from project.animal.animal import Bird
from project.food import Meat, Fruit, Seed, Vegetable


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def food_that_eats(self):
        return [Meat]

    def gain_weight(self):
        return 0.25


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Cluck"

    def food_that_eats(self):
        return [Meat, Fruit, Vegetable, Seed]

    def gain_weight(self):
        return 0.35

