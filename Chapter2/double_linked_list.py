class Node: 
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def create(self, data):
        node = Node(data)
        
        if self.head:
            current = self.head

            while current.next:
                current = current.next
            
            current.next = node
            node.prev = current
        
        else:
            self.head = node

    def print_double_linked_list(self):
        current = self.head

        while current:
            print("node data:", current.data, current)
            print("node next:", current.next)
            print("node previous", current.prev)
            current = current.next

nodesDataToCreate = [1,2,3,4,5,7,8]

dll = DoubleLinkedList()

for data in nodesDataToCreate:
    dll.create(data)

dll.print_double_linked_list()
