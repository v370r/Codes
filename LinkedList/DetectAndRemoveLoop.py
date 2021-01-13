class Node:
    def __init__(self,data):
        self.data =data
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_Node =Node(data)
        new_Node.next = self.head
        self.head = new_Node
    
    def detectAndRemoveLoop(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        slow_ptr =self.head
        fast_ptr =self.head

        while(fast_ptr is not None):
            if fast_ptr.next is None :
                break
            if slow_ptr ==fast_ptr:
                break
            slow_ptr =slow_ptr.next 
            fast_ptr =fast_ptr.next.next 
        if slow_ptr ==fast_ptr:
            slow_ptr =self.head
            while(slow_ptr.next!=fast_ptr.next):
                slow_ptr =slow_ptr.next 
                fast_ptr =fast_ptr.next 
            fast_ptr.next =None
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end="=>")
            temp = temp.next
        print()
        
llist = LinkedList()
llist.head = Node(50)
llist.head.next = Node(20)
llist.head.next.next = Node(15)
llist.head.next.next.next = Node(4)
llist.head.next.next.next.next = Node(10)
llist.head.next.next.next.next.next = llist.head.next.next
 
llist.detectAndRemoveLoop()
 
print("Linked List after removing loop")
llist.printList()

"""
    def detectAndRemove(self):
        slow_ptr = fast_ptr = self.head
        while(slow_ptr and fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next 
            fast_ptr =fast_ptr.next.next 
            if slow_ptr==fast_ptr:
                self.removeLoop(slow_ptr)
                return 1
        return 0
    def removeLoop(self,loop_node):
        temp =self.head
        while True:
            ptr2 = loop_node
            while(ptr2.next!=loop_node and ptr2.next!=temp):
                ptr2 =ptr2.next 
            if ptr2.next ==temp:
                break
            temp =temp.next
        ptr2.next =None
"""