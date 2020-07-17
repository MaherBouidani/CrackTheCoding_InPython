class Stack:
    #Dynamic Size Stack
    def __init__(self):
        self.list = []


    def stack_length(self):
        return len(self.list)

    def push(self, data):
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


    def is_empty(self): 
        return self.stack_length() == 0


stack = Stack()

for item in [1,2,3,4]:
    stack.push(item)
print(stack.list)

print(stack.pop()) 

print(stack.list)

print(stack.peek())

print(stack.list)

stack.push(5)

print(stack.list)

stack.push(3)
print(stack.list)

stack.pop()

print(stack.list)