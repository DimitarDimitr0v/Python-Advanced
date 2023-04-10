from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.tennis_player_1 = TennisPlayer("Grigor", 27, 40)
        self.tennis_player_2 = TennisPlayer("Rafael", 29, 50)



    def test_initialization(self):
        self.assertEqual("Grigor", self.tennis_player_1.name)
        self.assertEqual(27, self.tennis_player_1.age)
        self.assertEqual(40, self.tennis_player_1.points)
        self.assertEqual([], self.tennis_player_1.wins)



    def test_name_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player_1.name = "Lu"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))



    def test_name_setter_success(self):
        self.tennis_player_1.name = "Gringo"
        self.assertEqual("Gringo", self.tennis_player_1.name)



    def test_age_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player_1.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))



    def test_age_setter_success(self):
        self.tennis_player_1.age = 19
        self.assertEqual(19, self.tennis_player_1.age)



    def test_add_new_win_tournament_already_added_case(self):
        self.tennis_player_1.wins.append("USOpen")
        result = self.tennis_player_1.add_new_win("USOpen")
        self.assertEqual("USOpen has been already added to the list of wins!", result)



    def test_add_new_win_success(self):
        self.tennis_player_1.add_new_win("USOpen")
        self.assertEqual(["USOpen"], self.tennis_player_1.wins)



    def test_first_player_greater_than_second_player(self):
        # grigor 40
        # rafael 50
        result = self.tennis_player_1 < self.tennis_player_2
        self.assertEqual('Rafael is a top seeded player and he/she is better than Grigor', result)



    def test_second_player_greater_than_first_player(self):

        result = self.tennis_player_2 < self.tennis_player_1
        self.assertEqual(f'Rafael is a better player than Grigor', result)



    def test_dunder_str_empty_tournaments(self):
        result = str(self.tennis_player_1)
        self.assertEqual(f"Tennis Player: Grigor\n"
                         f"Age: 27\n"
                         f"Points: 40.0\n"
                         f"Tournaments won: ", result)


    def test_dunder_str_with_tournaments(self):
        self.tennis_player_1.wins = ["USOpen", "AustraliaOpen"]
        result = str(self.tennis_player_1)
        self.assertEqual(f"Tennis Player: Grigor\n"
                         f"Age: 27\n"
                         f"Points: 40.0\n"
                         f"Tournaments won: USOpen, AustraliaOpen", result)


if __name__ == '__main__':
    main()
