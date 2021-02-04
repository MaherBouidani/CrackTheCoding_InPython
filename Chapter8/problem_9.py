
# a d g
# b e h
# c f


import math

def print_f(string):

    

    list_string = string.split(" ")
   
    list_string = sorted(list_string)
    N = len(list_string)


    num = math.ceil(N/3)
    table=[]

  

    for row in range(num):
        temp=[]
        for col in range (row, N, 3):
           temp.append(list_string [col])
        table.append(temp)
    
    for element in table:
        print("")
        for item in element: 
            print(item, "\t", end='')
bin

print_f("a b c d e f g")
# print_f("a b c d e f g h")













# Input:
# "elephant cat caterpillar frog zebra rabbit dog cow alligator"
# Output:
# alligator   cow      frog
# cat         dog      rabbit
# caterpillar elephant zebra

# Example 2:
# Input: 
# "a b c d e f g"
# Output:
# a c e
# b d f
#     g
# or
# a d f
# b e g
# c
# PLEASE NOTE: The following output is INCORRECT:
# a d g
# b e  
# c f
#  
# Example 3:
# Input: 
# "a b c d e f g h"
# Output:
# a c f
# b d g
#   e h
# or
# a d g
# b e h
# c f


