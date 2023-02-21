import unittest
from unittest.mock import patch
# import sys
# import os

# sys.path.insert(1, os.getcwd())

from lotto import bill
from lotto.bill import Bill

bill.random.seed(10)


class TestBill(unittest.TestCase):
    @patch("builtins.input")
    def test_choose_bet_type(self, mock_inputs):
        mock_inputs.side_effect = ["ambo"]
        actual = Bill.choose_bet_type()
        expected = "ambo"
        self.assertEqual(actual, expected, "Expected the function return 'ambo'.")

    @patch("builtins.input")
    def test_choose_numbers(self, mock_inputs):
        mock_inputs.side_effect = [2]
        actual = Bill.choose_numbers("ambo")
        expected = 2
        self.assertEqual(actual, expected, "Expected the function return 2.")

    @patch("builtins.input")
    def test_choose_city(self, mock_inputs):
        mock_inputs.side_effect = ["Roma"]
        actual = Bill.choose_city()
        expected = "Roma"
        self.assertEqual(actual, expected, "Expected the function return Roma.")

    def test_generate_numbers(self):
        new_bill = Bill("terno", 5, "Firenze")
        actual = new_bill.generated_numbers
        expected = [2, 5, 55, 62, 74]
        self.assertEqual(actual, expected, "Expected the function return [2, 27, 55, 62, 74].")

    def test_print_bill(self):
        new_bill = Bill("ambo", 2, "Roma")
        actual = str(new_bill)
        numbers = new_bill.generated_numbers
        expected = "+------------------------------+\n|         Lotto Ticket         |\n+------------------------------+\n|  CITY       |      Roma      |\n|  BET TYPE   |      ambo      |\n+------------------------------+\n|{:^6}{:^6}                  |\n|                              |\n+------------------------------+\n".format(numbers[0], numbers[1])                  
        self.assertEqual(actual, expected, "Expected a different representation of the bill.")


if __name__ == "__main__":
    unittest.main()
