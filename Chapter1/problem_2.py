# -------------- Sorting --------------
string1 = "abdc"
string2 = "dbac"

def string_permutation(string1, string2):

    str_sort = sorted(string2)
    str_list = sorted(string1)
    
    #Sorted Without Functions
    string1_list = list(string1)
    for index1 in range(len(lis)):
        for index2 in range(index1+1, len(lis)):
            if ord(lis[index1]) > ord(lis[index2]):
                tmp = lis[index1]
                lis[index1] = lis[index2]
                lis[index2] = tmp

    if str_list == str_sort: 
        return True
    else: 
        return False 

string_permutation(string1, string2)