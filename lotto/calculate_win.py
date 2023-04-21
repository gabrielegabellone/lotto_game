from itertools import combinations

from lotto.bill import Bill
from lotto.bet_type import BetType
from lotto.extraction import Extraction

class CalculateWin:
    """Contains information and manages the calculations of a lottery win.

    :param gross_winnings: dict which contains the gross amount of Lotto winnings obtained by betting €1 on a single wheel, the key indicates the amount of bills played, and the value a list containing the winning amount for each type of bet 
    :param bet_type_indexes: dict where the key is the type of bet and the value is an integer that represents the reference index to obtain the amount in the values of the variable gross_winnings
    :param max_amount: represents the maximum amount beyond which a tax retention is applied, defaults to 500
    :param tax_retention: represents the percentage of tax retention, defaults to 8
    """
    gross_winnings = {1: [11.23],
                      2: [5.61, 250],
                      3: [3.74, 83.33, 4500],
                      4: [2.8, 41.66, 1125, 120000],
                      5: [2.24, 25, 450, 24000, 6000000],
                      6: [1.87, 16.66, 225, 8000, 1000000],
                      7: [1.6, 11.9, 128.57, 3428.57, 285714.28],
                      8: [1.4, 8.92, 80.35, 1714.28, 107142.85],
                      9: [1.24, 6.94, 53.57, 952.38, 47619.04],
                      10: [1.12, 5.55, 37.5, 571.42, 23809.52]}
    bet_type_indexes = {"ambata": 0, "ambo": 1, "terno": 2, "quaterna": 3, "cinquina": 4}
    max_amount = 500
    tax_retention = 8

    def __init__(self, bill: Bill, extraction: Extraction):
        """Constructor Method.
        
        :param bill: represents the winning bill
        :param extraction: represents the reference extraction
        :param self.guessed_numbers: represents the numbers guessed in total
        :param self.combinations: represents all guessed combinations
        :param self.gross_amount: represents the gross amount of the winnings
        :param self.net_amount: represents the net amount of the winnings without tax retention
        """
        self.bill = bill
        self.extraction = extraction
        self.guessed_numbers = extraction.count_guessed_numbers(bill)
        self.combinations = self.calculate_combinations()
        self.gross_amount = self.calculate_gross_amount()
        self.net_amount = self.calculate_net_amount()

    def calculate_combinations(self) -> int:
        """Takes care of calculating all combinations in a win.
        
        :return: the number of total combinations guessed
        """
        numbers_by_combination = BetType.available_bet_type[self.bill.bet_type]
        numbers_played = self.guessed_numbers
        total_combinations = len(list(combinations(range(numbers_played), numbers_by_combination)))
        return total_combinations
    
    def calculate_gross_amount(self) -> float:
        """Takes care of making calculations for the gross amount of the winnings.
        
        :return: the gross amount
        """
        combinations = self.combinations
        bet_type = self.bill.bet_type
        numbers_played = self.bill.numbers_to_generate
        bet_amount = self.bill.bet_amount
        i = CalculateWin.bet_type_indexes[bet_type]

        unit_amount = CalculateWin.gross_winnings[numbers_played][i]
        total_amount = unit_amount * bet_amount * combinations

        return total_amount
    
    def calculate_net_amount(self) -> float:
        """Takes care of making calculations for the net amount of the winnings.
        Tax retention is deducted only if the gross amount is greater than 500.

        :return: the net amount or the gross amount itself if it is less than or equal to 500
        """
        tax_retention = CalculateWin.tax_retention / 100
        gross_amount = self.gross_amount
        
        if gross_amount > CalculateWin.max_amount:
            net_amount = gross_amount - (gross_amount * tax_retention)
            return net_amount
        return gross_amount
    
    def __str__(self) -> str:
        representation = f"Gross amount: € {self.gross_amount}\nNet amount: € {self.net_amount} (-{CalculateWin.tax_retention}% tax retention)"
        return representation
