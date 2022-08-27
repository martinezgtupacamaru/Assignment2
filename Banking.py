from decimal import Decimal
from Accounts.Accounts import *

saving = Savings(25.00, 25.00, 0.00, 0, 0.00, 0, 0.02, 0.00, True)
checking = Checking(5.00, 5.00, 0.00, 0, 0.00, 0, 0.01, 0.00, True)
D1 = ""
D2 = ""
D3 = ""

while D1 != "Q":
    D1 = input("Bank menu: A: Savings, B: Checking, Q: Exit >")
    if D1 == "A":
        D2 = input("Savings menu: A: Deposit, B: Withdrawal, C: Report, Q: Return to Bank Menu >")
        while D2 != "Q":
            # D2 = input("Savings menu: A: Deposit, B: Withdrawal, C: Report, Q: Return to Bank Menu >")
            if D2 == "A":
                amount = int(input("Please enter the amount you wish to deposit >"))
                saving.deposit(amount)
                print(f"Your Savings account balance is {saving.current_balance}")
            if D2 == "B":
                amount = int(input("Please enter the amount you wish to withdraw >"))
                saving.withdrawal(amount)
                print(f"Your Savings account balance is {saving.current_balance}")
            if D2 == "C":
                # saving.close_month()
                print(f"Your Savings account report is: Starting balance: {saving.start_balance}, Total amount of deposit: {saving.total_deposit}, Total amount of withdrawal: {saving.total_withdrawal}, Service charges: {saving.monthly_service_charge}, Current Balance: {saving.current_balance}, Account Status: {saving.account_status}.")
            # else:
            #     pass
            D2 = input("Savings menu: A: Deposit, B: Withdrawal, C: Report, Q: Return to Bank Menu >")
    if D1 == "B":
        D3 = input("Checking menu: A: Deposit, B: Withdrawal, C: Report, Q: Return to Bank Menu >")
        while D3 != "Q":
            if D3 == "A":
                amount = int(input("Please enter the amount you wish to deposit >"))
                checking.deposit(amount)
                print(f"Your Checking account balance is {checking.current_balance}")
            if D3 == "B":
                amount = int(input("Please enter the amount you wish to withdraw >"))
                checking.withdrawal(amount)
                print(f"Your Checking account balance is {checking.current_balance}")
            if D3 == "C":
                # checking.close_month()
                print(f"Your Checking account report is: Starting balance: {checking.start_balance}, Total amount of deposit: {checking.total_deposit}, Total amount of withdrawal: {checking.total_withdrawal}, Service charges: {checking.monthly_service_charge}, Current Balance: {checking.current_balance}, Account Status: {checking.account_status}.")
            # else:
            #     pass
            D3 = input("Checking menu: A: Deposit, B: Withdrawal, C: Report, Q: Return to Bank Menu >")
    else:
        pass
print("Good bye")


