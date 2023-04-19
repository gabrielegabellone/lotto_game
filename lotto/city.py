class City:
    """It deals with the cities available in the game.
    
    :param cities: list of available cities, defaults to ["Bari", "Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia", "Tutte"]
    """
    cities = ["Bari", "Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia", "Tutte"]

    @staticmethod
    def is_a_valid_city(city: str) -> bool:
        """Check that a city is available in the game.
        
        :param city: string containing the name of a city
        :return: `True` if the city is available, `False` otherwise
        """
        if city in City.cities:
            return True
        return False
