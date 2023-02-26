import unittest

from lotto.printer import Printer


class TestPrinter(unittest.TestCase):
    def test_list_table(self):
        list_to_print = ["ambata", "ambo", "terno", "quaterna", "cinquina"]
        actual = Printer.list_table(list_to_print)
        expected = "+----------+----------+----------+----------+----------+\n|  ambata  |   ambo   |  terno   | quaterna | cinquina |\n+----------+----------+----------+----------+----------+\n"
        self.assertEqual(actual, expected, "Expected a different representation of the table.")

    def test_bill_representation(self):
        actual = Printer.bill_representation("ambo", [20, 48], "Roma")
        expected = "+------------------------------+\n|         Lotto Ticket         |\n+------------------------------+\n|  CITY       |      Roma      |\n|  BET TYPE   |      ambo      |\n+------------------------------+\n|  20    48                    |\n|                              |\n+------------------------------+\n"            
        self.assertEqual(actual, expected, "Expected a different representation of the bill.")


if __name__ == "__main__":
    unittest.main()
