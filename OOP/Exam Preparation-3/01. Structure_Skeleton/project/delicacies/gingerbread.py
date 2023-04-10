from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    def __init__(self, name: str, price: float):

        static_portion = 200
        super().__init__(name, static_portion, price)
        self.portion = static_portion


    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."
