import random

from lotto.bet_type import BetType
from lotto.city import City
from lotto.printer import Printer

class Bill():
    """Represents a lottery bill.
    
    :param max_numbers_per_bill: the maximum amount of random numbers that can be generated for each bill, defaults to 10
    :type max_numbers_per_bill: int
    :param min_random_number: the smallest random number that can be generated, defaults to 1
    :type min_random_number: int
    :param max_random_number: the largest random number that can be generated, defaults to 90
    :type max_random_number: int
    """
    max_numbers_per_bill = 10
    min_random_number = 1
    max_random_number = 90
    
    def __init__(self, bet_type: str, numbers_to_generate: int, city: str) -> None:
        """Constructor method.
        
        :param bet_type: the type of bet chosen
        :type bet_type: str
        :param numbers_to_generate: the amount of numbers to generate in a bill
        :type numbers_to_generate: int
        :param city: city on you have bet
        :type city: str
        :param generated_numbers: list containing randomly generated numbers
        :type generated_numbers: list
        """
        self.bet_type = bet_type
        self.numbers_to_generate = numbers_to_generate
        self.city = city
        self.generated_numbers = Bill.generate_numbers(self)

    def choose_bet_type() -> str:
        """Asks the user to enter the type of bet, returns the bet-type chosen by the user.
        
        :return: a string containing the bet-type
        :rtype: str
        """
        entered_bet_type = input(">> Choose the type of bet: ").lower().strip()
        while not BetType.is_a_valid_type(entered_bet_type):
            if entered_bet_type == "help":
                print(Printer.list_table(BetType.available_bet_type))
            else:
                print("Error! '{}' is not an allowed type of bet.".format(entered_bet_type))
            entered_bet_type = input(">> Choose a valid bet type (or enter 'help' to see the types of bets available): ").lower().strip()
        return entered_bet_type

    def choose_numbers(bet_type) -> int:
        """Asks the user to enter how many numbers to generate, returns the number chosen by the user.

        :param bet_type: the bet-type chosen by the user
        :rtype: str
        :return: the number chosen by the user
        :rtype: int
        """
        is_a_valid_number = False
        while not is_a_valid_number:
            try:
                entered_number = int(input(">> How many numbers you want to generate? "))
                if BetType.is_a_valid_bet(bet_type, entered_number):
                    is_a_valid_number = True
                else:
                    print("Error! For an '{}' bet, at least {} numbers must be generated.".format(bet_type, BetType.min_per_type[bet_type]))
            except ValueError:
                print("Error! Enter a numeric value.")
        return entered_number

    def choose_city() -> str:
        """Asks the user to enter which city he wants to play on, returns the city chosen by the user.

        :return: the city chosen by the user
        :rtype: str
        """
        entered_city = input(">> Enter the city: ").capitalize().strip()
        while not City.is_a_valid_city(entered_city):
            if entered_city.lower() == "help":
                print(Printer.list_table(City.cities))
            else:
                print("Error! '{}' is not an available city.".format(entered_city))
            entered_city = input(">> Enter a valid city (or enter 'help' to see the available cities): ").capitalize().strip()
        return entered_city   
                
    def generate_numbers(self) -> list:
        """Returns a list of randomly generated numbers.
        
        :return: list of random numbers
        :rtype: list
        """
        gen_num = set()
        while len(gen_num) < self.numbers_to_generate:
            gen_num.add(random.randint(Bill.min_random_number, Bill.max_random_number))
        return sorted(list(gen_num))

    def __str__(self) -> str:
        """
        :returns: a string containing a representation of a bill
        :rtype: str
        """
        return Printer.bill_representation(self.bet_type, self.generated_numbers, self.city)
