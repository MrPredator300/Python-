class Person:
    def __init__(self,name,age,address,phone):
        self.name=name
        self.age=age
        self.address=address
        self.phone=phone
    
    def greet(self):
        print('Hello I am',self.name)
    
    def is_adult(self):
        if self.age>10:
            return True
        else:
            return False
    
    def contact_details(self):
        print(self.address,self.phone)
    
class Employee(Person):
    def __init__(self,name,age,address,phone,salary,office_address,office_phone):
        super().__init__(name,age,address,phone)
        self.salary=salary
        self.office_address=office_address
        self.office_phone=office_phone
    
    def calculate_tax(self):
        if self.salary <50000:
            return 0
        else:
            return self.salary*0.05
    
    def contact_details(self):
        super().contact_details()
        print(self.address,self.phone)
        print(self.office_address,self.office_phone)

emp=Employee('Bob',29,'Shastri Nagar Mumbai','9978456310',50000,'5th street Bandra,Mumbai','8874596320')




        