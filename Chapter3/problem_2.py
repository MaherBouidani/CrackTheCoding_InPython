#Method1: Use Stack Init Member(self.minimum) to track the items that are pushed into the Stack
#It would be updated accordingly to always hold the most recent minimum item
#We would return self.minimum at end as the minimum item in the whole stack

#-------PseudoCode-----------
class Stack:
    class initilization: 
  
        self.minimum = None


    class method: push(self,  data):

        if self.minimum is not None:
            if self.minimum < data:
                    self.minimum = self.minimum
            else:
                    self.minimum = data
        else: 
            self.minimum = data

    
    class method: stack_min(self):
       
       return self.minimum 
#-------------------------------
    

#Method2: Initilize a static memeber of stack that belongs to main Class Stack. every time we push a new item to the stack, we would compare it with the top of static member. 
#If it is less than,we push this item as well to the static memeber.
#At the end, this static member holds minimum items where its final top element is the min of the Stack.

#-------PseudoCode-----------
class Stack:
    lis_min = []
    count = -1
    class initilization: 
  
       #-----------


    class method: push(self,  data):

        if Stack.count >= 0 :
            if data < Stack.lis_min[Stack.count]:
               Stack.lis_min += [data]
               Stack.count += 1  
        
        else:
            Stack.lis_min += [data]
            Stack.count += 1

    
    class method: stack_min(self):
       
        return Stack.lis_min[len(Stack.lis_min) - 1:]

#-------------------------------