class Emloyee:
    def __init__(self,first_name,last_name,,DOB,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.DOB=DOB
        self.salary=salary
    
    def display(self):
        print(f'''I am {self.first_name} {self.last_name} born in {self.DOB}''')
        
        
