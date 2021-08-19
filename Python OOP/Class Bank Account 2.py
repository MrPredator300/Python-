class BankAccount:

    rate_of_interest=5
    minimum_balance=100
    minimum_balance_fee=10

    def __init__(self,account_no,owner_name,balance):
        self.account_no=account_no
        self.owner_name=owner_name
        self.balance=balance
    
    def withdraw(self,amount):
        self.balance-=amount

    def deposite(self,amount):
        self.balance+=amount
        
    def display(self):
        print(self.rate_of_interest)
        print(self.minimum_balance)
        print(self.minimum_balance_fee)
        print(self.owner_name)
        print(self.account_no)
        print(self.balance)

account1=BankAccount('7894','Austin',50)
account2=BankAccount('2145','Amanda',400)

account1.display()
account2.display()


    

    