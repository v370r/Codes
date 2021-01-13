def Recursive(cost,m,n):
    if n<0 or m<0:
        return float("inf")
    if m ==0 and n==0:
        return cost[m][n]
    else:
        return(cost[m][n]+min(Recursive(cost,m-1,n),Recursive(cost,m,n-1),Recursive(cost,m-1,n-1)))
def Dynamic(cost,m,n):
    dp = [[0 for x in range(m+1)] for y in range(n+1)]
    for x in range(m+1):
        for y in range(n+1):
            if x==0 and y==0:
                dp[x][y] =cost[0][0]
            elif x==0:
                dp[x][y] = cost[0][y]+dp[0][y-1] 
            elif y==0:
                dp[x][y] = cost[x][0]+dp[x-1][0]
            else:
                dp[x][y] = cost[x][y]+min(dp[x-1][y-1],dp[x-1][y],dp[x][y-1])
    return dp[m][n]

cost= [ [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
m = 2
n = 2
print(Recursive(cost,m,n))
print(Dynamic(cost,m,n))