from lotto.input_bill_number import InputBillNumber
from lotto.bill import Bill


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
    bill_to_generate = InputBillNumber.enter_bill_number()
    start_new_game(bill_to_generate)
