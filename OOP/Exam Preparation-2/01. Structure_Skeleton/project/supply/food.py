from project.supply.supply import Supply


class Food(Supply):

    def __init__(self, name: str, energy=25):
        self.name = name
        self.energy = energy
