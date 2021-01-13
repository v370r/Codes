#Arrange in order 1L 1S 2L 2S 3L 3S  l is largest 
#note:A is sorted
def Reaarange(A): #O(n) time and O(n) storage
    i = 0
    j = len(A)-1
    B = []
    while(i<j):
        B.append(A[j])
        j-=1
        B.append(A[i])
        i +=1
        if i==j:
            B.append(A[i])
    return B
A = [1,2,3,4,5] #Odd is okay
print(Reaarange(A))
##Efficient solution
#We need O(1) space! dude
#Store two numbers in One afray location:
#https://youtu.be/ZRoVWxBngX0?list=PLEJXowNB4kPxQIN2dCUAnQ_92HIziG4x6
#C:\Users\dell\Dropbox\test\python\TechdosePics
def ConstSpace(A):
    n = len(A)
    me = A[n-1]+1
    max_indx = n-1
    min_indx =0
    for x in range(n):
        if x%2 ==0:
            A[x] = A[x]+(A[max_indx]%me)*(me)
            max_indx -=1
        else:
            A[x] += (A[min_indx]%me)*me
            min_indx+=1
    for i in range(n):
        A[i] = A[i]//(me)
    return(A)
A = [1,2,3,4,5]
print(ConstSpace(A))