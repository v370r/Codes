class MyClass:
     def f(self):
          print("check!")

def pyfunc(r):
     for x in range(r):
          print(" "*(r-x+1)+"* "*(x))
pyfunc(10)

import sys
x = "ABCDEF!`"
print(sys.getsizeof([]))
print(sys.getsizeof([x]))
print(sys.getsizeof([x,x,x,x,x]))

