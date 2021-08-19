class Rectangle:
    name='Rectangle'
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2*(self.length + self.breadth)
    
class Triangle:
    name='Triangle'
    def __init__(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
    
    def area(self):
        sp=(self.s1+self.s2+self.s3)/2
        return (sp*(sp-self.s1)*(sp-self.s2)*(sp-self.s3))
    
    def perimeter(self):
        return self.s1+self.s2+self.s3
    
class Circle:
    name='Circle'
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14*self.radius*self.radius
    
    def perimeter(self):
        return 2*3.14*self.radius
    
r1=Rectangle(15,25)
r2=Rectangle(12,20)
t1=Triangle(14,17,21)
t2=Triangle(22,25,28)
c1=Circle(15)
c2=Circle(25)

def find_area_perimeter(shape):
    print(shape.name)
    print('Area :',shape.area())
    print('Perimeter :',shape.perimeter())

shapes={r1,r2,t1,t2,c1,c2}

total_area=0
total_perimeter=0

for shape in shape:
    total_area +=shape.area()
    total_perimeter +=shape.perimeter()

print(total_area,total_perimeter)





        
    
        
