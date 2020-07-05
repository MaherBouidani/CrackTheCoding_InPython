# -------------- Sorting --------------
string1 = "abdc"
string2 = "cakcddd"

def string_permutation(string1, string2):

    str_sort = sorted(string2)
    str_list = sorted(string1)

    if str_list == str_sort: 
        return True
    else: 
        return False 

print(string_permutation(string1, string2))

# -----------Brute Force Sorting ------

    string1_list = list(string1)
    for index1 in range(len(lis)):
        for index2 in range(index1+1, len(lis)):
            if ord(lis[index1]) > ord(lis[index2]):
                tmp = lis[index1]
                lis[index1] = lis[index2]
                lis[index2] = tmp

# ----------- Using Hashtable - List---------

def string_permutation_check(string1, string2):

    # Edge Case: If both strings are not equal in length, they could not be a permutation as a definition

    if len(string1) != len(string2):
        return False
    
    letters = [0] * 128

    for letter in string1:
        letters[ord(letter)] += 1

    for index in range(len(string2)-1, -1, -1):    # or using reversed(): reversed(range(len(string2)))
        letters[ord(string2[index])] -= 1

        if letters[ord(string2[index])] < 0:
            return False
    
    return True

print(string_permutation_check(string1, string2))


    


