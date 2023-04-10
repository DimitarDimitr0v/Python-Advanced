from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver("Ivan", 100)

    def test_initialization(self):
        self.assertEqual("Ivan", self.driver.name)
        self.assertEqual(100, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)


    def test_earned_money_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -10

        self.assertEqual(f"Ivan went bankrupt.", str(ve.exception))


    def test_earned_money_setter_success(self):
        result = self.driver.earned_money = 100
        self.assertEqual(100, result)


    def test_add_cargo_offer_already_added_exception(self):
        self.driver.available_cargos = {"Madrid": 4000}

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Madrid", 4000)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))



    def test_add_cargo_offer_success(self):
        result = self.driver.add_cargo_offer("Madrid", 4000)
        self.assertEqual({"Madrid": 4000}, self.driver.available_cargos)
        self.assertEqual("Cargo for 4000 to Madrid was added as an offer.", result)


    def test_drive_best_cargo_offer_return_value_error(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)


    def test_drive_best_cargo_offer_success(self):
        self.driver.available_cargos = {"Madrid": 4000, "Italy": 2000}
        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(398_500, self.driver.earned_money)
        self.assertEqual(4000, self.driver.miles)
        self.assertEqual("Ivan is driving 4000 to Madrid.", result)



    def test_check_for_activities(self):
        self.driver.earned_money = 10_000
        self.driver.check_for_activities(250)
        self.assertEqual(9980, self.driver.earned_money)


    def test_eat(self):
        self.driver.earned_money = 1000
        self.driver.eat(4000)
        self.assertEqual(980, self.driver.earned_money)


    def test_sleep(self):
        self.driver.earned_money = 1000
        self.driver.sleep(4000)
        self.assertEqual(955, self.driver.earned_money)


    def test_pump_gas(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(1500)
        self.assertEqual(500, self.driver.earned_money)


    def test_repair_truck(self):
        self.driver.earned_money = 10_000
        self.driver.repair_truck(10_000)
        self.assertEqual(2_500, self.driver.earned_money)


    def test_repr(self):
        obj = TruckDriver('Alice', 30)
        expected_repr = 'Alice has 0 miles behind his back.'
        self.assertEqual(repr(obj), expected_repr)


if __name__ == '__main':
    main()
