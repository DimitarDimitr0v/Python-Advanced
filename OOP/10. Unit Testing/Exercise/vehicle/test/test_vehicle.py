from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 100)

    def test_initialization(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_without_enough_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_success(self):
        self.vehicle.drive(20)
        self.assertEqual(25, self.vehicle.fuel)

    def test_refuel_with_more_then_capacity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(200)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_enough_fuel_success(self):
        self.vehicle.fuel = 20
        self.vehicle.refuel(10)
        self.assertEqual(30, self.vehicle.fuel)


    def test_string_representation(self):
        self.assertEqual(f"The vehicle has 100 horse power with 50 fuel left and 1.25 fuel consumption", self.vehicle.__str__())


if __name__ == '__main__':
    main()
