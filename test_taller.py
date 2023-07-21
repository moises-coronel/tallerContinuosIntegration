import unittest
from taller import Meal, DiningExperienceManager

class TestDiningExperienceManager(unittest.TestCase):

    def setUp(self):
        self.manager = DiningExperienceManager()

    def test_validate_quantity_valid(self):
        valid_quantity = "5"
        result = self.manager.validate_quantity(valid_quantity)
        self.assertEqual(result, 5)

    def test_validate_quantity_invalid_string(self):
        invalid_quantity = "abc"
        result = self.manager.validate_quantity(invalid_quantity)
        self.assertIsNone(result)

    def test_validate_quantity_invalid_negative(self):
        invalid_quantity = "-2"
        result = self.manager.validate_quantity(invalid_quantity)
        self.assertIsNone(result)

    def test_validate_quantity_invalid_zero(self):
        invalid_quantity = "0"
        result = self.manager.validate_quantity(invalid_quantity)
        self.assertIsNone(result)

    def test_validate_quantity_invalid_over_100(self):
        invalid_quantity = "101"
        result = self.manager.validate_quantity(invalid_quantity)
        self.assertIsNone(result)

    def test_calculate_total_cost_no_selections(self):
        selections = {}
        result = self.manager.calculate_total_cost(selections)
        self.assertEqual(result, 0)

    def test_calculate_total_cost_no_special(self):
        selections = {0: 2, 1: 3, 2: 1}
        result = self.manager.calculate_total_cost(selections)
        expected_cost = 2*8 + 3*10 + 1*4
        self.assertEqual(result, expected_cost)

    def test_calculate_total_cost_with_special(self):
        selections = {0: 2, 1: 3, 2: 1}
        self.manager.menu[0].is_special = True
        self.manager.menu[1].is_special = True
        result = self.manager.calculate_total_cost(selections)
        expected_cost = 2*8 - 2*8*0.05 + 3*10 - 3*10*0.05 + 1*4
        self.assertEqual(result, expected_cost)

    def test_calculate_total_cost_discount_5_percent(self):
        selections = {0: 6}
        self.manager.menu[0].is_special = True
        result = self.manager.calculate_total_cost(selections)
        expected_cost = 6*8 - 6*8*0.05
        self.assertEqual(result, expected_cost)

    def test_calculate_total_cost_discount_10_percent(self):
        selections = {0: 11}
        self.manager.menu[0].is_special = True
        result = self.manager.calculate_total_cost(selections)
        expected_cost = 11*8 - 11*8*0.05
        self.assertEqual(result, expected_cost)

    def test_calculate_total_cost_special_offer_discount_10(self):
        selections = {1: 6}
        result = self.manager.calculate_total_cost(selections)
        expected_cost = 6*10 - 10
        self.assertEqual(result, expected_cost)

    def test_calculate_total_cost_special_offer_discount_25(self):
        selections = {1: 11}
        result = self.manager.calculate_total_cost(selections)
        expected_cost = 11*10 - 25
        self.assertEqual(result, expected_cost)

if __name__ == '__main__':
    unittest.main()
