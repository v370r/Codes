from threading import *
print(current_thread().getName())
current_thread().setName("Vijay")
print(current_thread().getName())
print("-"*30)
#Thread identification number
print("Thread Identification Number")
def test():
    print("Child Thread")
t = Thread(target=test,name= "child1")
t.start()
print("Main thread identification Number:",current_thread().ident)
print("Child Thread Identification Number",t.ident)
print("Thread count:",active_count())
# Use  active count()