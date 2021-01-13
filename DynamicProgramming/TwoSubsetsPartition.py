"""
Partition a set into two subsets such that 
the difference of subset sums is minimum
"""
# => Su1+su2 ~=Sum ==> su1 ~=(Sum-su2)
for j in range(su // 2, -1, -1):
        if dp[n][j] == True:
            diff = su - (2 * j)
            break       
    return diff
     