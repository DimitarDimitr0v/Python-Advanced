from unittest import TestCase, main

from project.cat import Cat


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Gringo")

    def test_cat_size_increase_after_eating(self):
        expected = self.cat.size + 1
        self.cat.eat()
        self.assertEqual(expected, self.cat.size)

    def test_cat_is_fed_after_eating(self):
        expected = True
        self.cat.eat()
        self.assertEqual(expected, self.cat.fed)

    def test_cat_cannot_eat_after_being_fed(self):
        self.cat.eat()

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_cat_cannot_sleep_before_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleep(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)


if __name__ == '__main__':
    main()
