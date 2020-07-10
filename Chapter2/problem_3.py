
#Note: The only difference is that we do not need to add a layer to cover the deletion from the start or end
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