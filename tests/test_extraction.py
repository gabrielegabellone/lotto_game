import unittest
from datetime import datetime

from lotto import extraction
from lotto.extraction import Extraction, is_a_winning_bill
from lotto.city import City
from lotto.bill import Bill

extraction.random.seed(10)
City.cities = ["Bari", "Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia", "Tutte"]
Bill.min_random_number, Bill.max_random_number = 1, 90

class Test_Extraction(unittest.TestCase):
    def setUp(self):
        self.extraction = Extraction()
    
    def test_extraction_and_date(self):
        expected_extraction = {"Bari": [36, 5, 84, 21, 63], "Cagliari": [32, 67, 10, 42, 63], "Firenze": [6, 78, 47, 18, 54],
                               "Genova": [37, 46, 49, 54, 87], "Milano": [34, 39, 23, 88, 59], "Napoli": [47, 18, 85, 59, 31], 
                               "Palermo": [6, 75, 79, 49, 57], "Roma": [1, 39, 18, 25, 31], "Torino": [69, 41, 47, 86, 31],
                               "Tutte": [65, 42, 75, 84, 21], "Venezia": [71, 9, 56, 58, 61]}
        self.assertEqual(self.extraction.extraction, expected_extraction, "Expected a different extraction.")
        self.assertEqual(self.extraction.date.day, datetime.now().day, "Expected a different day.")
        self.assertEqual(self.extraction.date.month, datetime.now().month, "Expected a different month.")
        self.assertEqual(self.extraction.date.year, datetime.now().year, "Expected a different year.")
        self.assertEqual(self.extraction.date.hour, datetime.now().hour, "Expected a different hour.")
        self.assertEqual(self.extraction.date.minute, datetime.now().minute, "Expected a different minute.")


    def test_new_extraction(self):
        new_extraction = Extraction.new_extraction()
        numbers_for_cities = 5
        for city in City.cities:
            self.assertIn(city, new_extraction.keys(), "Expected that the city is contained in the extraction.")
        for extraction in new_extraction.values():
            extraction_withuout_duplicates = set(extraction)
            self.assertEqual(len(extraction), len(extraction_withuout_duplicates), "Expected that the list does not contain duplicate elements.")
            self.assertEqual(len(extraction), numbers_for_cities, "The list is expected to consist of 5 elements.")
            for number in extraction:
                self.assertTrue(number in range(Bill.min_random_number, Bill.max_random_number), "Number outside the expected range.")
    
    def test_extraction_representation(self):
        extraction_date = self.extraction.date.strftime("%d/%m/%y, %H:%M")
        expected = f"Extraction of {extraction_date}\n+----------+------------------------------+\n|   Bari   |  64    5     53    29    31  |\n\
| Cagliari |  69    39    10    78    85  |\n| Firenze  |  73    11    48    50    20  |\n|  Genova  |  13    77    15    20    57  |\n\
|  Milano  |  45    22    54    56    25  |\n|  Napoli  |  32    36    19    88    58  |\n| Palermo  |  67    35    80    16    23  |\n\
|   Roma   |  39    84    85    22    59  |\n|  Torino  |  42    45    23    56    62  |\n| Venezia  |  1     70    6     43    29  |\n\
|  Tutte   |  32    34    41    11    58  |\n+----------+------------------------------+"
        self.assertEqual(str(self.extraction), expected)


    def test_is_a_winning_bill_return_true(self):
        new_bill = Bill("ambo", 5, "Roma")
        new_bill.generated_numbers = [7, 9, 10, 26, 53]
        self.assertTrue(is_a_winning_bill(new_bill, self.extraction), "Expected method to return True.")
        new_bill = Bill("ambata", 3, "Roma")
        new_bill.generated_numbers = [7, 49, 53]
        self.assertTrue(is_a_winning_bill(new_bill, self.extraction), "Expected method to return True.")
        new_bill = Bill("terno", 5, "Napoli")
        new_bill.generated_numbers = [21, 22, 27, 35, 47]
        self.assertTrue(is_a_winning_bill(new_bill, self.extraction), "Expected method to return True.")
        new_bill = Bill("quaterna", 7, "Torino")
        new_bill.generated_numbers = [8, 9, 12, 20, 45, 55, 80]
        self.assertTrue(is_a_winning_bill(new_bill, self.extraction), "Expected method to return True.")
        new_bill = Bill("cinquina", 10, "Firenze")
        new_bill.generated_numbers = [9, 11, 15, 24, 25, 55, 76, 81, 82, 83]
        self.assertTrue(is_a_winning_bill(new_bill, self.extraction), "Expected method to return True.")

    def test_is_a_winning_bill_return_false(self):
        new_bill = Bill("ambo", 5, "Roma")
        new_bill.generated_numbers = [8, 10, 11, 12, 13]
        self.assertFalse(is_a_winning_bill(new_bill, self.extraction), "Expected method to return False.")
        new_bill = Bill("ambata", 3, "Roma")
        new_bill.generated_numbers = [6, 11, 12]
        self.assertFalse(is_a_winning_bill(new_bill, self.extraction), "Expected method to return False.")
        new_bill = Bill("terno", 5, "Napoli")
        new_bill.generated_numbers = [23, 24, 52, 53, 70]
        self.assertFalse(is_a_winning_bill(new_bill, self.extraction), "Expected method to return False.")
        new_bill = Bill("quaterna", 7, "Torino")
        new_bill.generated_numbers = [10, 11, 17, 21, 22, 70, 71]
        self.assertFalse(is_a_winning_bill(new_bill, self.extraction), "Expected method to return False.")
        new_bill = Bill("cinquina", 7, "Firenze")
        new_bill.generated_numbers = [8, 10, 11, 12, 20, 60, 61, 72, 82]
        self.assertFalse(is_a_winning_bill(new_bill, self.extraction), "Expected method to return False.")
    