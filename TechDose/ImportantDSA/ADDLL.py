class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def addTwoLists(self,first,second):
        prev = None
        temp =None
        carry =0
        while(first is not None or second is not None):
            fdata = 0 if first is None else first.data 
            sdata = 0 if second is None else second.data 