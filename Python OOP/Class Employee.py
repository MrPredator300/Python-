class Employee:
    def __init__(self,name,password,salary):
        self.name=name
        self.password=password
        self.salary=salary
    
    @property
    def name(self):
        return self._name
    
    @property
    def password(self):
        raise AttributeError('password not possible')

    @password.setter
    def password(self,new_password):
        self._password=new_password
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,new_salary):
        self.password= new_salary

e=Employee("Austin","aus_feb_20",20000)




