import unittest
# import sys
# import os

# sys.path.insert(1, os.getcwd())    

from lotto.bet_type import BetType


class TestBetType(unittest.TestCase):
    def test_is_a_valid_type(self):
        valid_type = ["ambata", "ambo", "terno", "quaterna", "cinquina"]
        for value in valid_type:
            actual = BetType.is_a_valid_type(value)
            expected = True
            self.assertEqual(actual, expected, "Expected the method to return True.")
        actual = BetType.is_a_valid_type("estratto determinato")
        expected = False
        self.assertEqual(actual, expected, "Expected the method to return False.")

    def test_is_a_valid_bet(self):
        actual = BetType.is_a_valid_bet("quaterna", 4)
        expected = True
        self.assertEqual(actual, expected, "Expected the method to return True.")
        actual = BetType.is_a_valid_bet("quaterna", 3)
        expected = False
        self.assertEqual(actual, expected, "Expected the method to return False.")


if __name__ == "__main__":
    unittest.main()
