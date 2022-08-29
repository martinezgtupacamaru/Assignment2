from Accounts.Accounts import *

saving = Savings(Decimal(25.00), Decimal(25.00), Decimal(0.00), Decimal(0), Decimal(0.00), Decimal(0), Decimal(0.02), Decimal(0.00), True)
checking = Checking(Decimal(5.00), Decimal(5.00), Decimal(0.00), Decimal(0), Decimal(0.00), Decimal(0), Decimal(0.01), Decimal(0.00), True)
D1 = ""
D2 = ""
D3 = ""

while D1 != "Q":
    D1 = input("Bank menu: A: Savings, B: Checking, Q: Exit >")
    if D1 == "A":
        D2 = input("Savings menu: A: Deposit, B: Withdrawal, C: Report, Q: Return to Bank Menu >")
        while D2 != "Q":
            if D2 == "A":
                amount = int(input("Please enter the amount you wish to deposit >"))
                saving.deposit(amount)
                print(f"Your Savings account current balance is {saving.current_balance}$")
            if D2 == "B":
                amount = int(input("Please enter the amount you wish to withdraw >"))
                saving.withdrawal(amount)
                print(f"Your Savings account current balance is {saving.current_balance}$")
            if D2 == "C":
                print()
                print('Before the closing of the month:')
                print('Your Savings account report is:')
                print('Starting balance: {:.2f}$'.format(saving.start_balance))
                print('Total amount of deposit: {:.2f}$'.format(saving.total_deposit))
                print('Total amount of withdrawal: {:.2f}$'.format(saving.total_withdrawal))
                print('Service charges: {:.2f}$'.format(saving.monthly_service_charge))
                print('Current balance: {:.2f}$'.format(saving.current_balance))
                if saving.account_status == True:
                    print('Account status: Active')
                else:
                    print('Account status: Inactive')
                print()
                saving.close_month()
                print("The month is now closed.")
                print('Your Savings account report is: ')
                print('Starting balance: {:.2f}$'.format(saving.start_balance))
                print('Total amount of deposit: {:.2f}$'.format(saving.total_deposit))
                print('Total amount of withdrawal: {:.2f}$'.format(saving.total_withdrawal))
                print('Service charges: {:.2f}$'.format(saving.monthly_service_charge))
                print('Current balance: {:.2f}$'.format(saving.current_balance))
                if saving.account_status:
                    print('Account status: Active')
                else:
                    print('Account status: Inactive')
            else:
                pass
            D2 = input("Savings menu: A: Deposit, B: Withdrawal, C: Report, Q: Return to Bank Menu >")
    if D1 == "B":
        D3 = input("Checking menu: A: Deposit, B: Withdrawal, C: Report, Q: Return to Bank Menu >")
        while D3 != "Q":
            if D3 == "A":
                amount = int(input("Please enter the amount you wish to deposit >"))
                checking.deposit(amount)
                print(f"Your Checking account current balance is {checking.current_balance}$")
            if D3 == "B":
                amount = int(input("Please enter the amount you wish to withdraw >"))
                checking.withdrawal(amount)
                print(f"Your Checking account current balance is {checking.current_balance}$")
            if D3 == "C":
                print()
                print('Before the closing of the month:')
                print('Your Checking account report is:')
                print('Starting balance: {:.2f}$'.format(checking.start_balance))
                print('Total amount of deposit: {:.2f}$'.format(checking.total_deposit))
                print('Total amount of withdrawal: {:.2f}$'.format(checking.total_withdrawal))
                print('Service charges: {:.2f}$'.format(checking.monthly_service_charge))
                print('Current balance: {:.2f}$'.format(checking.current_balance))
                if checking.account_status:
                    print('Account status: Active')
                else:
                    print('Account status: Inactive')
                print()
                checking.close_month()
                print("The month is now closed:")
                print('Your Checking account report is: ')
                print('Starting balance: {:.2f}$'.format(checking.start_balance))
                print('Total amount of deposit: {:.2f}$'.format(checking.total_deposit))
                print('Total amount of withdrawal: {:.2f}$'.format(checking.total_withdrawal))
                print('Service charges: {:.2f}$'.format(checking.monthly_service_charge))
                print('Current balance: {:.2f}$'.format(checking.current_balance))
                if checking.account_status:
                    print('Account status: Active')
                else:
                    print('Account status: Inactive')
            else:
                pass
            D3 = input("Checking menu: A: Deposit, B: Withdrawal, C: Report, Q: Return to Bank Menu >")
    else:
        pass
print()
print('Thank you for incarnating into this 3rd Dimension, until next time...')


