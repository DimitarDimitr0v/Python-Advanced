from unittest import TestCase, main
from project.hero import Hero


class HeroTest(TestCase):

    def setUp(self):
        self.hero = Hero("Titan", 10, 100, 10)
        self.opponent = Hero("Danger", 10, 100, 10)

    def test_initialization(self):
        self.assertEqual("Titan", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_attacking_himself_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_fighting_without_health(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.opponent)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_fighting_opponent_who_do_not_have_health(self):
        self.opponent.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.opponent)

        self.assertEqual(f"You cannot fight Danger. He needs to rest", str(ve.exception))

    def test_battle_both_opponents_have_zero_health(self):
        result = self.hero.battle(self.opponent)
        self.assertEqual("Draw", result, "This also tests calculation of damage and removing it")

    def test_battle_enemy_hero_lose(self):
        self.hero = Hero("Titan", 100, 1000, 100)
        self.opponent = Hero("Danger", 10, 10, 10)
        result_of_the_battle = self.hero.battle(self.opponent)

        self.assertEqual("You win", result_of_the_battle)
        self.assertEqual(101, self.hero.level)
        self.assertEqual(905, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_battle_enemy_hero_win(self):
        self.hero = Hero("Titan", 10, 10, 10)
        self.opponent = Hero("Danger", 100, 1000, 100)
        result_of_the_battle = self.hero.battle(self.opponent)

        self.assertEqual("You lose", result_of_the_battle)
        self.assertEqual(101, self.opponent.level)
        self.assertEqual(905, self.opponent.health)
        self.assertEqual(105, self.opponent.damage)

    def test_str_representation(self):
        result = self.hero.__str__()
        self.assertEqual("Hero Titan: 10 lvl\nHealth: 100\nDamage: 10\n", result)


if __name__ == '__main__':
    main()