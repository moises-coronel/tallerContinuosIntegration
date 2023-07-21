import pytest
from taller import Meal, DiningExperienceManager


class TestDiningExperienceManager:

    @pytest.fixture
    def manager(self):
        return DiningExperienceManager()

    def test_validate_quantity_valid_input(self, manager):
        quantity = "5"
        result = manager.validate_quantity(quantity)
        assert result == 5

    def test_validate_quantity_invalid_input(self, manager):
        quantity = "-1"
        result = manager.validate_quantity(quantity)
        assert result is None

    def test_calculate_total_cost_with_discounts(self, manager):
        selections = {0: 5, 1: 6, 2: 7}
        result = manager.calculate_total_cost(selections)
        assert result == 83

    def test_calculate_discount(self, manager):
        selections = {0: 5, 1: 6, 2: 7}
        result = manager.calculate_discount(selections)
        assert result == 17

    def test_calculate_total_cost_special_offer_discount_10(self, manager):
        selections = {0: 5}
        result = manager.calculate_total_cost(selections)
        assert result == 38

    def test_calculate_total_cost_no_special(self, manager):
        selections = {1: 3, 2: 2}
        result = manager.calculate_total_cost(selections)
        assert result == 38

    def test_calculate_total_cost_discount_5_percent(self, manager):
        selections = {0: 6}
        result = manager.calculate_total_cost(selections)
        assert result == 41

    def test_calculate_total_cost_discount_10_percent(self, manager):
        selections = {0: 11}
        result = manager.calculate_total_cost(selections)
        assert result == 50

    def test_calculate_total_cost_discount_20_percent(self, manager):
        selections = {0: 15}
        result = manager.calculate_total_cost(selections)
        assert result == 96

    def test_calculate_total_cost_special_offer_discount_10(self, manager):
        selections = {0: 5}
        result = manager.calculate_total_cost(selections)
        assert result == 38

    def test_calculate_total_cost_special_offer_discount_25(self, manager):
        selections = {0: 9}
        result = manager.calculate_total_cost(selections)
        assert result == 51


