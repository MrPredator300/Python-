class salesperson:
   total_revenue=0
   names=[]

   def _init_(self,name,age):
        self.name=name
        self.age=age
        self.sales_amount=0
        salesperson.name.append(name)
    
   def make_sale(self,money):
        self.sales_amount+=money
    
   def show(self):
        print(self.name,self.age,self.sales_amount)
    
s1=salesperson('Ron',20)
s2=salesperson('Bob',25)
s3=salesperson('Sam',29)

s1.make_sale(1000)
s1.make_sale(1500)
s2.make_sale(5000)
s2.make_sale(5500)
s3.make_sale(8000)
s3.make_sale(8500)

s1.show()
s2.show()
s3.show()

print(salesperson.total_revenue)
print(salesperson.names)

        
    