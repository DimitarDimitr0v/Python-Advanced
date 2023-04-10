from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    def __init__(self, name: str, kind: str, price: float):

        static_weight = 7
        super().__init__(name, kind, price, static_weight)
        self.weight = static_weight


    def eating(self):
        self.weight += 1
