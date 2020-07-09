# Tutorial on How to make a LinkedList in python. We are not using the module LinkedList, rather creating class definition from scratch

class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next
  
  

class Head: 
    def __init__(self): 
        self.headPointer = None 
     

    def print(self):
        current = self.headPointer
        while current:
            print(current.data)
            current = current.next
        
    def insert_node_atEnd(self,data):
        newNode = Node(data)
        if(self.headPointer):
            current = self.headPointer
            while current.next:
                current = current.next
            
            current.next = newNode
        else:
            self.headPointer = newNode
    
    def search_list(self, search_value):
        current = self.headPointer
        count = 1
        while current:
            if current.data == search_value:
                return True, count
            current = current.next
            count += 1 
        return False
    
    def remove_item(self, node_id):
        current = self.headPointer
        prev_node = None
        current_id = 1

        while current:
        
            if current_id== node_id:
                if prev_node is not None: 
                    prev_node.next = current.next
                    return  
                else: 
                    self.headPointer = current.next
                    return "empty", self.headPointer   
            prev_node = current
            current = current.next
            current_id += 1 
        
        
            


    def list_length(self):
        count = 0
        current = self.headPointer
        while current:
            count += 1
            current = current.next
        
        return print("list length is:", count)
    

linked_list_head = Head()
# first_node = Node(1)
# second_node = Node(2)
# third_node = Node(3)

# first_node.next = second_node
# second_node.next = third_node
# linked_list_head.headPointer = first_node

# linked_list_head.insert_node_atEnd(7)

for data in [8]:
    linked_list_head.insert_node_atEnd(data)

linked_list_head.print()
linked_list_head.list_length()

# print(linked_list_head.search_list(8))
print(linked_list_head.remove_item(1))
linked_list_head.print()




