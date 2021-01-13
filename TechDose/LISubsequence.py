def LIS(A,n):
    dp =[1]*(n+1)
    for x in range(0,n):
        for y in range(0,x):
            if A[x]>A[y] and dp[x]<=dp[y]+1:
                dp[x] =dp[y]+1
    return dp
A = [5,3,4,7,2,1]
print(LIS(A,len(A)))