from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def food_that_eats(self):
        pass

    @abstractmethod
    def gain_weight(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    @staticmethod
    @abstractmethod
    def make_sound():
        pass


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}," \
               f" {self.wing_size}, {self.weight}, {self.food_eaten}]"

    def feed(self, food):
        if not type(food) in self.food_that_eats():
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += (self.gain_weight() * food.quantity)
        self.food_eaten += food.quantity


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}," \
               f" {self.weight}, {self.living_region}, {self.food_eaten}]"

    def feed(self, food):
        if not type(food) in self.food_that_eats():
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += (self.gain_weight() * food.quantity)
        self.food_eaten += food.quantity


