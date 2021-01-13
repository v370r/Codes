INT_MIN =-2**32
def Preorder(pre):
    stack = []
    root = INT_MIN
    for val in pre:
        if val<root:
            return False
        while(len(stack)>0 and stack[-1]<val):
            root = stack.pop()
        stack.append(val)
    return(True)


pre1 = [40 , 30 , 35 , 80 , 100] 
print(Preorder(pre1))