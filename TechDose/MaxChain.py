"""
Given (5,24),(39,60),(15,28),(27,40),(50,90)
make a chain
ANS MUST BE LIKE  
5   15  27  39   soon
24  28  40  60
"""
#Longest  increasing subsequence method

def LIS(A):
    n = len(A)
    lis = [1]*(n+1)
    for x in range(1,n):
        for y in range(0,x):
            if A[x][0]>A[y][1] and lis[x]<=lis[y]+1:
                lis[x] = lis[y]+1
    return(max(lis))
A = [[5,24],[15,28],[39,60]]
print(LIS(A))
