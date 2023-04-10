from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    def __init__(self, name: str, price: float):

        static_portion = 250
        super().__init__(name, static_portion, price)
        self.portion = static_portion


    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."

