from ss.elf import Elf


class MuseElf(Elf):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)
