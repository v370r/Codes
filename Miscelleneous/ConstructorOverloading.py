# Operator Overloading:
#: We can use the same operator for multiple purposes.
print(10+20)
print("Vijay"+"kumar")
"""
On class Object"
"""
class Books:
    def __init__(self,pages):
        self.pages = pages
b1 = Books(100)
b2  = Books(200)
#print(b1+b2) #throws error 
#python supports operator overloading reason: for every operator there is magic method
class Books:
    def __init__(self,pages):
        self.pages = pages
    def __mul__(self,other):
        return(self.pages+other.pages)
b1 = Books(100)
b2 = Books(200)
print(b1.__mul__(b2)) #can be any name but a magic method LOL!
"""
Method Overloading:
    If 2 methods having same name but different type of arguments then those methods are said to
    be overloaded methods
        But in Python Method overloading is not possible.
    If we are trying to declare multiple methods with same name and different number of arguments
    then Python will always consider only last method
    ython doesn’t declare types in method declarations, so basically, in Java you can have this:

try:
    class Test:
        def m1(self): #reason datatypes
            print("no-arg method")
        def m1(self,a):
            print("one-arg method")
        def m1(self,a,b):
            print("two-arg method")
"""

class Test:
    def m1(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("The sum of 3 numbers" ,a+b+c)
        elif a!=None and b!=None :
            print(a+b)

t = Test()
t.m1("Vijay","kumar")


