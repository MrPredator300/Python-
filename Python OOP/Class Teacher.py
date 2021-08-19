class Teacher:
    def greet(self):
        print('I am a Teacher')

class Student:
    def greet(self):
        print('I am a Student')
    
class TeachingAssistance(Teacher,Student):
    pass

x=TeachingAssistance()
x.greet()
