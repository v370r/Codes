class Box:
    def __init__(self,h,w,d):
        self.h = h
        self.w = w
        self.d = d
    def __lt__(self,other):
        return self.d*self.w<other.d*other.w 

def maxStackHeight(A,n):
    #All possible rotations we use ermute 3p2
    rot = [Box(0,0,0) for x in range(3*n)]
    index= 0
    for i in range(n): 
        # Normal
        rot[index].h = A[i].h
        rot[index].d = max(A[i].d,A[i].w)
        rot[index].w = min(A[i].d,A[i].w)
        index +=1
        # First rotation of the box 
        rot[index].h = A[i].w 
        rot[index].d = max(A[i].h, A[i].d) 
        rot[index].w = min(A[i].h, A[i].d) 
        index += 1
        # Second rotation of the box 
        rot[index].h = A[i].d
        rot[index].d = max(A[i].h, A[i].w) 
        rot[index].w = min(A[i].h, A[i].w) 
        index += 1
    n *=3
    rot.sort(reverse=True)
    #Maximum possible stack height
    msh =[0]*n
    for i in range(n):
        msh[i] = rot[i].h

    for i in range(1,n):
        for j in range(i):
            if (rot[i].w<rot[j].w) and (rot[i].d <rot[j].d):
                if msh[i]<msh[j]+rot[i].h:
                    msh[i]=msh[j]+rot[i].h
    return max(msh)
if __name__ == "__main__": 
    arr = [Box(4, 6, 7), Box(1, 2, 3), 
           Box(4, 5, 6), Box(10, 12, 32)] 
    n = len(arr) 
    print("The maximum possible height of stack is",maxStackHeight(arr,n))  
