def KnapSack(wt,val,W,n):
    dp = [[0 for x in range(W+1)] for y in range(n+1)]
    for x in range(n+1):
        for w in range(W+1):
            if x==0 and w==0:
                dp[x][w]=0
            elif x==0:
                dp[x][w]=0
            elif w==0:
                dp[x][w]=0
            elif wt[x-1]<=w:
                dp[x][w] = max(dp[x-1][w],val[x-1]+dp[x-1][w-wt[x-1]])
            else:
                dp[x][w]=dp[x-1][w]
    return dp[n][w]

val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(KnapSack(wt, val,W, n))