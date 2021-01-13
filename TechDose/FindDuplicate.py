class Duplicates:
    def hashing(self,A,n):
        d= {}
        for x in A:
            if x in d:
                d[x]+=1
            else:
                d[x] =1
        return(d)
        
    def Order1Space(self,A,n):
        flag = 0
        for i in range(0,n):
            if A[A[i]%n]>=n:
                if A[A[i]%n]<2*n:
                    print(A[i]%n,end =" ")
                    flag =1
            A[A[i]%n] +=n
        if flag ==0:
            print(-1) 

A=[1,2,3,4,4,7,6,2]
n =len(A)
ans = Duplicates()
print(ans.hashing(A,n))
print("Effcicient ")
ans.Order1Space(A,n)
