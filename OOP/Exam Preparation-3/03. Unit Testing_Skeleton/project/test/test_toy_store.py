from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToYStore(TestCase):
    def setUp(self):
        self.toy_store = ToyStore()

    def test_add_toy_method_exception_shelf_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("H", "papa")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_method_exception_toy_already_in_shelf(self):
        self.toy_store.toy_shelf["A"] = "papa"

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "papa")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_method_exception_shelf_already_taken(self):
        self.toy_store.toy_shelf["A"] = "book"

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "papa")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_method_success(self):
        result = self.toy_store.add_toy("A", "papa")

        self.assertEqual(f"Toy:papa placed successfully!", result)
        self.assertEqual('papa', self.toy_store.toy_shelf["A"])


    def test_remove_toy_method_shelf_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("H", "papa")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_method_toy_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "jonny")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_method_success(self):
        self.toy_store.toy_shelf["A"] = "jonny"
        result = self.toy_store.remove_toy("A", "jonny")

        self.assertEqual("Remove toy:jonny successfully!", result)
        self.assertEqual(None, self.toy_store.toy_shelf["A"])


if __name__ == '__main__':
    main()
