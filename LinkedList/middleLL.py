class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next =self.head
        self.head = new_node
    def printLL(self):
        temp =self.head
        while temp is not None:
            print(temp.data,end = "->")
            temp = temp.next 
        print()
    
    def middle(self):
        slow =self.head
        fast =self.head
        while(fast is not None and fast.next is not None):
            slow =slow.next 
            fast =fast.next.next 
        print(slow.data)
        
    def delMiddle(self):
        slow_ptr =self.head
        fast_ptr = self.head
        while(fast_ptr is not None and fast_ptr.next is not None):
            fast_ptr =fast_ptr.next.next 
            prev = slow_ptr
            slow_ptr =slow_ptr.next 
        prev.next = slow_ptr.next 
        slow_ptr =None
    

list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.push(21) 
list1.printLL()
list1.middle()  
list1.delMiddle()
list1.printLL()
