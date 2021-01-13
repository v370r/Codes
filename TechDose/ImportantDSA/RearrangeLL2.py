class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head =None
def arrange(head):
    temp =head
    if temp==None:
        return temp
    prev,curr=temp,temp.next 
    while(curr):
        if prev.data > curr.data:
            prev.data,curr.data = curr.data,prev.data 
        if (curr.next and curr.next.data>curr.data):
            curr.next.data, curr.data = curr.data, curr.next.data
        prev = curr.next 
        if not curr.next:
            break 
        curr = curr.next.next 
    return temp  
def push(head, k):
     
    tem = Node(k)
    tem.data = k
    tem.next = head
    head = tem
    return head

def display(head):
    curr = head
    while (curr != None):
        print(curr.data, end = " ")
        curr = curr.next

if __name__ == '__main__':
 
    head = None
    head = push(head, 7)
    head = push(head, 3)
    head = push(head, 8)
    head = push(head, 6)
    head = push(head, 9)
    head = arrange(head)
    display(head)