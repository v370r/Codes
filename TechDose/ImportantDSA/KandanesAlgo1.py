#MaximumSum Subarray
class MaxSum:
    def Kadane(self,A):
        max_so_far = A[0]
        curr_Sum = A[0]
        for x in range(1,len(A)):
            curr_Sum =max(A[x],curr_Sum+A[x])
            max_so_far =max(max_so_far,curr_Sum)
        return max_so_far
        """
    def Vague(self,A):# waste method  needs n**2 time and space
        Sum_arr=[]
        for x in range(len(A)):
            Sum = A[x]
            for y in range(x+1,len(A)):
                Sum+=A[y]
            Sum_arr.append(Sum)
        return(Sum_arr)
        """
    #better understandaing
    def Kadane2(self,A):
        max_Sum = 0
        res = float("-inf")
        for x in range(len(A)):
            max_Sum = max(A[x],A[x]+max_Sum)
            if max_Sum>res:
                res = max_Sum
        return res                

A = [-2,-3,4,-1,-2,1,5,-3]
t = MaxSum()
print(t.Kadane(A))
print(t.Kadane2(A))