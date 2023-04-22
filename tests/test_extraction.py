import unittest

from lotto import extraction
from lotto.extraction import Extraction, is_a_winning_bill
from lotto.city import City
from lotto.bill import Bill

extraction.random.seed(10)

class TestExtraction(unittest.TestCase):
    def setUp(self):
        self.extraction = Extraction()
        self.extraction.extraction = {"Bari": [36, 5, 84, 21, 63], "Cagliari": [32, 67, 10, 42, 63], "Firenze": [6, 78, 47, 18, 54],
                               "Genova": [37, 46, 49, 54, 87], "Milano": [34, 39, 23, 88, 59], "Napoli": [47, 18, 85, 59, 31], 
                               "Palermo": [6, 75, 79, 49, 57], "Roma": [1, 39, 18, 25, 31], "Torino": [69, 41, 47, 86, 31],
                               "Venezia": [71, 9, 56, 58, 61]}
    
    def test_new_extraction(self):
        new_extraction = Extraction.new_extraction()
        numbers_for_cities = 5
        cities = City.cities[:]
        cities.remove("Tutte") # When performing an extraction, the "Tutte" wheel should not be considered
        for city in cities:
            self.assertIn(city, new_extraction.keys(), "Expected that the city is contained in the extraction.")
        for extraction in new_extraction.values():
            extraction_withuout_duplicates = set(extraction)
            self.assertEqual(len(extraction), len(extraction_withuout_duplicates), "Expected that the list does not contain duplicate elements.")
            self.assertEqual(len(extraction), numbers_for_cities, "The list is expected to consist of 5 elements.")
            for number in extraction:
                self.assertTrue(number in range(Bill.min_random_number, Bill.max_random_number+1), "Number outside the expected range.")
    
    def test_extraction_representation(self):
        extraction_date = self.extraction.date.strftime("%d/%m/%y, %H:%M")
        expected = f"Extraction of {extraction_date}\n+----------+------------------------------+\n|   Bari   |  36    5     84    21    63  |\n\
| Cagliari |  32    67    10    42    63  |\n| Firenze  |  6     78    47    18    54  |\n|  Genova  |  37    46    49    54    87  |\n\
|  Milano  |  34    39    23    88    59  |\n|  Napoli  |  47    18    85    59    31  |\n| Palermo  |  6     75    79    49    57  |\n\
|   Roma   |  1     39    18    25    31  |\n|  Torino  |  69    41    47    86    31  |\n| Venezia  |  71    9     56    58    61  |\n\
+----------+------------------------------+"
        self.assertEqual(str(self.extraction), expected)


    def test_is_a_winning_bill_return_true(self):
        new_bill = Bill("ambo", 5, "Roma", 1)
        new_bill.generated_numbers = [1, 9, 10, 26, 39]
        self.assertTrue(is_a_winning_bill(new_bill, self.extraction), "Expected method to return True.")
        new_bill = Bill("ambata", 3, "Roma", 1)
        new_bill.generated_numbers = [7, 18, 25]
        self.assertTrue(is_a_winning_bill(new_bill, self.extraction), "Expected method to return True.")
        new_bill = Bill("terno", 5, "Napoli", 1)
        new_bill.generated_numbers = [18, 22, 27, 47, 85]
        self.assertTrue(is_a_winning_bill(new_bill, self.extraction), "Expected method to return True.")
        new_bill = Bill("quaterna", 7, "Torino", 1)
        new_bill.generated_numbers = [8, 9, 12, 41, 47, 69, 86]
        self.assertTrue(is_a_winning_bill(new_bill, self.extraction), "Expected method to return True.")
        new_bill = Bill("cinquina", 10, "Firenze", 1)
        new_bill.generated_numbers = [6, 11, 15, 18, 47, 54, 76, 78, 82, 83]
        self.assertTrue(is_a_winning_bill(new_bill, self.extraction), "Expected method to return True.")

    def test_is_a_winning_bill_return_false(self):
        new_bill = Bill("ambo", 5, "Roma", 1)
        new_bill.generated_numbers = [8, 10, 11, 12, 13]
        self.assertFalse(is_a_winning_bill(new_bill, self.extraction), "Expected method to return False.")
        new_bill = Bill("ambata", 3, "Roma", 1)
        new_bill.generated_numbers = [6, 11, 12]
        self.assertFalse(is_a_winning_bill(new_bill, self.extraction), "Expected method to return False.")
        new_bill = Bill("terno", 5, "Napoli", 1)
        new_bill.generated_numbers = [23, 24, 52, 53, 70]
        self.assertFalse(is_a_winning_bill(new_bill, self.extraction), "Expected method to return False.")
        new_bill = Bill("quaterna", 7, "Torino", 1)
        new_bill.generated_numbers = [10, 11, 17, 21, 22, 70, 71]
        self.assertFalse(is_a_winning_bill(new_bill, self.extraction), "Expected method to return False.")
        new_bill = Bill("cinquina", 7, "Firenze", 1)
        new_bill.generated_numbers = [8, 10, 11, 12, 20, 60, 61, 72, 82]
        self.assertFalse(is_a_winning_bill(new_bill, self.extraction), "Expected method to return False.")
    
    def test_count_guessed_numbers(self):
        new_bill = Bill("ambo", 5, "Bari", 1)
        new_bill.generated_numbers = [5, 36, 62, 70, 80]
        actual = self.extraction.count_guessed_numbers(new_bill)
        expected = 2
        self.assertEqual(actual, expected, "Expected method to return 2.")
        new_bill = Bill("ambo", 5, "Bari", 1)
        new_bill.generated_numbers = [4, 35, 62, 70, 80]
        actual = self.extraction.count_guessed_numbers(new_bill)
        expected = 0
        self.assertEqual(actual, expected, "Expected method to return 0.")

    def test_wheel_tutte(self):
        actual = {1, 5, 6, 9, 10, 18, 21, 23, 25, 31, 32, 34, 36, 37, 39, 41, 42, 46, 47, 49, 54, 56, 57, 58, 59, 61, 63, 67, 69, 71, 75, 78, 79, 84, 85, 86, 87, 88}
        expected = self.extraction.wheel_tutte()
        self.assertEqual(actual, expected, "Expected method to return a set containing the numbers drawn on all wheels.")