class Stack:

    def __init__(self):
        self.stack_list = []

    
    def stack_length(self):

        return len(self.stack_list)

    def push(self,data):
        self.stack_list +=[data]

        return self.stack_list

    def peek(self):
        if self.isEmpty():
            raise Exception("stack is empty")

        return self.stack_list[self.stack_length()-1:]

    def pop(self):
         if self.isEmpty():
            raise Exception("stack is empty")
         
         self.stack_list = self.stack_list[:len(self.stack_list)-1]
         return self.stack_list
    
    def isEmpty(self):

        return self.stack_length() == 0

    



stack_1 = Stack()
stack_2 = Stack()
stack_3 = Stack()
stack_temp = Stack()

for item in [4,3,2,1]:
    stack_1.push(item)


print(stack_1.stack_list)

for i in range(4):
    stack_temp.push(stack_1.peek()[0])
    stack_1.pop()

print(stack_temp.stack_list)

for i in range(4): 
    stack_2.push(stack_temp.peek()[0])
    stack_temp.pop()


print(stack_2.stack_list)

for i in range(4):
    stack_temp.push(stack_2.peek()[0])
    stack_2.pop()


print(stack_temp.stack_list)

for i in range(4): 
    stack_3.push(stack_temp.peek()[0])
    stack_temp.pop()

print(stack_3.stack_list)