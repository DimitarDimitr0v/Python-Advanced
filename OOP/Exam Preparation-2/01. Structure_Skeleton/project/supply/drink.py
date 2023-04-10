from project.supply.supply import Supply


class Drink(Supply):
    def __init__(self, name: str):
        self.name = name
        self.energy = 15



