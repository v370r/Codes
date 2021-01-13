class Node:
    def __init__(self,data):
        self.data =data
        self.right=None
        self.left =None
def lca(root,n1,n2):
    if root is None:
        return None
    if root.data>n1 and root.data>n2:
        return(lca(root.left,n1,n2))
    if root.data<n2 and root.data<n2:
        return(lca(root.right,n1,n2))
    return root.