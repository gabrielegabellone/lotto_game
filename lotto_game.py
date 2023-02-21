from lotto.bill import Bill


def enter_bill_number() -> int:
    """Allows the user to enter the number of bills.
    
    :return: the number of bills chosen by the user
    :rtype: int
    """
    input_validity = False
    while not input_validity:
        try:
            bill_number = int(input("\n>> Enter the number of bills you want to generate: "))
            if is_valid_input(bill_number):
                input_validity = True
            else:
                print("Invalid input! The number of bills must be between 1 and 5 (or 0 to exit).")
        except ValueError:
            print("Invalid input! Enter a numeric value.")
    return bill_number


def is_valid_input(entered_number: int) -> bool:
    """Check that the input is valid.
    
    :param entered_number: the number of bills entered by the user
    :type entered_number: int
    :return: `True` if the number is between 0 and 5, `False` otherwise
    :rtype: bool
    """
    min_number_bills = 1
    max_number_bills = 5    
    return min_number_bills <= entered_number <= max_number_bills or entered_number == 0


def start_new_game(bill_number: int) -> None:
    """Starts a new game session, by generating bills.
    
    :param bill_number: the number of bills chosen by the user
    :type bill_number: int
    """
    bills_generated = []
    if bill_number == 0:
        quit()
    print()

    for bill in range(bill_number):
        bet_type = Bill.choose_bet_type()
        numbers = Bill.choose_numbers(bet_type)
        city = Bill.choose_city()
        bills_generated.append(Bill(bet_type, numbers, city))
        print("Bill no. {} successfully generated!\n".format(bill+1)) 


if __name__ == "__main__":
        bill_to_generate = enter_bill_number()
        start_new_game(bill_to_generate)
