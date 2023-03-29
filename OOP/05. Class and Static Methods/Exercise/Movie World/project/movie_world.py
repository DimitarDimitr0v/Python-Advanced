from typing import List
from ss.dvd import DVD
from ss.customer import Customer


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.dvds: List[DVD] = []
        self.customers: List[Customer] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10


    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)


    def get_customer_and_dvd(self, customer_id, dvd_id):
        # Get the customer and dvd by their id and save them in a variables
        try:
            customer = [c for c in self.customers if c.id == customer_id][0]
            dvd = [d for d in self.dvds if d.id == dvd_id][0]
        except IndexError:
            pass

        return customer, dvd


    def rent_dvd(self, customer_id, dvd_id):
        customer, dvd = MovieWorld.get_customer_and_dvd(self, customer_id, dvd_id)

        # If customer has already rented the DVD
        for x in customer.rented_dvds:
            if x.id == dvd.id:
                return f"{customer.name} has already rented {dvd.name}"


        # If the DVD is rented by someone else
        for c in self.customers:
            for d in c.rented_dvds:
                if d.id == dvd_id:
                    if d.is_rented:
                        return f"DVD is already rented"


        # If the DVD is available, check for age restriction
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        else:
            customer.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{customer.name} has successfully rented {dvd.name}"


    def return_dvd(self, customer_id, dvd_id):
        customer, dvd = MovieWorld.get_customer_and_dvd(self, customer_id, dvd_id)

        for v in customer.rented_dvds:
            if v.id == dvd_id:
                dvd.is_rented = False
                customer.rented_dvds.remove(v)
                return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = '\n'.join([x.__repr__() for x in self.customers])
        result += '\n'
        result += '\n'.join(
            [dv.__repr__() for el in self.customers
             if len(el.rented_dvds) > 0 for dv in el.rented_dvds])

        return result
