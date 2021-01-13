#Use no of ways to partition elements
#n =2  set = {1,2}  find how many ways we can partions
#ans = {1,2},{1},{2}
# If set {1,2,3} then we have following ways:
#                   | {1,2} and {3}
#                   | {1,3}  and {2} + {1},{2},{3}+{1,2,3}
#                   | {2,3} and {1}
#         ==>Bell(2) = 2,Bell(3) = 5
#              ==>Bell(n) = sigma_k=1 to n (S(n,k)) 
#    ==>Bell(3) = sigma_k =1 to 3 (S(3,k))
#    ==> best S(n+1,k) =  k*S(n,k) +S(n,k-1)
#Link: https://youtu.be/oGYFJ9gSBKw?list=PLEJXowNB4kPxQIN2dCUAnQ_92HIziG4x6
def BellNumber(n):
    dp = [[0 for x in range(n+1)] for j in range(n+1)]
    dp[0][0] =1
    for i in range(1,n+1):
        dp[i][0] = dp[i-1][i-1]
        for j in range(1,i+1):
            dp[i][j] = dp[i-1][j-1]+dp[i][j-1]
    return(dp[n][0])
print(BellNumber(3))

"""
1
1 2
2 3 5
5 7 10 15
15 20 27 37 52
"""