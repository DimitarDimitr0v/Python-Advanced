class Subscription:
    ID_START = 0

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.get_next_id()

    @staticmethod
    def get_next_id():
        Subscription.ID_START += 1
        return Subscription.ID_START


    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"
