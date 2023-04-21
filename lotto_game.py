from lotto.input_bill_number import InputBillNumber
from lotto.bill import Bill
from lotto.extraction import Extraction, is_a_winning_bill
from lotto.calculate_win import CalculateWin


def start_new_game(bill_number: int) -> None:
    """Starts a new game session, by generating bills.
    Subsequently, an extraction is performed and it is checked whether each of the bills generated is successful, 
    if it is, the bill is printed.
    
    :param bill_number: the number of bills chosen by the user
    """
    bills_generated = []
    if bill_number == 0:
        quit()
    print()

    for bill in range(bill_number):
        bet_type = Bill.choose_bet_type()
        numbers = Bill.choose_numbers(bet_type)
        city = Bill.choose_city()
        bet_amount = Bill.choose_amount()
        bills_generated.append(Bill(bet_type, numbers, city, bet_amount))
        print("Bill no. {} successfully generated!\n".format(bill+1))

    extraction = Extraction()
    print(extraction)

    for b in range(bill_number):
        if is_a_winning_bill(bills_generated[b], extraction):
            print(f"\nBill no. {b+1}: won!\n{bills_generated[b]}")
            win = CalculateWin(bills_generated[b], extraction)
            print(win)
        else:
            print(f"\nBill no. {b+1}: not won.")


if __name__ == "__main__":
    bill_to_generate = InputBillNumber.enter_bill_number()
    start_new_game(bill_to_generate)
