#https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/
#Thread Synchrom=nization is mechanism
"""
Thread synchronization is a mechanism which ensures
that two are more current threads don not simulatneously
execute some particular programsegment
known as critical section
"""
from multiprocessing import Process

import threading
#gloabal x
x =0
def increment():
    global x
    x +=1
def thread_task(lock):
    for i in range(10000):
        increment()

def min_task():
    global x
    x = 0
    lock =threading.Lock()
    t1  = threading.Thread(target=thread_task,args=(lock,))
    t2 = threading.Thread(target=thread_task,args=(lock,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__": 
    for i in range(20): 
        min_task() 
        print("Iteration {0}: x = {1}".format(i,x)) 
