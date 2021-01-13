class Node:
    def __init__(self,data):
        self.data = data
        self.right =None
        self.left =None
def BottomView(root):
    d = dict()
    printBottomUtil(root,d,0,0)
    for i in sorted(d.keys()):
        print(d[i][0],end =" ")
def printBottomUtil(root,d,hd,level):
    if root is None:
        return
    if hd in d:
        if level>=d[hd][1]:
            d[hd] = [root.data,level]
    else:
        d[hd] = [root.data,level]
    
    printBottomUtil(root.left,d,hd-1,level+1)
    printBottomUtil(root.right,d,hd+1,level+1)
if __name__ == '__main__': 
      
    root = Node(20) 
    root.left = Node(8) 
    root.right = Node(22)  
    root.left.left = Node(5)  
    root.left.right = Node(3)  
    root.right.left = Node(4)  
    root.right.right = Node(25)  
    root.left.right.left = Node(10)  
    root.left.right.right = Node(14)  
      
    print("Bottom view of the given binary tree :") 
      
    BottomView(root)

