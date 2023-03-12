class Trainer:
    ID_START = 0

    def __init__(self, name):
        self.name = name
        self.id = Trainer.get_next_id()

    @staticmethod
    def get_next_id():
        Trainer.ID_START += 1
        return Trainer.ID_START

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"