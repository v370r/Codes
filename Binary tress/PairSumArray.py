def PairSum(A,Sum):
    d = {}
    for x in range(len(A)):
        if Sum-A[x] in d:
            return(d[Sum-A[x]])
        d[A[x]]=x





A = [10,20,10,40,50,60,70]
Sum = 50
print(PairSum(A,Sum))