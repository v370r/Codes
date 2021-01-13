results =[]
def permute(arr,i,n):
    if i==n:
        results.append("".join(arr))
    else:
        for j in range(i,n):
            arr[j],arr[i]=arr[i],arr[j]
            permute(arr,i+1,n)
            arr[j],arr[i]=arr[i],arr[j]
    return(results)
arr= ["A","B","C"]     
print(permute(arr,0,len(arr)))


