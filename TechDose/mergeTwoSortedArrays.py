def Merge(A,B):
    n =len(A)
    m=len(B)
    i = 0
    j = 0
    c= []
    while(i<n and j<m):
        if A[i]<B[j]:
            c.append(A[i])
            i+=1
        else:
            c.append(B[j])
            j+=1
    while(i<n):
        c.append(A[i])
        i+=1
    while(j<m):
        c.append(B[j])
    return(c)
A = [-1,1,2,2,5,6,8,]
B= [-2,-1,3,4,7]
print(Merge(A,B))
# With no extra space! best code!
def merge(A, B):
    i=len(A)-1
    j=len(B)-1
    A.extend(B)
    k=len(A)-1
    while i>-1 and j>-1:
        if A[i]>B[j]:
            A[k]=A[i]
            i-=1
        else:
            A[k]=B[j]
            j-=1
        k-=1
    while j>-1:
        A[k]=B[j]
        j-=1
        k-=1
    while i>-1:
        A[k]=A[i]
        i-=1
        k-=1
    return A