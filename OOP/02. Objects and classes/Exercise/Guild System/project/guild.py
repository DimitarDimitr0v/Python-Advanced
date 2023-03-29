from typing import List
from ss.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        if player.guild != Player.PLAYER_NOT_IN_GUILD:
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        """
                On the following line we use [0], because the player who match
                the name will always be either one or none. If there is no
                player found the list will be empty, and it will trow error as we try
                to access index 0(it doesn't exist).
                Also, can be checked with if statement.

                ---
                    if len(list) == 0:
                        return f"he is not in the guild"
                                                        ---
            """
        try:
            player = [p for p in self.players if p.name == player_name][0]
        except IndexError:
            return f"Player {player_name} is not in the guild."

        self.players.remove(player)
        player.guild = Player.PLAYER_NOT_IN_GUILD
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        players_info = '\n'.join([p.player_info() for p in self.players])

        return f"Guild: {self.name}\n" \
               f"{players_info}"


