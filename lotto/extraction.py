import random
from datetime import datetime

from lotto.city import City
from lotto.bill import Bill
from lotto.bet_type import BetType
from lotto.printer import Printer


class Extraction:
    """Manages the lotto extraction phase.
    
    :var numbers_to_draw_by_city: indicates how many numbers must be drawn for each city, defaults to 5
    :type numbers_to_draw_by_city: int
    """
    numbers_to_draw_by_city = 5

    def __init__(self):
        """Constructor method.
        
        :ivar self.extraction: contains a lotto extraction
        :type self.extraction: dict
        :ivar self.date: contains the date on which the extraction was made
        :type self.date: datetime
        
        """
        self.extraction = Extraction.new_extraction()
        self.date = datetime.now()

    @staticmethod
    def new_extraction() -> dict:
        """Takes care of creating a new extraction, generating 5 random numbers for each city.
        
        :return: a dict where the key is the city and the value is a list of numbers drawn for that city
        """
        lotto_extraction = {}

        for city in City.cities:
            extracted_numbers = set()
            while len(extracted_numbers) < Extraction.numbers_to_draw_by_city:
                extracted_numbers.add(random.randint(Bill.min_random_number, Bill.max_random_number))
            lotto_extraction[city] = list(extracted_numbers)

        return lotto_extraction
    
    def __str__(self) -> str:
        extraction_date = self.date.strftime("%d/%m/%y, %H:%M")
        extraction_table = Printer.extraction_table(self.extraction)
        representation = f"Extraction of {extraction_date}\n{extraction_table}"
        return representation


def is_a_winning_bill(bill: Bill, extraction: Extraction) -> bool:
    """Compare a bill to an extraction and see if the bill is a winner.
    
    :param extraction: an object of type Extraction, represents the reference extraction to carry out the check
    :param bill: an object of type Bill, represents the bill that is checked to see if it is successful
    :return: True if the bill wins, False otherwise
    """
    extracted_numbers = extraction.extraction[bill.city]
    numbers_to_guess = BetType.available_bet_type[bill.bet_type]
    guessed_numbers = 0
    i = 0
    
    while not guessed_numbers == numbers_to_guess and i < len(bill.generated_numbers):
        number_to_check = bill.generated_numbers[i]
        if number_to_check in extracted_numbers:
            guessed_numbers += 1
        i += 1

    return guessed_numbers >= numbers_to_guess
