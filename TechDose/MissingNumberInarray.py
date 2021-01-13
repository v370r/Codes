#For sorted Array
#No ==index+1 search
class CheckMissing:
    def SortedCheck(self,A,n):
        lo = 0
        hi = n-1
        while(lo<=hi):
            mid = (lo+hi)//2
            if A[mid] ==mid+1:
                lo =mid+1
            else:
                hi=mid-1
        return(lo+1) 

    def UnsortedSumMethod(self,A,n):
        SumAll = n*(n+1)//2
        Sum =sum(A)
        return(SumAll-Sum)
    
    def UnsortedXOR(self,A,n):
        x1 = A[0]
        x2 = 1
        for i in range(1,n):
            x1 ^= A[i]
        for i in range(2,n+2):
            x2 ^= i 
        return(x1^x2)

A= [1,2,3,4,6,7,8,9,10]
n =len(A)
Ans = CheckMissing()
print(Ans.SortedCheck(A,n))
# can do linear
print(Ans.UnsortedXOR(A,n))
print(Ans.UnsortedSumMethod(A,n))
#For UnSorted