# def get_perm(string):

#     perm = []

#     if len(string) == 0:
#         perm.append(" ")

#         return perm


#     first = string[0]
#     remaining = string[1:]

#     words = get_perm(remaining)

#     for word in words: 

#         index = 0

#         for letter in word:

#             permutation = charAt(word, first, index)

#             perm.append(permutation)

#             index += 1
    
#     return perm


# def charAt(word, first, index):
#     start = word[:index]
#     end = word[index:]

#     return start + first + end


# def check_palindrome(list_of_perm):
#     print(list_of_perm)

#     for word in list_of_perm:
#         word_nospace = word.strip()
#         str_new = ''
#         for ind in range(len(word_nospace)-1, -1, -1):
#             str_new += word[ind]
        
#         if word_nospace == str_new:
#             return True
#         else:
#             return False


    


# print(check_palindrome(get_perm("tact coa")))



def is_palindrome(string):

    table = [0] * 128

    for letter in string:
        table[ord(letter)] += 1 

    
    return check_max_odd_num(table)


def check_max_odd_num(table):
    index = 0

    for element in table:
        
        if element % 2 == 1:
            if index ==1:
                return False

            index += 1 


    return True


print(is_palindrome("tactcoa"))



