def Sort(A): #total n/3 iterations only
    lo = 0
    m =0
    hi = len(A)-1
    while(m<=hi):
        if A[m]==0:
            A[lo],A[m] = A[m],A[lo]
            lo+=1
            m +=1
        elif A[m]==1:
            m+=1
        else:
            A[m],A[hi] =A[hi],A[m]
            hi -=1
    return A

A = [0,1,2,1,0,1,1,1,2]
print(Sort(A))