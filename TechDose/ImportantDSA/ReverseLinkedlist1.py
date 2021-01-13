class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head =None
    
    def reversen(self, head, k): 
        current = head  
        next  = None
        prev = None
        count = 0 
        while(current  and count < k): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next 
            count += 1
        if next is not None: 
            head.next = self.reversen(next, k) 
        return prev 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data,end="=>") 
            temp = temp.next


llist = Linkedlist() 
llist.push(9) 
llist.push(8) 
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 
  
print("Given linked list")
llist.printList() 
llist.head = llist.reversen(llist.head, 3) 
print("\nReversed Linked list")
llist.printList() 
