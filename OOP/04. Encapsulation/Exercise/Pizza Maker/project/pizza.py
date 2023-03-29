from ss.topping import Topping
class Pizza:
    def __init__(self, name: str, dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value is not '':
            self.__name = value
        else:
            raise ValueError("The name cannot be an empty string")

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is not None:
            self.__dough = value
        else:
            raise ValueError("You should add dough to the pizza")

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if not value <= 0:
            self.__max_number_of_toppings = value
        else:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")


    def add_topping(self, topping):
        if len(self.toppings) == self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")

        elif topping.topping_type in self.toppings.keys():
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight


    def calculate_total_weight(self):
        total_weight = self.dough.weight
        total_weight += sum([x for x in self.toppings.values()])

        return total_weight
    