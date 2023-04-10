from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    @staticmethod
    def check_if_exists_with_name(name, sequence):
        for item in sequence:
            if item.name == name:
                return True
        return False

    @staticmethod
    def check_if_exists_with_booth_number(number, sequence):
        for item in sequence:
            if item.booth_number == number:
                return True
        return False

    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        if self.check_if_exists_with_name(name, self.delicacies):
            raise Exception(f"{name} already exists!")

        if type_delicacy == "Gingerbread":
            delicacy = Gingerbread(name, price)
        elif type_delicacy == "Stolen":
            delicacy = Stolen(name, price)
        else:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        if self.check_if_exists_with_booth_number(booth_number, self.booths):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth == "Open Booth":
            booth = OpenBooth(booth_number, capacity)
        elif type_booth == "Private Booth":
            booth = PrivateBooth(booth_number, capacity)
        else:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        try:
            available_booth = [x for x in self.booths if x.is_reserved is False and x.capacity >= number_of_people][0]
        except IndexError:
            raise Exception(f"No available booth for {number_of_people} people!")

        available_booth.reserve(number_of_people)
        return f"Booth {available_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):

        if not self.check_if_exists_with_booth_number(booth_number, self.booths):
            raise Exception(f"Could not find booth {booth_number}!")

        if not self.check_if_exists_with_name(delicacy_name, self.delicacies):
            raise Exception(F"No {delicacy_name} in the pastry shop!")

        booth = [x for x in self.booths if x.booth_number == booth_number][0]
        delicacy = [x for x in self.delicacies if x.name == delicacy_name][0]
        # it could be raising errors because I don't remove values from the capacity after adding delicacy

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):

        booth = [x for x in self.booths if x.booth_number == booth_number][0]

        bill = 0

        for order in booth.delicacy_orders:
            bill += order.price

        # freeing the booths
        bill += booth.price_for_reservation

        booth.price_for_reservation = 0
        booth.delicacy_orders = []
        booth.is_reserved = False

        self.income += bill
        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."


    def get_income(self):
        return f"Income: {self.income:.2f}lv."
