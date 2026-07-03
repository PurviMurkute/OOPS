# create account class with 2 attributes - balance and account number,
# create methods to debit, credit and printing the balance of the account.

class Account:
    def __init__(self, acc, balance):
        self.account_number = acc
        self.balance = balance

    def debit(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
            print("Debited:", amount)
        else:
            print("Insufficient balance")

    def credit(self, amount):
        self.balance += amount
        print("Credited:", amount)

    def print_balance(self):
        print("Balance:", self.balance)


acc1 = Account("123456", 1000)
print(acc1.account_number, acc1.balance)

acc1.debit(1001)
acc1.print_balance()
acc1.debit(500)
acc1.print_balance()
acc1.credit(2000)
acc1.print_balance()