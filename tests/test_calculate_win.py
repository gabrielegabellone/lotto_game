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
        self.bill = Bill("ambo", 4, "Firenze", 50)
        self.bill.generated_numbers = [6, 18, 47, 78]
        self.win = CalculateWin(self.bill, self.extraction)

    def test_calculate_combinations(self):
        actual = self.win.calculate_combinations()
        expected = 6
        self.assertEqual(actual, expected, "Expected method to return 6.")

    def test_calculate_gross_amount(self):
        actual = self.win.calculate_gross_amount()
        expected = 12498
        self.assertEqual(actual, expected, "Expected method to return 12498.")

    def test_calculate_gross_amount_city_tutte(self):
        new_bill = Bill("ambo", 4, "Tutte", 10)
        win = CalculateWin(new_bill, self.extraction)
        actual = win.calculate_gross_amount()
        expected = 41.66
        self.assertEqual(actual, expected, "Expected method to return 41.66.")

    def test_calculate_net_amount(self):
        actual = self.win.calculate_net_amount()
        expected = 11498.16
        self.assertEqual(actual, expected, "Expected method to return 11498.16.")

    def test_calculate_net_amount_without_tax_retention(self):
        new_bill = Bill("ambo", 5, "Tutte", 10)
        win = CalculateWin(new_bill, self.extraction)
        actual = win.calculate_gross_amount()
        expected = 25.0
        self.assertEqual(actual, expected, "Expected the gross amount to be 25.0.")
        actual = win.calculate_net_amount()
        expected = 25.0
        self.assertEqual(actual, expected, "Expected the net amount to be 25.0.")

    def test_print_win(self):
        actual = str(self.win)
        expected = "Gross amount: € 12498.0\nNet amount: € 11498.16 (-8% tax retention)"
        self.assertEqual(actual, expected, "Expected different representetion.")
