def LIS(A,n):
    dp = [1]*(n+1)
    for x in range(n):
        for y in range(0,x):
            if A[x]>A[y] and dp[x]<dp[y]+1:
                dp[x] =dp[y]+1
    return (max(dp))



A = [50, 3, 10, 7, 40, 80]
n = len(A)
print(LIS(A,n))