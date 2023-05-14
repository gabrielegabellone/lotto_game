import unittest

from lotto.extraction import Extraction
from lotto.bill import Bill
from lotto.calculate_win import CalculateWin


class TestCalculateWin(unittest.TestCase):
    def setUp(self):
        self.extraction = Extraction()
        self.extraction.extraction = {"Bari": [36, 5, 84, 21, 63], "Cagliari": [32, 67, 10, 42, 63], "Firenze": [6, 78, 47, 18, 54],
                                "Genova": [37, 46, 49, 54, 87], "Milano": [34, 39, 23, 88, 59], "Napoli": [47, 18, 85, 59, 31],
                                "Palermo": [6, 75, 79, 49, 57], "Roma": [1, 39, 18, 25, 31], "Torino": [69, 41, 47, 86, 31],
                                "Venezia": [71, 9, 56, 58, 61], "Tutte": [65, 42, 75, 84, 21]}

        winning_bill = Bill("ambo", 4, "Firenze", 50)
        winning_bill.generated_numbers = [6, 18, 47, 78]
        self.winning_case = CalculateWin(winning_bill, self.extraction)

        non_winning_bill = Bill("ambo", 4, "Firenze", 50)
        non_winning_bill.generated_numbers = [5, 77, 46, 47]
        self.non_winning_case = CalculateWin(non_winning_bill, self.extraction)

    def test_calculate_combinations_winning_bill(self):
        actual = self.winning_case.calculate_combinations()
        expected = 6
        self.assertEqual(actual, expected, "Expected method to return 6.")

    def test_calculate_combinations_non_winning_bill(self):
        actual = self.non_winning_case.calculate_combinations()
        expected = 0
        self.assertEqual(actual, expected, "Expected method to return 0.")

    def test_calculate_gross_amount_winning_bill(self):
        actual = self.winning_case.calculate_gross_amount()
        expected = 12498
        self.assertEqual(actual, expected, "Expected method to return 12498.")

    def test_calculate_gross_amount_non_winning_bill(self):
        actual = self.non_winning_case.calculate_gross_amount()
        expected = 0
        self.assertEqual(actual, expected, "Expected method to return 0.")

    def test_calculate_gross_amount_city_tutte(self):
        new_bill = Bill("ambo", 4, "Tutte", 10)
        new_bill.generated_numbers = [37, 46, 48, 55]
        win = CalculateWin(new_bill, self.extraction)
        actual = win.calculate_gross_amount()
        expected = 41.66
        self.assertEqual(actual, expected, "Expected method to return 41.66.")

    def test_calculate_net_amount_winning_bill(self):
        actual = self.winning_case.calculate_net_amount()
        expected = 11498.16
        self.assertEqual(actual, expected, "Expected method to return 11498.16.")

    def test_calculate_net_amount_non_winning_bill(self):
        actual = self.non_winning_case.calculate_net_amount()
        expected = 0
        self.assertEqual(actual, expected, "Expected method to return 0.")

    def test_calculate_net_amount_without_tax_retention(self):
        new_bill = Bill("ambo", 5, "Tutte", 10)
        new_bill.generated_numbers = [37, 46, 48, 55]
        win = CalculateWin(new_bill, self.extraction)
        actual = win.calculate_gross_amount()
        expected = 25.0
        self.assertEqual(actual, expected, "Expected the gross amount to be 25.0.")
        actual = win.calculate_net_amount()
        expected = 25.0
        self.assertEqual(actual, expected, "Expected the net amount to be 25.0.")

    def test_print_amounts_winning_bill(self):
        actual = str(self.winning_case)
        expected = "Gross amount: € 12498.0\nNet amount: € 11498.16 (-8% tax retention)"
        self.assertEqual(actual, expected, "Expected different representation.")

    def test_print_amounts_non_winning_bill(self):
        actual = str(self.non_winning_case)
        expected = "Gross amount: € 0.0\nNet amount: € 0.0 (-8% tax retention)"
        self.assertEqual(actual, expected, "Expected different representation.")

    def test_cases_not_valid_bill(self):
        # case in which you have a bill with an invalid bet type
        not_valid_bill = Bill("amb", 4, "Firenze", 50)
        with self.assertRaises(KeyError, msg="Expected that if a bill with an invalid bet type is passed, a KeyError "
                                             "will be raised."):
            CalculateWin(not_valid_bill, self.extraction)

        # case of a bill that has few numbers played compared to the type of bet
        not_valid_bill = Bill("ambo", 1, "Firenze", 50)
        with self.assertRaises(IndexError, msg="Expected if a bill that has few numbers played (1) with respect to "
                                               "the type of bet (ambo), an IndexError is raised."):
            CalculateWin(not_valid_bill, self.extraction)

        # case of a bill that has an invalid city
        not_valid_bill = Bill("ambo", 2, "Firenz", 50)
        with self.assertRaises(KeyError, msg="Expected that if a bill that has an invalid city a KeyError is raised."):
            CalculateWin(not_valid_bill, self.extraction)

        # case of a bill that has an invalid amount
        not_valid_bill = Bill("ambo", 2, "Firenze", "50")
        with self.assertRaises(TypeError, msg="Expected that if the amount is not of type int a TypeError is raised."):
            CalculateWin(not_valid_bill, self.extraction)
