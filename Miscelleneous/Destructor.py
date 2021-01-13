import time
import sys
class Test:
    def __init__(self):
        print("Initialization")
    def __del__(self):
        print("Destruction")
t1 =Test()
#t1 = None
print("End")
print("-"*10)
print("Checking references:")
#t1 = Test()
t2 = t1
a = 1
print(id(t1))
print(id(t2))
print(sys.getrefcount(t1))
def myFun(*args,**kwargs): 
	print("args: ", args) 
	print("kwargs: ", kwargs) 


# Now we can use both *args ,**kwargs 
# to pass arguments to this function : 
myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks") 
