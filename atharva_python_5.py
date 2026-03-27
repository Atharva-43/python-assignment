# Method Overloading
class Calc:
    def add(self,a,b=0,c=0):
        return a + b + c
c = Calc()
print(c.add(10))
print(c.add(10,20))
print(c.add(10,20,30))