class Person:

    species = "Homo sapiens"

    def __init__(self,name,age):
        self.name= name
        self.age=age

    def display(self):
        print(f'{self.name} is {self.age} years old')
    
p1=Person("Austin",21)
p2=Person("Ron",24)

p1.display()
p2.display()