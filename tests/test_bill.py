import unittest
from unittest.mock import patch
from io import StringIO
import sys

from lotto import bill
from lotto.bill import Bill

bill.random.seed(10)


class TestBill(unittest.TestCase):
    @patch("builtins.input")
    def test_choose_bet_type(self, mock_inputs):
        mock_inputs.side_effect = ["2", "amb", "help", "ambo"]
        actual = Bill.choose_bet_type()
        expected = "ambo"
        self.assertEqual(actual, expected, "Expected the method return 'ambo'.")

    @patch("builtins.input")
    def test_choose_numbers(self, mock_inputs):
        mock_inputs.side_effect = ["ambo", "1", "help", "2"]
        actual = Bill.choose_numbers("ambo")
        expected = 2
        self.assertEqual(actual, expected, "Expected the method return 2.")

    @patch("builtins.input")
    def test_choose_city(self, mock_inputs):
        mock_inputs.side_effect = ["2", "help", "romaa", "roma"]
        actual = Bill.choose_city()
        expected = "Roma"
        self.assertEqual(actual, expected, "Expected the method return 'Roma'.")

    @patch("builtins.input")
    def test_choose_amount(self, mock_inputs):
        mock_inputs.side_effect = ["0", "1"]
        actual = Bill.choose_amount()
        expected = 1
        self.assertEqual(actual, expected, "Expected the method return 1.")

    def test_is_a_valid_amount_return_true(self):
        amounts_to_test = [1, 50, 200]
        for a in amounts_to_test:
            result = Bill.is_a_valid_amount(a)
            self.assertTrue(result, f"Expected {a} to be a valid amount, so the method shoud return True.")

    def test_is_a_valid_amount_return_false(self):
        amounts_to_test = [0, 1.5, 201]
        for a in amounts_to_test:
            result = Bill.is_a_valid_amount(a)
            self.assertFalse(result, f"Expected that {a} is not a valid amount, so the method shoud return False.")

    def test_generate_numbers(self):
        new_bill = Bill("terno", 5, "Firenze", 1)
        actual = new_bill.generated_numbers
        expected = [2, 5, 55, 62, 74]
        self.assertEqual(actual, expected, "Expected the method return [2, 27, 55, 62, 74].")

    def test_print_bill(self):
        new_bill = Bill("ambo", 2, "Roma", 1)
        actual = str(new_bill)
        numbers = new_bill.generated_numbers
        expected = "+------------------------------+\n|         Lotto Ticket         |\n+------------------------------+\n|  CITY       |      Roma      |\n|  BET TYPE   |      ambo      |\n+------------------------------+\n|{:^6}{:^6}                  |\n|                              |\n+------------------------------+\n".format(numbers[0], numbers[1])                  
        self.assertEqual(actual, expected, "Expected a different representation of the bill.")
