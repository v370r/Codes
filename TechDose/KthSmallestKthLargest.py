from heapq import heapify,heappush,nsmallest,nlargest
import time
from random import randint
class Kthelement:
    def Heap(self,A):
        heapify(A) #Order of complexity O(2*n) for sorting and heap building
        return(nsmallest(2,A))
    def Sort(self,A):
        A.sort() #Order of O(nlogn)
        return(A[:2])


obj1 = Kthelement()
A= []
for x in range(10,10000000):
    A.append(randint(0,x))
start1 = time.time()
print(obj1.Heap(A),"-----Execution------",time.time()-start1)
start2 = time.time()
print(obj1.Sort(A),"-----Execution------",time.time()-start2)
"""
[0, 0] -----Execution------ 10.462909698486328
[0, 0] -----Execution------ 61.38333511352539
"""