def LIS(A):
    n = len(A)
    lis = [1]*(n+1)
    for x in range(1,n):
        for y in range(0,x):
            if A[x]>A[y] and lis[x]<=lis[y]+1:
                lis[x] = lis[y]+1
    return(max(lis))

A = [5,3,4,7,2,1]
print(LIS(A))