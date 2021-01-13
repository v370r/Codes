def cutRod(price,n):
    val = [0 for x in range(n+1)]
    for i in range(1,n+1):
        max_val = -float("inf")
        for j in range(i):
            max_val=max(max_val,price[j]+val[i-j-1])
        val[i] = max_val
    return val[n]
arr = [1, 5, 8, 9, 10, 17, 17, 20] 
n =len(arr)
print(cutRod(arr,n))




def unboundedKnapsack(W, n, val, wt):
    dp = [0 for i in range(W + 1)]
    ans = 0
    for i in range(W + 1):
        for j in range(n):
            if (wt[j] <= i):
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])