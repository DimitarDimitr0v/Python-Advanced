from ss.animal import Animal


class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def __repr__(self):
        return f"This is {self.name}." \
               f" {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

    @staticmethod
    def make_sound():
        return "Woof!"