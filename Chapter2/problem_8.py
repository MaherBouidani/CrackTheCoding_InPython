class Node: 
    def __init__(self, data=None, next=None): 
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
        
    
    def circular(self, node_id):

        current = self.head 
        count = 1
        while current.next:
            if count == node_id:
                node = current
            current = current.next
            count += 1 
        current.next = node

        return node.data

   

 #NOTE1: or using append, **** BE CAREFUL IN PYTHON****: concat + only applies on the same type. Example: TypeError for concat two different types int and list           
    def print_ll(self):
        current = self.head
        ll_data = []
        while current:
            ll_data +=  [current.data] #Ref_To NOTE1
            current = current.next
        return ll_data
    


ll = SingleLinkedList()

for item in ['A','B','C','D','E']:
    ll.add_node(item)

print(ll.print_ll())


print(ll.circular(4))

