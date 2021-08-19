class Person:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print(self.name,self.age)

    def set_age(self, new_age):
        if 20 < new_age < 80:
            self._age=new_age
        else:
            raise ValueError("Age must be between 20 to 80")

    def get_age(self):
        return self.age()  

if __name__=='__main__':
    p=Person("Raj",33)
    p.display()

