class Stack:
    #Fixed Size Stack
    def __init__(self, stack_size):
        self.list = []
        self.stack_size = stack_size
    


    def stack_length(self):
        return len(self.list)

    

    def push(self,  data):
      
        if self.is_full():
            raise Exception('stack is full')
        self.list += [data]
        
        return self.list


    def pop(self):
        if self.is_empty():
            raise Exception('stack is empty')
        self.list = self.list[:len(self.list)-1]
        return self.list
    
    def peek(self):
        if self.is_empty():
            raise Exception('stack is empty')
        return self.list[len(self.list)-1:]
    


    def is_full(self): 
        return self.stack_length() == self.stack_size

    def is_empty(self): 
        return self.stack_length() == 0


stack = Stack(4)

for item in [10,1,3,10]:
    stack.push(item)



    


