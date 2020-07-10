
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
 #NOTE1: or using append, **** BE CAREFUL IN PYTHON****: concat + only applies on the same type. Example: TypeError for concat two different types int and list           
    def print_ll(self):
        current = self.head
        ll_data = []
        while current:
            ll_data +=  [current.data] #Ref_To NOTE1
            current = current.next
        return ll_data
    
    def remove_duplicates(self):
        current = self.head 

        while current:
            pointer = current.next
            prev_node = None
            
            while pointer:
                if prev_node is not None:
                    if current.data == pointer.data:
                        prev_node.next = pointer.next 
                        return
                    prev_node = pointer
                    pointer = pointer.next
                else:
                    prev_node = self.head
            current = current.next
        
            
            


        
    
ll = SingleLinkedList()


for item in [13,13,15,8,16,3]:
    ll.add_node(item)

print(ll.print_ll())

ll.remove_duplicates()
print(ll.print_ll())





