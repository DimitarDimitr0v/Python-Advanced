from project.supply.drink import Drink
from project.supply.food import Food


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []


    def add_player(self, *args):
        currently_added_players_names = []

        for player in args:
            if player not in self.players:
                self.players.append(player)
                currently_added_players_names.append(player.name)

        return f"Successfully added: {', '.join(currently_added_players_names)}"



    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

        self.supplies = self.supplies[::-1]



    def sustain(self, player_name: str, sustenance_type: str):

        try:
            player = [x for x in self.players if x.name == player_name][0]
        except IndexError:
            # If the player doesn't exist, ignore the command
            return


        if sustenance_type == "Food":
            try:
                supply = [x for x in self.supplies if x.__class__.__name__ == "Food"][0]
            except IndexError:
                raise Exception("There are no food supplies left!")


        elif sustenance_type == "Drink":
            try:
                supply = [x for x in self.supplies if x.__class__.__name__ == "Drink"][0]
            except IndexError:
                raise Exception("There are no drink supplies left!")


        else:        # This case means that the sustenance type is invalid, and we ignore the command
            return



        if not player.need_sustenance:
            self.supplies.append(supply)
            return f"{player_name} have enough stamina."



        if player.stamina + supply.energy <= 100:
            player.stamina += supply.energy

        elif player.stamina + supply.energy > 100:
            player.stamina = 100

        self.supplies.remove(supply)
        return f"{player_name} sustained successfully with {supply.name}."




    def duel(self, first_player_name: str, second_player_name: str):
        first_player = [x for x in self.players if x.name == first_player_name][0]
        second_player = [x for x in self.players if x.name == second_player_name][0]

        if first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\n" \
                   f"Player {second_player_name} does not have enough stamina."

        if first_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        if second_player.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."


        for _ in range(2):
            players = [first_player, second_player]

            first_attacker = first_player if first_player.stamina < second_player.stamina else second_player
            players.remove(first_attacker)

            attacker = first_attacker
            being_attacked = players[0]

            attacker_dmg = attacker.stamina / 2
            being_attacked.stamina -= attacker_dmg

            attacker.update_need_sustenance()
            being_attacked.update_need_sustenance()

            if being_attacked.stamina <= 0:
                being_attacked.stamina = 0
                winner = attacker
                return f"Winner {winner.name}"

            if being_attacked.stamina > attacker.stamina:
                return f"Winner: {being_attacked.name}"

        return f"Winner: {attacker.name}"

    def next_day(self):

        # reducing player's stamina
        for player in self.players:
            if player.stamina - player.age * 2 >= 0:
                player.stamina -= player.age * 2
            else:
                player.stamina = 0

        # sustaining players
        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ""

        for p in self.players:
            result += f"Player: {p.name}, {p.age}, {p.stamina}, {p.need_sustenance}\n"

        for s in self.supplies[::-1]:
            result += f"{s.__class__.__name__}: {s.name}, {s.energy}\n"

        return result
