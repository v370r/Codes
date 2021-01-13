def LCsubsequence(X,Y,m,n):
    dp = [[0 for x in range(n+1)] for y in range(m+1)]
    #starting is 0 for bothcases since 0 element subsequence is 0
    for x in range(m+1):
        for y in range(n+1):
            if x==0 or y==0:
                dp[x][y]=0
            elif X[x-1] ==Y[y-1]:
                dp[x][y]= 1+dp[x-1][y-1]
            else:
                dp[x][y]= max(dp[x-1][y],dp[x][y-1])
    return dp[m][n]



X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", LCsubsequence(X , Y, len(X), len(Y)))