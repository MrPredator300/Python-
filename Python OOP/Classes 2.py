class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print("I am",self.name)
              
    def greet(self):
        if self.age < 80:
             print("Hello, how you doing?")
        else:
            print("Hello, I am fine how about you")
        
p1=Person("Ash",20)

p1.display()
p1.greet()

p2=Person("Marry",28)

p2.display()
p2.greet()



         