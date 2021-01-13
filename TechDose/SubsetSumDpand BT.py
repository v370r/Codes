# Link:https://youtu.be/34l1kTIQCIA?list=PLEJXowNB4kPxQIN2dCUAnQ_92HIziG4x6
#Include or exclude
#isSS(set,n,Sum) = isSS(set,n-1,Sum)||isSS(set,n-1,Sum-set[n-1])
import time
class subset:
    def backTracking(self,set,n,Sum):
        if Sum==0:
            return True
        if n==0 and Sum !=0:
            return False
        if set[n-1]>Sum:
            return(self.backTracking(set,n-1,Sum))
        return(self.backTracking(set,n-1,Sum) + self.backTracking(set,n-1,Sum-set[n-1]))

    def Dynamic(self,A,Sum):
        n = len(A)
        dp = [[0 for x in range(Sum+1)] for y in range(n+1)]
        for x in range(Sum+1):
            dp[0][x] =0
        for y in range(n+1):
            dp[y][0] = 1
        for i in range(1,n+1):
            for j in range(1,Sum+1):
                if A[i-1]<=j:
                    dp[i][j] = dp[i-1][j] +dp[i-1][j-A[i-1]]#+ for all and or for atleast 1
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][Sum]

if __name__=='__main__':
    set = [3, 34, 4, 12, 5, 2,7,1,2,3,425,52,1,19,14515,626,631,52,3,425,52,1,19,14515,626,631,52,5, 2,7,1,2,3,425,52,1,19,14515,626,631,52,3,425,52,1,19,14515,626,631,52,3, 34, 4, 12, 5, 2,7,1,2,3,425,52,1,19,14515,626,631,52,3,425,52,1,19,14515,626,631,52,5, 2,7,1,2,3,425,52,1,19,14515,626,631,52,3,425,52,1,19,14515,626,631,52]
    Sum = 9
    n = len(set)
    obj1 = subset()
    start1 = time.time()
    print("Using Backtracking:\n")
    print(obj1.backTracking(set,n,Sum))
    print("-------------Execution Time-------",time.time()-start1)
    print("-"*100)
    start2 = time.time()
    print("Using Dynamic Programing:\n")
    print(obj1.Dynamic(set,Sum))
    print("-------------Execution Time-------",time.time()-start2)


        


