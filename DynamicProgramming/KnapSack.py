def knapSack(W,wt,val,n):
    dp =[[0 for x in range(W+1)] for y in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,W+1):
            if wt[i-1]<=w:
                dp[i][w] = max(dp[i-1][w],dp[i-1][w-wt[i-1]]+val[i-1])
    return(dp[n][W])




val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W, wt, val, n)) 