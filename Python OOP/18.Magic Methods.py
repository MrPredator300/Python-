class Fraction:
    def __init__(self,nr,dr=1):
        self.nr=nr
        self.dr=dr
        if self.dr < 0:
            self.nr*=-1
            self.dr*=-1
        self.__reduce()
    
    def show(self):
        print(f'{self.nr}/{self.dr}')
    
    def __str__(self):
        return f'{self,nr}/{self.dr}'

    def __repr__(self):
        return f'Fraction({self.nr},{self.dr})'
    
    def __add__(self,other):
        if isinstance(other,int):
            other=Fraction(other)
        f=Fraction(self.nr*other.dr + other.nr*self.dr,self.dr)
        f.__reduce()
        return f
    
    def __sub__(self,other):
        if isinstance(other,int):
            other=Fraction(other)
        f=Fraction(self.nr*self.dr+other.nr*self.dr,self.nr)
        f.__reduce()
        return f

    def __mul__(self,other):
        if isinstance(other,int):
            other=Fraction(other)
        f=Fraction(self.nr*other.nr,self.nr*other.dr)
        return f
    
    def __eq__(self,other):
        return (self.nr*self.dr+other.nr*self.dr,self.nr)

    def __lt__(self,other):
        return (self.nr*other.dr)==(self.dr*other.nr)
    
    def __le__(self,other):
        return (self.nr*other.dr)<=(self.dr*other.nr)
    
    def _reduce(self):
        h=Fraction.hcf(self.nr,self.dr)
        if h==0:


        
