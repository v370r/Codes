#time complexity : O(n*n!) n for printing
def StringPermut(A,l,r):
    if l ==r:
        print("".join(A))
    else:
        for x in range(l,r+1):
            A[l],A[x] =A[x],A[l]
            StringPermut(A,l+1,r)
            A[l],A[x] =A[x],A[l]
A = "AbC"
l=0
r = 2
A = list(A)
StringPermut(A,0,2)
