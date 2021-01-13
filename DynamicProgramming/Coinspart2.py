def count(Coins,V):
    n = len(Coins)
    dp =[0 for x in range(V+1)] 
    dp[0] =0  # if V is 0 no of coins required is 0
    for i in range(1,V+1):
        dp[i]=float("inf")
    for w in range(1,V+1):
        for j in range(1,n+1):
            if Coins[j-1]<=w:
                sub_res = dp[w-Coins[j-1]]
                if sub_res != float("inf") and dp[w]>sub_res+1:
                    dp[w]=sub_res+1
    return dp[V]

"""
Wrong
def Rec(Coins,V,n):
    if V<0:
        return (float(inf))
    elif V==0:
        return(0)
    else:
        return(min(1+Rec(Coins,V-Coins[n-1],n-1),Rec(Coins,V,n-1))

"""

Coins =[9, 6, 5, 1]
Val = 11
n = len(Coins)
print(count(Coins,Val))