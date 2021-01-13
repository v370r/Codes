def singleNumber( A):
    x = 0
    for n in A:
        x = x ^ n 
    return x
print(singleNumber([1,1,2,2,3,4,4]))

from collections import Counter
def UsingCounter(B):
    b = Counter(B)
    for x in b:
        if b[x] ==1:
            return x
         
print(UsingCounter([1,1,2,2,3,4,4]))
