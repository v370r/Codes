"""
Time      Event Type     Total Platforms Needed 
                               at this Time                               
 9:00       Arrival                  1
 9:10       Departure                0
 9:40       Arrival                  1
 9:50       Arrival                  2
 11:00      Arrival                  3 
 11:20      Departure                2
 11:30      Departure                1
 12:00      Departure                0
 15:00      Arrival                  1
 18:00      Arrival                  2 
 19:00      Departure                1
 20:00      Departure                0
 Max = 3
 """
def findPlatform(Arr,dep,n):
    Arr.sort()
    dep.sort()
    platform =1
    result =1
    i=1
    j=0
    while(i<n and j<n):
        if Arr[i]<=dep[j]:
            platform +=1
            i+=1
        elif Arr[i]>dep[j]:
            platform -=1
            j+=1
        if platform>result:
            result=platform
    return result
arr = [900, 940, 950, 1100, 1500, 1800] 
dep = [910, 1200, 1120, 1130, 1900, 2000] 
n = len(arr) 

print("Minimum Number of Platforms Required = ",findPlatform(arr, dep, n)) 