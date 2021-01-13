def equilibrium(A): #O(n) time and O(n) space
    n = len(A)
    SumArr=[0]*n
    curr_sum = 0
    for x in range(n):
        curr_sum+=A[x]
        SumArr[x] =curr_sum
    for x in range(1,n-1):
        if SumArr[x]-A[x]==SumArr[n-1]-SumArr[x]:
            return x
    return(-1)
A = [1,2,6,4,0,-1]
print(equilibrium(A))