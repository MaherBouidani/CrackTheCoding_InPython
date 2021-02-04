
# ---------------
# def string_compression(string):
#     count = 0
#     str_new =""
#     for index in range(len(string)):
#         print(index) 
#         if string[index] == string[index -1] or index == 0:
#             count += 1
#             if index == len(string)-1:
#                 str_new += string[index-1] + str(count)
            
#         else: 
#             str_new += string[index-1] + str(count)
#             count = 1
#             if index == len(string)-1:
#                 str_new += string[index] + str(count)
    
#     return str_new

# print(string_compression("bcCcdef"))

#---------------

# def string_compression(string):
#     chars_list = [0] * 128
#     str_new = ""
#     for letter in string: 
#         chars_list[ord(letter)] += 1
    
#     print(chars_list)
#     for index, char in enumerate(chars_list):
#         if char > 0:
#             str_new += chr(index) + str(char)
    
#     return str_new
    

# print(string_compression("abbcccdddd"))


#-----------------
def string_compression(string):

    dict_count = {}
    result = ''

    for i in range(len(string)):
        if string[i] in dict_count:
            dict_count[string[i]] +=1
        else:
            dict_count[string[i]] = 1
            
    
    print(dict_count)

    for key, value in dict_count.items():
        result += key+str(value)

    return result
   


print(string_compression("aabbbcccccddddddddddd"))



            
                
            
        
            

