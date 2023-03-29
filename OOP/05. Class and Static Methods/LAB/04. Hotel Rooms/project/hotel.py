from typing import List
from ss.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                Room.take_room(room, people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                Room.free_room(room)

    def status(self):
        free_rooms = [x.number for x in self.rooms if not x.is_taken]
        taken_rooms = [x.number for x in self.rooms if x.is_taken]
        total_guests = sum([x.guests for x in self.rooms])
        return f"Hotel {self.name} has {total_guests} total guests\n" \
               f"Free rooms: {', '.join([str(x) for x in free_rooms])}\n" \
               f"Taken rooms: {', '.join([str(x) for x in taken_rooms])}\n"
