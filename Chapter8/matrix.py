# import random
# import os 
# import time
# import sys


# terminal_size = os.get_terminal_size()

# def recursive(): 
#     num = 3
#     for col in range(terminal_size[0]):
        
        
#         for position in range(0, terminal_size[1]):
#            num *= random.randint(1, 10)
#            f = random.randint(1, 2)

#            if f == 1:
#                print(" ",end=' ')

#            sys.stdout.flush()
#            time.sleep(0.1)
#            print(num,end=' ')


lis = [1]* 1000000

sum = 0 
def sum_recursive(lis, sum):
    
    chr_string = lis[0]

    sum += ord(str(chr_string))
    substr = lis[1:]

    if len(substr) == 0:

        return sum

    else: 

        return sum_recursive(substr, sum)


print(sum_recursive(lis, sum))







        

        
                  

   
               
        #    print(num,flush=True)
    
    # recursive()


         
    

# recursive()
# print('foo', flush=True) )



# num = 3
# for col in range(terminal_size[0]):
#    for position in range(0, terminal_size[1]):
        
#         num *= random.randint(1, 10)

# import turtle, random

# colors  = ["red","green","blue","orange","purple","pink","yellow"] # Make a list of colors to picvk from

# turtle.width(10) #What does this line do?

# length = 5

# for count in range(100):
#   color = random.choice(colors) #Choose a random color
#   turtle.forward(length)
#   turtle.right(135)
#   turtle.color(color) # Why is color spelt like this?
#   length = length + 5
  
# print(num)      
        

# for 

# for position in range(terminal_size[0)
# for 
# print(random.randint(1, 10))