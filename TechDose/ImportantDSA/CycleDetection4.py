class Node:
    def __init__(self,data):
        self.data =data
        self.next =None
class LinkedList:
    def __init__(self):
        self.head= None
    def detectionandRemove(self):
        slow_ptr,fast_ptr = self.head,self.head
        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next 
            fast_ptr = fast_ptr.next.next 
            if fast_ptr ==slow_ptr:
                self.removeLoop(slow_ptr)
                return 1
        return 0

    def removeLoop(self,slow_ptr):
        ptr1 = self.head 
        while True:
            ptr2 = slow_ptr
            while(ptr2.next!=slow_ptr and ptr2.next != ptr1):
                ptr2 = ptr2.next 
            if ptr2.next == ptr1: #circle ll for first loop
                break 
            ptr1 = ptr1.next 
        ptr2.next =None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end="->")
            temp = temp.next
llist = LinkedList()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)
llist.head.next.next.next.next.next = llist.head.next.next
llist.detectionandRemove()
print("Linked List after removing loop")
llist.printList()