
class Node: 
    def __init__(self, data=None, next=Node): 
        self.data = data
        self.next = next
    
class SingleLinkedList: 
    def __init__(self): 
        self.head = None

    def add_node(self, data):
        newNode = Node(data)
        
        if self.head:
            current = self.head
            while current.next: 
                current = current.next
            current.next = newNode

        else: 
            self.head = newNode
            
    
ll = SingleLinkedList()


for item in [4,15,13,13,16,3]:
    ll.add_node(item)





