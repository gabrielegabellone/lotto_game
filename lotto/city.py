class City:
    """It deals with the cities available in the game.
    
    :param cities: list of avaible cities, defaults to ["Bari", "Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia", "Tutte"]
    :type cities: list
    """
    cities = ["Bari", "Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia", "Tutte"]

    @staticmethod
    def is_a_valid_city(city: str) -> bool:
        """Check that a city is available in the game.
        
        :param city: string containing the name of a city
        :type city: str
        :return: `True` if the city is avaible, `False` otherwise
        :rtype: str
        """
        if city in City.cities:
            return True
        return False
