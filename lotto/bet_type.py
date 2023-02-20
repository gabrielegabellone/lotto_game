class BetType():
    """It deals with the types of bets available in the game.
    
    :param available_bet_type: list of types of bets available, defaults to ["ambata", "ambo", "terno", "quaterna", "cinquina"]
    :type available_bet_type: list 
    :param min_per_type: indicates for each bet type the minimum number of numbers to be generated, defaults to {"ambata": 2, "ambo": 2, "terno": 3, "quaterna": 4, "cinquina": 5}
    :type min_per_type: dict
    """
    available_bet_type = ["ambata", "ambo", "terno", "quaterna", "cinquina"]
    min_per_type = {"ambata": 2, "ambo": 2, "terno": 3, "quaterna": 4, "cinquina": 5}

    @staticmethod
    def is_a_valid_type(bet_type: str) -> bool:
        """Check that a bet-type is available in the game.
        
        :param bet: string containing a type of bet
        :type bet: str
        :return: `True` if the bet-type is available, `False` otherwise
        :rtype: bool
        """
        if bet_type in BetType.available_bet_type:
            return True
        return False

    @staticmethod
    def is_a_valid_bet(bet_type: str, num: int) -> bool:
        """Check that it is possible to generate a bet by comparing the bet-type with the numbers to be generated.
        
        :param bet_type: string containing a type of bet
        :type bet_type: str
        :param num: number to compare with the bet type
        :type num: int
        :return: `True` if the bet is valid, `False` otherwise
        :rtype: bool
        """
        minimum = BetType.min_per_type[bet_type]
        maximum = 10
        if minimum <= num <= maximum:
            return True
        return False
