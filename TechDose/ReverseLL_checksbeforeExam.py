# Using Normal
class Node:
    def __init__(self,data):
        self.data = data
        self.next =None
class LinkedList:
    def __init__(self):
        self.head =None
    def push(self,data):
        temp = self.head
        node = Node(data)
        node.next = temp
        self.head = node
    def PrintLL(self):
        temp =self.head
        while(temp):
            print(temp.data,end = "=>")
            temp =temp.next 
        print()
    def Reverse(self):
        prev=None
        curr = self.head
        while(curr):
            Next = curr.next 
            curr.next = prev 
            prev = curr
            curr = Next
        self.head = prev

    def ReverseRecursion(self,curr,prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
        Next =curr.next 
        curr.next = prev
        self.ReverseRecursion(Next,curr)
    
    def reverseRec(self):
        if self.head is None:
            return
        self.ReverseRecursion(self.head,None)

llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 
print("Given Linked List")
llist.PrintLL() 
llist.Reverse() 
llist.PrintLL() 
"""
llist.reverseRec() #Not to use recusrion depths
llist.PrintLL()
"""