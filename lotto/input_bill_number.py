class InputBillNumber:
    """
    Manages the input operations and input validation of the number of bills at the start of the game.

    :param min_number_bills: the minimum number of bills that can be generated, defaults to 1
    :param max_number_bills: the maximum number of bills that can be generated, defaults to 5
    :param input_to_exit: the value to enter to exit the game, defaults to 0
    """
    min_number_bills = 1
    max_number_bills = 5
    input_to_exit = 0

    @staticmethod
    def enter_bill_number() -> int:
        """Allows the user to enter the number of bills.
        
        :return: the number of bills chosen by the user
        """
        input_validity = False

        while not input_validity:
            try:
                bill_number = int(input("\n>> Enter the number of bills you want to generate: "))
                if InputBillNumber.is_valid_input(bill_number):
                    input_validity = True
                else:
                    print(f"Invalid input! The number of bills must be between {InputBillNumber.min_number_bills} and {InputBillNumber.max_number_bills} (or {InputBillNumber.input_to_exit} to exit).")
            except ValueError:
                print("Invalid input! Enter a numeric value.")
    
        return bill_number

    @staticmethod
    def is_valid_input(entered_number: int) -> bool:
        """Check that the input is valid.
        
        :param entered_number: the number of bills entered by the user
        :return: `True` if the number is between 0 and 5, `False` otherwise
        """
        if entered_number in range(InputBillNumber.min_number_bills, InputBillNumber.max_number_bills+1) or entered_number == InputBillNumber.input_to_exit:
            return True
        return False
