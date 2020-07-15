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
    
    def intesect_ll (self, first_ll, second_ll):

        current_first = first_ll.head
        current_second = second_ll.head
         
        #Edge Case: If one of them at least is empty, no need to continue checking ! because there is not intersection then. 
        if current_first is None or current_second is None: 
            return False

        list_intersect = []

        while current_first and current_second:
            print(current_first.data, current_first, current_second.data, current_second)
            
            if current_first == current_second:
                list_intersect += [current_first.data]

                
               
            current_first = current_first.next
            current_second = current_second.next
        
        for item in list_intersect:
            self.add_node(item)
        
        return self.print_ll()






ll1 = SingleLinkedList()
ll2 = SingleLinkedList()
resulted_ll = SingleLinkedList()
node1 = Node(9)
node2 = Node(2)
node3 = Node(4)
node4 = Node(10)
 

ll1.head = node1 
node1.next = node2
node2.next = node3 

ll2.head = node4
node4.next = node2
node2.next = node3


print(resulted_ll.intesect_ll(ll1,ll2))

