class Printer():
    """Takes care of the printing operations.
    """

    @staticmethod
    def list_table(elements: list):
        """
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
    def bill_representation(bet_type: str, numbers: list, city: str):
        """
        return: a bill represented as an ascii art table
        rtype: str
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
        
        representation = "{}{}{}{}{}{}{}{}".format(dashed_line, title_line, dashed_line, city_line, bet_line, dashed_line, numbers_line, dashed_line)
        return representation
