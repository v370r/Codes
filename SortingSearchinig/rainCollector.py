def Water(Arr,n):
    amount = 0
    left_max= 0
    right_max=0
    lo=0
    hi=n-1
    while(lo<=hi):
        if Arr[lo]<Arr[hi]:
            if left_max<Arr[lo]:
                left_max = Arr[lo]
            else:
                amount +=left_max-Arr[lo]
            lo+=1
        else:
            if Arr[hi]>right_max:
                right_max=Arr[hi]
            else:
                amount +=right_max-Arr[hi]
            hi -=1
    return amount

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
 
print("Maximum water that can be accumulated is ",Water(arr, n))
