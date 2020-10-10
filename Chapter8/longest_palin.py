# def longest_palindrome(string):

#     # i = 0
#     # j = len(string) - 1 

#     # while i<j:

#     #     if string[i] == string[j]:
#     #         new_str = string[i:j+1]
#     #         print(new_str)
            
#     #         if is_plaindrome(new_str):
#     #             return new_str
        
#     #     i += 1
#     #     j -= 1 
#     perm = []

#     for i in range(len(string)):
#         for j in range(i+1, len(string)):

#             str_new = string[i:j+1]
            


#             if is_plaindrome(str_new):
#                 perm.append(str_new)

#     return max(perm)

    
  
    

# def is_plaindrome(new_str):

#     reverse=''

#     for i in range(len(new_str)-1, -1,-1):
#         reverse += new_str[i]

#     if reverse != new_str:

#         return False
    
#     return True





# print(longest_palindrome("ebsmeem"))


# def longest_palindrome(string):

#     table = [[0]*len(string) for i in range(len(string))]

#     for i in range(len(string)):
#         table[i][i] = 1

    

    


# longest_palindrome("mah")

lis1 = {'item1', 'item2'}

lis2 = {'item2', 'item4'}


def largestItemAssociation(itemAssociation):
    
    list_of_items = []
    
    
    for item in range(len(itemAssociation)):
        
        list_of_items.append(set(item))
        
    
    for i in range(len(itemAssociation)):
        
        for j in range(i+1, len(itemAssociation)):
            
            intersection = itemAssociation[i] & itemAssociation[j]
            
            if len(intersection) >= 1:
                
                res = itemAssociation[i] | itemAssociation[j]
                
    
    return res


    