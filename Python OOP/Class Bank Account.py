class BankAccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balane=balance

    def display(self):
        print(self.name,self.balance)
    
    def withdraw(self,amount):
        self.amount-=amount
    
    def deposite(self,amount):
        self.amount+=amount
    
a1=BankAccount('Mike',200)
a2=BankAccount("Tom")

a1.display()
a2.display()

a1.withdraw(100)
a2.deposite(500)

a1.display()
a2.display()

