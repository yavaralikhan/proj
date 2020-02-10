class BankAccount:
    def __init__(self):
        self.amount = 10000
        self.minBalance = 1000
        self.attempts = 0
        print("Account opend and have balance", self.amount)

    def Withdraw(self, balance):
        self.amount -= balance
        if self.amount < self.minBalance:
            self.amount += balance
            print("Withdraw Failed")
            print("Current balance is : ", self.amount)
            self.attempts += 1
        else:
            print("Withdraw Successful")
            print("New Balance is: ", self.amount)

        if self.attempts == 3:
            error = IndexError
            raise error

print("Banking Started ")

jeoaccount = BankAccount()
""""
jeoaccount.Withdraw(2000)
jeoaccount.Withdraw(10000)
jeoaccount.Withdraw(120.3)
jeoaccount.Withdraw(563)
"""

for i in range(1, 6000):
    jeoaccount.Withdraw(3000)
print("Banking Finished")