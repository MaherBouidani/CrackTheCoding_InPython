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
    
    def sum_linkedlists(self, first_ll, second_ll):
        
        current_first = first_ll.head
        current_second = second_ll.head
        carry_digit = 0
        lis_res = []
        while current_first and current_second:
            digit_sum = current_first.data + current_second.data + carry_digit
            if digit_sum >= 10: 
                lis_calc = list(str(digit_sum))
                lis_res += lis_calc[1]
                carry_digit = int(lis_calc[0])
            else: 
                lis_calc = list(str(digit_sum))
                lis_res += lis_calc[0]
            current_first = current_first.next
            current_second = current_second.next
            
        for item in lis_res:
            self.add_node(int(item))
    
        
    
ll1 = SingleLinkedList()
ll2 = SingleLinkedList()
sum_result = SingleLinkedList()


for item in [0,2,9]:
    ll1.add_node(item)
for item in [0,8,0]:
    ll2.add_node(item)

sum_result.sum_linkedlists(ll1, ll2)

print(sum_result.print_ll())
sum_result_str = ''
for item in reversed(sum_result.print_ll()):
   sum_result_str += str(item)

sum_result_int = int(sum_result_str)

print(sum_result_int)





# print(ll.print_ll())
# print(ll.print_ll())

