class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,new_node):
        new_node = Node(new_node)
        new_node.next = self.head
        self.head = new_node
        
    def deleteNode(self,data):
        temp =self.head
        if temp is not None:
            if temp.data == data:
                self.head = temp.next 
                temp =None
                return
        while(temp is not None):
            if temp.data ==data:
                break
            prev = temp
            temp =temp.next 
        if temp==None: #not present
            return
        prev.next = temp.next 
        temp = None

    def printLL(self):
        temp =self.head
        while temp is not None:
            print(temp.data,end = "->")
            temp =temp.next 
        print()
    
        
llist = LinkedList()  
llist.push(7)  
llist.push(1)  
llist.push(3)  
llist.push(2)  
  
print ("Created Linked List: ") 
llist.printLL()  
llist.deleteNode(1)  
print ("\nLinked List after Deletion of 1:") 
llist.printLL()  