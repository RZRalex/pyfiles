class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < 0:
            print('Insufficient funds: Charging a $5 fee, thank you.')
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


cooper = BankAccount(int_rate=0.05, balance=25)
alex = BankAccount(int_rate=0.03, balance=100)


cooper.deposit(25).deposit(80).deposit(45).withdraw(18).yield_interest().display_account_info()
alex.deposit(85).deposit(145).withdraw(25).withdraw(12).withdraw(42).withdraw(67).yield_interest().display_account_info()

