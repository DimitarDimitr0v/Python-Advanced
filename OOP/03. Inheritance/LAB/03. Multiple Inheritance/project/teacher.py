from ss.person import Person
from ss.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
