def binomialCoeff(x, n, k):
    sum = 0;
    term = 1;
    i = 1;
    while(i <= n and sum < k): 
        term *= x - i + 1;
        term /= i;
        sum += term;
        i += 1;
    return sum

def minTrials(n, k):
    low = 1;
    high = k;
    while (low < high):
        mid = int((low + high) / 2);
        if (binomialCoeff(mid, n, k) < k):
            low = mid + 1;
        else:
            high = mid;
 
    return int(low);
 
# Driver Code
print("Ans : \n",minTrials(2, 10));

"""
Using Dp
"""
INT_MAX = 32767
def eggDrop(n, k): 
    eggFloor = [[0 for x in range(k + 1)] for x in range(n + 1)] 
    for i in range(1, n + 1): 
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0
    for j in range(1, k + 1): 
        eggFloor[1][j] = j 

    for i in range(2, n + 1): 
        for j in range(2, k + 1): 
            eggFloor[i][j] = INT_MAX 
            for x in range(1, j + 1): 
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]) 
                if res < eggFloor[i][j]: 
                    eggFloor[i][j] = res 
  
    return eggFloor[n][k] 
n = 2
k = 36
print("Minimum number of trials in worst case with" + str(n) + "eggs and " 
       + str(k) + " floors is " + str(eggDrop(n, k))) 