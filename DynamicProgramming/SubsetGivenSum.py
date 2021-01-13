def Subset(A,Sum):
    n = len(A)
    dp = [[0 for x in range(Sum+1)] for y in range(n+1)]
    for x in range(n+1):
        for w in range(Sum+1):
            if x==0 and w==0:
                dp[x][w] =1
            elif x==0:
                dp[x][w]=0
            elif w==0:
                dp[x][w]=1
            elif A[x-1]<=w:
                dp[x][w]=dp[x-1][w] | dp[x-1][w-A[x-1]]
            else:
                dp[x][w] = dp[x-1][w]
    return(dp[n][Sum])


A =[3, 34, 4, 12, 5, 2]
Sum = 9
print(Subset(A,Sum))