class Node:
    def __init__(self,data):
        self.data = data 
        self.right = None
        self.left =None
def removeShortPath(root,level,k):
    if root is None:
        return None
    root.left = removeShortPath(root.left,level+1,k)
    root.right = removeShortPath(root.right,level+1,k)
    if root.left is None and root.right is None and level<k:
        return None
    return root