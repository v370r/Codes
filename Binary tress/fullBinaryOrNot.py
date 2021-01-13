class Node:
    def __init__(self,data):
        self.data =data
        self.right =None
        self.left =None
def FullBinary(root):
    if root is Node:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return (FullBinary(root.left) and FullBinary(root.right))
    return False
    

