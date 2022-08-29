from decimal import Decimal

class Account:
    start_balance = Decimal("0.00")
    current_balance = Decimal("0.00")
    total_deposit = Decimal("0.00")
    number_deposit = Decimal("0")
    total_withdrawal = Decimal("0.00")
    number_withdrawal = Decimal("0")
    annual_interest_rate = Decimal("0.00")
    monthly_service_charge = Decimal("0.00")
    account_status = True

    def __init__(self, start_balance: Decimal, current_balance: Decimal, total_deposit: Decimal, number_deposit: Decimal,  total_withdrawal: Decimal, number_withdrawal: Decimal, annual_interest_rate: Decimal, monthly_service_charge: Decimal, account_status):
        self.start_balance = start_balance
        self.current_balance = current_balance
        self.total_deposit = total_deposit
        self.number_deposit = number_deposit
        self.total_withdrawal = total_withdrawal
        self.number_withdrawal = number_withdrawal
        self.annual_interest_rate = annual_interest_rate
        self.monthly_service_charge = monthly_service_charge
        self.account_status = account_status

    def deposit (self, amount):
        self.current_balance += amount
        self.total_deposit += amount
        self.number_deposit += 1

    def withdrawal (self, amount):
        self.current_balance -= amount
        self.total_withdrawal += amount
        self.number_withdrawal += 1

    def calc_interest(self):
        self.current_balance += (self.current_balance*self.annual_interest_rate/12)

    def close_month(self):
        self.current_balance -= self.monthly_service_charge
        self.calc_interest()
        self.start_balance = self.current_balance
        self.number_withdrawal = 0
        self.number_deposit = 0
        self.monthly_service_charge = 0

class Savings (Account):

    def __init__(self, start_balance: Decimal, current_balance: Decimal, total_deposit: Decimal, number_deposit: Decimal,  total_withdrawal: Decimal, number_withdrawal: Decimal, annual_interest_rate: Decimal, monthly_service_charge: Decimal, account_status):
        super().__init__(start_balance, current_balance, total_deposit, number_deposit, total_withdrawal, number_withdrawal, annual_interest_rate, monthly_service_charge, account_status)

    def deposit(self, amount):
        if self.current_balance + amount >= 25 and not self.account_status:
            self.account_status = True
            print("Your account is now active.")
        super().deposit(amount)
        self.number_deposit += 1

    def withdrawal(self, amount):
        if self.account_status and self.current_balance - amount < 25:
            self.account_status = False
            print("The balance of this account is less than 25, this account is now inactive.")
            super().withdrawal(amount)

        elif not self.account_status:
            print("Sorry, cannot withdraw on an inactive account.")

        else:
            super().withdrawal(amount)

    def close_month(self):
        if self.number_withdrawal > 4:
            self.monthly_service_charge += (self.number_withdrawal - 4)
        super().close_month()

class Checking (Account):
    def __init__(self, start_balance: Decimal, current_balance: Decimal, total_deposit: Decimal, number_deposit: Decimal,  total_withdrawal: Decimal, number_withdrawal: Decimal, annual_interest_rate: Decimal, monthly_service_charge: Decimal, account_status):
        super().__init__(start_balance, current_balance, total_deposit, number_deposit, total_withdrawal, number_withdrawal, annual_interest_rate, monthly_service_charge, account_status)

    def deposit(self, amount):
        super().deposit(amount)
        print(f"The amount of {amount}$ has been deposited to the account.")

    def withdrawal(self, amount):
        if self.current_balance <= 0:
            print("The withdrawal cannot be made due to insufficient funds.")

        elif self.current_balance - amount < 0:
            self.monthly_service_charge += 15
            print("The withdrawal cannot be made due to insufficient funds.")

        else:
            super().withdrawal(amount)

    def close_month(self):
        self.monthly_service_charge += Decimal("5") + (self.number_withdrawal*Decimal("0.10"))
        super().close_month()


