class Player:

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.__need_sustenance = False


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name not valid!")
        self.__name = value


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value


    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value


    @property
    def need_sustenance(self):
        return self.__need_sustenance

    def update_need_sustenance(self):
        if self.stamina < 100:
            self.__need_sustenance = True


    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"


