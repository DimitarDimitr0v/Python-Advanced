from project.animal.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

    def food_that_eats(self):
        return [Vegetable, Fruit]

    def gain_weight(self):
        return 0.10


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

    def food_that_eats(self):
        return [Meat]

    def gain_weight(self):
        return 0.40


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    def food_that_eats(self):
        return [Vegetable, Meat]

    def gain_weight(self):
        return 0.30


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def food_that_eats(self):
        return [Meat]

    def gain_weight(self):
        return 1.00
