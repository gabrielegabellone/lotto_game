import unittest

from lotto.city import City


class TestCity(unittest.TestCase):
    def test_is_a_valid_city_return_true(self):
        value_to_test = ["Bari", "Cagliari", "Firenze"]
        for value in value_to_test:
            test_value = City.is_a_valid_city(value)
            self.assertTrue(test_value, "Expected the method to return True.")
    
    def test_is_a_valid_city_return_false(self):
        value_to_test = ["Bergamo", "bAri", 1, None]
        for value in value_to_test:
            test_value = City.is_a_valid_city(value)
            self.assertFalse(test_value, "Expected the method to return False.")
