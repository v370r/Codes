def CountWays(n):
    dp= [1]*(n+2)
    dp[0] = 1
    if n>=1:
        dp[1] = 1
        dp[2] = 2
        if n>=3:
            for x in range(3,n+1):
                dp[x] = dp[x-1]+dp[x-2]+dp[x-3]
    return dp[n]
n=10
print(CountWays(n))