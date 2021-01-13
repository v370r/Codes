class Node:
    def __init__(self,data):
        self.data =data
        self.next =None

class LinkedList:
    def __init__(self):
        self.head =None

    def push(self,key):
        newNode = Node(key)
        temp =self.head
        newNode.next = temp
        self.head =newNode
    
    def PrintLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end="->")
            temp =temp.next 
        print()
    
    def Middle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while(slow_ptr.next and fast_ptr.next and fast_ptr.next.next):
            slow_ptr = slow_ptr.next 
            fast_ptr = fast_ptr.next.next 
        print("Middle Element->",slow_ptr.data)
List1 =LinkedList()
List1.push(1)
List1.push(4)
List1.push(-5)
List1.push(0)
List1.push(10)
List1.PrintLL()
List1.Middle()