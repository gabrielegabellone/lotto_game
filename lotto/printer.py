class Printer:
    """Takes care of the printing operations.
    """

    @staticmethod
    def list_table(elements: list) -> str:
        """Creates a table from a list of strings.

        :param elements: list containing elements to be printed in table form
        :return: string containing the table
        """
        table = ""
        dashed_line = "+----------" * len(elements) + "+\n"
        table += dashed_line
        for e in elements:
            table += "|" + "{:^10}".format(e)
        table += "|\n" + dashed_line
        return table
    
    @staticmethod
    def bill_representation(bet_type: str, numbers: list, city: str) -> str:
        """Creates the representation of the bill.

        :return: a bill represented as an ascii art table
        """
        dashed_line = "+{:-^30}+\n".format("")
        title_line = "|{:^30}|\n".format("Lotto Ticket")
        city_line = "|{:14}{:^16}|\n".format("  CITY       |", city)
        bet_line = "|{:14}{:^16}|\n".format("  BET TYPE   |", bet_type)

        max_numbers_per_bill = 10
        max_num_per_row = 5
        numbers_line = "|"
        for n in range(max_numbers_per_bill):
            if n == max_num_per_row:
                numbers_line += "|\n|"
            if n < len(numbers):
                numbers_line += "{:^6}".format(numbers[n])
            else:
                numbers_line += "      "
        numbers_line += "|\n"
        
        representation = f"{dashed_line}{title_line}{dashed_line}{city_line}{bet_line}{dashed_line}{numbers_line}{dashed_line}"
        return representation

    @staticmethod
    def extraction_table(extraction: dict) -> str:
        """Creates a table representing a lotto extraction.
        
        :param extraction: a dict containing the city as the key and a list of 5 numbers as the value
        :return: extraction represented as a table
        """
        dashed_line = "+{:-^10}+{:-^30}+".format("", "")
        extraction_rows = "\n"

        for city in extraction:
            extraction_rows += "|{:^10}|".format(city)
            for number in extraction[city]:
                extraction_rows += "{:^6}".format(number)
            extraction_rows += "|\n"

        representation = f"{dashed_line}{extraction_rows}{dashed_line}"
        return representation
