#bank account
class Bankaccount:
    def __init__(self):
        self.name=" "
        self.account=" "
        self.balance=0
    def data(self):
        self.name=str(input("enter name:"))
        self.account=int(input("enter account number:"))
        self.balance=int(input("enter account balance:"))
    def deposit(self):
        self.new_amount=int(input("enter new amount to be deposited:"))
        self.balance=self.balance+self.new_amount
        print("current balance is",self.balance)
    def withdrawal(self):
        self.withdraw_amount=int(input("enter amount to be withdrawed:"))
        if self.balance<self.withdraw_amount:
            print("insufficient balance")
        else:
            self.balance=self.balance-self.withdraw_amount
            print("current balance is",self.balance)
    def account_balance(self):
        print("current balance is",self.balance)
class Saving_account(Bankaccount):
    def calculate_interest(self):
        self.principal=int(input("enter principal amount"))
        self.n=int(input("enter no of yeras"))
        self.final=self.principal*self.n*(4/100)
        print("interest is",self.final)
class Fixed_account(Bankaccount):
    def calculate_interest(self):
        self.principle=int(input("enter principle amount"))
        self.n=int(input("enter number of times interest is compounded per year "))
        self.final=self.principle*self.n*(7/100)
        print("interest is",self.final)
obj=Bankaccount()
while(True):
    print("menu \n 1.Deposit \n 2.Withdrawal \n 3.Account balance \n 4.Saving account interest \n 5.Fixed account interest \n 6.Exit ")

        

