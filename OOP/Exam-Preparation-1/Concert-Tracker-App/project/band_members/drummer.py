from project.band_members.musician import Musician


class Drummer(Musician):
    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def available_skills(self):
        return [
            "play the drums with drumsticks",
            "play the drums with drum brushes",
            "read sheet music",
        ]


# drummer = Drummer("Georgi",  22)
# print(drummer.learn_new_skill("play the drums with drumsticks"))
