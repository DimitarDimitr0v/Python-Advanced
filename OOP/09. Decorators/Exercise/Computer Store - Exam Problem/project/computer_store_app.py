from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []  # store the built computers
        self.profits = 0  # represents the store profit

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: int, ram: int):
        if type_computer == "Laptop":
            new_laptop = Laptop(manufacturer, model)
            self.warehouse.append(new_laptop)

            return new_laptop.configure_computer(processor, ram)

        elif type_computer == "Desktop Computer":
            new_pc = DesktopComputer(manufacturer, model)
            self.warehouse.append(new_pc)

            return new_pc.configure_computer(processor, ram)

        raise ValueError(F"{ type_computer } is not a valid type computer!")


    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):

        for pc in self.warehouse:
            if pc.price <= client_budget:
                if pc.processor == wanted_processor:
                    if pc.ram >= wanted_ram:
                        profit = client_budget - pc.price
                        self.profits += profit
                        self.warehouse.remove(pc)
                        return f"{ pc.__repr__() } sold for { client_budget }$."

        raise Exception(f"Sorry, we don't have a computer for you.")
