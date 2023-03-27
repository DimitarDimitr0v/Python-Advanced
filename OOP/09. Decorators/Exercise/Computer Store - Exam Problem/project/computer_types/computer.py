from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")

        self.__model = value


    @property
    @abstractmethod
    def available_processors(self):
        ...

    @property
    @abstractmethod
    def max_ram_range(self):
        ...


    @property
    @abstractmethod
    def machine_type(self):
        ...

    def calculate_processor_price(self, processor):
        dict_with_processors = self.available_processors
        machine_type = self.machine_type

        for curr_processor in dict_with_processors:
            if curr_processor == processor:
                return dict_with_processors[curr_processor]

        if machine_type == "Laptop":
            raise ValueError(f"{ processor } is not compatible with laptop "
                             f"{ self.manufacturer } { self.model }!")

        elif machine_type == "DesktopComputer":
            raise ValueError(f"{ processor } is not compatible with desktop computer "
                             f"{ self.manufacturer } { self.model }!")


    def calculate_ram_price(self, ram_in_gb):
        range_limit = self.max_ram_range
        machine_type = self.machine_type

        for i in range(1, range_limit):
            if 2 ** i == ram_in_gb:
                return i * 100

        if machine_type == "Laptop":
            raise ValueError(f"{ ram_in_gb }GB RAM is not compatible with laptop "
                             f"{ self.manufacturer } { self.model }!")

        elif machine_type == "DesktopComputer":
            raise ValueError(f"{ram_in_gb}GB RAM is not compatible with desktop computer"
                             f" {self.manufacturer} {self.model}!")



    def configure_computer(self, new_processor: str, new_ram: int):

        processor_price = self.calculate_processor_price(new_processor)
        ram_price = self.calculate_ram_price(new_ram)
        computer_price = processor_price + ram_price + self.price

        self.processor = new_processor
        self.ram = new_ram
        self.price = computer_price

        return f"Created {self.manufacturer} {self.model}" \
               f" with {self.processor} and {self.ram}GB RAM for {computer_price}$."


    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

