#MultiThreading 
#A thread is an entity with in a process that can be scheduled for execution
#Smallest entity ina OS
import threading

def printPrime(n):
    for x in range(2,n):
        for y in range(2,int(x**(0.5))+1):
            if x%y ==0:
                break
        else:
            print(x,end="->")
    print()

if __name__ =="__main__":
    t1 = threading.Thread(target=printPrime,args=(10,))
    t2 = threading.Thread(target=printPrime,args=(10,))
    t1.start()#starts
    t2.start()
    t1.join() #wait until t1 completes and joins
    t2.join()
    print("Done!")
            
        