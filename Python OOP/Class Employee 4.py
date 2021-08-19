class employee:
    allowed_domains={'gmail.com','outlook.com','hotmail.com','yahoo.com'}

    def _init_(self,name,email):
        self.name=name
        self.email=email
    
    def display(self):
        print(self.name,self.email)
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,new_email):
        domain=new_email[new_email.index('@')+1:]
        if domain in employee.allowed_domains:
            self.email=new_email
        else:
            raise RuntimeError(f'Domain {domain} is not allowed')


e1=employee('Jack','jack1547@gmail.com')
e2=employee('Ron','ron457@hotmail.com')
e3=employee('Bob','bob123@gmail.com')
e4=employee('Ash','ash342@yahoo.com')
e5=employee('Brock','brock447@outlook.com')
e6=employee('Cindy','cindy823@hotmail.com')