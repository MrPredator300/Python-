class Product:
    def __init__(self,x,y):
        self._x=x
        self._y=y
    
    def display(self):
        print(self._x,self._y)
    
    def value(self):
        return self._x
    
P=Product(12,24)
