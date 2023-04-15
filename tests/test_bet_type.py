import unittest

from lotto.bet_type import BetType


class TestBetType(unittest.TestCase):
    def test_is_a_valid_type_return_true(self):
        value_to_test = ["ambata", "ambo", "terno", "quaterna", "cinquina"]
        for value in value_to_test:
            test_value = BetType.is_a_valid_type(value)
            self.assertTrue(test_value, "Expected the method to return True.")
    
    def test_is_a_valid_type_return_false(self):
        value_to_test = ["estratto determinato", "amb", 1, True, None]
        for value in value_to_test:
            test_value = BetType.is_a_valid_type(value)
            self.assertFalse(test_value, "Expected the method to return False.")

    def test_is_a_valid_bet_return_true(self):
        values_to_test = [4, 5, 6, 7, 8, 9, 10]
        for value in values_to_test:
            test_value = BetType.is_a_valid_bet("quaterna", value)
            self.assertTrue(test_value, "Expected the method to return True.")

    def test_is_a_valid_bet_return_false(self):
        value_to_test = [3, 4.5, "4", True, None]
        for value in value_to_test:
            test_value = BetType.is_a_valid_bet("quaterna", value)
            self.assertFalse(test_value, "Expected the method to return False.")
