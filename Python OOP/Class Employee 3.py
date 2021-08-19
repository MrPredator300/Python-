class employee:
    domains=set()

    def __init__(self,name,email):
        self.name=name
        self.email=email
        domain=email[email.index('@')+1:]
        employee.domains.add(domain)
    
    def display(self):
        print(self.name,self.email)
    
e1=employee('Jack','jack1547@gmail.com')
e2=employee('Ron','ron457@hotmail.com')
e3=employee('Bob','bob123@gmail.com')
e4=employee('Ash','ash342@yahoo.com')
e5=employee('Brock','brock447@outlook.com')
e6=employee('Cindy','cindy823@hotmail.com')

print(employee.domains)
    
