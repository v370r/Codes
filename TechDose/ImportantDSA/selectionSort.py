#Select and move farther
"""
arr[] = 64 25 12 22 11

// Find the minimum element in arr[0...4]
// and place it at beginning
11 25 12 22 64

// Find the minimum element in arr[1...4]
// and place it at beginning of arr[1...4]
11 12 25 22 64
soonS
"""
def selectionSort(A):
    for x in range(len(A)-1):
        for y in range(x+1,len(A)):
            if A[x]>A[y]:
                A[x],A[y] =A[y],A[x]
    return A
A = [64,25,12,22,11]
B= A
print(selectionSort(A))
"""
Time Complexity: O(n2) as there are two nested loops.
Auxiliary Space: O(1) worst n(n+1)/2
"""

def Bubblesort(A):
    for x in range(len(A)):
        for y in range(0,len(A)-x-1):
            if A[y]>A[y+1]:
                A[y],A[y+1] = A[y+1],A[y]
    return A
A = [64,25,12,22,11]
print(Bubblesort(A))

def insertion(A):
    for x in range(1,len(A)):
        j =x-1
        key = A[x]
        while j>=0 and key<A[j]:
            A[j+1] =A[j]
            j -=1
        A[j+1] =key
    return A
    
A = [64,25,12,22,11]
print(insertion(A))

def MergeSort(A):
    if len(A)>1:
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]
        MergeSort(L)
        MergeSort(R)
        i=j=k=0
        while i< len(L) and j<len(R):
            if L[i]<R[j]:
                A[k]=L[i]
                i+=1
            else:
                A[k] =R[j]
                j+=1
            k+=1
        while i<len(L):
            A[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            A[k]=R[j]
            j +=1
            k+=1
        
A = [64,25,12,22,11]
MergeSort(A)
print(A)