from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Simba", "Lion", "Roar")

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Simba makes Roar", result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual('animals', result)

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual("Simba is of type Lion", result)


if __name__ == '__main__':
    main()
