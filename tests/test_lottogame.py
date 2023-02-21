import unittest
from unittest.mock import patch
# import sys
# import os

# sys.path.insert(1, os.getcwd())

from lotto_game import enter_bill_number, is_valid_input


class TestLottoGame(unittest.TestCase):
    @patch("builtins.input")
    def test_enter_bill_number(self, mock_inputs):
        mock_inputs.side_effect = [5]
        actual = enter_bill_number()
        expected = 5
        self.assertEqual(actual, expected, "Expected the function to return 5.")
    
    def test_is_valid_input(self):
        valid_input = [0, 1, 2, 3, 4, 5]
        for value in valid_input:
            actual = is_valid_input(value)
            expected = True
            self.assertEqual(actual, expected, "Expected the function to return True.")
        actual = is_valid_input(6)
        expected = False
        self.assertEqual(actual, expected, "Expected the function to return False.")


if __name__ == "__main__":
    unittest.main()
