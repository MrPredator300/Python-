class Person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("I am",self.name,self.age, "years old")
        
    @classmethod
    def from_str(cls,s):
        name,age=s.split(',')
        return cls(name,int(age))
    
    @classmethod
    def from_str(cls,d):
        return cls(d['name'],d['age'])

p1=Person('Jhon',20)
p2=Person('Jack',34)

s='Jim 23'
p3=Person.from_str(s)
p3.display()

d={'name':'Jane','age':34}
p4=Person.from_dict(d)
p4.display()

