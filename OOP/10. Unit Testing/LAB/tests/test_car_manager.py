from unittest import TestCase, main
from project.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Nissan", "GT-R", 15, 75)

    def test_correct_initialising(self):
        self.assertEqual('Nissan', self.car.make)
        self.assertEqual('GT-R', self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(75, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = None
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_correct(self):
        self.assertEqual('Nissan', self.car.make)

    def test_model_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = None
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_correct(self):
        self.assertEqual("GT-R", self.car.model)

    def test_fuel_consumption_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_correct(self):
        self.assertEqual(15, self.car.fuel_consumption)

    def test_fuel_capacity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_correct(self):
        self.assertEqual(75, self.car.fuel_capacity)

    def test_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -10
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount_correct(self):
        self.assertEqual(0, self.car.fuel_amount)

    def test_refuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_add_fuel_to_fuel_amount(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_add_overloading_fuel_amount(self):
        self.car.refuel(10_000)
        self.assertEqual(self.car.fuel_capacity, self.car.fuel_amount)

    def test_drive_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(500)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_decreasing_fuel_amount(self):
        self.car.fuel_amount = 100
        self.car.drive(100)
        self.assertEqual(85, self.car.fuel_amount)


if __name__ == "__main__":
    main()
