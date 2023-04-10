from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []


    @staticmethod
    def name_already_added(target, place_to_look_for):
        for el in place_to_look_for:
            if el.name == target:
                return True
        return False


    @staticmethod
    def band_members_role_check(band_name):
        singer = False
        drummer = False
        guitarist = False

        for member in band_name.members:
            if isinstance(member, Singer):
                singer = True
            elif isinstance(member, Drummer):
                drummer = True
            elif isinstance(member, Guitarist):
                guitarist = True


        if singer and guitarist and drummer:
            return True
        else:
            return False


    @staticmethod
    def band_members_skills_check(concert_name, band_name):

        singer = [x for x in band_name.members if type(x).__name__ == "Singer"][0]
        drummer = [x for x in band_name.members if type(x).__name__ == "Drummer"][0]
        guitarist = [x for x in band_name.members if type(x).__name__ == "Guitarist"][0]

        if concert_name.genre == "Rock":
            if "sing high pitch notes" in singer.skills:
                if "play the drums with drumsticks" in drummer.skills:
                    if "play rock" in guitarist.skills:
                        return True

            return False

        if concert_name.genre == "Metal":
            if "sing low pitch notes" in singer.skills:
                if "play the drums with drumsticks" in drummer.skills:
                    if "play metal" in guitarist.skills:
                        return True

            return False

        if concert_name.genre == "Jazz":
            if "sing high pitch notes and sing low pitch notes" in singer.skills:
                if "play the drums with drum brushes" in drummer.skills:
                    if "play jazz" in guitarist.skills:
                        return True

            return False


    def create_musician(self, musician_type: str, name: str, age: int):
        musician_types = [Drummer, Singer, Guitarist]

        for current_instance in musician_types:

            if musician_type in globals() and isinstance(globals()[musician_type](name, age), current_instance):

                if self.name_already_added(name, self.musicians):
                    raise Exception(f"{name} is already a musician!")

                new_musician = current_instance(name, age)
                self.musicians.append(new_musician)
                return f"{name} is now a {musician_type}."

        raise ValueError("Invalid musician type!")




    def create_band(self, name: str):
        if self.name_already_added(name, self.bands):
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."




    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):

        for curr_concert in self.concerts:
            if curr_concert.place == place:
                raise Exception(f"{place} is already registered for {curr_concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."





    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            band_to_add = [x for x in self.bands if x.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician_to_add = [x for x in self.musicians if x.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a musician!")

        band_to_add.members.append(musician_to_add)
        return f"{musician_name} was added to {band_name}."





    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band_to_remove_from = [x for x in self.bands if x.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician_to_remove = [x for x in self.musicians if x.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band_to_remove_from.members.remove(musician_to_remove)
        return f"{musician_name} was removed from {band_name}."




    def start_concert(self, concert_place: str, band_name: str):

        band = [x for x in self.bands if x.name == band_name][0]
        concert = [x for x in self.concerts if x.place == concert_place][0]

        if not self.band_members_role_check(band):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if not self.band_members_skills_check(concert, band):
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

