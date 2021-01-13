#Can be used for min coins required tooo!
#best code 
def CoinChange(A,n,Val):
    dp = [[0 for x in range(Val+1)] for x in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1  #if no coin taken value is always 0
    for i in range(1,n+1):
        for w in range(1,Val+1):
            if A[i-1]<=w:
                dp[i][w] = dp[i-1][w]+dp[i][w-A[i-1]] #both exclude and include and not need to remove like O-1 knapsack we can use the same 
            else:
                dp[i][w]=dp[i-1][w] # exclude it
    return dp[n][Val]

arr = [1, 2, 3] 
m = len(arr) 
n = 4
print(CoinChange(arr,m,n))
"""
for x in range(n+1):
    for w in range(W+1):
        elif wt[x-1]<=w:
            dp[x][w] = max(dp[x-1][w],val[x-1]+dp[x-1][w-wt[x-1]])
        else:
            dp[x][w]=dp[x-1][w]

def unboundedKnapsack(W, n, val, wt):
    dp = [0 for i in range(W + 1)]
    ans = 0
    for i in range(W + 1):
        for j in range(1,n):
            if (wt[j-1] <= i):
                dp[i] = max(dp[i], dp[i - wt[j-1]] + val[j-1])
"""