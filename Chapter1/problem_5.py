# # -------------------Brute ----------------
# string1 = "apple"
# string2 = "appless"
# def one_way(string1, string2): 
#     #Edge Case, Initial Check
#     # if abs(len(string1) - len(string2)) > 1: 
#     #     return False
#     #----------------

#     lis_ascii_1 = [0] * 128
#     lis_ascii_2 = [0] * 128

#     difference = []

#     for letter in string1:
#         lis_ascii_1[ord(letter)] += 1
    
    
#     for letter in string2:
#         lis_ascii_2[ord(letter)] += 1

#     obj_zip = zip(lis_ascii_1, lis_ascii_2)

#     for i, j in obj_zip:
#         difference += [abs(i-j)] # or append
    
#     print(difference)
#     count = 0

#     for item in difference:
#         if item != 0:
#             count += 1 
#         if count > 1 or item ==2: 
#             return False
    
#     return True

# print(one_way(string1, string2))

s1 = "pales"
s2 = "pale"

def edit_check(s1,s2):

    compare = {}
    count = 0

    for i in range(len(s2)):
        compare[i] = s2[i]
    
    for j in range (len(s1)):
        print(count)
        if s1[j] not in compare.values():
                count +=1 

    if count > 1:
        return False
    else:
         return True


print(edit_check(s1,s2))





# def sum (num):
#   if num == 0:
#       return 0
#   else:
#      return num + sum(num-1)

# def fact(num):
#     if num ==1:
#         return 1
#     else:
#         return num*fact(num-1)

# def f(s1,s2):

#     if len(s2) == 0:
#         return "It is not a substring"


#     for idx in range (len(s1)):
       
#          if s1[idx:idx+len(s2)] == s2:

#              return fact(len(s2))
           

            
        

    


    # idx = 0

    # while idx < len(s1):
       
    #     if s1[idx:idx+len(s2)] == s2:
    #         return "It is a substring"
    #     else:
    #         idx+=1
    
#     return "It is not "
    


    



# print(sum([1,2,3]))
# print(sum(range(5)))
    
    



