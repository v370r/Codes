#mef = maximum ending element
#msf = Int_Min max so far
#Kandanes Algorithm:
# https://youtu.be/YxuK6A3SvTs?list=PLEJXowNB4kPxQIN2dCUAnQ_92HIziG4x6
def Kandane(A,n):
    curr_sum = 0
    msf = float("-inf")
    for i in range(n):
        curr_sum += A[i]
        if curr_sum<A[i]:
            curr_sum = A[i]
        if curr_sum>msf:
            msf = curr_sum
    return msf

A= [-2,-3,4,-1,-2,1,5,-3]
n = len(A)
print(Kandane(A,n))