class Node:
    def __init__(self,data):
        self.data =data
        self.right =None
        self.left =None
def minDepth(root):
    if root is None:
        return float("inf")
    if root.left is None and root.right is None:
        return 1
    else:
        return(1+min(minDepth(root.left),minDepth(root.right)))


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.right.left = Node(9) 
print(minDepth(root)) 
  