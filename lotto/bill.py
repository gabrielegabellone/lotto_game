import random

from lotto.bet_type import BetType
from lotto.city import City
from lotto.printer import Printer


class Bill:
    """Represents a lottery bill.
    
    :param max_numbers_per_bill: the maximum amount of random numbers that can be generated for each bill, defaults to 10
    :param min_random_number: the smallest random number that can be generated, defaults to 1
    :param max_random_number: the largest random number that can be generated, defaults to 90
    :param min_amount_allowed: the minimum amount in euros allowed for a bill, defaults to 1
    :param max_amount_allowed: the maximum amount in euros allowed for a bill, defaults to 200
    """
    max_numbers_per_bill = 10
    min_random_number = 1
    max_random_number = 90
    min_amount_allowed = 1
    max_amount_allowed = 200
    
    def __init__(self, bet_type: str, numbers_to_generate: int, city: str, bet_amount: int) -> None:
        """Constructor method.
        
        :param bet_type: the type of bet chosen
        :param numbers_to_generate: the amount of numbers to generate in a bill
        :param city: city on you have bet
        :param bet_amount: amount of money for the bet
        :param self.generated_numbers: list containing randomly generated numbers
        """
        self.bet_type = bet_type
        self.numbers_to_generate = numbers_to_generate
        self.city = city
        self.generated_numbers = Bill.generate_numbers(self)
        self.bet_amount = bet_amount

    @staticmethod
    def choose_bet_type() -> str:
        """Asks the user to enter the type of bet.
        
        :return: the bet-type chosen by the user
        """
        entered_bet_type = input(">> Choose the type of bet: ").lower().strip()

        while not BetType.is_a_valid_type(entered_bet_type):
            if entered_bet_type == "help":
                print(Printer.list_table(sorted(BetType.available_bet_type.keys())))
            else:
                print(f"Error! '{entered_bet_type}' is not an allowed type of bet.")
            entered_bet_type = input(">> Choose a valid bet type (or enter 'help' to see the types of bets available): ").lower().strip()

        return entered_bet_type

    @staticmethod
    def choose_numbers(bet_type: str) -> int:
        """Asks the user to enter how many numbers to generate.

        :param bet_type: the bet-type chosen by the user
        :return: the number chosen by the user
        """
        is_a_valid_number = False

        while not is_a_valid_number:
            try:
                entered_number = int(input(">> How many numbers you want to generate? "))
                if BetType.is_a_valid_bet(bet_type, entered_number):
                    is_a_valid_number = True
                else:
                    print(f"Error! For an '{bet_type}' bet, at least {BetType.available_bet_type[bet_type]} numbers must be generated.")
            except ValueError:
                print("Error! Enter a numeric value.")

        return entered_number

    @staticmethod
    def choose_city() -> str:
        """Asks the user to enter which city he wants to play on.

        :return: the city chosen by the user
        """
        entered_city = input(">> Enter the city: ").capitalize().strip()

        while not City.is_a_valid_city(entered_city):
            if entered_city.lower() == "help":
                print(Printer.list_table(City.cities))
            else:
                print(f"Error! '{entered_city}' is not an available city.")
            entered_city = input(">> Enter a valid city (or enter 'help' to see the available cities): ").capitalize().strip()
        
        return entered_city

    @staticmethod
    def choose_amount() -> int:
        """Asks the user to enter the amount in money.

        :return: the amount in money choosen by the user
        """
        is_a_valid_amount = False
        error_message = f"Error! Enter a valid amount, a valid amount must be between €{Bill.min_amount_allowed} and €{Bill.max_amount_allowed}."
        
        while not is_a_valid_amount:
            try:
                entered_amount = int(input(">> Enter amount of money for this bet: "))
                is_a_valid_amount = Bill.is_a_valid_amount(entered_amount)
            except ValueError:
                print(error_message)
                continue
            if not is_a_valid_amount:
                print(error_message)
        
        return entered_amount
    
    @staticmethod
    def is_a_valid_amount(amount: int) -> bool:
        """Check that an amount is between the minimum and the maximum allowed, if yes, it is a valid amount.
        
        :param amount: the amount of money to check
        :return: `True` if the amount is valid, `False` otherwise
        """
        min_amount = Bill.min_amount_allowed
        max_amount = Bill.max_amount_allowed

        return amount in range(min_amount, max_amount+1)            
                
    def generate_numbers(self) -> list:
        """Returns a list of randomly generated numbers.
        
        :return: list of random numbers
        """
        gen_num = set()

        while len(gen_num) < self.numbers_to_generate:
            gen_num.add(random.randint(Bill.min_random_number, Bill.max_random_number))
    
        return sorted(list(gen_num))

    def __str__(self) -> str:
        """
        :returns: a string containing a representation of a bill
        """
        return Printer.bill_representation(self.bet_type, self.generated_numbers, self.city)
