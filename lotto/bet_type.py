class BetType:
    """It deals with the types of bets available in the game.
    
    :param available_bet_type: dict whose keys indicate an available bet-type, while the values indicate the minimum number of numbers that must be generated for that specific type
    """
    available_bet_type = {"ambata": 1, "ambo": 2, "terno": 3, "quaterna": 4, "cinquina": 5}

    @staticmethod
    def is_a_valid_type(bet_type: str) -> bool:
        """Check that a bet-type is available in the game.
        
        :param bet_type: string containing a type of bet
        :return: `True` if the bet-type is available, `False` otherwise
        """
        if bet_type in BetType.available_bet_type.keys():
            return True
        return False

    @staticmethod
    def is_a_valid_bet(bet_type: str, num: int) -> bool:
        """Check that it is possible to generate a bet by comparing the bet-type with the numbers to be generated.
        
        :param bet_type: string containing a type of bet
        :param num: number to compare with the bet type
        :return: `True` if the bet is valid, `False` otherwise
        """
        min_numbers_to_generate = BetType.available_bet_type[bet_type]
        max_numbers_to_generate = 10

        if num in range(min_numbers_to_generate, max_numbers_to_generate+1):
            return True
        return False
