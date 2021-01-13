################################################################
######  MULTI THREADING  ###################################
##############################################################
##  Types:
##          Process based Multi-Tasking (Independednt of each other)
##          Thread based Multi-Tasking  (Smallest segment of process is thread and can communicate with each other)
print("-"*10)
import threading
print("Current Executing thread :",threading.current_thread().getName())
#We can Execute thread in 3 ways:
#           1.Without using class  2.extending thread class 3.thread without extending thread class
from threading import *
def WithoutClass():
    for i in range(1,11):
        print("child Thread")

t1= Thread(target =WithoutClass)
t1.start()
for i in range(1,11):
    print("Main Thread")
#Note:
"""
If multiple threads present in our program, then we cannot expect execution order and hence we
cannot expect exact output for the multi threaded programs. B'z of this we cannot provide exact
output for the above program.It is varied from machine to machine and run to run.
Note:
Thread is a pre defined class present in threading module which can be used to create our
own Threads.
"""
#Creating thread by using thread class
print("="*30)
print("Thread by extending thread class")
print("="*30)
class Mythread(Thread):
    def run(self):
        for i in range(5):
            print("Child Method")
    def __del__(self):
        print("--Destruction!--")
t = Mythread()
t.start()
for i in range(5):
    print("Main thread")
#If i use t again it will destruct the fuctre one

print("-"*30)
print("Method 3 : Without extending thread class")
print("-"*30)
class Test:
    def run(self):
        for i in range(5):
            print("Child Thread")
obj = Test()
t2= Thread(target=obj.run)
t2.start()
for i in range(5):
    print("Main thread")
