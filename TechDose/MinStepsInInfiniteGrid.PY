#Given : i)Infinite Grid
#        2 )Initial X and Y  
#Task: Find min steps to travel all the given cell Must follow the sequebce
# URL:https://youtu.be/ZNh35dFqklM?list=PLEJXowNB4kPxQIN2dCUAnQ_92HIziG4x6
#Ex: {(4,6),(1,2),(4,5),(3,1)}
#Trick:
#       min_distance = max(abs(x1-x2),abs(y1,y2))
def Maxdist(A):
    Max = 0
    for x in range(len(A)-1):
        Max += max(abs(A[x][0]-A[x+1][0]),abs(A[x][1]-A[x+1][1]))
    return Max

A = [(4,6),(1,2),(4,5),(3,1)]
print(Maxdist(A))