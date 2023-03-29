from unittest import TestCase, main
from project.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.integer_list = IntegerList('50', 1, False, 3.5, 2, 3)  # 1, 2, 3

    def test_correct_initializing(self):
        self.assertEqual([1, 2, 3], self.integer_list._IntegerList__data)

    def test_correct_get_data(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_with_non_integer_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add('100')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_correct(self):
        result = self.integer_list.add(4)

        self.assertEqual([1, 2, 3, 4], result)
        self.assertEqual(self.integer_list._IntegerList__data, [1, 2, 3, 4])

    def test_remove_index_with_invalid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_with_correct_index(self):
        result = self.integer_list.remove_index(1)

        self.assertNotIn(2, self.integer_list._IntegerList__data)
        self.assertEqual(result, 2)

    def test_get_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_correct(self):
        self.assertEqual(2, self.integer_list.get(1))

    def test_insert_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(5, 66)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1, 'string')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_correct(self):
        self.integer_list.insert(2, 4)
        self.assertEqual([1, 2, 4, 3], self.integer_list._IntegerList__data)

    def test_get_biggest(self):
        result = self.integer_list.get_biggest()
        self.assertEqual(3, result)

    def test_get_index(self):
        result = self.integer_list.get_index(1)
        self.assertEqual(0, result)


if __name__ == "__main__":
    main()
