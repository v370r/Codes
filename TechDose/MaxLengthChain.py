def MaxLenChain(A,n):
    dp=[1]*(n+1)
    for x in range(n):
        for y in range(x):
            if A[x][0]>A[y][1] and dp[x]<dp[y]+1:
                dp[x] =dp[y]+1
    return(max(dp))
A=[(5,24),(39,60),(15,28),(27,40),(50,90)]
n=len(A)
print(MaxLenChain(A,n))