class Equipment:
    ID_START = 0

    def __init__(self, name):
        self.name = name
        self.id = Equipment.get_next_id()

    @staticmethod
    def get_next_id():
        Equipment.ID_START += 1
        return Equipment.ID_START

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

