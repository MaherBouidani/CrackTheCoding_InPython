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

    # def is_palindrome(self): 
    #     current = self.head
    #     list_ll = []
    #     reversed_list_ll = []
    #     while current: 
    #         list_ll += [current.data]
    #         current = current.next

    #     for item in reversed(list_ll):
    #         reversed_list_ll += [item]

        
    #     if list_ll != reversed_list_ll:
    #         return False
        
    #     return True
    
    # def is_palindrome_sol2 (self):
    #     current = self.head
    #     list_ll = []    

    #     while current: 
    #         list_ll += [current.data]
    #         current = current.next

    #     middle_node = int(len(list_ll)/2)
    #     prev = middle_node - 1
    #     for i in range(middle_node, len(list_ll)):
    #         if i == middle_node:
    #             continue

    #         prev_node = list_ll[prev]
    #         if list_ll[i] != prev_node:
    #             return False
    #         prev = prev- 1  
        
    #     return True
    
    def is_palindrome_sol3 (self):
        current = self.head

        list_ll = []

        while current: 
            list_ll += [current.data]
            current = current.next
        i = 0
        j = len(list_ll) - 1
        # This is not an efficiet way because it did not terminate at the middle. I.E, waste time by doing extra steps
        # while i < len(list_ll) and j >= 0:
        #     print(i, j)
        #     if list_ll[i] == list_ll[j]:
        #         pass
        #     else: 
        #         return False


        #     i += 1
        #     j -= 1

       #This is better while loop
        while i < j:
            if list_ll[i] == list_ll[j]:
                i += 1 
                j -= 1
            else:
                return False 
            
        
        return True

    def is_palindrome_sol4(self):
        current = self.head
        list_ll = []    

        while current: 
            list_ll += [current.data]
            current = current.next
        
        i = 0 
        j = len(list_ll) - 1 

        

        def recursive(i,j):

            if i < j:
                if list_ll[i] != list_ll[j]:
                    return False
                else:
                    i += 1 
                    j -= 1
                    recursive(i,j) 
                
            return True
            



           
        
        return recursive(i,j)

     
           

    





    





        







ll = SingleLinkedList()

for item in ['R','A','D','A', 'R']:
    ll.add_node(item)
print(ll.print_ll())

print(ll.is_palindrome_sol4())

