def numberOfPainters(A,n,maxLen):
    total =0
    numPainter =1
    for x in A:
        total+=x
        if total>=maxLen:
            total=x
            numPainter +=1
    return numPainter

def Partition(A,n,k):
    lo = max(A)
    hi = sum(A)
    while(lo<=hi):
        mid = (lo+hi)//2
        if numberOfPainters(A,n,mid)<=k:
            hi =mid-1
        else:
            lo = mid+1
    return lo
A= [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(A)
k =3
print(Partition(A,n,k))
