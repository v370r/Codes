def Partition(n,k):
    dp = [[0 for x in range(k+1)] for y in range(n+1)]
    for i in range(n+1): # base condition
        dp[i][0] =0
    for i in range(k+1):
        dp[0][i] =0
    for i in range(1,n+1):
        for j in range(1,i+1):
            if j==1 or j==i:
                dp[i][j] =1 #idf no of elements is same as no of sets then each set must have oly 1
            else:
                dp[i][j] = j*dp[i-1][j] +dp[i-1][j-1] # first is last number has possibility to go any other ways 
    return dp                   #dp[i-1][j-1] means new set done by last element

    
##Reference: https://youtu.be/0Q_U9_gryRg?list=PLEJXowNB4kPxQIN2dCUAnQ_92HIziG4x6
print(Partition(3,4))
print(1/10+2/10 -3/10)
#Next read fork()