def Spiral(A):
    n  = len(A)
    top,down=0,n-1
    left,right=0,n-1
    dir=0
    while(top<=down and left<=right):
        if dir ==0:
            for i in range(left,right+1):
                print(A[top][i],end="->")
            top+=1
        elif(dir==1):
            for i in range(top,down+1):
                print(A[i][right],end="->")
            right -=1
        elif(dir==2):
            for i in range(right,left-1,-1):
                print(A[down][i],end="->")
            down -=1
        else:
            for i in range(down,top-1,-1):
                print(A[i][left],end= "->")
            left+=1
        dir = (dir+1)%4

    return
        
A = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
print(Spiral(A))