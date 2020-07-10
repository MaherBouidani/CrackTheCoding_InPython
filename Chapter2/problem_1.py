
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
 # -------------------Brute Force ------------------------       
    def remove_duplicates_brute_sol(self):
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
 # -------------------Hash Table ------------------------   
    def remove_duplicates_hashtable_sol(self):
        hash_table = set()
        current = self.head
        prev_node = None
        while current:
            if prev_node is not None:
                if current.data in hash_table:
                    prev_node.next = current.next
                    return 
                prev_node = current
                hash_table.add(current.data)
                current = current.next
            else:
                prev_node = self.head


        
            
            


        
    
ll = SingleLinkedList()


for item in [13,34,76,8,16,13]:
    ll.add_node(item)

print(ll.print_ll())

ll.remove_duplicates_hashtable_sol()
print(ll.print_ll())





