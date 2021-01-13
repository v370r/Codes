def Leader(A):
    n =len(A)
    for x in range(n-2):
        if A[x]<A[x+1] and A[x+1]>A[x+2]:
            print(A[x+1],end="->")
    print(A[n-1])
    return 
A=[15,18,5,3,6,2]
print(Leader(A))
        
#Best 
def Leader1(A):
    n = len(A)
    a = A[n-1]
    print(a,end=" ")
    for x in range(n-2,-1,-1):
        if A[x]>a:
            a = A[x]
            print(a,end=" ")
    return
    
A=[15,18,5,3,6,2]
print(Leader1(A))
