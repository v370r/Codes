def Rainwater(A):
    res = 0
    left_max = 0
    right_max = 0
    lo = 0
    hi = len(A)-1
    while lo<=hi:
        if A[lo]<A[hi]:
            if A[lo]>left_max:
                left_max =A[lo]
            else:
                res += left_max-A[lo]
            lo +=1
        else:
            if A[hi]>right_max:
                right_max =A[hi]
            else:
                res += right_max-A[hi]
            hi -=1
    return res

A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Rainwater(A))
