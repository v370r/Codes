class Node:
    def __init__(self,data):
        self.data =data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,data):
        temp =self.head
        NewNode =Node(data)
        NewNode.next = temp
        self.head = NewNode
    
    def DetectLoop(self):
        slow_ptr = self.head
        fast_ptr = self.head
        prev = None
        while(slow_ptr and fast_ptr.next and fast_ptr.next.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr ==fast_ptr:
                self.removeLoop(slow_ptr)
                return 1
        return 0 

    def removeLoop(self,node): #Loop existed 
        slow_ptr = self.head
        fast_ptr = node
        while(slow_ptr.next != fast_ptr.next): #imp ortant junction
            slow_ptr =slow_ptr.next 
            fast_ptr =fast_ptr.next 
        fast_ptr.next =None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end = "->")
            temp = temp.next

llist = LinkedList()
llist.head = Node(50)
llist.head.next = Node(20)
llist.head.next.next = Node(15)
llist.head.next.next.next = Node(4)
llist.head.next.next.next.next = Node(10)
llist.head.next.next.next.next.next = llist.head.next.next
llist.DetectLoop()
llist.printList()

            
