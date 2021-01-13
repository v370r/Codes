def Subset(A,Sum):
    n = len(A)
    dp = [[0 for x in range(Sum+1)] for y in range(n+1)]
    for x in range(Sum+1):
        dp[0][x] =0
    for y in range(n+1):
        dp[y][0] = 1
    for x in range(1,n+1):
        for Su in range(1,Sum+1):
            if Su<A[x-1]:
                