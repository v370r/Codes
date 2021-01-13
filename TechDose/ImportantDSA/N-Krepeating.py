#Given n number find k repearting numbers
from collections import Counter
class NKrepeat:
    def majorityElement(self,nums,n,k):
        b = Counter(nums)
        n = len(nums)
        for x in b:
            if b[x]>(n//k):
                yield x
        

#Importat Note: yeild is a generator 

A = [3,1,2,2,1,2,3,3]
t = NKrepeat()
print(list(t.majorityElement(A,len(A),3)))
