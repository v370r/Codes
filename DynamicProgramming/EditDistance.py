def EditDistance(X,Y,m,n):
    dp = [[0 for x in range(n+1)] for y in range(m+1)]
    for x in range(m+1):
        for y in range(n+1):
            if x==0 :
                dp[x][y] = y
            elif y==0:
                dp[x][y] =x 
            elif X[x-1]==Y[y-1]:
                dp[x][y] =dp[x-1][y-1]
            else:
                dp[x][y] = 1+min(dp[x-1][y],dp[x][y-1],dp[x-1][y-1])
    return dp[m][n]



A = "sunday"
B = "saturday"
print(EditDistance(A,B,len(A),len(B)))

