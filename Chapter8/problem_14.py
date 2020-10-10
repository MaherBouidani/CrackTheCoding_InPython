# def get_pos(lis):

#     current_score = 0
#     total_score = 0
#     list_1 =[]
#     list_2 =[]
#     list_3 = []

#     list_1_len = 0
#     list_2_len = 0
#     list_3_len = 0
    
   

#     for i in range(len(lis)):
       

#         if type(lis[i]) == int:
#             current_score = lis[i]
#             total_score += current_score
#             print("curent", current_score, total_score)
            

#         else: 
#             if lis[i] == 'Z':
#                 total_score -= current_score
#                 if lis[i-2] == '+':
#                     current_score = list_3[list_3_len-1]
#                 else:
#                     current_score = lis[i-2]


                
#                 list_2.append(current_score)
#                 list_2_len += 1
#                 print(list_2)

#                 print( current_score, total_score)
                

#             elif lis[i] == 'X':
#                 current_score *= 2
#                 list_1.append(current_score)
#                 list_1_len += 1 
                
               
#                 total_score += current_score
#                 print("current", current_score, total_score)
                
            
#             elif lis[i] == '+':
#                 if lis[i-2] == 'X':
#                     current_score += list_1[list_1_len-1]
#                 elif lis[i-2] == 'Z':
#                     current_score += list_2[list_2_len-1]
#                 elif lis[i-2] == '+':
#                     current_score += list_3[list_3_len-2]
                   
                  

#                 else:
#                     current_score += lis[i-2]
#                 total_score += current_score
#                 list_3.append(current_score)
          
#                 list_3_len += 1
#                 print("current", current_score, total_score)
            
            
            
             
                 

    
#     return total_score


# print(get_pos([1,2,3,'Z','X','+', '+', '+', '+', '+', 'X', 'Z', 1]))


# lis = [0, 1, 4, 50, 52, 91]
# lis_new = []

# for i in range(len(lis)):

#     if i == 0:
#         continue

#     if lis[i] == lis[i-1] + 1:
#         continue
#     elif i == len(lis) - 1:
#         if 100 - lis[i] > 10:   
#             start = lis[i]+1
#             end = 99 
#             string = str(start)+'-'+str(end)
#             lis_new.append(string)
#         else:
#             for j in range(lis[i]+1,100):
#                lis_new.append(j)

#     else:
#         if lis[i] - lis[i-1] > 10:
#             start = lis[i-1] + 1 
#             end = lis[i] - 1
#             string = str(start)+'-'+str(end)
#             lis_new.append(string)
#         else:
#             for j in range(lis[i-1]+1,lis[i]):
#                lis_new.append(j)
    
    

# print(lis_new)




def union(lis):

    list_of_sets = []
    list_of_union = []
    intersection = set()
    

    for item in lis:
        list_of_sets +=[set(item)]
    
    for i in range(len(list_of_sets)):
        for j in range(i+1, len(list_of_sets)):
            if len(list_of_sets[i] & list_of_sets[j]) >= 1:
                if len(intersection & list_of_sets[i]) >=1:

                   intersection  =  intersection | (list_of_sets[i] | list_of_sets[j])

                else: 
                    intersection = list_of_sets[i] | list_of_sets[j]
                
                list_of_union.append(list(intersection))
    
    count = 0
    print(count)
    
    
    for i in range(len(list_of_union)):

        if len(list_of_union[i]) > count:
            count = len(list_of_union[i])
            print(count)
            index = i 

        
    return list_of_union[index]






                
        

    
    
    
   
    


    
    


lis = [['item1', 'item2'],['item2', 'item3'],['item3', 'item5'],['item10', 'item6'],['item6', 'item7']]

print(union(lis))
        

