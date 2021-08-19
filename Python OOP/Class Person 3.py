class Person:
    def __init__(self,id):
        self.id=id
    
class Teacher:
    def __init__(self,id):
        Person.__init__(self,id)
        self.id+='T'

class Student(Person):
    def __init__(self, id):
        super().__init__(id)
        self.id+='S'
    
class TeachingAssistant(Student,Teacher):
    def __init__(self, id):
        Student.__init__(self,id)
        Teacher.__init__(self,id)

x=TeachingAssistant('0147')
print(x.id)
y=Student('254208')
print(y.id)
z=Teacher('0085')
print(z.id)
p=Person('7458')
print(p.id)

        
