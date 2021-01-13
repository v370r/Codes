# 1 ,1, 2, 5,14,42
# 0 , 1,2 ,3,4, 5
#Best time : C(n) = 2nCn/(n+1) = 2n!/(n!(n+1)!) O(n) time for one element
"""
Applications: 
    1.Count no of possible BSTs with n-keys
    2.No of FBTs(full binary trres ) with n+1 leaves
    3.A, return number of ways you can draw A chords in a circle
     with 2 x A points such that no 2 chords intersect.
"""

import time
class catalian:
    def recursive(self,n):  # disadvantage : Recusive
        start1 = time.time()
        if n<=1:
            return 1
        else:
            res =0
            for i in range(n):
                res += self.recursive(i)*self.recursive(n-i-1)
            return res

    def Dynamic(self,n): #best for creating matrix! or array
        start2 = time.time() #Disadvantge: 0(n^2) needed for both single or array 
        dp = [0]*(n+1)
        dp[0] = dp[1] =1
        for i in range(2,n+1):
            for j in range(i):
                dp[i] +=dp[j]*dp[i-j-1]
        return dp

    def Factorial(self,m):
        dp = [0]*(m+1)
        dp[0]=dp[1] =1
        for x in range(2,m+1):
            dp[x] =x*dp[x-1]
        return(dp)
    
    def UsingBinomial(self,n): # best O(n)
        dp = self.Factorial(2*n)
        return(dp[2*n]//(dp[n]*dp[n+1]))

obj1 = catalian()
print(obj1.recursive(5))
print(obj1.Dynamic(10))
print(obj1.UsingBinomial(10))