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

    def test_extraction_table(self):
        extraction = {"Bari": [70, 75, 88, 56, 27], "Cagliari": [7, 39, 79, 55, 28], "Firenze": [69, 39, 45, 46, 26],
                      "Genova": [36, 70, 17, 84, 56], "Milano": [65, 33, 76, 44, 59], "Napoli": [75, 12, 55, 28, 31],
                      "Palermo": [32, 68, 13, 88, 28], "Roma": [65, 68, 37, 52, 55], "Torino": [34, 38, 76, 54, 28],
                      "Venezia": [41, 47, 51, 28, 63], "Tutte": [1, 39, 45, 86, 55]}
        actual = Printer.extraction_table(extraction)
        expected = "+----------+------------------------------+\n|   Bari   |  70    75    88    56    27  |\n| Cagliari |  7     39    79    55    28  |\n\
| Firenze  |  69    39    45    46    26  |\n|  Genova  |  36    70    17    84    56  |\n|  Milano  |  65    33    76    44    59  |\n\
|  Napoli  |  75    12    55    28    31  |\n| Palermo  |  32    68    13    88    28  |\n|   Roma   |  65    68    37    52    55  |\n\
|  Torino  |  34    38    76    54    28  |\n| Venezia  |  41    47    51    28    63  |\n|  Tutte   |  1     39    45    86    55  |\n\
+----------+------------------------------+"
        self.assertEqual(actual, expected, "Expected different representation of the extraction.")
        