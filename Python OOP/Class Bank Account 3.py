class bankaccount:

    bank_name="HDFC Bank,MG Road,Bangalore"

    def __init__(self,name,balance=0,bank=bank_name):
        self.name=name
        self.balance=balance
        self.bank=bank
    
    def display(self):
        print(self.name,self.balance,self.bank)
    
    def withdraw(self,amount):
        self.balance-=amount
    
    def deposite(self,amount):
        self.balance+=amount

a1=bankaccount("Mike",1000,"Axis Bank Chennai")
a2=bankaccount("Ross")

a1.display()
a2.display()


        