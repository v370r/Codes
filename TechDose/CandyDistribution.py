def Candy(A,n):
    candies_sum =0
    dp =[1]*(n+1)
    for x in range(0,n):
        if A[x]>A[x-1]:
            dp[x] =dp[x-1]+1
    for x in range(n-2,-1,-1):
        if A[x]>A[x+1]:
            dp[x] =max(dp[x],dp[x+1]+1)
    #last number error
    if A[-2]<A[-1]:
        dp[-1] = dp[-2]+1
    return(dp)
A = [12,4,3,11,34,34,1,6,7]
print(A)
print(Candy(A,len(A)))