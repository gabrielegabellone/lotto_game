import unittest
# import sys
# import os

# sys.path.insert(1, os.getcwd())

from lotto.city import City


class TestCity(unittest.TestCase):
    def test_is_a_valid_city(self):
        actual = City.is_a_valid_city("Bari")
        expected = True
        self.assertEqual(actual, expected, "Expected the method to return True.")
        actual = City.is_a_valid_city("Bergamo")
        expected = False
        self.assertEqual(actual, expected, "Expected the method to return False.")


if __name__ == "__main__":
    unittest.main()
