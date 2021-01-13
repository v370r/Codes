def minPartition(A,n):
    S = sum(A)
    dp = [[0 for x in range(S+1)] for y in range(n+1)]
    for x in range(n+1):
        for w in range(S+1):
            if x==0 and w==0: ##condition i always forget!
                dp[x][w]=True
            elif x==0:
                dp[x][w]=False
            elif w==0:
                dp[x][w]=True
            elif A[x-1]<=w:
                dp[x][w]= dp[x-1][w] |dp[x-1][w-A[x-1]]
            else:
                dp[x][w] =dp[x-1][w]
    Max = float("inf")
    for j in range(S//2,-1,-1):
        if dp[n][j]==True:
            Max = S-2*j
            break
    return Max
    #Now dp table is formed!!! Now find the m


A = [1,6,11,5,7]
n = len(A)
print(minPartition(A,n))




