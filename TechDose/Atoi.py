#given string print if it int we can try using try except funciton
#https://youtu.be/2I9XO8jwZCA?list=PLEJXowNB4kPxQIN2dCUAnQ_92HIziG4x6
#my easy:
"""
try:
    a = int(input())
    print(a)
except:
    print(-1)
"""
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0,n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 
  
bubbleSort(arr) 
  
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i],end=","), 