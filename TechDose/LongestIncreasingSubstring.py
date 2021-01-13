def Increasing(A,n):
    dp = [1]*(n+1)
    for x in range(1,n):
        for y in range(0,x):
            if A[x]>A[y] and dp[x]<=dp[y]+1:
                dp[x] = dp[y]+1
    return max(dp)

A = [2,3,4,51,2,3,4,2,0]
n = len(A)
print(Increasing(A,n))