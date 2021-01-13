class Node:
    def __init__(self,data):
        self.data= data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head =None
    def getIntersection(self,headA,headB):
        dic ={}
        while headA:
            dic[headA]=1
            headA = headA.next 
        while headB:
            if headB in dic:
                return headB
            headB =headB.next 
        return None
headA = Node(4)
headB = Node(5)

