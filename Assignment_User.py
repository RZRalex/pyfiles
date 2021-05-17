class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        print(f'Account Balance: ${self.balance} for User: {self.name}')

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount



mike = User('Michael Fassbender', 'Mike@gmail.com')
cooper = User('Cooper Cheong', 'coop@gmail.com')
alex = User('Alexander Cheong', 'alex@gmail.com')

mike.make_deposit(150)
mike.make_deposit(75)
mike.make_deposit(125)
mike.make_withdrawal(100)
mike.display_user_balance()

cooper.make_deposit(535)
cooper.make_deposit(85)
cooper.make_withdrawal(25)
cooper.make_withdrawal(40)
cooper.display_user_balance()

alex.make_deposit(1400)
alex.make_withdrawal(325)
alex.make_withdrawal(65)
alex.make_withdrawal(120)
alex.display_user_balance()

mike.transfer_money(alex,50)
mike.display_user_balance()
alex.display_user_balance()